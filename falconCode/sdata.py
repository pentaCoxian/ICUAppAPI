import json
import falcon

class Sdata:
    def on_get(self, req, resp):
        doc = {
            'text': str(resp),
            'obj': str(req)
        }
        resp.text = json.dumps(doc, ensure_ascii=False)