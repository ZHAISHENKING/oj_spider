import requests
import json

a=[1,2,3,145]
se = requests.session()
for i in a:
    filename = '/Users/mac/Desktop/rename/package/problem%d.zip' % i
    try:
        r = se.get('https://loj.ac/problem/%d/testdata/download' % i, timeout=10)
        if int(r.headers["Content-Length"])/1000000 > 10:
            s = {
                "err_number": i,
                "size": int(r.headers["Content-Length"]) / 1000000,
                "err_message": "文件过大"
            }
            with open('err.json', 'a+', encoding='utf-8') as f:
                json_str = json.dumps(s, ensure_ascii=False, indent=4)
                f.write(json_str + "," + '\n')
                f.close()
        else:
            with open(filename, "wb") as f:
                f.write(r.content)


    except Exception as e:
        s = {
            "err_number": i,
            "size": 0,
            "err_message": "测试用例缺失"
        }
        with open('err.json', 'a+', encoding='utf-8') as f:
            json_str = json.dumps(s, ensure_ascii=False, indent=4)
            f.write(json_str + "," + '\n')
            f.close()
