import csv
import html
import json
import math
import re
import shutil
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import requests
from docx import Document


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
PAPER_DIR = ROOT / "paper"
START_YEAR = 2000
END_YEAR = date.today().year
YEARS = list(range(START_YEAR, END_YEAR + 1))
YEAR_RANGE_TEXT = f"{START_YEAR}-{END_YEAR}"
YEAR_FILE_STEM = f"{START_YEAR}_{END_YEAR}"
PAPERS_JSON = f"papers_{YEAR_FILE_STEM}.json"
PAPERS_CSV = f"papers_{YEAR_FILE_STEM}.csv"
CANDIDATES_JSON = f"candidates_top500_{YEAR_FILE_STEM}.json"
CANDIDATES_CSV = f"candidates_top500_{YEAR_FILE_STEM}.csv"
TAXONOMY_CSV = f"papers_taxonomy_{YEAR_FILE_STEM}.csv"
PERIOD_ANALYSIS_JSON = f"period_analysis_{YEAR_FILE_STEM}.json"
TARGET_PER_YEAR = 100
CANDIDATES_PER_YEAR = 500

S2_BULK_URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
S2_FIELDS = ",".join([
    "paperId",
    "title",
    "year",
    "authors",
    "venue",
    "publicationVenue",
    "publicationDate",
    "citationCount",
    "influentialCitationCount",
    "abstract",
    "url",
    "externalIds",
    "openAccessPdf",
    "s2FieldsOfStudy",
    "publicationTypes",
])

QUERIES = [
    "brain computer interface",
    "brain machine interface",
    "BCI EEG",
    "motor imagery BCI",
    "SSVEP BCI",
    "P300 BCI",
    "brain computer interface rehabilitation",
    "invasive brain computer interface",
    "neural decoding brain computer interface",
    "deep learning brain computer interface",
]

RELEVANCE_PATTERNS = [
    r"\bbrain[- ]computer interface",
    r"\bbrain[- ]machine interface",
    r"\bBCI\b",
    r"\bSSVEP\b",
    r"\bP300\b",
    r"\bmotor imagery\b",
    r"\bneural decoding\b",
    r"\bintracortical\b",
    r"\belectrocorticography\b",
]

CATEGORIES = [
    ("Motor Imagery and Movement Decoding", ["motor imagery", "movement", "motor", "kinematic", "hand", "gait"]),
    ("SSVEP, P300, and ERP Spellers", ["ssvep", "p300", "erp", "speller", "steady state", "visual evoked"]),
    ("Rehabilitation and Neuroprosthetics", ["rehabilitation", "stroke", "prosthe", "exoskeleton", "restoration", "therapy"]),
    ("Invasive and Implantable Interfaces", ["invasive", "intracortical", "implant", "electrocorticography", "ecog", "microelectrode"]),
    ("Deep Learning and Representation Learning", ["deep learning", "convolution", "transformer", "graph neural", "domain adaptation", "self supervised"]),
    ("EEG Signal Processing and Datasets", ["eeg", "artifact", "signal processing", "dataset", "benchmark", "classification"]),
    ("Speech, Language, and Communication BCIs", ["speech", "language", "communication", "typing", "text", "decoding words"]),
    ("Hybrid, Affective, and Closed-loop BCIs", ["hybrid", "affective", "closed-loop", "closed loop", "neurofeedback", "adaptive"]),
]

TAXONOMY_VISUALS = {
    "Motor Imagery and Movement Decoding": {
        "motif": "motor",
        "accent": "#0f766e",
        "secondary": "#60a5fa",
    },
    "SSVEP, P300, and ERP Spellers": {
        "motif": "speller",
        "accent": "#7c3aed",
        "secondary": "#f59e0b",
    },
    "Rehabilitation and Neuroprosthetics": {
        "motif": "rehab",
        "accent": "#dc2626",
        "secondary": "#22c55e",
    },
    "Invasive and Implantable Interfaces": {
        "motif": "implant",
        "accent": "#2563eb",
        "secondary": "#a855f7",
    },
    "Deep Learning and Representation Learning": {
        "motif": "deep",
        "accent": "#9333ea",
        "secondary": "#14b8a6",
    },
    "EEG Signal Processing and Datasets": {
        "motif": "eeg",
        "accent": "#0891b2",
        "secondary": "#f97316",
    },
    "Speech, Language, and Communication BCIs": {
        "motif": "speech",
        "accent": "#be123c",
        "secondary": "#06b6d4",
    },
    "Hybrid, Affective, and Closed-loop BCIs": {
        "motif": "hybrid",
        "accent": "#16a34a",
        "secondary": "#8b5cf6",
    },
    "General BCI Methods and Systems": {
        "motif": "general",
        "accent": "#334155",
        "secondary": "#0f766e",
    },
}

LANGUAGES = {
    "en": "English",
    "ko": "한국어",
    "zh": "中文",
    "ja": "日本語",
}

UI_LABELS = {
    "en": {
        "papers": "papers",
        "categories": "categories",
        "overview": "Category Overview",
        "limitations": "Limitations",
        "analysis": "Selected-period analysis",
        "totalSelected": "Total selected papers",
        "categoryCount": "Categories",
    },
    "ko": {
        "papers": "편",
        "categories": "개 분류",
        "overview": "분류 개요",
        "limitations": "한계",
        "analysis": "선택 기간 분석",
        "totalSelected": "총 선정 논문",
        "categoryCount": "분류",
    },
    "zh": {
        "papers": "篇论文",
        "categories": "个分类",
        "overview": "分类概览",
        "limitations": "局限性",
        "analysis": "所选期间分析",
        "totalSelected": "入选论文总数",
        "categoryCount": "分类数",
    },
    "ja": {
        "papers": "本",
        "categories": "分類",
        "overview": "カテゴリ概要",
        "limitations": "限界",
        "analysis": "選択期間の分析",
        "totalSelected": "選定論文総数",
        "categoryCount": "カテゴリ数",
    },
}

TAXONOMY_TRENDS = {
    "Motor Imagery and Movement Decoding": [
        "The field is moving from subject-specific pipelines toward cross-subject, calibration-light, and transfer-learning decoders for EEG motor imagery.",
        "Deep CNN, temporal convolution, graph, attention, and large EEG representation models are increasingly used to improve robustness under noisy and low-data conditions.",
        "Application work is expanding from binary hand imagery toward gait, lower-limb control, soft robotics, virtual feedback, and rehabilitation-oriented closed-loop use.",
    ],
    "SSVEP, P300, and ERP Spellers": [
        "Research is concentrating on high-speed, many-target communication systems with lower calibration burden and more stable target recognition.",
        "Training-free and adaptive spatial filtering, task-discriminant component analysis, and deep neural decoders are prominent directions for SSVEP/P300 reliability.",
        "Hybrid paradigms that combine SSVEP, P300, RSVP, EOG, or augmented/virtual reality interfaces are becoming a practical route to richer command sets.",
    ],
    "Rehabilitation and Neuroprosthetics": [
        "The dominant trend is integration of BCI with robotic gloves, exoskeletons, FES, VR, and task-oriented therapy for post-stroke and motor impairment rehabilitation.",
        "Studies increasingly ask whether BCI training transfers to activities of daily living rather than only improving offline decoding accuracy.",
        "Recent work points toward home-use, patient-centered protocols, multimodal feedback, and combined motor-cognitive-affective rehabilitation.",
    ],
    "Invasive and Implantable Interfaces": [
        "Invasive BCI research is shifting toward high-bandwidth, stable, long-term decoding for movement, communication, and sensory feedback.",
        "Key engineering themes include wireless operation, power efficiency, signal longevity, surgical risk, and reliability outside tightly controlled laboratory sessions.",
        "Clinical translation is increasingly tied to home use, user safety, tactile feedback, speech decoding, and realistic functional tasks.",
    ],
    "Deep Learning and Representation Learning": [
        "Deep learning work is moving beyond single-dataset CNN classifiers toward temporal, spectral, graph, transformer, and attention-based architectures.",
        "A major trend is representation learning that can transfer across users, sessions, headsets, and BCI paradigms with less subject-specific calibration.",
        "Interpretability, uncertainty, robustness to artifacts, and benchmark comparability are becoming as important as peak classification accuracy.",
    ],
    "EEG Signal Processing and Datasets": [
        "This taxonomy emphasizes reproducible preprocessing, artifact handling, channel selection, spatial filtering, and benchmark datasets for EEG-based BCI.",
        "The field is gradually shifting from isolated algorithm papers toward shared datasets, standardized evaluation, and metadata-aware comparisons.",
        "Hybrid EEG/fNIRS, transfer learning, and open benchmark resources are recurring themes for improving generalization and clinical relevance.",
    ],
    "Speech, Language, and Communication BCIs": [
        "Communication BCI is expanding from spelling paradigms toward imagined speech, decoded language, and higher-bandwidth text production.",
        "Both invasive and non-invasive studies are exploring more naturalistic communication, including speech motor cortex decoding and inner-speech EEG datasets.",
        "The central challenge remains preserving accuracy, latency, vocabulary size, and user autonomy in real-world assistive communication.",
    ],
    "Hybrid, Affective, and Closed-loop BCIs": [
        "Hybrid BCI combines multiple signals or paradigms to improve reliability, command diversity, and asynchronous control.",
        "Closed-loop and neurofeedback work is increasingly focused on user adaptation, mental-state awareness, fatigue, affect, and training protocols.",
        "The trend is toward systems that adapt to the user over time rather than treating decoding as a one-shot offline classification problem.",
    ],
    "General BCI Methods and Systems": [
        "General BCI work is consolidating definitions, system architectures, evaluation principles, and long-term challenges across invasive and non-invasive approaches.",
        "Recent surveys increasingly emphasize translation, usability, ethics, safety, reproducibility, and the gap between laboratory performance and real-world use.",
        "This area functions as the conceptual bridge between signal processing, neural engineering, clinical deployment, and human-centered design.",
    ],
}

TAXONOMY_LIMITATIONS = {
    "Motor Imagery and Movement Decoding": [
        "Cross-subject and cross-session variability still limits real-world robustness, especially when calibration time is short.",
        "Many high-scoring methods remain validated on offline datasets rather than sustained closed-loop control or clinical rehabilitation outcomes.",
        "Citation-ranked lists can favor mature EEG motor imagery pipelines over newer low-citation work on multimodal movement decoding.",
    ],
    "SSVEP, P300, and ERP Spellers": [
        "Visual fatigue, gaze dependence, and stimulus comfort remain practical barriers for long-duration communication use.",
        "High-speed results often depend on controlled displays, known target layouts, and calibration conditions that may not transfer to daily use.",
        "Hybrid paradigms improve command diversity but add setup complexity and make fair benchmarking harder.",
    ],
    "Rehabilitation and Neuroprosthetics": [
        "Clinical evidence is often fragmented across small cohorts, heterogeneous protocols, and short follow-up windows.",
        "Improvements in decoder accuracy or therapy-session metrics do not always demonstrate transfer to activities of daily living.",
        "Metadata alone cannot assess patient selection, therapist involvement, adverse events, or trial quality.",
    ],
    "Invasive and Implantable Interfaces": [
        "Surgical risk, long-term signal stability, device maintenance, and participant burden remain major translation barriers.",
        "Many studies involve small cohorts or case reports, so headline performance can be difficult to generalize.",
        "Home deployment, cybersecurity, informed consent, explantation, and support infrastructure are underrepresented in metadata-level screening.",
    ],
    "Deep Learning and Representation Learning": [
        "Performance can be inflated by dataset leakage, weak cross-subject splits, or inconsistent preprocessing across benchmarks.",
        "Large models often improve accuracy while reducing interpretability, uncertainty awareness, and clinical trust.",
        "Low-data and noisy-session robustness remains unresolved for many architectures outside curated datasets.",
    ],
    "EEG Signal Processing and Datasets": [
        "Benchmark datasets vary widely in task design, sensors, preprocessing, and participant populations.",
        "Artifact handling, channel selection, and evaluation protocols are not standardized enough for simple leaderboard-style comparison.",
        "Metadata may miss important dataset attributes such as participant counts, trial structure, hardware, and licensing.",
    ],
    "Speech, Language, and Communication BCIs": [
        "Vocabulary size, latency, privacy, and user autonomy remain difficult to balance in practical assistive communication.",
        "The strongest decoding results often rely on invasive recordings or carefully constrained tasks with limited participant diversity.",
        "Non-invasive imagined-speech datasets are still comparatively small and hard to evaluate consistently.",
    ],
    "Hybrid, Affective, and Closed-loop BCIs": [
        "Combining paradigms can improve reliability but increases calibration, hardware, and user workload.",
        "Closed-loop adaptation is hard to evaluate because user learning, fatigue, and affect change during use.",
        "Longitudinal real-world studies remain scarce, so durability and user acceptance are not well captured.",
    ],
    "General BCI Methods and Systems": [
        "Survey and system papers can dominate citation-ranked views while obscuring smaller empirical advances.",
        "Evaluation language remains inconsistent across paradigms, making taxonomy boundaries imperfect.",
        "Metadata-driven curation cannot replace PDF-level quality appraisal, reproducibility checks, or expert clinical review.",
    ],
}

CATEGORY_LOCALIZATION = {
    "Motor Imagery and Movement Decoding": {
        "en": {
            "name": "Motor Imagery and Movement Decoding",
            "focus": "movement intention decoding, motor imagery EEG, gait, hand control, and rehabilitation-oriented feedback",
            "challenge": "cross-subject variability and offline-only validation remain the main interpretation risks",
        },
        "ko": {
            "name": "운동상상 및 움직임 디코딩",
            "focus": "운동 의도 해석, 운동상상 EEG, 보행·손 제어, 재활 피드백",
            "challenge": "개인차와 세션 차이, 오프라인 검증 중심 결과가 핵심 해석 한계입니다",
        },
        "zh": {
            "name": "运动想象与运动解码",
            "focus": "运动意图解码、运动想象 EEG、步态和手部控制、康复反馈",
            "challenge": "跨被试差异、跨会话不稳定以及偏离线验证是主要解释风险",
        },
        "ja": {
            "name": "運動イメージと運動デコーディング",
            "focus": "運動意図の解読、運動イメージ EEG、歩行・手の制御、リハビリ向けフィードバック",
            "challenge": "被験者差、セッション差、オフライン評価中心である点が主な解釈上の制約です",
        },
    },
    "SSVEP, P300, and ERP Spellers": {
        "en": {
            "name": "SSVEP, P300, and ERP Spellers",
            "focus": "visual evoked responses, ERP spelling, high-speed target selection, and calibration-light communication",
            "challenge": "visual fatigue, gaze dependence, and controlled display assumptions limit daily-use transfer",
        },
        "ko": {
            "name": "SSVEP, P300, ERP 스펠러",
            "focus": "시각유발반응, ERP 스펠링, 고속 표적 선택, 저보정 의사소통",
            "challenge": "시각 피로, 시선 의존성, 통제된 디스플레이 조건이 실사용 전이를 제한합니다",
        },
        "zh": {
            "name": "SSVEP、P300 与 ERP 拼写器",
            "focus": "视觉诱发反应、ERP 拼写、高速目标选择、低校准通信",
            "challenge": "视觉疲劳、凝视依赖和受控显示条件限制了日常使用迁移",
        },
        "ja": {
            "name": "SSVEP・P300・ERP スペラー",
            "focus": "視覚誘発反応、ERP スペリング、高速ターゲット選択、低キャリブレーション通信",
            "challenge": "視覚疲労、視線依存、制御された表示環境への依存が日常利用への移行を制約します",
        },
    },
    "Rehabilitation and Neuroprosthetics": {
        "en": {
            "name": "Rehabilitation and Neuroprosthetics",
            "focus": "post-stroke therapy, robotic assistance, FES, exoskeletons, neuroprosthetic control, and functional recovery",
            "challenge": "small cohorts and heterogeneous protocols make clinical effect size difficult to compare",
        },
        "ko": {
            "name": "재활 및 신경보철",
            "focus": "뇌졸중 후 재활, 로봇 보조, FES, 외골격, 신경보철 제어, 기능 회복",
            "challenge": "소규모 코호트와 이질적 프로토콜 때문에 임상 효과 비교가 어렵습니다",
        },
        "zh": {
            "name": "康复与神经假体",
            "focus": "卒中后治疗、机器人辅助、FES、外骨骼、神经假体控制和功能恢复",
            "challenge": "小样本和异质方案使临床效果大小难以比较",
        },
        "ja": {
            "name": "リハビリテーションと神経補綴",
            "focus": "脳卒中後リハビリ、ロボット支援、FES、外骨格、神経補綴制御、機能回復",
            "challenge": "小規模コホートと不均一なプロトコルにより臨床効果の比較が難しくなります",
        },
    },
    "Invasive and Implantable Interfaces": {
        "en": {
            "name": "Invasive and Implantable Interfaces",
            "focus": "intracortical arrays, ECoG, implantable devices, high-bandwidth decoding, sensory feedback, and home use",
            "challenge": "surgical risk, signal longevity, device maintenance, and participant burden remain central constraints",
        },
        "ko": {
            "name": "침습형 및 이식형 인터페이스",
            "focus": "피질내 전극, ECoG, 이식형 장치, 고대역폭 디코딩, 감각 피드백, 가정 사용",
            "challenge": "수술 위험, 장기 신호 안정성, 장치 유지관리, 참여자 부담이 핵심 제약입니다",
        },
        "zh": {
            "name": "侵入式与植入式接口",
            "focus": "皮层内阵列、ECoG、植入设备、高带宽解码、感觉反馈和家庭使用",
            "challenge": "手术风险、信号寿命、设备维护和参与者负担仍是核心约束",
        },
        "ja": {
            "name": "侵襲型・植込み型インターフェース",
            "focus": "皮質内アレイ、ECoG、植込みデバイス、高帯域デコーディング、感覚フィードバック、在宅利用",
            "challenge": "手術リスク、信号の長期安定性、デバイス保守、参加者負担が中心的な制約です",
        },
    },
    "Deep Learning and Representation Learning": {
        "en": {
            "name": "Deep Learning and Representation Learning",
            "focus": "CNNs, temporal models, graph networks, transformers, self-supervised learning, and cross-subject transfer",
            "challenge": "dataset leakage, weak splits, low interpretability, and poor low-data robustness can overstate performance",
        },
        "ko": {
            "name": "딥러닝 및 표현학습",
            "focus": "CNN, 시간 모델, 그래프 네트워크, 트랜스포머, 자기지도학습, 피험자 간 전이",
            "challenge": "데이터 누수, 약한 분할, 낮은 해석가능성, 저데이터 강건성 부족이 성능을 과대평가할 수 있습니다",
        },
        "zh": {
            "name": "深度学习与表征学习",
            "focus": "CNN、时序模型、图网络、Transformer、自监督学习和跨被试迁移",
            "challenge": "数据泄漏、划分不严、可解释性低和低数据鲁棒性不足可能夸大性能",
        },
        "ja": {
            "name": "深層学習と表現学習",
            "focus": "CNN、時系列モデル、グラフネットワーク、Transformer、自己教師あり学習、被験者間転移",
            "challenge": "データリーク、不十分な分割、低い解釈性、少量データでの脆弱性が性能を過大評価させる可能性があります",
        },
    },
    "EEG Signal Processing and Datasets": {
        "en": {
            "name": "EEG Signal Processing and Datasets",
            "focus": "preprocessing, artifacts, channel selection, spatial filtering, open datasets, and benchmark protocols",
            "challenge": "dataset heterogeneity and inconsistent evaluation protocols make direct comparisons fragile",
        },
        "ko": {
            "name": "EEG 신호처리 및 데이터셋",
            "focus": "전처리, 아티팩트, 채널 선택, 공간 필터링, 공개 데이터셋, 벤치마크 프로토콜",
            "challenge": "데이터셋 이질성과 평가 프로토콜 불일치가 직접 비교를 취약하게 만듭니다",
        },
        "zh": {
            "name": "EEG 信号处理与数据集",
            "focus": "预处理、伪迹、通道选择、空间滤波、开放数据集和基准协议",
            "challenge": "数据集异质性和评估协议不一致使直接比较较脆弱",
        },
        "ja": {
            "name": "EEG 信号処理とデータセット",
            "focus": "前処理、アーチファクト、チャネル選択、空間フィルタリング、公開データセット、ベンチマーク",
            "challenge": "データセットの不均一性と評価プロトコルの不一致により直接比較は脆弱になります",
        },
    },
    "Speech, Language, and Communication BCIs": {
        "en": {
            "name": "Speech, Language, and Communication BCIs",
            "focus": "spelling, text production, speech decoding, imagined speech, language models, and assistive communication",
            "challenge": "vocabulary size, latency, privacy, and autonomy remain difficult to optimize together",
        },
        "ko": {
            "name": "음성·언어·의사소통 BCI",
            "focus": "스펠링, 텍스트 생성, 음성 디코딩, 상상 음성, 언어 모델, 보조 의사소통",
            "challenge": "어휘 규모, 지연시간, 프라이버시, 사용자 자율성을 동시에 최적화하기 어렵습니다",
        },
        "zh": {
            "name": "语音、语言与通信 BCI",
            "focus": "拼写、文本生成、语音解码、想象语音、语言模型和辅助通信",
            "challenge": "词汇规模、延迟、隐私和用户自主性难以同时优化",
        },
        "ja": {
            "name": "音声・言語・コミュニケーション BCI",
            "focus": "スペリング、テキスト生成、音声デコーディング、想像音声、言語モデル、支援コミュニケーション",
            "challenge": "語彙規模、遅延、プライバシー、ユーザー自律性を同時に最適化することは困難です",
        },
    },
    "Hybrid, Affective, and Closed-loop BCIs": {
        "en": {
            "name": "Hybrid, Affective, and Closed-loop BCIs",
            "focus": "multimodal control, affective state awareness, neurofeedback, adaptive decoding, and closed-loop training",
            "challenge": "added sensors and adaptive feedback improve flexibility but complicate evaluation and usability",
        },
        "ko": {
            "name": "하이브리드·정서·폐루프 BCI",
            "focus": "다중모달 제어, 정서 상태 인식, 뉴로피드백, 적응형 디코딩, 폐루프 훈련",
            "challenge": "추가 센서와 적응형 피드백은 유연성을 높이지만 평가와 사용성을 복잡하게 만듭니다",
        },
        "zh": {
            "name": "混合、情感与闭环 BCI",
            "focus": "多模态控制、情感状态感知、神经反馈、自适应解码和闭环训练",
            "challenge": "额外传感器和自适应反馈提高灵活性，但会使评估和可用性复杂化",
        },
        "ja": {
            "name": "ハイブリッド・感情・閉ループ BCI",
            "focus": "マルチモーダル制御、感情状態認識、ニューロフィードバック、適応デコーディング、閉ループ訓練",
            "challenge": "追加センサーと適応フィードバックは柔軟性を高めますが、評価と使いやすさを複雑にします",
        },
    },
    "General BCI Methods and Systems": {
        "en": {
            "name": "General BCI Methods and Systems",
            "focus": "system architecture, conceptual frameworks, surveys, evaluation principles, ethics, usability, and translation",
            "challenge": "broad survey papers can dominate citation-ranked views while detailed empirical evidence remains scattered",
        },
        "ko": {
            "name": "일반 BCI 방법론 및 시스템",
            "focus": "시스템 아키텍처, 개념 프레임워크, 서베이, 평가 원칙, 윤리, 사용성, 전환 연구",
            "challenge": "광범위한 서베이 논문이 인용 순위를 지배하면서 세부 실증 근거가 흩어져 보일 수 있습니다",
        },
        "zh": {
            "name": "通用 BCI 方法与系统",
            "focus": "系统架构、概念框架、综述、评估原则、伦理、可用性和转化",
            "challenge": "广泛综述可能主导引用排序，而细粒度实证证据仍较分散",
        },
        "ja": {
            "name": "一般的な BCI 方法論とシステム",
            "focus": "システム構成、概念枠組み、レビュー、評価原則、倫理、ユーザビリティ、実装への移行",
            "challenge": "広範なレビュー論文が引用順位を支配し、詳細な実証知見が散在して見える可能性があります",
        },
    },
}

IMPORTANT_VENUES = [
    "nature", "science", "cell", "neuron", "nature biomedical engineering",
    "nature neuroscience", "nature communications", "science robotics",
    "journal of neural engineering", "neuroimage", "ieee transactions",
    "ieee trans", "frontiers in neuroscience", "frontiers in neurorobotics",
    "brain", "npj", "plos", "elife", "neural networks",
]


def norm_text(value):
    return re.sub(r"\s+", " ", value or "").strip()


def safe_slug(value):
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value[:80] or "paper"


def period_chart_filename(kind, start, end):
    return f"{kind}_{start}_{end}.png"


def period_chart_src(kind, start, end):
    return f"assets/periods/{period_chart_filename(kind, start, end)}"


def taxonomy_visual_src(category):
    return f"assets/taxonomy/{safe_slug(category)}.svg"


def taxonomy_visual_svg(category):
    visual = TAXONOMY_VISUALS.get(category, TAXONOMY_VISUALS["General BCI Methods and Systems"])
    accent = visual["accent"]
    secondary = visual["secondary"]
    motif = visual["motif"]
    title = html.escape(category)
    common_brain = f"""
      <path d="M126 81c-20 0-35 13-35 32 0 20 14 35 34 35h37c19 0 34-14 34-33 0-18-14-32-32-32-5-13-19-22-38-22z" fill="#ffffff" stroke="{accent}" stroke-width="5" stroke-linejoin="round"/>
      <path d="M117 91c-9 6-13 16-9 25m23-29c-9 8-10 20-2 30m25-26c10 8 12 20 3 31m-42 10c13 8 29 8 44 0" fill="none" stroke="{secondary}" stroke-width="4" stroke-linecap="round"/>
      <circle cx="129" cy="124" r="3" fill="{accent}"/>
      <circle cx="153" cy="124" r="3" fill="{accent}"/>
      <path d="M133 135q9 7 18 0" fill="none" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
    """
    motifs = {
        "motor": f"""
          {common_brain}
          <path d="M79 158c31-8 47-20 60-39" fill="none" stroke="{accent}" stroke-width="7" stroke-linecap="round"/>
          <path d="M74 159l-20 23m26-20 19 22m-24-25 4-34" fill="none" stroke="{secondary}" stroke-width="8" stroke-linecap="round"/>
          <path d="M198 149c25-8 44-24 55-48" fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="round" stroke-dasharray="7 10"/>
          <path d="M249 96l8 3-2 9" fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
        """,
        "speller": f"""
          <rect x="67" y="55" width="185" height="123" rx="18" fill="#ffffff" stroke="{accent}" stroke-width="5"/>
          <path d="M115 188h90m-45-10v24" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
          <g fill="{secondary}">
            <rect x="91" y="78" width="32" height="25" rx="8"/>
            <rect x="143" y="78" width="32" height="25" rx="8"/>
            <rect x="195" y="78" width="32" height="25" rx="8"/>
            <rect x="91" y="119" width="32" height="25" rx="8"/>
            <rect x="143" y="119" width="32" height="25" rx="8"/>
            <rect x="195" y="119" width="32" height="25" rx="8"/>
          </g>
          <circle cx="159" cy="132" r="18" fill="#fff7ed" stroke="{accent}" stroke-width="5"/>
          <path d="M159 116l4 10 11 1-8 7 2 11-9-6-9 6 2-11-8-7 11-1z" fill="{accent}"/>
        """,
        "rehab": f"""
          <path d="M96 66v74c0 25 19 45 44 45h35c26 0 48-22 48-48v-37" fill="#ffffff" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
          <path d="M124 65v73m27-82v82m27-75v77m26-56v61" stroke="{secondary}" stroke-width="9" stroke-linecap="round"/>
          <path d="M91 132c29 2 52 16 67 42" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
          <circle cx="230" cy="66" r="18" fill="#dcfce7" stroke="{secondary}" stroke-width="5"/>
          <path d="M221 66h18m-9-9v18" stroke="{secondary}" stroke-width="5" stroke-linecap="round"/>
        """,
        "implant": f"""
          {common_brain}
          <g stroke="{accent}" stroke-width="5" stroke-linecap="round">
            <path d="M96 61l-28-28m54 25-9-36m56 43 26-37m17 74 42-9"/>
          </g>
          <g fill="{secondary}" stroke="#ffffff" stroke-width="3">
            <circle cx="68" cy="33" r="11"/>
            <circle cx="113" cy="22" r="11"/>
            <circle cx="195" cy="28" r="11"/>
            <circle cx="254" cy="93" r="11"/>
          </g>
          <rect x="115" y="151" width="92" height="31" rx="10" fill="#eef2ff" stroke="{accent}" stroke-width="5"/>
          <path d="M130 165h62" stroke="{secondary}" stroke-width="5" stroke-linecap="round"/>
        """,
        "deep": f"""
          <g stroke="{secondary}" stroke-width="4" opacity="0.9">
            <path d="M82 74l66 38-66 48m66-48 83-39m-83 39 82 47m-82-47v69"/>
            <path d="M82 160l67 21 81-22"/>
          </g>
          <g fill="#ffffff" stroke="{accent}" stroke-width="5">
            <circle cx="82" cy="74" r="18"/>
            <circle cx="82" cy="160" r="18"/>
            <circle cx="148" cy="112" r="18"/>
            <circle cx="149" cy="181" r="18"/>
            <circle cx="231" cy="73" r="18"/>
            <circle cx="230" cy="159" r="18"/>
          </g>
          <path d="M70 74h24m-12-12v24m137 71h22m-11-11v22" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>
        """,
        "eeg": f"""
          <rect x="58" y="55" width="204" height="124" rx="18" fill="#ffffff" stroke="{accent}" stroke-width="5"/>
          <path d="M77 118c18 0 12-42 31-42s11 83 32 83 13-71 34-71 13 53 34 53 12-31 34-31" fill="none" stroke="{secondary}" stroke-width="6" stroke-linecap="round"/>
          <path d="M85 189h150" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
          <path d="M108 70v95m52-95v95m52-95v95" stroke="#dbeafe" stroke-width="3"/>
          <path d="M226 58l22-28m-8 27 26-5" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
        """,
        "speech": f"""
          {common_brain}
          <path d="M203 62h49c20 0 36 15 36 34s-16 34-36 34h-20l-25 24 6-24h-10c-20 0-36-15-36-34s16-34 36-34z" fill="#ffffff" stroke="{accent}" stroke-width="5" stroke-linejoin="round"/>
          <circle cx="215" cy="96" r="5" fill="{secondary}"/>
          <circle cx="235" cy="96" r="5" fill="{secondary}"/>
          <circle cx="255" cy="96" r="5" fill="{secondary}"/>
          <path d="M79 169c24 16 58 16 82 0" fill="none" stroke="{secondary}" stroke-width="7" stroke-linecap="round"/>
        """,
        "hybrid": f"""
          {common_brain}
          <path d="M78 80c-22 33-17 79 13 108m151-6c29-34 29-80 1-113" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round"/>
          <path d="M78 80l2 19 17-8m145 91-18-2 7-17" fill="none" stroke="{accent}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M65 154c-21-19-5-51 20-34 25-17 41 15 20 34l-20 18z" fill="#fee2e2" stroke="{secondary}" stroke-width="5" stroke-linejoin="round"/>
          <circle cx="248" cy="62" r="22" fill="#f5f3ff" stroke="{secondary}" stroke-width="5"/>
          <path d="M248 48v14l11 7" stroke="{secondary}" stroke-width="5" stroke-linecap="round"/>
        """,
        "general": f"""
          {common_brain}
          <rect x="55" y="143" width="76" height="47" rx="10" fill="#ffffff" stroke="{accent}" stroke-width="5"/>
          <rect x="192" y="143" width="76" height="47" rx="10" fill="#ffffff" stroke="{secondary}" stroke-width="5"/>
          <path d="M132 166h58m-28-28v54" stroke="{accent}" stroke-width="5" stroke-linecap="round" stroke-dasharray="6 9"/>
          <path d="M74 160h38m-38 15h27m109-15h38m-38 15h26" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
        """,
    }
    motif_svg = motifs.get(motif, motifs["general"])
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="320" height="220" viewBox="0 0 320 220" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">Original license-safe schematic illustration for the {title} taxonomy.</desc>
  <rect width="320" height="220" rx="28" fill="#f8fafc"/>
  <circle cx="64" cy="54" r="35" fill="{secondary}" opacity="0.16"/>
  <circle cx="266" cy="176" r="41" fill="{accent}" opacity="0.12"/>
  <path d="M31 190c45-24 93-24 144 0s92 24 114 0" fill="none" stroke="#e2e8f0" stroke-width="7" stroke-linecap="round"/>
  {motif_svg}
</svg>
"""


def write_taxonomy_illustrations(categories):
    asset_dir = DOCS_DIR / "assets" / "taxonomy"
    asset_dir.mkdir(parents=True, exist_ok=True)
    for category in categories:
        target = asset_dir / f"{safe_slug(category)}.svg"
        target.write_text(taxonomy_visual_svg(category), encoding="utf-8")


def paper_key(paper):
    ext = paper.get("externalIds") or {}
    for key in ("DOI", "ArXiv", "PubMed", "CorpusId"):
        if ext.get(key):
            return f"{key}:{ext[key]}"
    return paper.get("paperId") or paper.get("url") or paper.get("title", "")


def is_relevant(paper):
    title = paper.get("title") or ""
    abstract = paper.get("abstract") or ""
    title_matches = title_relevance_count(paper)
    abstract_matches = sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, abstract, re.I))
    return title_matches >= 1 or abstract_matches >= 2


def title_relevance_count(paper):
    title = paper.get("title") or ""
    return sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, title, re.I))


def venue_name(paper):
    venue = paper.get("venue") or ""
    pv = paper.get("publicationVenue") or {}
    return norm_text(venue or pv.get("name") or "")


def author_text(paper, max_authors=6):
    authors = paper.get("authors") or []
    names = [norm_text(a.get("name", "")) for a in authors if a.get("name")]
    if len(names) > max_authors:
        return ", ".join(names[:max_authors]) + ", et al."
    return ", ".join(names)


def category_for(paper):
    text = f"{paper.get('title') or ''} {paper.get('abstract') or ''}".lower()
    for category, needles in CATEGORIES:
        if any(n in text for n in needles):
            return category
    return "General BCI Methods and Systems"


def primary_link(paper):
    ext = paper.get("externalIds") or {}
    if ext.get("DOI"):
        return f"https://doi.org/{ext['DOI']}"
    if ext.get("ArXiv"):
        return f"https://arxiv.org/abs/{ext['ArXiv']}"
    return paper.get("url") or ""


def importance_score(paper):
    """Transparent metadata score used to reduce 500 candidates to 100 papers."""
    title = paper.get("title") or ""
    abstract = paper.get("abstract") or ""
    venue = venue_name(paper)
    text = f"{title} {abstract}".lower()
    venue_l = venue.lower()
    citations = int(paper.get("citationCount") or 0)
    influential = int(paper.get("influentialCitationCount") or 0)
    score = math.log1p(citations) * 22.0 + math.log1p(influential) * 18.0
    reasons = [f"citations={citations}", f"influential={influential}"]

    if any(v in venue_l for v in IMPORTANT_VENUES):
        score += 10.0
        reasons.append("recognized venue")
    if re.search(r"\b(review|survey|meta-analysis|systematic review)\b", text):
        score += 7.0
        reasons.append("review/survey")
    if re.search(r"\b(dataset|benchmark|competition|open data)\b", text):
        score += 5.0
        reasons.append("dataset/benchmark")
    if re.search(r"\b(clinical|stroke|rehabilitation|prosthe|paralysis|patient)\b", text):
        score += 5.0
        reasons.append("clinical/rehab relevance")
    if re.search(r"\b(invasive|intracortical|implant|electrocorticography|ecog)\b", text):
        score += 5.0
        reasons.append("invasive/high-bandwidth BCI")
    if re.search(r"\b(deep learning|transformer|self-supervised|domain adaptation|foundation model)\b", text):
        score += 4.0
        reasons.append("modern ML method")
    match_count = sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, text, re.I))
    if match_count:
        score += min(8.0, match_count * 1.5)
        reasons.append(f"BCI term matches={match_count}")
    title_match_count = sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, title, re.I))
    if title_match_count:
        score += min(6.0, title_match_count * 2.0)
        reasons.append(f"title BCI matches={title_match_count}")
    if paper.get("openAccessPdf"):
        score += 1.0
        reasons.append("open PDF metadata")
    return round(score, 3), "; ".join(reasons)


def fetch_year_query(year, query, max_pages=2):
    params = {
        "query": query,
        "year": str(year),
        "fields": S2_FIELDS,
        "sort": "citationCount:desc",
    }
    out = []
    token = None
    for _ in range(max_pages):
        if token:
            params["token"] = token
        resp = requests.get(S2_BULK_URL, params=params, timeout=60)
        if resp.status_code == 429:
            time.sleep(8)
            resp = requests.get(S2_BULK_URL, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        out.extend(data.get("data") or [])
        token = data.get("token")
        if not token:
            break
        time.sleep(1.0)
    return out


def collect_papers():
    selected = {}
    all_candidates = {}
    for year in YEARS:
        merged = {}
        for query in QUERIES:
            print(f"[collect] {year} :: {query}", flush=True)
            try:
                for paper in fetch_year_query(year, query):
                    if paper.get("year") != year:
                        continue
                    if not paper.get("title") or not is_relevant(paper):
                        continue
                    merged[paper_key(paper)] = paper
            except Exception as exc:
                print(f"[warn] {year} {query}: {exc}", flush=True)
            time.sleep(1.0)

        ranked = sorted(
            merged.values(),
            key=lambda p: (
                importance_score(p)[0],
                int(p.get("citationCount") or 0),
                int(p.get("influentialCitationCount") or 0),
                p.get("title") or "",
            ),
            reverse=True,
        )
        candidate_pool = ranked[:CANDIDATES_PER_YEAR]
        citation_ranked = sorted(
            candidate_pool,
            key=lambda p: (
                int(p.get("citationCount") or 0),
                int(p.get("influentialCitationCount") or 0),
                importance_score(p)[0],
                p.get("title") or "",
            ),
            reverse=True,
        )
        selected_pool = citation_ranked[:TARGET_PER_YEAR]
        all_candidates[year] = [normalize_paper(p, year, i + 1, candidate=True) for i, p in enumerate(candidate_pool)]
        selected[year] = [normalize_paper(p, year, i + 1) for i, p in enumerate(selected_pool)]
        print(
            f"[collect] {year}: selected {len(selected[year])}/{TARGET_PER_YEAR} "
            f"by citations from top {len(candidate_pool)}/{min(CANDIDATES_PER_YEAR, len(ranked))} candidates "
            f"({len(ranked)} relevant records)",
            flush=True,
        )
    return selected, all_candidates


def normalize_paper(paper, year, rank, candidate=False):
    ext = paper.get("externalIds") or {}
    oa = paper.get("openAccessPdf") or {}
    fields = paper.get("s2FieldsOfStudy") or []
    score, reasons = importance_score(paper)
    return {
        "year": year,
        "rank": rank,
        "candidateRank": rank if candidate else "",
        "selectionRank": "" if candidate else rank,
        "importanceScore": score,
        "importanceReasons": reasons,
        "paperId": paper.get("paperId", ""),
        "title": norm_text(paper.get("title", "")),
        "authors": author_text(paper),
        "venue": venue_name(paper),
        "publicationDate": paper.get("publicationDate") or "",
        "citationCount": int(paper.get("citationCount") or 0),
        "influentialCitationCount": int(paper.get("influentialCitationCount") or 0),
        "category": category_for(paper),
        "abstract": norm_text(paper.get("abstract", "")),
        "doi": ext.get("DOI", ""),
        "arxiv": ext.get("ArXiv", ""),
        "pubmed": str(ext.get("PubMed", "")),
        "url": primary_link(paper),
        "semanticScholarUrl": paper.get("url", ""),
        "openAccessPdf": oa.get("url", "") if isinstance(oa, dict) else "",
        "fieldsOfStudy": "; ".join(sorted({f.get("category", "") for f in fields if f.get("category")})),
        "candidate": candidate,
    }


def write_json_csv(selected, candidates):
    flat = [paper for year in YEARS for paper in selected.get(year, [])]
    candidate_flat = [paper for year in YEARS for paper in candidates.get(year, [])]
    DATA_DIR.mkdir(exist_ok=True)
    with (DATA_DIR / PAPERS_JSON).open("w", encoding="utf-8") as f:
        json.dump({
            "generated": date.today().isoformat(),
            "candidate_pool_per_year": CANDIDATES_PER_YEAR,
            "target_per_year": TARGET_PER_YEAR,
            "papers": flat,
        }, f, ensure_ascii=False, indent=2)
    with (DATA_DIR / CANDIDATES_JSON).open("w", encoding="utf-8") as f:
        json.dump({
            "generated": date.today().isoformat(),
            "candidate_pool_per_year": CANDIDATES_PER_YEAR,
            "candidates": candidate_flat,
        }, f, ensure_ascii=False, indent=2)
    fields = list(flat[0].keys()) if flat else []
    candidate_fields = list(candidate_flat[0].keys()) if candidate_flat else fields
    with (DATA_DIR / PAPERS_CSV).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(flat)
    with (DATA_DIR / CANDIDATES_CSV).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=candidate_fields)
        writer.writeheader()
        writer.writerows(candidate_flat)
    for year in YEARS:
        rows = selected.get(year, [])
        with (DATA_DIR / f"papers_{year}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        candidate_rows = candidates.get(year, [])
        with (DATA_DIR / f"candidates_top500_{year}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=candidate_fields)
            writer.writeheader()
            writer.writerows(candidate_rows)
    return flat


def year_stats(flat):
    by_year = defaultdict(list)
    for p in flat:
        by_year[p["year"]].append(p)
    stats = {}
    for year, rows in by_year.items():
        stats[year] = {
            "count": len(rows),
            "citations": sum(p["citationCount"] for p in rows),
            "influential": sum(p["influentialCitationCount"] for p in rows),
            "top": rows[0] if rows else None,
        }
    return stats


def category_stats(flat):
    return Counter(p["category"] for p in flat)


def md_link(label, url):
    label = label.replace("|", "\\|")
    return f"[{label}]({url})" if url else label


def first_sentence(value, fallback="Metadata-only record; no abstract sentence was available."):
    text = norm_text(value)
    if not text:
        return fallback
    parts = re.split(r"(?<=[.!?])\s+", text)
    return parts[0][:360].rstrip()


def method_tags(p):
    text = f"{p.get('title', '')} {p.get('abstract', '')}".lower()
    tags = []
    checks = [
        ("review", r"\b(review|survey|meta-analysis|systematic review)\b"),
        ("dataset/benchmark", r"\b(dataset|benchmark|competition|open data)\b"),
        ("clinical/rehab", r"\b(clinical|stroke|rehabilitation|prosthe|patient|paralysis)\b"),
        ("invasive", r"\b(invasive|intracortical|implant|electrocorticography|ecog)\b"),
        ("deep learning", r"\b(deep learning|cnn|convolution|transformer|graph neural|self-supervised|domain adaptation)\b"),
        ("communication", r"\b(speech|language|speller|typing|communication)\b"),
        ("closed-loop", r"\b(closed-loop|closed loop|neurofeedback|adaptive)\b"),
    ]
    for label, pattern in checks:
        if re.search(pattern, text):
            tags.append(label)
    return tags[:4] or ["BCI method"]


def enrich_paper(p):
    """Add reproducible interpretation fields from title, abstract, and metadata."""
    abstract = p.get("abstract", "")
    idea = first_sentence(abstract, f"Positions {p.get('title', 'this paper')} within {p.get('category', 'BCI research')}.")
    tags = method_tags(p)
    strengths = []
    if p.get("citationCount", 0) >= 100:
        strengths.append(f"high citation signal ({p['citationCount']:,})")
    if p.get("influentialCitationCount", 0) >= 10:
        strengths.append(f"influential citation signal ({p['influentialCitationCount']:,})")
    if "recognized venue" in p.get("importanceReasons", ""):
        strengths.append("recognized venue")
    if p.get("openAccessPdf"):
        strengths.append("open-access PDF metadata")
    if not strengths:
        strengths.append("selected by citation count from the audited BCI candidate pool")

    limitations = []
    if not abstract:
        limitations.append("abstract unavailable in metadata")
    if not p.get("venue"):
        limitations.append("venue missing in metadata")
    if p.get("year", 0) >= 2025:
        limitations.append("recent work may be under-cited")
    if p.get("citationCount", 0) < 25:
        limitations.append("limited citation history")
    if not p.get("openAccessPdf"):
        limitations.append("PDF link not available from metadata")
    if not limitations:
        limitations.append("metadata-level appraisal; full PDF review still needed")

    enriched = dict(p)
    enriched["keyIdea"] = idea
    enriched["strengths"] = "; ".join(strengths[:3])
    enriched["limitations"] = "; ".join(limitations[:3])
    enriched["methodTags"] = "; ".join(tags)
    enriched["paperLink"] = p.get("url") or p.get("semanticScholarUrl") or ""
    return enriched


def enriched_flat(flat):
    return [enrich_paper(p) for p in flat]


def category_groups(flat):
    groups = defaultdict(list)
    for p in enriched_flat(flat):
        groups[p["category"]].append(p)
    for rows in groups.values():
        rows.sort(key=lambda p: (p["citationCount"], p["influentialCitationCount"], p["importanceScore"]), reverse=True)
    return groups


def taxonomy_trends(category):
    return TAXONOMY_TRENDS.get(category, TAXONOMY_TRENDS["General BCI Methods and Systems"])


def taxonomy_limitations(category):
    return TAXONOMY_LIMITATIONS.get(category, TAXONOMY_LIMITATIONS["General BCI Methods and Systems"])


def category_localization(category, language):
    profile = CATEGORY_LOCALIZATION.get(category, CATEGORY_LOCALIZATION["General BCI Methods and Systems"])
    return profile.get(language, profile["en"])


def period_key(start, end):
    return f"{start}-{end}"


def period_label(start, end):
    if start == START_YEAR and end == END_YEAR:
        return f"All years ({YEAR_RANGE_TEXT})"
    return str(start) if start == end else f"{start}-{end}"


def all_period_ranges():
    return [(start, end) for start in YEARS for end in range(start, END_YEAR + 1)]


def period_select_ranges():
    full_range = (START_YEAR, END_YEAR)
    return [full_range] + [range_pair for range_pair in all_period_ranges() if range_pair != full_range]


def top_metadata_values(rows, key, limit=3):
    counts = Counter()
    for row in rows:
        value = row.get(key) or ""
        if key == "methodTags":
            for tag in value.split("; "):
                if tag:
                    counts[tag] += 1
        elif value:
            counts[value] += 1
    return [value for value, _ in counts.most_common(limit)]


def language_period_analysis(language, category, rows, start, end):
    profile = category_localization(category, language)
    count = len(rows)
    citations = sum(p["citationCount"] for p in rows)
    top = max(rows, key=lambda p: (p["citationCount"], p["influentialCitationCount"], p["title"]))
    year_counts = Counter(p["year"] for p in rows)
    active_year, active_count = year_counts.most_common(1)[0]
    no_pdf = sum(1 for p in rows if not p.get("openAccessPdf"))
    no_abstract = sum(1 for p in rows if not p.get("abstract"))
    limited_citation = sum(1 for p in rows if p.get("citationCount", 0) < 25)
    recent = sum(1 for p in rows if p.get("year", 0) >= END_YEAR - 1)
    tags = ", ".join(top_metadata_values(rows, "methodTags")) or profile["focus"]
    venues = ", ".join(top_metadata_values(rows, "venue")) or "mixed venues"
    top_title = top["title"]
    top_citations = top["citationCount"]

    templates = {
        "en": {
            "overview": [
                f"In {start}-{end}, {profile['name']} contains {count:,} selected papers and {citations:,} citations. The most active year is {active_year} ({active_count:,} papers), and the leading citation-ranked paper is \"{top_title}\" ({top_citations:,} citations).",
                f"The category emphasis in this period is {profile['focus']}. Frequent metadata tags include {tags}, with visible venue concentration around {venues}.",
            ],
            "limitations": [
                f"Metadata limitations in this period: {no_pdf:,} papers lack open PDF links, {no_abstract:,} lack abstracts, {limited_citation:,} have limited citation history, and {recent:,} recent papers may be under-cited.",
                f"Interpretation caution: {profile['challenge']}. Because final ranking is citation-based, newer or niche papers can be understated even when scientifically important.",
            ],
        },
        "ko": {
            "overview": [
                f"{start}-{end} 기간의 {profile['name']} 분류에는 선정 논문 {count:,}편과 인용 {citations:,}회가 포함됩니다. 가장 활발한 해는 {active_year}년({active_count:,}편)이며, 인용 기준 대표 논문은 \"{top_title}\"({top_citations:,}회)입니다.",
                f"이 기간의 핵심 초점은 {profile['focus']}입니다. 자주 나타나는 메타데이터 태그는 {tags}이고, 주요 venue 신호는 {venues}에 집중됩니다.",
            ],
            "limitations": [
                f"이 기간의 메타데이터 한계는 다음과 같습니다. 공개 PDF 링크가 없는 논문 {no_pdf:,}편, 초록이 없는 논문 {no_abstract:,}편, 인용 이력이 짧은 논문 {limited_citation:,}편, 최신 논문이라 저인용될 수 있는 논문 {recent:,}편이 있습니다.",
                f"해석 시 주의점: {profile['challenge']}. 최종 순위가 인용회수 기반이므로 최신 또는 세부 주제 논문은 과소평가될 수 있습니다.",
            ],
        },
        "zh": {
            "overview": [
                f"在 {start}-{end} 期间，{profile['name']} 类别包含 {count:,} 篇入选论文和 {citations:,} 次引用。最活跃年份是 {active_year} 年（{active_count:,} 篇），引用排序最高的代表论文是“{top_title}”（{top_citations:,} 次引用）。",
                f"该时期的类别重点是{profile['focus']}。常见元数据标签包括 {tags}，主要期刊/会议信号集中在 {venues}。",
            ],
            "limitations": [
                f"该时期的元数据局限包括：{no_pdf:,} 篇论文缺少开放 PDF 链接，{no_abstract:,} 篇缺少摘要，{limited_citation:,} 篇引用历史较短，{recent:,} 篇近期论文可能被低估。",
                f"解释时需注意：{profile['challenge']}。由于最终排序基于引用次数，新近或细分方向的重要论文可能被低估。",
            ],
        },
        "ja": {
            "overview": [
                f"{start}-{end} 年の {profile['name']} には、選定論文 {count:,} 本と引用 {citations:,} 件が含まれます。最も活発な年は {active_year} 年（{active_count:,} 本）で、引用順の代表論文は「{top_title}」（{top_citations:,} 件）です。",
                f"この期間の主な焦点は {profile['focus']} です。頻出するメタデータタグは {tags} で、主な掲載先シグナルは {venues} に見られます。",
            ],
            "limitations": [
                f"この期間のメタデータ上の限界は、公開 PDF リンクなし {no_pdf:,} 本、抄録なし {no_abstract:,} 本、引用履歴が短い論文 {limited_citation:,} 本、最近のため過小引用の可能性がある論文 {recent:,} 本です。",
                f"解釈上の注意点: {profile['challenge']}。最終順位は引用数に基づくため、新しい論文や細分化された重要研究は過小評価されることがあります。",
            ],
        },
    }
    result = templates[language]
    result["categoryName"] = profile["name"]
    return result


def build_period_analysis(flat):
    enriched = enriched_flat(flat)
    ranges = [
        {"key": period_key(start, end), "label": period_label(start, end), "from": start, "to": end}
        for start, end in period_select_ranges()
    ]
    analysis = {}
    for start, end in all_period_ranges():
        range_rows = [p for p in enriched if start <= p["year"] <= end]
        groups = category_groups(range_rows)
        range_entry = {}
        for category, rows in groups.items():
            if not rows:
                continue
            slug = safe_slug(category)
            range_entry[slug] = {
                language: language_period_analysis(language, category, rows, start, end)
                for language in LANGUAGES
            }
        analysis[period_key(start, end)] = range_entry
    return {
        "generated": date.today().isoformat(),
        "yearRange": YEAR_RANGE_TEXT,
        "languages": LANGUAGES,
        "uiLabels": UI_LABELS,
        "ranges": ranges,
        "analysis": analysis,
    }


def write_period_analysis(flat):
    payload = build_period_analysis(flat)
    DATA_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "data").mkdir(exist_ok=True)
    for target in (DATA_DIR / PERIOD_ANALYSIS_JSON, DOCS_DIR / "data" / PERIOD_ANALYSIS_JSON):
        with target.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))


def write_taxonomy_dataset(flat):
    rows = []
    for category, papers in sorted(category_groups(flat).items()):
        for idx, p in enumerate(papers, 1):
            row = dict(p)
            row["taxonomyRank"] = idx
            row["categoryOverview"] = " ".join(taxonomy_trends(category))
            row["categoryLimitations"] = " ".join(taxonomy_limitations(category))
            row["researchTrend"] = row["categoryOverview"]
            rows.append(row)
    if not rows:
        return
    fields = [
        "category", "taxonomyRank", "year", "title", "authors", "venue", "publicationDate",
        "citationCount", "influentialCitationCount", "importanceScore", "categoryOverview",
        "categoryLimitations", "researchTrend", "methodTags",
        "keyIdea", "strengths", "limitations", "paperLink", "semanticScholarUrl",
        "openAccessPdf", "doi", "arxiv", "pubmed", "fieldsOfStudy",
    ]
    with (DATA_DIR / TAXONOMY_CSV).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def readme_taxonomy_table(rows, total_count):
    out = [
        '<table width="100%">',
        "<colgroup>",
        '<col width="5%">',
        '<col width="22%">',
        '<col width="13%">',
        '<col width="30%">',
        '<col width="15%">',
        '<col width="15%">',
        "</colgroup>",
        "<thead>",
        "<tr>",
        '<th align="right">Rank</th>',
        "<th>Paper</th>",
        "<th>Meta</th>",
        "<th>Key idea</th>",
        "<th>Strengths</th>",
        "<th>Limitations</th>",
        "</tr>",
        "</thead>",
        "<tbody>",
    ]
    for idx, p in enumerate(rows, 1):
        title = html.escape(p["title"])
        link = html.escape(p["paperLink"])
        paper = f'<a href="{link}">{title}</a>' if link else title
        authors = html.escape(p["authors"] or "Unknown authors")
        venue = html.escape(p["venue"] or "Unknown venue")
        out.extend([
            "<tr>",
            f'<td align="right" width="5%">{idx}</td>',
            f'<td width="22%">{paper}<br><sub>{authors}</sub></td>',
            f'<td width="13%">{p["year"]}<br>{venue}<br>{p["citationCount"]:,} citations</td>',
            f'<td width="30%">{html.escape(p["keyIdea"])}</td>',
            f'<td width="15%">{html.escape(p["strengths"])}</td>',
            f'<td width="15%">{html.escape(p["limitations"])}</td>',
            "</tr>",
        ])
    if total_count > len(rows):
        out.extend([
            "<tr>",
            f'<td colspan="6">See the website and taxonomy CSV for all {total_count} papers.</td>',
            "</tr>",
        ])
    out.extend(["</tbody>", "</table>"])
    return out


def write_readme(flat):
    stats = year_stats(flat)
    cats = category_stats(flat)
    groups = category_groups(flat)
    lines = [
        "# Awesome BCI",
        "",
        "[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)",
        "",
        "A taxonomy-first, citation-ranked map of recent Brain-Computer Interface (BCI) research.",
        "",
        f"Generated on {date.today().isoformat()} from free public Semantic Scholar metadata. The current edition investigates up to {CANDIDATES_PER_YEAR} BCI-related candidate papers per year for {YEAR_RANGE_TEXT}, keeps an audited candidate pool, selects the top {TARGET_PER_YEAR} papers per year by citation count, and reorganizes the final {len(flat):,} papers by research taxonomy.",
        "",
        "## Project Links",
        "",
        "- Website: https://honggi82.github.io/awesome-BCI/",
        f"- Selected dataset: `data/{PAPERS_CSV}`",
        f"- Taxonomy dataset with paper-level ideas, strengths, and limitations: `data/{TAXONOMY_CSV}`",
        f"- Precomputed period and language analysis: `data/{PERIOD_ANALYSIS_JSON}`",
        f"- Candidate pool: `data/{CANDIDATES_CSV}`",
        "- English review draft: `paper/review_en.html`, `paper/review_en.docx`",
        "- Korean review draft: `paper/review_ko.html`",
        "",
        "## Taxonomy Overview",
        "",
        f"- **Total selected papers**: {len(flat):,} papers",
    ]
    for cat, count in cats.most_common():
        lines.append(f"- **{cat}**: {count} papers")

    lines.extend(["", "## Taxonomy Collections", ""])
    for cat, _ in cats.most_common():
        rows = groups[cat]
        top = rows[:30]
        years = sorted({p["year"] for p in rows})
        citations = sum(p["citationCount"] for p in rows)
        lines.extend([
            f"### {cat}",
            "",
            f"- Papers selected: **{len(rows)}**",
            f"- Years covered: **{years[0]}-{years[-1]}**",
            f"- Citation count in selected set: **{citations:,}**",
            "- Category Overview (main research trends):",
            *[f"  - {trend}" for trend in taxonomy_trends(cat)],
            "- Limitations:",
            *[f"  - {limitation}" for limitation in taxonomy_limitations(cat)],
            "",
            "<details>",
            f"<summary>Show representative papers for {cat}</summary>",
            "",
        ])
        lines.extend(readme_taxonomy_table(top, len(rows)))
        lines.extend(["", "</details>", ""])

    lines.extend([
        "## Yearly Coverage",
        "",
        "| Year | Selected papers | Citation count | Top paper |",
        "| ---: | ---: | ---: | --- |",
    ])
    by_year = defaultdict(list)
    for p in flat:
        by_year[p["year"]].append(p)
    for year in YEARS:
        rows = by_year.get(year, [])
        top = rows[0] if rows else None
        top_link = md_link(top["title"], top["url"]) if top else "n/a"
        lines.append(
            f"| {year} | {len(rows)} | {stats.get(year, {}).get('citations', 0):,} | {top_link} |"
        )
    lines.extend([
        "## Method",
        "",
        "The collection uses Semantic Scholar's Academic Graph paper search. Queries combine broad BCI terms and common subfields, results are filtered to the target publication year, relevance-filtered by BCI terms in title/abstract, deduplicated by DOI/arXiv/PubMed/CorpusId/paperId, and reduced to a maximum of 500 candidates per year. Importance scoring is retained for candidate auditing and combines log-scaled citation count, log-scaled influential citation count, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive/high-bandwidth interfaces, and modern ML methods. The final awesome list selects the top 100 papers per year by citation count from the audited candidate pool.",
        "",
        "## Caveats",
        "",
        f"- Citation counts favor older papers and may under-rank recent {END_YEAR} work.",
        "- Metadata search is not equivalent to a full systematic review of PDFs.",
        "- Some venues and publication dates are missing in upstream metadata.",
    ])
    (ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def category_summary(category, rows):
    top_tags = Counter()
    for p in rows:
        for tag in p.get("methodTags", "").split("; "):
            if tag:
                top_tags[tag] += 1
    lead = rows[0] if rows else {}
    return {
        "count": len(rows),
        "years": f"{min(p['year'] for p in rows)}-{max(p['year'] for p in rows)}" if rows else "",
        "citations": sum(p["citationCount"] for p in rows),
        "top": lead.get("title", "n/a"),
        "tags": ", ".join(tag for tag, _ in top_tags.most_common(4)) or "BCI method",
        "trends": taxonomy_trends(category),
        "limitations": taxonomy_limitations(category),
    }


def paper_card(p, taxonomy_rank):
    title = html.escape(p["title"])
    link = html.escape(p["paperLink"])
    semantic = html.escape(p.get("semanticScholarUrl") or "")
    pdf = html.escape(p.get("openAccessPdf") or "")
    data_title = html.escape(p["title"], quote=True)
    data_venue = html.escape(p["venue"] or "Unknown venue", quote=True)
    data_limitations = html.escape(p["limitations"], quote=True)
    paper_link = f'<a href="{link}">Paper</a>' if link else ""
    semantic_link = f'<a href="{semantic}">Semantic Scholar</a>' if semantic else ""
    pdf_link = f'<a href="{pdf}">PDF</a>' if pdf else ""
    links = " ".join(x for x in [paper_link, semantic_link, pdf_link] if x) or "No link"
    return f"""
      <article class="paper-card" data-year="{p['year']}" data-citations="{p['citationCount']}" data-title="{data_title}" data-venue="{data_venue}" data-limitations="{data_limitations}">
        <div class="paper-rank">#{taxonomy_rank}</div>
        <div class="paper-body">
          <h3>{f'<a href="{link}">{title}</a>' if link else title}</h3>
          <p class="authors">{html.escape(p["authors"] or "Unknown authors")}</p>
          <div class="meta">
            <span>{p["year"]}</span>
            <span>{html.escape(p["venue"] or "Unknown venue")}</span>
            <span>{p["citationCount"]:,} citations</span>
            <span>{p["influentialCitationCount"]:,} influential</span>
            <span>score {p["importanceScore"]}</span>
          </div>
          <p><strong>Key idea:</strong> {html.escape(p["keyIdea"])}</p>
          <div class="assessment">
            <p><strong>Strengths:</strong> {html.escape(p["strengths"])}</p>
            <p><strong>Limitations:</strong> {html.escape(p["limitations"])}</p>
          </div>
          <p class="tags">{html.escape(p["methodTags"])}</p>
          <p class="links">{links}</p>
        </div>
      </article>
    """


def taxonomy_section(category, rows):
    slug = safe_slug(category)
    summary = category_summary(category, rows)
    cards = "\n".join(paper_card(p, idx) for idx, p in enumerate(rows, 1))
    return f"""
    <section id="{slug}" class="taxonomy-section" data-category="{slug}">
      <details>
        <summary>
          <span class="summary-title">{html.escape(category)}</span>
          <span class="category-count">{summary['count']} papers</span>
          <span class="category-years">{summary['years']}</span>
          <span class="category-citations">{summary['citations']:,} citations</span>
        </summary>
        <div class="section-intro">
          <div class="section-visual"><img src="{taxonomy_visual_src(category)}" alt="{html.escape(category)} illustration"></div>
          <p><strong>Representative emphasis:</strong> {html.escape(summary['tags'])}</p>
          <p><strong>Top-ranked paper:</strong> <span class="top-paper">{html.escape(summary['top'])}</span></p>
          <div class="insight-grid">
            <div class="insight-box">
              <strong class="overview-heading">Category Overview</strong>
              <ul class="category-overview-list">{''.join(f'<li>{html.escape(trend)}</li>' for trend in summary['trends'])}</ul>
            </div>
            <div class="insight-box limitation-box">
              <strong class="limitation-heading">Limitations</strong>
              <ul class="category-limitations-list">{''.join(f'<li>{html.escape(limitation)}</li>' for limitation in summary['limitations'])}</ul>
            </div>
          </div>
        </div>
        <div class="paper-list">{cards}</div>
      </details>
    </section>
    """


def write_site(flat):
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "assets").mkdir(exist_ok=True)
    (DOCS_DIR / "data").mkdir(exist_ok=True)
    (DOCS_DIR / "paper").mkdir(exist_ok=True)
    groups = category_groups(flat)
    cats = category_stats(flat)
    write_taxonomy_illustrations([cat for cat, _ in cats.most_common()])
    total_cites = sum(p["citationCount"] for p in flat)
    start_year_options = "\n".join(
        f'<option value="{year}"{" selected" if year == min(YEARS) else ""}>{year}</option>'
        for year in YEARS
    )
    end_year_options = "\n".join(
        f'<option value="{year}"{" selected" if year == max(YEARS) else ""}>{year}</option>'
        for year in YEARS
    )
    period_options = "\n".join(
        f'<option value="{period_key(start, end)}" data-from="{start}" data-to="{end}"{" selected" if start == START_YEAR and end == END_YEAR else ""}>{period_label(start, end)}</option>'
        for start, end in period_select_ranges()
    )
    language_options = "\n".join(
        f'<option value="{code}"{" selected" if code == "en" else ""}>{html.escape(label)}</option>'
        for code, label in LANGUAGES.items()
    )
    year_filter_script = """
  <script>
    (() => {
      const periodSelect = document.getElementById("periodPreset");
      const languageSelect = document.getElementById("languageSelect");
      const startSelect = document.getElementById("startYear");
      const endSelect = document.getElementById("endYear");
      const resetButton = document.getElementById("resetYears");
      const rangeStatus = document.getElementById("rangeStatus");
      const statPapers = document.getElementById("statPapers");
      const statYears = document.getElementById("statYears");
      const statCitations = document.getElementById("statCitations");
      const statCategories = document.getElementById("statCategories");
      const taxonomyTotalSummary = document.getElementById("taxonomyTotalSummary");
      const categoryChart = document.getElementById("categoryDistributionChart");
      const citationChart = document.getElementById("yearlyCitationsChart");
      const categoryChartCaption = document.getElementById("categoryChartCaption");
      const citationChartCaption = document.getElementById("citationChartCaption");
      const defaultStart = startSelect.value;
      const defaultEnd = endSelect.value;
      const validYears = Array.from(startSelect.options).map(option => option.value);
      const periodOptions = Array.from(periodSelect.options);
      const defaultLanguage = languageSelect.value;
      let precomputed = null;

      function formatNumber(value) {
        return Number(value).toLocaleString("en-US");
      }

      function yearRangeText(years) {
        if (!years.length) return "No years";
        const sorted = [...new Set(years)].sort((a, b) => a - b);
        return sorted[0] === sorted[sorted.length - 1]
          ? String(sorted[0])
          : `${sorted[0]}-${sorted[sorted.length - 1]}`;
      }

      function selectedRangeValue(start, end) {
        const match = periodOptions.find(option =>
          option.dataset.from === String(start) && option.dataset.to === String(end)
        );
        return match ? match.value : "custom";
      }

      function updatePeriodSelect(start, end) {
        periodSelect.value = selectedRangeValue(start, end);
      }

      function setFromUrl() {
        const params = new URLSearchParams(window.location.search);
        const lang = params.get("lang");
        if (lang && Array.from(languageSelect.options).some(option => option.value === lang)) {
          languageSelect.value = lang;
        }
        const period = params.get("period");
        if (period) {
          const option = periodOptions.find(item => item.value === period && item.dataset.from && item.dataset.to);
          if (option) {
            periodSelect.value = period;
            startSelect.value = option.dataset.from;
            endSelect.value = option.dataset.to;
            return;
          }
        }
        const from = params.get("from");
        const to = params.get("to");
        if (validYears.includes(from)) startSelect.value = from;
        if (validYears.includes(to)) endSelect.value = to;
        updatePeriodSelect(startSelect.value, endSelect.value);
      }

      function syncUrl(start, end) {
        const url = new URL(window.location.href);
        const language = languageSelect.value;
        if (language === defaultLanguage) {
          url.searchParams.delete("lang");
        } else {
          url.searchParams.set("lang", language);
        }
        if (String(start) === defaultStart && String(end) === defaultEnd) {
          url.searchParams.delete("period");
          url.searchParams.delete("from");
          url.searchParams.delete("to");
        } else {
          const periodValue = selectedRangeValue(start, end);
          if (periodValue !== "custom") {
            url.searchParams.set("period", periodValue);
            url.searchParams.delete("from");
            url.searchParams.delete("to");
          } else {
            url.searchParams.delete("period");
            url.searchParams.set("from", start);
            url.searchParams.set("to", end);
          }
        }
        window.history.replaceState(null, "", url);
      }

      function rangeKey(start, end) {
        return `${start}-${end}`;
      }

      function rangeLabel(start, end) {
        return start === end ? String(start) : `${start}-${end}`;
      }

      function chartPath(kind, start, end) {
        return `assets/periods/${kind}_${start}_${end}.png`;
      }

      function updateCharts(start, end) {
        const label = rangeLabel(start, end);
        if (categoryChart) {
          categoryChart.src = chartPath("category_distribution", start, end);
          categoryChart.alt = `Category distribution chart for ${label}`;
        }
        if (citationChart) {
          citationChart.src = chartPath("yearly_citations", start, end);
          citationChart.alt = `Yearly citation chart for ${label}`;
        }
        if (categoryChartCaption) categoryChartCaption.textContent = `Category distribution (${label})`;
        if (citationChartCaption) citationChartCaption.textContent = `Yearly citation mass (${label})`;
      }

      function labels() {
        return precomputed?.uiLabels?.[languageSelect.value] || precomputed?.uiLabels?.en || {
          papers: "papers",
          categories: "categories",
          overview: "Category Overview",
          limitations: "Limitations",
          analysis: "Selected-period analysis",
          totalSelected: "Total selected papers",
          categoryCount: "Categories"
        };
      }

      function setList(target, items) {
        if (!target || !items) return;
        target.innerHTML = "";
        items.forEach(item => {
          const li = document.createElement("li");
          li.textContent = item;
          target.appendChild(li);
        });
      }

      function applyPrecomputedAnalysis(section, start, end) {
        const language = languageSelect.value;
        const entry = precomputed?.analysis?.[rangeKey(start, end)]?.[section.dataset.category];
        const analysis = entry?.[language] || entry?.en;
        if (!analysis) return;
        const copy = labels();
        const title = section.querySelector(".summary-title");
        if (title) title.textContent = analysis.categoryName;
        const card = document.querySelector(`.taxonomy-card[data-category="${section.dataset.category}"] strong`);
        if (card) card.textContent = analysis.categoryName;
        const overviewHeading = section.querySelector(".overview-heading");
        const limitationHeading = section.querySelector(".limitation-heading");
        if (overviewHeading) overviewHeading.textContent = copy.overview;
        if (limitationHeading) limitationHeading.textContent = copy.limitations;
        setList(section.querySelector(".category-overview-list"), analysis.overview);
        setList(section.querySelector(".category-limitations-list"), analysis.limitations);
      }

      function applyYearFilter(sync = true) {
        let start = Number(startSelect.value);
        let end = Number(endSelect.value);
        const copy = labels();
        if (start > end) {
          const previousStart = start;
          start = end;
          end = previousStart;
          startSelect.value = String(start);
          endSelect.value = String(end);
        }

        let totalPapers = 0;
        let totalCitations = 0;
        let activeCategories = 0;
        const activeYears = [];

        document.querySelectorAll(".taxonomy-section").forEach(section => {
          let sectionCount = 0;
          let sectionCitations = 0;
          const sectionYears = [];

          section.querySelectorAll(".paper-card").forEach(card => {
            const year = Number(card.dataset.year);
            const citations = Number(card.dataset.citations || 0);
            const visible = year >= start && year <= end;
            card.hidden = !visible;
            if (visible) {
              sectionCount += 1;
              sectionCitations += citations;
              sectionYears.push(year);
              activeYears.push(year);
            }
          });

          const hasPapers = sectionCount > 0;
          section.hidden = !hasPapers;
          const overview = document.querySelector(`.taxonomy-card[data-category="${section.dataset.category}"]`);
          if (overview) {
            overview.hidden = !hasPapers;
            const overviewCount = overview.querySelector(".overview-count");
            if (overviewCount) overviewCount.textContent = `${formatNumber(sectionCount)} ${copy.papers}`;
          }
          if (!hasPapers) return;

          activeCategories += 1;
          totalPapers += sectionCount;
          totalCitations += sectionCitations;
          section.querySelector(".category-count").textContent = `${formatNumber(sectionCount)} ${copy.papers}`;
          section.querySelector(".category-years").textContent = yearRangeText(sectionYears);
          section.querySelector(".category-citations").textContent = `${formatNumber(sectionCitations)} citations`;
          const topPaper = section.querySelector(".paper-card:not([hidden]) h3");
          const topPaperTarget = section.querySelector(".top-paper");
          if (topPaper && topPaperTarget) topPaperTarget.textContent = topPaper.textContent.trim();
          applyPrecomputedAnalysis(section, start, end);
        });

        statPapers.textContent = formatNumber(totalPapers);
        statYears.textContent = formatNumber(new Set(activeYears).size);
        statCitations.textContent = formatNumber(totalCitations);
        statCategories.textContent = formatNumber(activeCategories);
        updatePeriodSelect(start, end);
        updateCharts(start, end);
        if (taxonomyTotalSummary) {
          taxonomyTotalSummary.innerHTML = `<strong>${copy.totalSelected}:</strong> ${formatNumber(totalPapers)} ${copy.papers}; <strong>${copy.categoryCount}:</strong> ${formatNumber(activeCategories)} ${copy.categories}.`;
        }
        rangeStatus.textContent = `${start}-${end} · ${formatNumber(totalPapers)} ${copy.papers} · ${formatNumber(activeCategories)} ${copy.categories}`;
        if (sync) syncUrl(start, end);
      }

      setFromUrl();
      applyYearFilter(false);
      fetch("data/__ANALYSIS_JSON__")
        .then(response => response.json())
        .then(data => {
          precomputed = data;
          applyYearFilter(false);
        })
        .catch(() => {
          rangeStatus.textContent = "Precomputed analysis could not be loaded.";
        });
      periodSelect.addEventListener("change", () => {
        const option = periodSelect.selectedOptions[0];
        if (option && option.dataset.from && option.dataset.to) {
          startSelect.value = option.dataset.from;
          endSelect.value = option.dataset.to;
        }
        applyYearFilter(true);
      });
      languageSelect.addEventListener("change", () => applyYearFilter(true));
      startSelect.addEventListener("change", () => applyYearFilter(true));
      endSelect.addEventListener("change", () => applyYearFilter(true));
      resetButton.addEventListener("click", () => {
        startSelect.value = defaultStart;
        endSelect.value = defaultEnd;
        periodSelect.value = `${defaultStart}-${defaultEnd}`;
        applyYearFilter(true);
      });
    })();
  </script>
""".replace("__ANALYSIS_JSON__", PERIOD_ANALYSIS_JSON)
    sections = []
    for cat, _ in cats.most_common():
        sections.append(taxonomy_section(cat, groups[cat]))
    cat_cards = "\n".join(
        f"<a class='card taxonomy-card' data-category='{safe_slug(cat)}' href='#{safe_slug(cat)}'><strong>{html.escape(cat)}</strong><span class='overview-count'>{count} papers</span></a>"
        for cat, count in cats.most_common()
    )
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,">
  <title>Awesome BCI</title>
  <style>
    :root {{ color-scheme: light; --ink:#18212f; --muted:#5b6678; --line:#d9dee8; --accent:#0f766e; --accent2:#7c3aed; --bg:#f7f9fc; --panel:#ffffff; }}
    body {{ margin:0; font-family: Inter, Segoe UI, Arial, sans-serif; color:var(--ink); background:var(--bg); }}
    header {{ padding:54px 7vw 34px; background:linear-gradient(120deg,#e9fbf8,#eef2ff); border-bottom:1px solid var(--line); }}
    h1 {{ font-size:48px; margin:0 0 12px; letter-spacing:0; }}
    h2 {{ margin-top:36px; }}
    p {{ line-height:1.65; color:var(--muted); }}
    main {{ padding:28px 7vw 72px; }}
    .stats, .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; margin:24px 0; }}
    .filters {{ display:flex; flex-wrap:wrap; align-items:end; gap:12px; margin:24px 0; padding:14px; background:white; border:1px solid var(--line); border-radius:8px; }}
    .filter-field {{ display:grid; gap:6px; }}
    .wide-field {{ min-width:min(100%, 280px); }}
    .filter-field label {{ font-weight:700; font-size:13px; color:#344255; }}
    select {{ min-width:104px; height:38px; border:1px solid var(--line); border-radius:8px; background:white; color:var(--ink); padding:0 10px; font:inherit; }}
    #periodPreset {{ min-width:280px; }}
    button {{ height:38px; border:1px solid #bfc8d8; border-radius:8px; background:#f6f8fb; color:var(--ink); padding:0 14px; font-weight:700; cursor:pointer; }}
    button:hover {{ background:#eef2f7; }}
    #rangeStatus {{ color:var(--muted); font-weight:700; min-height:38px; display:inline-flex; align-items:center; }}
    .figures {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; margin:24px 0; }}
    .chart-figure {{ margin:0; }}
    .chart-figure figcaption {{ margin-top:8px; color:var(--muted); font-size:13px; font-weight:700; }}
    .figures img {{ width:100%; aspect-ratio:16 / 9; object-fit:contain; background:white; border:1px solid var(--line); border-radius:8px; display:block; }}
    .stat, .card {{ background:white; border:1px solid var(--line); border-radius:8px; padding:16px; }}
    .stat strong {{ display:block; font-size:28px; color:var(--accent); }}
    .card span {{ display:block; margin-top:8px; color:var(--muted); }}
    .overview-count {{ font-weight:800; color:var(--accent); }}
    nav a {{ display:inline-block; margin:0 12px 10px 0; color:var(--accent2); font-weight:600; }}
    .card {{ display:block; color:var(--ink); }}
    .taxonomy-section {{ margin-top:16px; }}
    details {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden; }}
    summary {{ cursor:pointer; display:grid; grid-template-columns:minmax(260px,1fr) repeat(3, minmax(110px, auto)); gap:12px; align-items:center; padding:16px 18px; font-weight:700; }}
    .summary-title {{ color:var(--accent); }}
    .section-intro {{ padding:0 18px 14px; border-top:1px solid var(--line); }}
    .section-visual {{ margin:14px 0 4px; }}
    .section-visual img {{ width:min(320px, 100%); aspect-ratio:16 / 11; object-fit:contain; border:1px solid var(--line); border-radius:8px; background:#f8fafc; display:block; }}
    .insight-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:12px; margin-top:12px; }}
    .insight-box {{ padding:12px 14px; background:#f4faf8; border:1px solid #cfe7df; border-radius:8px; }}
    .limitation-box {{ background:#fff8f1; border-color:#ead7c1; }}
    .insight-box strong span {{ color:var(--muted); font-weight:600; }}
    .insight-box ul {{ margin:8px 0 0; padding-left:20px; color:var(--muted); line-height:1.55; }}
    .paper-list {{ display:grid; gap:12px; padding:16px; background:#f9fbfd; }}
    .paper-card {{ display:grid; grid-template-columns:56px 1fr; gap:14px; padding:16px; background:white; border:1px solid var(--line); border-radius:8px; }}
    .paper-rank {{ font-weight:800; color:var(--accent2); }}
    .paper-card h3 {{ margin:0 0 6px; font-size:18px; line-height:1.35; }}
    .authors {{ margin:0 0 8px; }}
    .meta {{ display:flex; flex-wrap:wrap; gap:8px; margin:8px 0 10px; }}
    .meta span, .tags {{ display:inline-block; background:#eef2f7; border:1px solid #dce3ee; border-radius:999px; padding:5px 9px; color:#344255; font-size:13px; }}
    .assessment {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:8px; }}
    .links a {{ margin-right:12px; font-weight:700; }}
    a {{ color:#0f5f97; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    @media (max-width:760px) {{
      h1 {{ font-size:36px; }}
      summary {{ grid-template-columns:1fr; }}
      .paper-card {{ grid-template-columns:1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Awesome BCI</h1>
    <p>A taxonomy-first map of Brain-Computer Interface research from {START_YEAR} through {END_YEAR}. Each year investigates up to {CANDIDATES_PER_YEAR} candidate papers, selects the top {TARGET_PER_YEAR}, and organizes the final papers by BCI research theme.</p>
    <nav>
      <a href="https://github.com/honggi82/awesome-BCI">README</a>
      <a href="data/{PAPERS_CSV}">CSV Dataset</a>
      <a href="data/{TAXONOMY_CSV}">Taxonomy CSV</a>
      <a href="data/{PERIOD_ANALYSIS_JSON}">Period Analysis JSON</a>
      <a href="data/{CANDIDATES_CSV}">Candidate Pool</a>
      <a href="paper/review_en.html">Review Paper</a>
      <a href="paper/review_ko.html">Korean Review</a>
    </nav>
  </header>
  <main>
    <div class="stats">
      <div class="stat"><strong id="statPapers">{len(flat)}</strong><span>selected papers</span></div>
      <div class="stat"><strong id="statYears">{len(YEARS)}</strong><span>years covered</span></div>
      <div class="stat"><strong id="statCitations">{total_cites:,}</strong><span>citation count total</span></div>
      <div class="stat"><strong id="statCategories">{len(cats)}</strong><span>topic categories</span></div>
    </div>
    <form class="filters" id="yearFilter">
      <div class="filter-field wide-field">
        <label for="periodPreset">Period</label>
        <select id="periodPreset" name="period">{period_options}</select>
      </div>
      <div class="filter-field">
        <label for="languageSelect">Language</label>
        <select id="languageSelect" name="lang">{language_options}</select>
      </div>
      <div class="filter-field">
        <label for="startYear">Start year</label>
        <select id="startYear" name="from">{start_year_options}</select>
      </div>
      <div class="filter-field">
        <label for="endYear">End year</label>
        <select id="endYear" name="to">{end_year_options}</select>
      </div>
      <button type="button" id="resetYears">Reset</button>
      <span id="rangeStatus"></span>
    </form>
    <h2>Taxonomy</h2>
    <p id="taxonomyTotalSummary"><strong>Total selected papers:</strong> {len(flat):,} papers; <strong>Categories:</strong> {len(cats)} categories.</p>
    <p>Each taxonomy section lists papers with publication year, journal or venue, citation count, main idea, strengths, limitations, and paper links. Sections are collapsed by default to keep the page scannable.</p>
    <div class="figures">
      <figure class="chart-figure">
        <img id="categoryDistributionChart" src="{period_chart_src('category_distribution', START_YEAR, END_YEAR)}" alt="Category distribution chart for {YEAR_RANGE_TEXT}">
        <figcaption id="categoryChartCaption">Category distribution ({YEAR_RANGE_TEXT})</figcaption>
      </figure>
      <figure class="chart-figure">
        <img id="yearlyCitationsChart" src="{period_chart_src('yearly_citations', START_YEAR, END_YEAR)}" alt="Yearly citation chart for {YEAR_RANGE_TEXT}">
        <figcaption id="citationChartCaption">Yearly citation mass ({YEAR_RANGE_TEXT})</figcaption>
      </figure>
    </div>
    <div class="cards">{cat_cards}</div>
    {''.join(sections)}
  </main>
{year_filter_script}
</body>
</html>
"""
    (DOCS_DIR / "index.html").write_text(html_doc, encoding="utf-8")
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")


def write_charts(flat):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    assets = DOCS_DIR / "assets"
    assets.mkdir(exist_ok=True)
    period_assets = assets / "periods"
    period_assets.mkdir(exist_ok=True)
    for stale in period_assets.glob("category_distribution_*.png"):
        stale.unlink()
    for stale in period_assets.glob("yearly_citations_*.png"):
        stale.unlink()

    def render_category_chart(rows, start, end, target):
        cats = category_stats(rows).most_common()
        labels = [c for c, _ in cats][::-1] or ["No papers"]
        values = [v for _, v in cats][::-1] or [0]
        fig, ax = plt.subplots(figsize=(11, 6), dpi=150)
        ax.barh(labels, values, color="#0f766e")
        ax.set_xlabel("Selected papers")
        ax.set_title(f"BCI Paper Taxonomy, {period_label(start, end)}")
        ax.grid(axis="x", alpha=0.25)
        fig.tight_layout()
        fig.savefig(target)
        plt.close(fig)

    def render_citation_chart(rows, start, end, target):
        stats = year_stats(rows)
        years = list(range(start, end + 1))
        citations = [stats.get(year, {}).get("citations", 0) for year in years]
        fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
        ax.bar([str(year) for year in years], citations, color="#7c3aed")
        ax.set_ylabel("Citation count in selected set")
        ax.set_title(f"Yearly Citation Mass, {period_label(start, end)}")
        ax.grid(axis="y", alpha=0.25)
        if len(years) > 8:
            ax.tick_params(axis="x", labelrotation=45)
        fig.tight_layout()
        fig.savefig(target)
        plt.close(fig)

    for start, end in all_period_ranges():
        rows = [p for p in flat if start <= p["year"] <= end]
        category_target = period_assets / period_chart_filename("category_distribution", start, end)
        citation_target = period_assets / period_chart_filename("yearly_citations", start, end)
        render_category_chart(rows, start, end, category_target)
        render_citation_chart(rows, start, end, citation_target)

    shutil.copyfile(
        period_assets / period_chart_filename("category_distribution", START_YEAR, END_YEAR),
        assets / "category_distribution.png",
    )
    shutil.copyfile(
        period_assets / period_chart_filename("yearly_citations", START_YEAR, END_YEAR),
        assets / "yearly_citations.png",
    )


def reference_line(p):
    authors = p["authors"] or "Unknown authors"
    venue = p["venue"] or "Unknown venue"
    link = p["url"] or p["semanticScholarUrl"]
    return f"{authors}. ({p['year']}). {p['title']}. {venue}. {link}"


def review_sections(flat, korean=False):
    stats = year_stats(flat)
    cats = category_stats(flat)
    top_by_year = [stats[y]["top"] for y in YEARS if stats.get(y, {}).get("top")]
    if korean:
        title = f"{YEAR_RANGE_TEXT}년 뇌-컴퓨터 인터페이스 연구 동향: 공개 메타데이터 기반 리뷰"
        abstract = (
            f"이 리뷰 초안은 {START_YEAR}년부터 {END_YEAR}년까지의 Brain-Computer Interface(BCI) 연구를 "
            f"연도별 최대 {CANDIDATES_PER_YEAR}편의 후보로 조사하고 인용회수 기준으로 {TARGET_PER_YEAR}편씩 선별해 정리한다. 선별은 무료 공개 Semantic Scholar 메타데이터를 "
            "사용했으며, 검색어 기반 후보군을 연도 필터, 강화된 BCI 관련성 필터, 중복 제거, 후보 감사용 중요도 점수화로 처리했다. "
            "결과는 운동상상/운동 디코딩, SSVEP/P300/ERP, 재활과 신경보철, 침습형 인터페이스, 딥러닝, EEG 신호처리, "
            "언어/의사소통 BCI, 폐루프/하이브리드 BCI로 나뉜다."
        )
        methods = (
            "방법: 각 연도에 대해 BCI 관련 질의를 Semantic Scholar Academic Graph bulk search에 보내고, "
            "제목 또는 초록에 BCI 관련 핵심 표현이 있는 논문만 남겼다. DOI, arXiv, PubMed, CorpusId, paperId 순서로 "
            f"중복을 제거했다. 이후 연도별 최대 {CANDIDATES_PER_YEAR}편의 후보 풀을 만들고, 그 안에서 인용회수 상위 {TARGET_PER_YEAR}편을 최종 목록에 사용했다. "
            "영향력 있는 인용 수와 중요도 점수는 동률 처리와 감사용 보조 신호로 유지했다. 중요도 점수는 로그 변환 인용 수, 영향력 있는 인용 수, 주요 venue 신호, BCI 핵심어 밀도, 리뷰/서베이, 데이터셋/벤치마크, "
            f"임상/재활 관련성, 침습형 고대역폭 BCI, 최신 머신러닝 방법 보너스를 합산했다. {END_YEAR}년은 {date.today().isoformat()} 현재의 부분 연도라는 점에 유의해야 한다."
        )
        trends_intro = "주요 경향은 다음과 같다."
        caveat = (
            "한계: 이 문서는 전문 PDF를 모두 읽은 체계적 문헌고찰이 아니라 메타데이터 기반 리뷰 초안이다. "
            "인용 수는 최신 논문에 불리하며, 일부 논문의 venue/date 정보는 원천 데이터에서 누락될 수 있다."
        )
        conclusion = (
            f"결론적으로 {START_YEAR}년 이후 BCI 연구는 딥러닝 기반 EEG 디코딩과 벤치마크, 재활 응용, 침습형 고성능 디코딩, "
            "사용자 친화적 의사소통 시스템 사이에서 빠르게 확장되고 있다. 향후 리뷰에서는 실제 PDF 기반 품질 평가, "
            "임상 전환성, 데이터셋 재현성, 장기 안정성, 안전성과 윤리 문제를 함께 검토해야 한다."
        )
    else:
        title = f"Brain-Computer Interface Research from {START_YEAR} to {END_YEAR}: A Metadata-Driven Review"
        abstract = (
            f"This draft review maps Brain-Computer Interface (BCI) research from {START_YEAR} through {END_YEAR}, investigating up to "
            f"{CANDIDATES_PER_YEAR} candidate papers per year from free public Semantic Scholar metadata and selecting {TARGET_PER_YEAR} papers per year by citation count. Candidate papers were retrieved with BCI-related "
            "queries, filtered by target year and strengthened BCI relevance terms, deduplicated, and scored for candidate auditing. The resulting "
            "collection highlights work on motor imagery and movement decoding, SSVEP/P300/ERP systems, rehabilitation and "
            "neuroprosthetics, invasive interfaces, deep learning, EEG signal processing, speech and communication BCIs, and "
            "hybrid or closed-loop systems."
        )
        methods = (
            "Methods: For each year, BCI-oriented queries were sent to the Semantic Scholar Academic Graph bulk search endpoint. "
            "Records were retained when their title or abstract matched BCI relevance expressions, deduplicated by DOI, arXiv, "
            f"PubMed, CorpusId, or paperId, and reduced to at most {CANDIDATES_PER_YEAR} candidate papers per year. The final {TARGET_PER_YEAR} papers per year were selected by citation count, with influential citation count and the metadata importance score retained as tie-breakers and audit signals. The importance score combines log-scaled citations, log-scaled influential citations, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive high-bandwidth BCIs, and modern machine-learning methods. The year {END_YEAR} should be interpreted as a partial year as of {date.today().isoformat()}."
        )
        trends_intro = "The main metadata-level trends are as follows."
        caveat = (
            "Limitations: this is a metadata-driven review draft rather than a full systematic review of every PDF. Citation counts "
            f"favor older work, recent {END_YEAR} papers are structurally under-counted, and some venues or publication dates are missing upstream."
        )
        conclusion = (
            f"Overall, BCI research since {START_YEAR} is expanding across deep-learning EEG decoding, benchmarks and datasets, rehabilitation, "
            "high-performance invasive decoding, and usable communication systems. A full manuscript should next add PDF-level appraisal, "
            "clinical translation evidence, dataset reproducibility, long-term stability, safety, and ethics."
        )
    category_lines = [f"{cat}: {count}" for cat, count in cats.most_common()]
    year_lines = [
        f"{y}: {stats[y]['count']} papers, {stats[y]['citations']:,} citations in selected set, top paper: {stats[y]['top']['title']}"
        for y in YEARS if y in stats
    ]
    refs = [reference_line(p) for p in top_by_year]
    return title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs


def review_deep_dive(flat, korean=False):
    cats = category_stats(flat)
    stats = year_stats(flat)
    top_scored = sorted(flat, key=lambda p: p["importanceScore"], reverse=True)[:12]
    top_cited = sorted(flat, key=lambda p: p["citationCount"], reverse=True)[:12]
    leading_cat, leading_count = cats.most_common(1)[0]
    total_cites = sum(p["citationCount"] for p in flat)
    peak_year = max(stats, key=lambda y: stats[y]["citations"])
    newest_year = max(YEARS)

    if korean:
        findings = [
            f"선정된 {len(flat)}편은 총 {total_cites:,}회의 인용을 포함하며, 인용량은 {peak_year}년에 가장 높다.",
            f"가장 큰 축은 {leading_cat}({leading_count}편)으로, {START_YEAR}년 이후 BCI 연구가 여전히 운동 의도 해석과 운동 기능 보조를 중심으로 조직되어 있음을 보여준다.",
            f"{newest_year}년 논문은 부분 연도라 인용 수가 낮지만, foundation model, 장기 안정성, 고성능 침습형 디코딩, 임상 전환성 같은 주제가 두드러진다.",
            "비침습 EEG-BCI는 데이터셋/벤치마크와 딥러닝 방법론이 빠르게 늘었고, 침습형 BCI는 의사소통·운동 복원 성능을 실제 사용성 문제와 연결하는 방향으로 이동하고 있다.",
        ]
        category_discussion = [
            f"{cat}: {count}편. 이 범주는 최종 목록의 {count / len(flat):.1%}를 차지한다."
            for cat, count in cats.most_common()
        ]
        future = [
            "PDF 전문 기반의 임상근거 수준 평가와 risk-of-bias 코딩을 추가한다.",
            "데이터셋 공개 여부, 재현 코드, 피험자 수, 장기 안정성 지표를 별도 열로 정규화한다.",
            "후보 500편 풀에서 연도별 저인용 최신 논문의 잠재력을 전문가 검토로 보정한다.",
            "장애 당사자 중심 사용성, 안전성, 개인정보, 신경윤리 기준을 별도 taxonomy로 확장한다.",
        ]
        top_scored_heading = "메타데이터 중요도 점수 상위 논문(감사용)"
        top_cited_heading = "인용 수 상위 논문"
    else:
        findings = [
            f"The {len(flat)} selected papers account for {total_cites:,} citations in the selected set, with the largest citation mass in {peak_year}.",
            f"The dominant category is {leading_cat} ({leading_count} papers), indicating that movement intention decoding and motor assistance remain the organizing center of BCI research since {START_YEAR}.",
            f"Papers from {newest_year} are structurally citation-disadvantaged because the year is partial, but they surface emerging themes around foundation models, stability, invasive high-bandwidth decoding, and clinical translation.",
            "Non-invasive EEG-BCI work is increasingly shaped by datasets, benchmarks, and deep learning, while invasive BCI work is moving from peak decoding performance toward communication, autonomy, and usability constraints.",
        ]
        category_discussion = [
            f"{cat}: {count} papers, representing {count / len(flat):.1%} of the selected set."
            for cat, count in cats.most_common()
        ]
        future = [
            "Add PDF-level appraisal of clinical evidence and risk-of-bias indicators.",
            "Normalize dataset availability, released code, participant counts, and long-term stability metrics.",
            "Use expert review to compensate for low citation counts among very recent papers in the 500-candidate pools.",
            "Extend the taxonomy with user-centered usability, safety, privacy, and neuroethics criteria.",
        ]
        top_scored_heading = "Top Papers by Metadata Importance Score (Audit Signal)"
        top_cited_heading = "Top Papers by Citation Count"

    return {
        "findings": findings,
        "category_discussion": category_discussion,
        "future": future,
        "top_scored": top_scored,
        "top_cited": top_cited,
        "top_scored_heading": top_scored_heading,
        "top_cited_heading": top_cited_heading,
    }


def html_ranked_table(rows, metric):
    heading = "Importance" if metric == "importance" else "Citations"
    out = [
        "<table>",
        f"<thead><tr><th>Year</th><th>Rank</th><th>Paper</th><th>{heading}</th><th>Category</th></tr></thead>",
        "<tbody>",
    ]
    for p in rows:
        metric_value = p["importanceScore"] if metric == "importance" else p["citationCount"]
        link = f'<a href="{html.escape(p["url"])}">{html.escape(p["title"])}</a>' if p["url"] else html.escape(p["title"])
        out.append(
            f"<tr><td>{p['year']}</td><td>{p['rank']}</td><td>{link}</td>"
            f"<td>{metric_value}</td><td>{html.escape(p['category'])}</td></tr>"
        )
    out.extend(["</tbody>", "</table>"])
    return "\n".join(out)


def write_review_html(flat, korean=False):
    title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs = review_sections(flat, korean)
    deep = review_deep_dive(flat, korean)
    lang = "ko" if korean else "en"
    heading_refs = "선정 참고문헌 예시" if korean else "Selected References"
    heading_findings = "핵심 발견" if korean else "Key Findings"
    heading_category = "분야별 해석" if korean else "Category-Level Interpretation"
    heading_future = "향후 연구 의제" if korean else "Future Research Agenda"
    html_doc = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Georgia, 'Noto Serif KR', serif; max-width: 920px; margin: 40px auto; padding: 0 22px; line-height: 1.72; color:#172033; }}
    h1 {{ line-height:1.15; }}
    h2 {{ margin-top: 34px; }}
    li {{ margin: 6px 0; }}
    .abstract {{ background:#f5f7fb; border-left:4px solid #0f766e; padding:14px 18px; }}
    table {{ width:100%; border-collapse:collapse; margin:16px 0; }}
    th,td {{ border-bottom:1px solid #d9dee8; padding:8px; vertical-align:top; text-align:left; }}
    th {{ background:#f4f6fa; }}
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <p><strong>Generated:</strong> {date.today().isoformat()} &middot; <strong>Dataset:</strong> {len(flat)} papers</p>
  <h2>Abstract</h2>
  <p class="abstract">{html.escape(abstract)}</p>
  <h2>1. Introduction and Scope</h2>
  <p>{html.escape(methods)}</p>
  <h2>2. {heading_findings}</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in deep['findings'])}</ul>
  <h2>3. Taxonomy</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in category_lines)}</ul>
  <h2>4. {heading_category}</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in deep['category_discussion'])}</ul>
  <h2>5. Year-by-Year Trends</h2>
  <p>{html.escape(trends_intro)}</p>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in year_lines)}</ul>
  <h2>6. {deep['top_cited_heading']}</h2>
  {html_ranked_table(deep['top_cited'], 'citations')}
  <h2>7. {deep['top_scored_heading']}</h2>
  {html_ranked_table(deep['top_scored'], 'importance')}
  <h2>8. {heading_future}</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in deep['future'])}</ul>
  <h2>9. Limitations</h2>
  <p>{html.escape(caveat)}</p>
  <h2>10. Conclusion</h2>
  <p>{html.escape(conclusion)}</p>
  <h2>{heading_refs}</h2>
  <ol>{''.join(f'<li>{html.escape(ref)}</li>' for ref in refs)}</ol>
</body>
</html>
"""
    name = "review_ko.html" if korean else "review_en.html"
    (PAPER_DIR / name).write_text(html_doc, encoding="utf-8")


def write_review_docx(flat):
    title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs = review_sections(flat, korean=False)
    deep = review_deep_dive(flat, korean=False)
    doc = Document()
    doc.add_heading(title, level=0)
    doc.add_paragraph(f"Generated: {date.today().isoformat()} | Dataset: {len(flat)} papers")
    doc.add_heading("Abstract", level=1)
    doc.add_paragraph(abstract)
    doc.add_heading("1. Introduction and Scope", level=1)
    doc.add_paragraph(methods)
    doc.add_heading("2. Key Findings", level=1)
    for line in deep["findings"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("3. Taxonomy", level=1)
    for line in category_lines:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("4. Category-Level Interpretation", level=1)
    for line in deep["category_discussion"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("5. Year-by-Year Trends", level=1)
    doc.add_paragraph(trends_intro)
    for line in year_lines:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("6. Top Papers by Citation Count", level=1)
    for p in deep["top_cited"]:
        doc.add_paragraph(f"{p['year']} #{p['rank']}: {p['title']} ({p['citationCount']} citations)", style="List Number")
    doc.add_heading("7. Top Papers by Metadata Importance Score (Audit Signal)", level=1)
    for p in deep["top_scored"]:
        doc.add_paragraph(f"{p['year']} #{p['rank']}: {p['title']} ({p['importanceScore']})", style="List Number")
    doc.add_heading("8. Future Research Agenda", level=1)
    for line in deep["future"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("9. Limitations", level=1)
    doc.add_paragraph(caveat)
    doc.add_heading("10. Conclusion", level=1)
    doc.add_paragraph(conclusion)
    doc.add_heading("Selected References", level=1)
    for ref in refs:
        doc.add_paragraph(ref, style="List Number")
    doc.save(PAPER_DIR / "review_en.docx")


def main():
    for path in (DATA_DIR, DOCS_DIR, PAPER_DIR):
        path.mkdir(exist_ok=True)
    selected, candidates = collect_papers()
    flat = write_json_csv(selected, candidates)
    write_taxonomy_dataset(flat)
    write_period_analysis(flat)
    write_readme(flat)
    write_charts(flat)
    write_site(flat)
    write_review_html(flat, korean=False)
    write_review_html(flat, korean=True)
    write_review_docx(flat)
    shutil.copyfile(DATA_DIR / PAPERS_CSV, DOCS_DIR / "data" / PAPERS_CSV)
    shutil.copyfile(DATA_DIR / TAXONOMY_CSV, DOCS_DIR / "data" / TAXONOMY_CSV)
    shutil.copyfile(DATA_DIR / CANDIDATES_CSV, DOCS_DIR / "data" / CANDIDATES_CSV)
    shutil.copyfile(PAPER_DIR / "review_en.html", DOCS_DIR / "paper" / "review_en.html")
    shutil.copyfile(PAPER_DIR / "review_ko.html", DOCS_DIR / "paper" / "review_ko.html")
    (ROOT / "LICENSE").write_text("CC-BY-4.0 for text and metadata curation; upstream paper metadata belongs to original sources.\n", encoding="utf-8")
    print(f"[done] generated {len(flat)} selected papers", flush=True)


if __name__ == "__main__":
    main()
