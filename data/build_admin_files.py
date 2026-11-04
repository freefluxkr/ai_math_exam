# -*- coding: utf-8 -*-
import os

sql_admin_html = open(r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam\admin.html", "r", encoding="utf-8").read()
sql_admin_js = open(r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam\js\admin-app.js", "r", encoding="utf-8").read()

ai_admin_html = (
    sql_admin_html
    .replace("SQL 평가 관리자 콘솔 | 채점 · 6대 통계지표 · 주관식 검수", "AI 수학·엔지니어링 평가 관리자 콘솔 | 5대 파트 75문항 6대 통계지표")
    .replace("SQL 평가 관리자 채점 · 통계 센터", "AI & LLM 사전학습(수학·엔지니어링) 평가 관리자 센터")
    .replace("객관식 45 · 주관식 45 | SQL 실행 결과 자동채점 및 6대 통계지표 분석", "Book 21701 5대 파트 × 15문항 = 총 75문항 | 실시간 채점 및 6대 통계지표 분석")
    .replace("4. 문항별 정답률 분석 (90문항)", "4. 문항별 정답률 분석 (75문항)")
    .replace("SQL 기초(Ch05) · SQL 활용(Ch06) · SQL 응용(Ch07) 성취도 비교", "선형대수 · 미적분 · 확률/정보이론 · 이산/상태그래프 · AI 파이썬 성취도 비교")
    .replace('<option value="SQL 기초">SQL 기초 (Ch05)</option>', '<option value="선형대수학: 인공지능의 다차원 공간 언어">Part 1. 선형대수학</option>')
    .replace('<option value="SQL 활용">SQL 활용 (Ch06)</option>', '<option value="미적분 & 최적화: 딥러닝과 머신러닝의 학습 엔진">Part 2. 미적분 & 최적화</option>')
    .replace(
        '<option value="SQL 응용">SQL 응용 (Ch07)</option>',
        '<option value="확률통계 & 정보이론: 불확실성과 데이터의 본질 정량화">Part 3. 확률통계 & 정보이론</option>\n'
        '              <option value="이산수학 & 상태 그래프: 자율 에이전트 아키텍처의 뼈대">Part 4. 이산수학 & 상태 그래프</option>\n'
        '              <option value="실전 AI 파이썬 엔지니어링: 코드로 구현하는 차세대 시스템">Part 5. 실전 AI 파이썬 엔지니어링</option>'
    )
)

ai_admin_js = (
    sql_admin_js
    .replace("dmdg_sql_exam_admin_authed", "dmdg_ai_math_exam_admin_authed")
    .replace("dmdg_sql_exam_demo_cleaned_v2", "dmdg_ai_math_exam_demo_cleaned_v1")
    .replace("const areas = ['SQL 기초', 'SQL 활용', 'SQL 응용'];", "const areas = global.SqlExamStorage.CATEGORIES || [];")
    .replace("labels: ['SQL 기초 (Ch05)', 'SQL 활용 (Ch06)', 'SQL 응용 (Ch07)'],", "labels: ['Part 1. 선형대수', 'Part 2. 미적분/최적화', 'Part 3. 확률/정보이론', 'Part 4. 이산/상태그래프', 'Part 5. AI 파이썬'],")
    .replace("sql_exam_results_", "ai_math_exam_results_")
)

open(r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\admin.html", "w", encoding="utf-8").write(ai_admin_html)
open(r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\js\admin-app.js", "w", encoding="utf-8").write(ai_admin_js)
print("Successfully created admin.html and js/admin-app.js for ai_math_exam")

import json
qs = json.load(open(r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\questions.json", "r", encoding="utf-8"))
lines = [
    "# 📘 《AI 와 데이터 분석 & 최신 LLM 에이전트 완벽 정복을 위한 사전 학습(수학·기초 엔지니어링)》(Book 21701) 객관식 75문항 문제집",
    "",
    "- **구성**: 5대 파트 × 15문항 = 총 75문항 (4지선다 객관식, 문항당 1분 제한, 배점 2점)",
    "- **웹 평가 시스템 경로**: `DMDG_PRJ/ai_math_exam/index.html` (복사 방지, 재응시 차단, 관리자 콘솔 탑재)",
    "",
    "---",
    ""
]

cur_cat = None
for q in qs:
    if q["category"] != cur_cat:
        cur_cat = q["category"]
        lines.append(f"## 📌 {cur_cat} (15문항)")
        lines.append("")
    no_val = q["no"]
    qid = q["id"]
    ch = q["chapter"]
    title = q["title"]
    lines.append(f"### Q{no_val:02d}. [{qid} · {ch}] {title}")
    if q["description"]:
        lines.append(f"> {q['description']}")
    lines.append("")
    for i, opt in enumerate(q["options"], 1):
        lines.append(f"{i}. {opt}")
    lines.append("")
    lines.append(f"- **정답**: **{q['answer']}번**")
    lines.append(f"- **해설**: {q['explanation']}")
    lines.append("")

out_p = r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\AI_MATH_EXAM_75_QUESTIONS.md"
open(out_p, "w", encoding="utf-8").write("\n".join(lines))
print("Generated markdown question book:", out_p)
