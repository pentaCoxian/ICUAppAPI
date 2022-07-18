import json
import falcon
import time

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
        print('+++start main+++')
        start = time.time()
        print(req.host)
        
        q=''
        params = req.params
        q = params['search']
        print(q)
        f = searchFullText(q)
        resp.text = json.dumps(f, ensure_ascii=False)
        print("---main %s seconds ---" % (time.time() - start))