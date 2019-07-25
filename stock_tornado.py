import tornado.ioloop
import tornado.web
import os
import stock_arithmetic_root
from database_root import Select_Without_State
class InputHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        id=self.get_argument('id')
        print(id)
        self.redirect('/result/'+id)

class MainHandler(tornado.web.RequestHandler):
    def get(self,id):
        print(id)
        stock_arithmetic_root.stock_arithmetic.stock_code = str(id)
        open = stock_arithmetic_root.stock_arithmetic("", "open").stock_sklearn()
        close = stock_arithmetic_root.stock_arithmetic("", "close").stock_sklearn()
        high = stock_arithmetic_root.stock_arithmetic("", "high").stock_sklearn()
        low = stock_arithmetic_root.stock_arithmetic("", "low").stock_sklearn()
        stock_forecast=[open, close, high, low]
        database_name = ['sh'+id]
        get_stock_database = Select_Without_State(database_name).Select()
        self.render('candlestick.html',id=id,stock_forecast=stock_forecast,get_stock_database=get_stock_database)


def make_app():
    return tornado.web.Application([
        (r"/result/(\w+)", MainHandler),
        (r"/", InputHandler),
    ],
     template_path=os.path.join(os.path.dirname(__file__), "templates"),
     static_path=os.path.join(os.path.dirname(__file__), "static"),
    )
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()