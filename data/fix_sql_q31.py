# -*- coding: utf-8 -*-
import json

for path in [
    r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam\data\questions.json",
    r"C:\DMDG_Jobs\DMDG_PRJ\sql_exam\js\questions-data.js"
]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace(
        "MySQL 주요 문자 내장 함수 중, 문자열 '데이터베이스'의 실제 바이트 수(12바이트)가 아닌 순수한 문자 개수(6개)를 반환하는 함수는?",
        "MySQL 주요 문자 내장 함수 중, 문자열 '데이터베이스'의 실제 바이트 수(18바이트)가 아닌 순수한 문자 개수(6개)를 반환하는 함수는?"
    )
    text = text.replace(
        "`LENGTH()` 함수는 문자열의 바이트 수(UTF-8 한글 한 글자당 3바이트 적용 시 12)를 반환하고, `CHAR_LENGTH()` 함수는 순수한 문자 글자 수(6)를 반환합니다.",
        "`LENGTH()` 함수는 문자열의 바이트 수(UTF-8 한글 한 글자당 3바이트 × 6글자 = 18)를 반환하고, `CHAR_LENGTH()` 함수는 순수한 문자 글자 수(6)를 반환합니다."
    )
    text = text.replace(
        "1. LENGTH('데이터베이스'): 12 (바이트 수 반환, 한글 1자당 3바이트 x 4 = 12)\\n2. CHAR_LENGTH('데이터베이스'): 4 (순수 글자 수 반환)",
        "1. LENGTH('데이터베이스'): 18 (바이트 수 반환, 한글 1자당 3바이트 x 6 = 18)\\n2. CHAR_LENGTH('데이터베이스'): 6 (순수 글자 수 반환)"
    )
    old_kw = """    "keywords": [
      "18",
      "12",
      "6",
      "4",
      "바이트",
      "글자"
    ]"""
    new_kw = """    "keywords": [
      "18",
      "6"
    ]"""
    text = text.replace(old_kw, new_kw)
    text = text.replace(old_kw.replace("\n", "\r\n"), new_kw.replace("\n", "\r\n"))

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print("Updated:", path)

