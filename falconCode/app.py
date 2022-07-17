import falcon
from falcon_marshmallow import Marshmallow
from sdata import Sdata, GetData


application = falcon.App(
     middleware=[
        Marshmallow(),
     ]
)

datas = Sdata()
application.add_route('/deo',datas)

getData = GetData()
application.add_route('/api/v1/getData',getData)