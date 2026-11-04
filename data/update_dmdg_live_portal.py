# -*- coding: utf-8 -*-
import os

INDEX_PATH = r"C:\DMDG_Jobs\DMDG_PRJ\dmdg_live_dot_com\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add quick nav button in header-nav if not already present
nav_target = """      <a href="https://dmdg.wikidocs.net/" target="_blank" rel="noopener noreferrer" class="nav-link-btn" style="background: #FFFFFF !important; color: #0B1B3D !important; border: 1.5px solid #0B1B3D !important; box-shadow: 0 2px 8px rgba(0,0,0,0.18) !important;">
        <span style="color: #0B1B3D !important; font-weight: 800 !important;">📚 위키북스</span>
      </a>"""

nav_addition = nav_target + """
      <a href="#panel-exams" class="nav-link-btn" style="background: linear-gradient(135deg, #2563EB, #0284C7) !important; color: #FFFFFF !important; border: 1.5px solid #2563EB !important; box-shadow: 0 2px 8px rgba(37,99,235,0.28) !important;">
        <span style="color: #FFFFFF !important; font-weight: 800 !important;">📝 역량 평가 센터 (4종)</span>
      </a>"""

if "#panel-exams" not in html:
    if nav_target in html:
        html = html.replace(nav_target, nav_addition, 1)
    elif nav_target.replace("\n", "\r\n") in html:
        html = html.replace(nav_target.replace("\n", "\r\n"), nav_addition.replace("\n", "\r\n"), 1)

# 2. Add Dedicated Competency Assessment Hub Category Section right inside <main class="main-dashboard">
exam_section_html = """  <main class="main-dashboard">
    <!-- ===================================================================
         CATEGORY: COMPETENCY ASSESSMENT HUB · 실무 역량 평가 센터 (4종)
         =================================================================== -->
    <section class="dash-panel" id="panel-exams" style="margin-bottom: 1.5rem; border: 1.5px solid rgba(37, 99, 235, 0.22); background: linear-gradient(180deg, rgba(255,255,255,0.96) 0%, rgba(248,250,252,0.96) 100%);">
      <div class="panel-header" style="border-bottom: 2px solid rgba(37, 99, 235, 0.12);">
        <div class="panel-title">
          <span>🎓</span> 실무 역량 평가 센터 (COMPETENCY ASSESSMENT HUB)
        </div>
        <span class="panel-count-badge" style="background: #EFF6FF; border-color: #BFDBFE; color: #1D4ED8; font-weight: 800;">4 Live Exams · 총 400문항</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 1rem;">
        <!-- Exam 1: SQL 실무 역량 평가 (90문항) -->
        <article class="app-item-card" data-keyword="sql 시험 평가 mysql 데이터베이스 쿼리 역량 평가 90문항 sql_exam" style="margin-bottom: 0; border-top: 3px solid #0284C7;">
          <div class="app-card-head">
            <div class="app-brand-row">
              <div class="app-avatar" style="background: rgba(2, 132, 199, 0.12); border-color: rgba(2, 132, 199, 0.28); color: #0284C7;">🗄️</div>
              <div class="app-title-group">
                <h3>SQL 실무 역량 평가 (MySQL)</h3>
                <span>SQL 기초 · 활용 · 응용 (총 90문항)</span>
              </div>
            </div>
            <span class="badge-tag live" style="background: #0284C7;">90문항</span>
          </div>
          <p class="app-card-desc">
            MySQL 데이터베이스 마스터 바이블(Book 21965) 기반 객관식 및 실시간 SQL 쿼리 실행·자동 채점 역량 평가 시스템입니다.
          </p>
          <div class="app-card-footer" style="margin-top: auto; padding-top: 0.4rem;">
            <a href="https://freefluxkr.github.io/sql_exam/" target="_blank" rel="noopener noreferrer" class="btn-view-app" style="background: linear-gradient(135deg, #0284C7, #2563EB);">
              <span>시험 응시하기</span> <span>➔</span>
            </a>
            <a href="https://freefluxkr.github.io/sql_exam/admin.html" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; font-weight: 800; color: #475569; text-decoration: none; padding: 0.35rem 0.65rem; border-radius: 8px; border: 1px solid #CBD5E1; background: #F8FAFC;">
              ⚙️ 관리자 콘솔
            </a>
          </div>
        </article>

        <!-- Exam 2: AI & LLM 사전 학습(수학·기초 엔지니어링) 역량 평가 (75문항) -->
        <article class="app-item-card" data-keyword="ai llm 사전학습 수학 기초 엔지니어링 선형대수 미적분 확률 이산수학 역량 평가 75문항 ai_math_exam" style="margin-bottom: 0; border-top: 3px solid #4F46E5;">
          <div class="app-card-head">
            <div class="app-brand-row">
              <div class="app-avatar" style="background: rgba(79, 70, 229, 0.12); border-color: rgba(79, 70, 229, 0.28); color: #4F46E5;">📐</div>
              <div class="app-title-group">
                <h3>AI &amp; LLM 사전 학습 역량 평가</h3>
                <span>수학 · 기초 엔지니어링 5대 파트 (총 75문항)</span>
              </div>
            </div>
            <span class="badge-tag live" style="background: #4F46E5;">75문항</span>
          </div>
          <p class="app-card-desc">
            Book 21701 기반 선형대수학(15)·미적분&amp;최적화(15)·확률&amp;정보이론(15)·이산수학&amp;상태그래프(15)·실전 AI 파이썬(15) 평가입니다.
          </p>
          <div class="app-card-footer" style="margin-top: auto; padding-top: 0.4rem;">
            <a href="https://freefluxkr.github.io/ai_math_exam/" target="_blank" rel="noopener noreferrer" class="btn-view-app" style="background: linear-gradient(135deg, #4F46E5, #6366F1);">
              <span>시험 응시하기</span> <span>➔</span>
            </a>
            <a href="https://freefluxkr.github.io/ai_math_exam/admin.html" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; font-weight: 800; color: #475569; text-decoration: none; padding: 0.35rem 0.65rem; border-radius: 8px; border: 1px solid #CBD5E1; background: #F8FAFC;">
              ⚙️ 관리자 콘솔
            </a>
          </div>
        </article>

        <!-- Exam 3: AI 와 데이터 분석 역량 평가 (90문항) -->
        <article class="app-item-card" data-keyword="ai와 데이터 분석 역량 평가 cnn rnn xai 최적화 생성ai 피지컬ai 90문항 ai_data_exam" style="margin-bottom: 0; border-top: 3px solid #059669;">
          <div class="app-card-head">
            <div class="app-brand-row">
              <div class="app-avatar" style="background: rgba(5, 150, 105, 0.12); border-color: rgba(5, 150, 105, 0.28); color: #059669;">🧠</div>
              <div class="app-title-group">
                <h3>AI 와 데이터 분석 역량 평가</h3>
                <span>CNN · RNN · XAI · 최적화 · LLM · 피지컬AI (총 90문항)</span>
              </div>
            </div>
            <span class="badge-tag live" style="background: #059669;">90문항</span>
          </div>
          <p class="app-card-desc">
            Book 21658 기반 컴퓨터비전(15)·시계열(15)·앙상블 XAI(15)·모델최적화(15)·생성AI&amp;LLM(15)·산업융합 피지컬AI(15) 평가입니다.
          </p>
          <div class="app-card-footer" style="margin-top: auto; padding-top: 0.4rem;">
            <a href="https://freefluxkr.github.io/ai_data_exam/" target="_blank" rel="noopener noreferrer" class="btn-view-app" style="background: linear-gradient(135deg, #059669, #10B981);">
              <span>시험 응시하기</span> <span>➔</span>
            </a>
            <a href="https://freefluxkr.github.io/ai_data_exam/admin.html" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; font-weight: 800; color: #475569; text-decoration: none; padding: 0.35rem 0.65rem; border-radius: 8px; border: 1px solid #CBD5E1; background: #F8FAFC;">
              ⚙️ 관리자 콘솔
            </a>
          </div>
        </article>

        <!-- Exam 4: 파이썬 판다스·넘파이·ML/DL 역량 평가 (145문항) -->
        <article class="app-item-card" data-keyword="파이썬 판다스 넘파이 ml dl 역량 평가 점프투파이썬 pandas numpy 145문항 python_ai_exam" style="margin-bottom: 0; border-top: 3px solid #D97706;">
          <div class="app-card-head">
            <div class="app-brand-row">
              <div class="app-avatar" style="background: rgba(217, 119, 6, 0.12); border-color: rgba(217, 119, 6, 0.28); color: #D97706;">🐍</div>
              <div class="app-title-group">
                <h3>파이썬 판다스·넘파이·ML/DL 역량 평가</h3>
                <span>파이썬(75) · 판다스(20) · 넘파이(20) · ML/DL(30) (총 145문항)</span>
              </div>
            </div>
            <span class="badge-tag live" style="background: #D97706;">145문항</span>
          </div>
          <p class="app-card-desc">
            파이썬 기초·제어문·입출력·클래스·정규표현식(75문항) 및 Pandas(20)·NumPy(20)·머신러닝&amp;딥러닝(30) 8대 파트 통합 평가입니다.
          </p>
          <div class="app-card-footer" style="margin-top: auto; padding-top: 0.4rem;">
            <a href="https://freefluxkr.github.io/python_ai_exam/" target="_blank" rel="noopener noreferrer" class="btn-view-app" style="background: linear-gradient(135deg, #D97706, #F59E0B);">
              <span>시험 응시하기</span> <span>➔</span>
            </a>
            <a href="https://freefluxkr.github.io/python_ai_exam/admin.html" target="_blank" rel="noopener noreferrer" style="font-size: 0.75rem; font-weight: 800; color: #475569; text-decoration: none; padding: 0.35rem 0.65rem; border-radius: 8px; border: 1px solid #CBD5E1; background: #F8FAFC;">
              ⚙️ 관리자 콘솔
            </a>
          </div>
        </article>
      </div>
    </section>

    <div class="panels-grid">"""

main_target = """  <main class="main-dashboard">
    <div class="panels-grid">"""

if 'id="panel-exams"' not in html:
    if main_target in html:
        html = html.replace(main_target, exam_section_html, 1)
    elif main_target.replace("\n", "\r\n") in html:
        html = html.replace(main_target.replace("\n", "\r\n"), exam_section_html.replace("\n", "\r\n"), 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated dmdg-live.com index.html with 4 Exam Sites category.")

