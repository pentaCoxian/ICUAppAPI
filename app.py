import falcon
from falcon_marshmallow import Marshmallow
from falconCode.sdata import Sdata


application = falcon.App(
     middleware=[
        Marshmallow(),
     ]
)

datas = Sdata()
application.add_route('/deo',datas)