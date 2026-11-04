# -*- coding: utf-8 -*-
import sys
import os
import json
import subprocess
import urllib.request
import urllib.error

def deploy_exam_repo(base_dir, repo_name, description):
    res = subprocess.run(
        ["git", "-C", r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam", "remote", "get-url", "origin"],
        capture_output=True, text=True, check=True
    )
    origin_url = res.stdout.strip()
    auth_part = origin_url.split("https://")[1].split("@github.com")[0]
    username, token = auth_part.split(":", 1)

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "DMDG-Exam-Deployer"
    }

    # 1. Create GitHub repository
    create_repo_url = "https://api.github.com/user/repos"
    repo_payload = json.dumps({
        "name": repo_name,
        "description": description,
        "private": False,
        "has_issues": True,
        "has_projects": False,
        "has_wiki": False
    }).encode("utf-8")

    req = urllib.request.Request(create_repo_url, data=repo_payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"[{repo_name}] Created GitHub repo: {resp.status}")
    except urllib.error.HTTPError as e:
        if e.code == 422:
            print(f"[{repo_name}] GitHub repo already exists (422), continuing...")
        else:
            raise

    # 2. Initialize Git, commit, and push
    def run_git(args):
        return subprocess.run(["git", "-C", base_dir] + args, capture_output=True, text=True)

    run_git(["init"])
    run_git(["config", "user.name", "freefluxkr"])
    run_git(["config", "user.email", "freefluxkr@users.noreply.github.com"])
    run_git(["branch", "-M", "main"])

    remote_target = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
    r_rem = subprocess.run(["git", "-C", base_dir, "remote"], capture_output=True, text=True)
    if "origin" in r_rem.stdout.split():
        run_git(["remote", "set-url", "origin", remote_target])
    else:
        run_git(["remote", "add", "origin", remote_target])

    run_git(["add", "-A"])
    run_git(["commit", "-m", f"feat: Deploy {repo_name} exam service + 12-student whitelist + 2026-11-05 date lock"])
    push_res = run_git(["push", "-u", "origin", "main", "--force"])
    print(f"[{repo_name}] Git push exit code: {push_res.returncode}")

    # 3. Enable GitHub Pages
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
            print(f"[{repo_name}] GitHub Pages enabled: {resp.status}")
    except urllib.error.HTTPError as e:
        if e.code == 409:
            print(f"[{repo_name}] GitHub Pages already enabled (409).")
        else:
            print(f"[{repo_name}] GitHub Pages API {e.code}")

if __name__ == "__main__":
    target = sys.argv[1]
    if target == "ai_data_exam":
        deploy_exam_repo(
            r"C:\DMDG_Jobs\DMDG_PRJ\ai_data_exam",
            "ai_data_exam",
            "AI 와 데이터 분석 (Book 21658) 90문항 역량 평가 시스템"
        )
    elif target == "python_ai_exam":
        deploy_exam_repo(
            r"C:\DMDG_Jobs\DMDG_PRJ\python_ai_exam",
            "python_ai_exam",
            "점프 투 파이썬 & 판다스·넘파이·ML/DL 145문항 통합 역량 평가 시스템"
        )

