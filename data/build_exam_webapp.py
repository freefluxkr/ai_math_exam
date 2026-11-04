# -*- coding: utf-8 -*-
import os
import shutil

SRC_DIR = r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam"

EXAMS = [
    {
        "slug": "ai_data_exam",
        "dir": r"C:\DMDG_Jobs\DMDG_PRJ\ai_data_exam",
        "title": "AI 와 데이터 분석 역량 평가",
        "short_title": "AI 와 데이터 분석 역량 평가",
        "header_sub": "위키독스 Book 21658 공식 평가 | 컴퓨터비전(CNN) · 시계열(RNN) · 앙상블/XAI · 모델최적화 · 생성AI/LLM · 피지컬AI (총 90문항)",
        "card_kicker": "위키독스 Book 21658 · 6대 핵심 영역 문제은행",
        "card_heading": "AI 와 데이터 분석 역량 평가 (6대 파트 · 총 90문항)",
        "book_badge": "위키독스 Book 21658 공식 평가 센터",
        "book_desc": "《AI 와 데이터 분석》 (https://wikidocs.net/book/21658) — 6대 핵심 트랙 × 15문항 = 총 90문항",
        "total_q": 90,
        "parts_count": 6,
        "categories": [
            ("1. 컴퓨터 비전 & 합성곱 신경망", "Part 1. 컴퓨터 비전 & CNN", 15, "CNN · MaxPooling2D · Flatten/Dense · ReLU/Softmax", "indigo"),
            ("2. 순환 신경망 & 시계열 수요 예측", "Part 2. 순환 신경망 & 시계열", 15, "RNN · BPTT · LSTM 게이트 · 시계열 예측", "cyan"),
            ("3. 설명 가능한 머신러닝 & 앙상블 XAI", "Part 3. 설명 가능한 ML & XAI", 15, "Decision Tree · Random Forest · XGBoost · LightGBM", "emerald"),
            ("4. 프로덕션 모델 최적화 & 정규화 백신", "Part 4. 모델 최적화 & 정규화", 15, "과적합/드롭아웃 · 편향-분산 · 조기종료 · Keras 콜백", "amber"),
            ("5. 최신 생성 AI & 대형 언어 모델 (16~18편)", "Part 5. 생성 AI & LLM", 15, "Transformer 어텐션 · GPT/BERT · GAN 적대적 학습", "purple"),
            ("6. 산업 융합 피지컬 AI & 스마트 팩토리 실무", "Part 6. 피지컬 AI & 스마트팩토리", 15, "로봇 팔 제어 · 반도체 웨이퍼/FDC · 엣지 MLOps", "rose"),
        ]
    },
    {
        "slug": "python_ai_exam",
        "dir": r"C:\DMDG_Jobs\DMDG_PRJ\python_ai_exam",
        "title": "파이썬 판다스·넘파이·ML/DL 역량 평가",
        "short_title": "파이썬 판다스·넘파이·ML/DL 역량 평가",
        "header_sub": "파이썬(75문항) · 판다스(20문항) · 넘파이(20문항) · ML/DL(30문항) 통합 공식 평가 (총 145문항)",
        "card_kicker": "파이썬 · 판다스 · 넘파이 · ML/DL · 8대 핵심 영역 문제은행",
        "card_heading": "파이썬 판다스·넘파이·ML/DL 역량 평가 (총 145문항)",
        "book_badge": "파이썬 · 판다스 · 넘파이 · ML/DL 공식 평가 센터",
        "book_desc": "파이썬 기초·심화(75문항) + 판다스(20)·넘파이(20)·ML/DL(30) = 총 145문항",
        "total_q": 145,
        "parts_count": 8,
        "categories": [
            ("1. 파이썬 프로그래밍의 기초, 자료형", "Part 1. 파이썬 기초·자료형", 15, "숫자 · 문자열 · 리스트 · 튜플 · 딕셔너리 · 집합 · 복사", "indigo"),
            ("2. 프로그램의 구조를 쌓는다! 제어문", "Part 2. 파이썬 제어문", 15, "if 조건문 · while/for 반복문 · 컴프리헨션 · enumerate/zip", "cyan"),
            ("3. 파이썬의 입출력", "Part 3. 파이썬 입출력·함수", 15, "함수 · *args/**kwargs · 스코프 · 파일 I/O · sys.argv", "emerald"),
            ("4. 파이썬 날개 달기", "Part 4. 클래스·모듈·예외·내장함수", 15, "클래스/상속 · 모듈/패키지 · 예외처리 · 이터레이터/데코레이터", "amber"),
            ("5. 파이썬 프로그래밍, 어떻게 시작해야 할까?", "Part 5. 실전 문제해결·정규표현식", 15, "알고리즘 설계 · 페이지네이션 · 디렉터리 탐색 · 정규식(re)", "purple"),
            ("6. 판다스", "Part 6. 판다스 (Pandas)", 20, "DataFrame · loc/iloc · 결측치 · groupby · merge/pivot", "rose"),
            ("7. 넘파이", "Part 7. 넘파이 (NumPy)", 20, "ndarray · 브로드캐스팅 · 축(axis) 집계 · 벡터화 · 선형대수", "sky"),
            ("8. ML/DL", "Part 8. 머신러닝 & 딥러닝 (ML/DL)", 30, "전처리/누수방지 · 회귀/분류/앙상블 · 평가지표 · 역전파/PyTorch", "fuchsia"),
        ]
    }
]

for cfg in EXAMS:
    target_dir = cfg["dir"]
    slug = cfg["slug"]
    os.makedirs(os.path.join(target_dir, "js"), exist_ok=True)
    os.makedirs(os.path.join(target_dir, "data"), exist_ok=True)

    # Copy grader.js directly
    shutil.copyfile(
        os.path.join(SRC_DIR, "js", "grader.js"),
        os.path.join(target_dir, "js", "grader.js")
    )

    # 1. Build storage-service.js
    with open(os.path.join(SRC_DIR, "js", "storage-service.js"), "r", encoding="utf-8") as f:
        ss = f.read()

    cat_list_js = "[\n" + ",\n".join([f"    '{c[0]}'" for c in cfg["categories"]]) + "\n  ]"
    old_cat_block = """  const CATEGORIES = [
    '선형대수학: 인공지능의 다차원 공간 언어',
    '미적분 & 최적화: 딥러닝과 머신러닝의 학습 엔진',
    '확률통계 & 정보이론: 불확실성과 데이터의 본질 정량화',
    '이산수학 & 상태 그래프: 자율 에이전트 아키텍처의 뼈대',
    '실전 AI 파이썬 엔지니어링: 코드로 구현하는 차세대 시스템',
  ];"""
    ss = ss.replace(old_cat_block, f"  const CATEGORIES = (global.AI_MATH_EXAM_CATEGORIES && global.AI_MATH_EXAM_CATEGORIES.length) ? global.AI_MATH_EXAM_CATEGORIES : {cat_list_js};")
    ss = ss.replace("dmdg_ai_math_exam_", f"dmdg_{slug}_")
    ss = ss.replace("ai_math_exam_config", f"{slug}_config")
    ss = ss.replace("ai_math_exam_submissions", f"{slug}_submissions")
    ss = ss.replace(
        "AI & LLM 사전 학습(수학·기초 엔지니어링) 역량 평가 (총 75문항)",
        f"{cfg['title']} (총 {cfg['total_q']}문항)"
    )

    old_get_q = """  function getQuestions() {
    try {
      const customRaw = localStorage.getItem(LS_KEYS.CUSTOM_QUESTIONS);
      if (customRaw) {
        const parsed = JSON.parse(customRaw);
        if (Array.isArray(parsed) && parsed.length > 0) {
          return parsed;
        }
      }
    } catch (_) {}
    return Array.isArray(global.SQL_EXAM_QUESTIONS) ? global.SQL_EXAM_QUESTIONS : [];
  }"""

    new_get_q = """  function normalizeQuestionsList(rawArr) {
    if (!Array.isArray(rawArr) || rawArr.length === 0) return [];
    const isZeroBased = rawArr.some(function (q) { return Number(q.answer) === 0; });
    return rawArr.map(function (q, idx) {
      const rawAns = Number(q.answer);
      const ans1Based = isZeroBased ? (rawAns + 1) : rawAns;
      return {
        id: typeof q.id === 'number' ? ('Q-' + String(q.id).padStart(3, '0')) : String(q.id || ('Q-' + (idx + 1))),
        no: q.no || (idx + 1),
        category: q.category || '',
        chapter: q.chapter || q.day || ('Part ' + (idx + 1)),
        type: 'choice',
        timeLimit: q.timeLimit || 60,
        points: q.points || 2,
        title: q.title || q.question || '',
        description: q.description !== undefined ? q.description : (q.code || ''),
        options: Array.isArray(q.options) ? q.options : [],
        answer: ans1Based,
        explanation: q.explanation || ''
      };
    });
  }

  function getQuestions() {
    try {
      const customRaw = localStorage.getItem(LS_KEYS.CUSTOM_QUESTIONS);
      if (customRaw) {
        const parsed = JSON.parse(customRaw);
        if (Array.isArray(parsed) && parsed.length > 0) {
          return normalizeQuestionsList(parsed);
        }
      }
    } catch (_) {}
    const src = global.SQL_EXAM_QUESTIONS || global.AI_DATA_EXAM_QUESTIONS || global.PYTHON_AI_EXAM_QUESTIONS || global.AI_MATH_EXAM_QUESTIONS || [];
    return normalizeQuestionsList(src);
  }"""

    ss = ss.replace(old_get_q, new_get_q)

    with open(os.path.join(target_dir, "js", "storage-service.js"), "w", encoding="utf-8") as f:
        f.write(ss)

    # 2. Build exam-app.js
    with open(os.path.join(SRC_DIR, "js", "exam-app.js"), "r", encoding="utf-8") as f:
        ea = f.read()

    short_labels_entries = [f"    ALL: '전체 {cfg['parts_count']}대 파트 ({cfg['total_q']}문항)'"]
    for c_full, c_short, c_cnt, _, _ in cfg["categories"]:
        short_labels_entries.append(f"    '{c_full}': '{c_short}'")
        # Also support stripped prefix in case question bank omits "1. "
        stripped = c_full.split(". ", 1)[1] if ". " in c_full else c_full
        if stripped != c_full:
            short_labels_entries.append(f"    '{stripped}': '{c_short}'")

    old_short_block = """  const SHORT_CAT_LABELS = {
    ALL: '전체 5대 파트 (75문항)',
    '선형대수학: 인공지능의 다차원 공간 언어': 'Part 1. 선형대수학',
    '미적분 & 최적화: 딥러닝과 머신러닝의 학습 엔진': 'Part 2. 미적분 & 최적화',
    '확률통계 & 정보이론: 불확실성과 데이터의 본질 정량화': 'Part 3. 확률통계 & 정보이론',
    '이산수학 & 상태 그래프: 자율 에이전트 아키텍처의 뼈대': 'Part 4. 이산수학 & 상태 그래프',
    '실전 AI 파이썬 엔지니어링: 코드로 구현하는 차세대 시스템': 'Part 5. 실전 AI 파이썬 엔지니어링',
  };"""
    ea = ea.replace(old_short_block, "  const SHORT_CAT_LABELS = {\n" + ",\n".join(short_labels_entries) + "\n  };")

    # Make category matching flexible (matches exact or stripped prefix)
    old_filter_fn = """  function getFilteredQuestions(categoryFilter) {
    const allQs = global.SqlExamStorage.getQuestions();
    return allQs.filter(function (q) {
      return categoryFilter === 'ALL' || q.category === categoryFilter;
    });
  }"""
    new_filter_fn = """  function normCat(str) {
    return String(str || '').replace(/^\\d+\\.\\s*/, '').trim();
  }
  function getFilteredQuestions(categoryFilter) {
    const allQs = global.SqlExamStorage.getQuestions();
    return allQs.filter(function (q) {
      return categoryFilter === 'ALL' || q.category === categoryFilter || normCat(q.category) === normCat(categoryFilter);
    });
  }"""
    ea = ea.replace(old_filter_fn, new_filter_fn)
    ea = ea.replace("객관식 15문항] 구성이 선택되었습니다.", "선택 파트] 구성이 선택되었습니다.")

    with open(os.path.join(target_dir, "js", "exam-app.js"), "w", encoding="utf-8") as f:
        f.write(ea)

    # 3. Build admin-app.js
    with open(os.path.join(SRC_DIR, "js", "admin-app.js"), "r", encoding="utf-8") as f:
        aa = f.read()

    old_admin_short = """  const SHORT_CAT_LABELS = {
    '선형대수학: 인공지능의 다차원 공간 언어': 'Part 1. 선형대수학',
    '미적분 & 최적화: 딥러닝과 머신러닝의 학습 엔진': 'Part 2. 미적분 & 최적화',
    '확률통계 & 정보이론: 불확실성과 데이터의 본질 정량화': 'Part 3. 확률통계 & 정보이론',
    '이산수학 & 상태 그래프: 자율 에이전트 아키텍처의 뼈대': 'Part 4. 이산수학 & 상태 그래프',
    '실전 AI 파이썬 엔지니어링: 코드로 구현하는 차세대 시스템': 'Part 5. 실전 AI 파이썬',
  };"""
    aa = aa.replace(old_admin_short, "  const SHORT_CAT_LABELS = {\n" + ",\n".join(short_labels_entries) + "\n  };")
    aa = aa.replace("ai_math_exam_questions_75.json", f"{slug}_questions_{cfg['total_q']}.json")
    aa = aa.replace("AI수학엔지니어링_채점통계_", f"{slug}_채점통계_")
    aa = aa.replace("기본 75문항(5대 파트 × 15문항)으로 복원되었습니다.", f"기본 {cfg['total_q']}문항으로 복원되었습니다.")

    with open(os.path.join(target_dir, "js", "admin-app.js"), "w", encoding="utf-8") as f:
        f.write(aa)

    # 4. Build index.html
    with open(os.path.join(SRC_DIR, "index.html"), "r", encoding="utf-8") as f:
        idx_html = f.read()

    idx_html = idx_html.replace("AI & LLM 사전 학습(수학·기초 엔지니어링) 역량 평가 (Book 21701)", cfg["title"])
    idx_html = idx_html.replace("AI & LLM 사전 학습(수학·기초 엔지니어링) 역량 평가", cfg["short_title"])
    idx_html = idx_html.replace("AI & LLM 사전학습(수학·기초 엔지니어링) 역량 평가", cfg["short_title"])
    idx_html = idx_html.replace(
        "위키독스 Book 21701 공식 평가 | 선형대수 · 미적분 · 확률/정보이론 · 이산/상태그래프 · AI 파이썬 (총 75문항)",
        cfg["header_sub"]
    )
    idx_html = idx_html.replace("위키독스 Book 21701 · 5대 핵심 영역 문제은행", cfg["card_kicker"])
    idx_html = idx_html.replace("AI 수학 & 기초 엔지니어링 5대 파트 실전 평가", cfg["card_heading"])
    idx_html = idx_html.replace("아래 <strong>5대 파트 카드</strong>를 클릭하여 파트별(15문항)로 응시하거나, 우측 패널에서 <strong>전체 75문항 통합 평가</strong>를 선택해 시험을 시작할 수 있습니다.", f"아래 <strong>{cfg['parts_count']}대 파트 카드</strong>를 클릭하여 파트별로 응시하거나, 우측 패널에서 <strong>전체 {cfg['total_q']}문항 통합 평가</strong>를 선택해 시험을 시작할 수 있습니다.")
    idx_html = idx_html.replace("위키독스 Book 21701 (Day 01~Day 20) · 5대 파트 × 15문항 = 총 75문항", cfg["book_desc"])
    idx_html = idx_html.replace("위키독스 Book 21701 공식 평가 센터", cfg["book_badge"])
    idx_html = idx_html.replace("총 75문항 (파트별 15문항 × 5)", f"총 {cfg['total_q']}문항 ({cfg['parts_count']}대 파트)")
    idx_html = idx_html.replace("전체 5대 파트 · 객관식 75문항", f"전체 {cfg['parts_count']}대 파트 · 객관식 {cfg['total_q']}문항")
    idx_html = idx_html.replace("최대 75분", f"최대 {cfg['total_q']}분")

    # Replace quick cards in index.html
    cards_html = []
    for i, (c_full, c_short, c_cnt, c_sub, c_color) in enumerate(cfg["categories"], 1):
        cards_html.append(f"""              <div class="glass-panel rounded-xl p-4 border-t-2 border-t-{c_color}-500">
                <div class="flex items-center justify-between mb-1.5">
                  <span class="text-xs font-bold text-{c_color}-400">PART {i}</span>
                  <span class="text-[11px] text-slate-400">{c_sub}</span>
                </div>
                <h3 class="text-sm font-bold text-white mb-2.5">{c_full}</h3>
                <button type="button" onclick="quickSelectPreset('{c_full}')"
                  class="w-full text-left px-3 py-2 rounded-lg bg-slate-800/90 hover:bg-{c_color}-600/25 border border-slate-700 hover:border-{c_color}-400 transition flex items-center justify-between text-xs">
                  <span><i class="fa-solid fa-list-check mr-1.5 text-{c_color}-400"></i>Part {i} 단독 응시</span>
                  <span class="code-font font-bold text-slate-200">{c_cnt}문항 · {c_cnt}분</span>
                </button>
              </div>""")

    start_marker = "<!-- 5 Parts Quick Select Cards -->"
    end_marker = "<!-- Exam Rules Box -->"
    s_idx = idx_html.find(start_marker)
    e_idx = idx_html.find(end_marker)
    if s_idx != -1 and e_idx != -1:
        idx_html = (
            idx_html[:s_idx]
            + "<!-- Quick Select Cards -->\n            <div class=\"grid grid-cols-1 sm:grid-cols-2 gap-3.5 mb-6\">\n"
            + "\n".join(cards_html)
            + "\n            </div>\n\n            "
            + idx_html[e_idx:]
        )

    # Replace category buttons in index.html
    cat_btns_html = [
        f"""                  <button type="button" onclick="selectStartFilter('category', 'ALL')" data-cat="ALL"
                    class="cat-opt-btn bg-indigo-600 text-white border border-indigo-400 font-bold text-xs py-2.5 px-3 rounded-xl transition flex items-center justify-between">
                    <span>전체 통합 평가 (Part 1 ~ Part {cfg['parts_count']})</span>
                    <span class="code-font">{cfg['total_q']}문항</span>
                  </button>"""
    ]
    for c_full, c_short, c_cnt, _, _ in cfg["categories"]:
        cat_btns_html.append(f"""                  <button type="button" onclick="selectStartFilter('category', '{c_full}')" data-cat="{c_full}"
                    class="cat-opt-btn bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-700 font-semibold text-xs py-2.5 px-3 rounded-xl transition flex items-center justify-between">
                    <span>{c_full}</span>
                    <span class="code-font">{c_cnt}문항</span>
                  </button>""")

    cs_start = idx_html.find('<div class="grid grid-cols-1 gap-2" id="category-select-group">')
    cs_end = idx_html.find('<!-- Selected Summary Box -->')
    if cs_start != -1 and cs_end != -1:
        idx_html = (
            idx_html[:cs_start]
            + '<div class="grid grid-cols-1 gap-2" id="category-select-group">\n'
            + "\n".join(cat_btns_html)
            + "\n                </div>\n              </div>\n\n              "
            + idx_html[cs_end:]
        )

    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx_html)

    # 5. Build admin.html
    with open(os.path.join(SRC_DIR, "admin.html"), "r", encoding="utf-8") as f:
        adm_html = f.read()

    adm_html = adm_html.replace("AI & LLM 사전학습(수학·엔지니어링) 평가 관리자 센터", f"{cfg['short_title']} 관리자 센터")
    adm_html = adm_html.replace("Book 21701 5대 파트 × 15문항 = 총 75문항", cfg["book_desc"])
    adm_html = adm_html.replace("총 75문항", f"총 {cfg['total_q']}문항")
    adm_html = adm_html.replace("75문항", f"{cfg['total_q']}문항")

    # Replace select options in admin.html
    opt_lines = [f'              <option value="ALL">전체 {cfg["parts_count"]}대 파트 ({cfg["total_q"]}문항)</option>']
    for c_full, c_short, c_cnt, _, _ in cfg["categories"]:
        opt_lines.append(f'              <option value="{c_full}">{c_short} ({c_cnt}문항)</option>')

    sel_start = adm_html.find('<select id="qstat-cat-filter"')
    sel_end = adm_html.find('</select>', sel_start)
    if sel_start != -1 and sel_end != -1:
        adm_html = (
            adm_html[:sel_start]
            + '<select id="qstat-cat-filter" onchange="renderQuestionStatsTable()"\n              class="bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-slate-200 outline-none">\n'
            + "\n".join(opt_lines)
            + "\n            "
            + adm_html[sel_end:]
        )

    with open(os.path.join(target_dir, "admin.html"), "w", encoding="utf-8") as f:
        f.write(adm_html)

    # 6. Create .nojekyll, .gitignore, README.md
    with open(os.path.join(target_dir, ".nojekyll"), "w", encoding="utf-8") as f:
        f.write("")
    with open(os.path.join(target_dir, ".gitignore"), "w", encoding="utf-8") as f:
        f.write("__pycache__/\n*.pyc\n.DS_Store\n")
    with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {cfg['title']}\n\n- 학생용 시험 페이지: https://freefluxkr.github.io/{slug}/\n- 관리자 대시보드: https://freefluxkr.github.io/{slug}/admin.html\n")

    print(f"Built web app for {slug} ({cfg['total_q']} questions) in {target_dir}")
