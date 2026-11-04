# -*- coding: utf-8 -*-
import os
import json
import subprocess
import urllib.request
import urllib.error
import time

BASE_DIR = r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam"

# 1. Create .nojekyll, .gitignore, README.md, firestore.rules, firebase.json, .firebaserc
with open(os.path.join(BASE_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
    f.write("")

with open(os.path.join(BASE_DIR, ".gitignore"), "w", encoding="utf-8") as f:
    f.write("__pycache__/\n*.pyc\n.DS_Store\n")

readme_md = """# 🧠 AI & LLM 사전학습(수학·기초 엔지니어링) 75문항 역량 평가 시스템

위키독스 전자책 **《AI 와 데이터 분석 & 최신 LLM 에이전트 완벽 정복을 위한 사전 학습(수학·기초 엔지니어링)》** ([https://wikidocs.net/book/21701](https://wikidocs.net/book/21701)) 기반의 **75문항 4지선다 객관식 역량 평가 웹 서비스**입니다.

## 🔗 서비스 접속 주소
- **학생용 시험 응시 페이지**: [https://freefluxkr.github.io/ai_math_exam/](https://freefluxkr.github.io/ai_math_exam/)
- **강사/관리자 대시보드**: [https://freefluxkr.github.io/ai_math_exam/admin.html](https://freefluxkr.github.io/ai_math_exam/admin.html)

## 📚 출제 파트 구성 (총 5개 파트 × 15문항 = 75문항)
1. **Part 1. 선형대수학: 인공지능의 다차원 공간 언어** (15문항, Day 01~04)
2. **Part 2. 미적분 & 최적화: 딥러닝과 머신러닝의 학습 엔진** (15문항, Day 05~08)
3. **Part 3. 확률통계 & 정보이론: 불확실성과 데이터의 본질 정량화** (15문항, Day 09~12)
4. **Part 4. 이산수학 & 상태 그래프: 자율 에이전트 아키텍처의 뼈대** (15문항, Day 13~16)
5. **Part 5. 실전 AI 파이썬 엔지니어링: 코드로 구현하는 차세대 시스템** (15문항, Day 17~20)

## 🛡️ 주요 기능
- **무단 복사/드래그/우클릭/단축키 원천 차단**: `user-select: none`, 우클릭 방지, `Ctrl+C/A/X/U/S/P` 및 `F12` 개발자 도구 차단 및 경고 토스트 알림
- **중복 응시 원천 차단**: 동일 성명 및 동일 브라우저/기기(Device Fingerprint) 재응시 차단
- **관리자 콘솔 선택 학생 삭제**: 체크박스 다중 선택을 통한 특정 학생 데이터 일괄 삭제 및 재응시 허용 기능 (`admin.html`)
"""
with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

firestore_rules = """rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /sql_exam_config/{docId} {
      allow read, write: if true;
    }
    match /sql_exam_submissions/{subId} {
      allow read, write: if true;
    }
    match /ai_math_exam_config/{docId} {
      allow read, write: if true;
    }
    match /ai_math_exam_submissions/{subId} {
      allow read, write: if true;
    }
  }
}
"""
with open(os.path.join(BASE_DIR, "firestore.rules"), "w", encoding="utf-8") as f:
    f.write(firestore_rules)

with open(os.path.join(BASE_DIR, "firebase.json"), "w", encoding="utf-8") as f:
    f.write('{\n  "firestore": {\n    "rules": "firestore.rules"\n  }\n}\n')

with open(os.path.join(BASE_DIR, ".firebaserc"), "w", encoding="utf-8") as f:
    f.write('{\n  "projects": {\n    "default": "dmdg-live"\n  }\n}\n')

print("Static config files created.")

# 2. Extract GitHub token from sql_exam remote URL (read-only lookup)
res = subprocess.run(
    ["git", "-C", r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam", "remote", "get-url", "origin"],
    capture_output=True, text=True, check=True
)
origin_url = res.stdout.strip()
# Format: https://freefluxkr:TOKEN@github.com/freefluxkr/sql_exam.git
auth_part = origin_url.split("https://")[1].split("@github.com")[0]
username, token = auth_part.split(":", 1)
repo_name = "ai_math_exam"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json",
    "User-Agent": "DMDG-AI-Math-Exam-Deployer"
}

# 3. Create repository freefluxkr/ai_math_exam if not exists
create_repo_url = "https://api.github.com/user/repos"
repo_payload = json.dumps({
    "name": repo_name,
    "description": "AI & LLM 사전학습(수학·기초 엔지니어링) 75문항 역량 평가 시스템 (Book 21701)",
    "private": False,
    "has_issues": True,
    "has_projects": False,
    "has_wiki": False
}).encode("utf-8")

req = urllib.request.Request(create_repo_url, data=repo_payload, headers=headers, method="POST")
try:
    with urllib.request.urlopen(req) as resp:
        print("Created GitHub repo:", resp.status)
except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="ignore")
    if e.code == 422:
        print("GitHub repo already exists (422), continuing...")
    else:
        print(f"GitHub repo creation error {e.code}: {err_body}")
        raise

# 4. Initialize Git in BASE_DIR, commit, and push to main
def run_git(args):
    r = subprocess.run(["git", "-C", BASE_DIR] + args, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"git {' '.join(args)} -> {r.returncode}: {r.stderr.strip()}")
    return r

run_git(["init"])
run_git(["config", "user.name", "freefluxkr"])
run_git(["config", "user.email", "freefluxkr@users.noreply.github.com"])
run_git(["branch", "-M", "main"])

remote_target = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
r_rem = subprocess.run(["git", "-C", BASE_DIR, "remote"], capture_output=True, text=True)
if "origin" in r_rem.stdout.split():
    run_git(["remote", "set-url", "origin", remote_target])
else:
    run_git(["remote", "add", "origin", remote_target])

run_git(["add", "-A"])
run_git(["commit", "-m", "feat: Deploy AI Math & Engineering 75-question exam service + anti-copy + selective student delete"])
push_res = run_git(["push", "-u", "origin", "main", "--force"])
print("Git push completed with code:", push_res.returncode)

# 5. Enable GitHub Pages on main branch / root
pages_url = f"https://api.github.com/repos/{username}/{repo_name}/pages"
pages_payload = json.dumps({
    "source": {
        "branch": "main",
        "path": "/"
    }
}).encode("utf-8")

req_pages = urllib.request.Request(pages_url, data=pages_payload, headers=headers, method="POST")
try:
    with urllib.request.urlopen(req_pages) as resp:
        print("GitHub Pages enabled:", resp.status)
except urllib.error.HTTPError as e:
    err_body = e.read().decode("utf-8", errors="ignore")
    if e.code == 409:
        print("GitHub Pages already enabled (409).")
    else:
        print(f"GitHub Pages API {e.code}: {err_body}")
