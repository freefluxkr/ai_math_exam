# -*- coding: utf-8 -*-
import os
import sys
import time
import zipfile

def create_backup():
    downloads_dir = r"C:\Users\PC\Downloads"
    zip_path = os.path.join(downloads_dir, "DMDG_작업통합백업_20261104.zip")
    
    print(f"Creating backup zip at: {zip_path}")
    t0 = time.time()
    
    # 1. Prepare README content
    readme_content = """# 🚀 DMDG & Do it! 안티그래비티 통합 작업 백업 가이드 (2026-11-04)

본 압축 파일은 오늘까지 진행된 **Do it! 안티그래비티 도서/강의 자료**와 **4대 역량 평가 시스템 & dmdg-live.com 포털 연동 작업**의 전체 결과물입니다. 집에서 압축을 풀고 바로 이어서 작업하거나 열람하실 수 있습니다.

---

## 📂 폴더 구조 안내

```text
DMDG_작업통합백업_20261104/
│
├── 01_DOIT_안티그래비티_강의자료_및_PDF/
│   ├── 00_안티그래비티_실습_프롬프트_치트시트.md  (1~8장 및 부록 프롬프트/코드 1클릭 복사용)
│   ├── 1장 안티그래비티와 프롬프트 기초.pdf       (검색/선택 가능 Searchable PDF)
│   ├── 2장 안티그래비티 시작하기.pdf
│   ├── 3장 안티그래비티 실전 활용법.pdf
│   ├── 4장 레트로 게임 만들기.pdf
│   ├── 5장 자동화 도구를 만들어 생산성 향상하기.pdf
│   ├── 6장 웹 서비스 개발의 기초 이해하기.pdf
│   ├── 7장 나만의 개발자 성향 테스트 만들기.pdf
│   ├── 8장 디지털 롤링페이퍼 서비스 구현하기.pdf
│   ├── 부록 AI를 외부 세상과 연결해 주는 MCP 활용법.pdf
│   ├── *.docx (원본 원고 파일 9종)
│   ├── doit_antigravity_book-main/ (예제 소스 코드 및 프롬프트 저장소)
│   └── DOIT_안티그레비티_강의PPT/ (강의용 공식 슬라이드 덱)
│
├── 02_DMDG_4대역량평가시스템/
│   ├── sql_exam/          (SQL Master 역량 평가 시스템 - 90문항)
│   ├── ai_math_exam/      (AI 수학 역량 평가 시스템 - 60문항)
│   ├── ai_data_exam/      (빅데이터 분석 및 엔지니어링 평가 시스템 - 90문항)
│   ├── python_ai_exam/    (파이썬 & 생성형 AI 실전 평가 시스템 - 145문항)
│   └── dmdg_live_portal/  (dmdg-live.com 포털 연동 웹 파일)
│
└── 03_자동화스크립트_및_도구/
    ├── build_all_searchable_pdfs.py (Windows OCR 기반 투명 텍스트 레이어 PDF 변환기)
    ├── build_exam_webapp.py         (시험 웹앱 원클릭 빌더)
    └── update_dmdg_live_portal.py   (포털 카테고리 자동 동기화기)
```

---

## 🌐 4대 역량 평가 시스템 온라인 라이브 링크 (설치 없이 즉시 접속 가능)

인터넷이 연결된 환경에서는 압축을 풀지 않아도 아래 공식 라이브 링크로 언제든 접속하실 수 있습니다:

1. **SQL Master 역량 평가 시스템**
   - URL: https://junsu-cho.github.io/sql_master_exam/
2. **AI 수학 역량 평가 시스템**
   - URL: https://junsu-cho.github.io/ai_math_exam/
3. **빅데이터 & 분석 역량 평가 시스템**
   - URL: https://junsu-cho.github.io/ai_data_exam/
4. **파이썬 & 생성형 AI 실전 평가 시스템**
   - URL: https://junsu-cho.github.io/python_ai_exam/
5. **DMDG 통합 라이브 포털**
   - URL: https://dmdg-live.com (또는 GitHub Pages 연동 주소)

> **관리자 콘솔 비밀번호**: `dmdg2026!`

---

## 💻 집에서 로컬로 실행하는 방법

1. 압축을 원하는 폴더에 풉니다.
2. 터미널(PowerShell 또는 CMD)을 열고 실행하려는 평가 시스템 폴더로 이동합니다:
   ```bash
   cd 02_DMDG_4대역량평가시스템/sql_exam
   python -m http.server 8000
   ```
3. 브라우저에서 `http://localhost:8000` 으로 접속하면 바로 시험을 보거나 관리자 콘솔을 사용할 수 있습니다.

---

## 📖 도서 PDF 텍스트 복사 및 실습 팁
- 모든 PDF는 **Searchable & Selectable PDF**로 변환되어 있어 마우스 드래그로 본문이나 프롬프트 상자를 긁어 `Ctrl + C`로 복사할 수 있습니다.
- 오탈자 없는 깨끗한 프롬프트 원문은 `00_안티그래비티_실습_프롬프트_치트시트.md` 파일에서 마크다운 뷰어/VS Code로 열어 바로 복사해 쓰시면 더욱 편리합니다.
"""

    exclude_dirs = {'.git', 'node_modules', '__pycache__', '.pytest_cache'}
    exclude_extensions = {'.tmp', '.pyc'}

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        # Add README
        zf.writestr("README_집에서_이어하기_가이드.md", readme_content.encode('utf-8'))
        print("Added: README_집에서_이어하기_가이드.md")

        # 1. DOIT_안티그레비티 도서내용 및 강의자료
        base_doit = r"C:\Users\PC\Downloads\DOIT_안티그레비티 도서내용 및 강의자료\DOIT_안티그레비티 도서내용 및 강의자료"
        print("\nAdding DOIT Antigravity materials...")
        for root, dirs, files in os.walk(base_doit):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for f in files:
                if any(f.endswith(ext) for ext in exclude_extensions) or f.startswith('test_'):
                    continue
                file_path = os.path.join(root, f)
                rel_path = os.path.relpath(file_path, base_doit)
                arc_path = os.path.join("01_DOIT_안티그래비티_강의자료_및_PDF", rel_path)
                zf.write(file_path, arc_path)
        print("DOIT materials added.")

        # 2. 4 Exam platforms
        exam_dirs = [
            ("sql_exam", r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam"),
            ("ai_math_exam", r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam"),
            ("ai_data_exam", r"C:\DMDG_Jobs\DMDG_PRJ\ai_data_exam"),
            ("python_ai_exam", r"C:\DMDG_Jobs\DMDG_PRJ\python_ai_exam"),
        ]
        print("\nAdding 4 Exam platforms...")
        for name, path in exam_dirs:
            if not os.path.exists(path):
                continue
            for root, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if d not in exclude_dirs]
                for f in files:
                    if any(f.endswith(ext) for ext in exclude_extensions) or f.startswith('test_') or f.endswith('.png') and 'test_' in f:
                        continue
                    file_path = os.path.join(root, f)
                    rel_path = os.path.relpath(file_path, path)
                    arc_path = os.path.join("02_DMDG_4대역량평가시스템", name, rel_path)
                    zf.write(file_path, arc_path)
            print(f"  Added {name}")

        # 3. Automation scripts
        script_files = [
            r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\build_all_searchable_pdfs.py",
            r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\build_exam_webapp.py",
            r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\build_question_bank.py",
            r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\update_dmdg_live_portal.py",
            r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\deploy_github_pages.py",
            r"c:\DMDG_Jobs\scripts\wikidocs_tools\publish_3_boiled_frog_novels.py",
            r"c:\DMDG_Jobs\scripts\build_boiled_frog_complete.py",
        ]
        print("\nAdding Automation scripts...")
        for sf in script_files:
            if os.path.exists(sf):
                arc_path = os.path.join("03_자동화스크립트_및_도구", os.path.basename(sf))
                zf.write(sf, arc_path)
                print(f"  Added {os.path.basename(sf)}")

        # 4. Boiled Frog Novels & Multilingual E-Reader
        novel_zip_path = os.path.join(downloads_dir, "DMDG_서재_삶은개구리_단편소설_및_EReader_20261104.zip")
        if os.path.exists(novel_zip_path):
            print("\nAdding Boiled Frog novels package...")
            with zipfile.ZipFile(novel_zip_path, 'r') as nz:
                for n_info in nz.infolist():
                    data = nz.read(n_info.filename)
                    arc_path = os.path.join("04_DMDG_서재_삶은개구리_단편소설_및_EReader", n_info.filename).replace('\\', '/')
                    zf.writestr(arc_path, data)
            print("Boiled Frog novels package added.")

    sz_mb = os.path.getsize(zip_path) / (1024 * 1024)
    t1 = time.time()
    print(f"\n==========================================")
    print(f"Successfully created: {zip_path}")
    print(f"Size: {sz_mb:.2f} MB in {t1 - t0:.1f}s")
    print(f"==========================================")

if __name__ == "__main__":
    create_backup()

