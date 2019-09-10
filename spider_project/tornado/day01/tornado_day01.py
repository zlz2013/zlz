import tornado

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url


#用来响应用户请求
class IndexHandler(RequestHandler):
    #用来响应以get方式发起的请求
    def get(self,*args,**kwargs):
        #服务器给浏览器的想用内容
        self.write("hello tornado")
    #响应以post方式发起的请求
    def post(self):
        pass

#创建application对象，进行若干个对服务器的设置
#例如：路由列表，模板路径，静态资源路径
app=Application([('/',IndexHandler)])
#创建服务器程序
server=HTTPServer(app)
#让服务器监听某个端口
server.listen(8888)
#启动服务器
IOLoop.current().start()

