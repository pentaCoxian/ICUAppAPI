import json
import falcon

class Sdata:
    def on_get(self, req, resp):
        doc = {
            'text':'test data'
        }
        resp.text = json.dumps(doc, ensure_ascii=False)