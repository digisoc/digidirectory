import json
import requests

url = "https://www.handbook.unsw.edu.au/api/es/search"
headers = {"content-type": "application/json", "date": "Sun, 03 Jul 2022 11:39:45 GMT"}

i = 0
while (i <= 6700):
    payload = json.dumps({"query":{"bool":{"must":[{"term":{"live":True}},[{"bool":{"minimum_should_match":"50%","should":[{"query_string":{"fields":["*implementationYear*"],"query":"*2022*"}}]}},{"bool":{"minimum_should_match":"50%","should":[{"query_string":{"fields":["*active*"],"query":"1"}}]}}]],"filter":[{"terms":{"contenttype":["unsw_psubject","unsw_pcourse","unsw_pcourse","unsw_paos"]}}]}},"sort":[{"unsw_psubject.code_dotraw":{"order":"asc"}},{"unsw_pcourse.code_dotraw":{"order":"asc"}},{"unsw_paos.code_dotraw":{"order":"asc"}}],"from":i,"size":50,"track_scores":True,"_source":{"includes":["*.code","*.name","*.award_titles","*.keywords","urlmap","contenttype"],"excludes":["",None]}})
    r = requests.post(url, data=payload, headers=headers)

    data = r.json()["contentlets"]

    info = []

    for d in data:
        temp = {}
        temp["code"] = d["code"]
        temp["title"] = d["title"]
        if "description" in d:
            temp["description"] = d["description"]
        info.append(temp)

    i += 50

with open('courses.txt', 'w') as f:
    f.write(json.dumps(info))