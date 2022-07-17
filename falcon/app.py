import falcon
from sdata import Sdata
application = falcon.App()

datas = Sdata()
application.add_route('/deo',datas)