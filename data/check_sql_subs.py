# -*- coding: utf-8 -*-
import urllib.request
import json

url = "https://firestore.googleapis.com/v1/projects/dmdg-live/databases/(default)/documents/sql_exam_submissions?pageSize=100"
r = urllib.request.urlopen(url, timeout=10)
data = json.loads(r.read().decode("utf-8"))
docs = data.get("documents", [])

for doc in docs:
    fields = doc.get("fields", {})
    name = fields.get("studentName", {}).get("stringValue", "")
    details_arr = fields.get("details", {}).get("arrayValue", {}).get("values", [])
    for d in details_arr:
        mv = d.get("mapValue", {}).get("fields", {})
        qid = mv.get("questionId", {}).get("stringValue", "")
        if qid == "A-S-01":
            u_ans = mv.get("userAnswer", {}).get("stringValue", "")
            is_corr = mv.get("isCorrect", {}).get("booleanValue", False)
            score = mv.get("score", {}).get("integerValue", "0")
            print(f"Student: {name} | A-S-01 userAnswer: {repr(u_ans)} | isCorrect: {is_corr} | score: {score}")

