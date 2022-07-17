import json
import falcon

import sys
sys.path.append("../dbAccess")
from search import searchFullText

class Sdata:
    def on_get(self, req, resp):
        doc = {
            'text': str(resp),
            'obj': str(req)
        }
        resp.text = json.dumps(doc, ensure_ascii=False)

class GetData:
    def on_get(self,req,resp):
        q=''
        for k,v in req.params.items():
            q += ' +'+v
        print(q)
        f = searchFullText(q)
        print(f)
        resp.text = json.dumps(f, ensure_ascii=False)