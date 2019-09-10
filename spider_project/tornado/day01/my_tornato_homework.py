import tornado

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler, url


#用来响应用户请求
class IndexHandler(RequestHandler):
    #用来响应以get方式发起的请求
    def get(self,*args,**kwargs):
        #服务器给浏览器的想用内容
        html='''<form method=post action=/login enctype=multipart/form-data><br>
                <input type=text name=name><br>
                <input type=password name=password><br>
                <input type=file name=avatar><br>
                <input type=submit value=提交>&nbsp
                <input type=reset value=重置>
                
                </form>'''
        self.write(html)
    #响应以post方式发起的请求
    def post(self):
        pass
class LoginHandler(RequestHandler):
    def get(self,*args,**kwargs):
        pass
    def post(self,*args,**kwargs):
        name=self.get_body_argument('name',None)
        password=self.get_body_argument('password',None)
        print('用户名：',name,"密码:",password)

        files=self.request.files
        avatars=files.get('avatar')[0]
        filename=avatars.get('filename')
        body=avatars.get('body')
        f=open('picture/%s'%filename,'wb')
        f.write(body)
        f.close()


define('port',default=8888,type=int,multiple=False)
parse_config_file('config')
#创建application对象，进行若干个对服务器的设置
#例如：路由列表，模板路径，静态资源路径
app=Application([('/',IndexHandler),('/login',LoginHandler)])
#创建服务器程序
server=HTTPServer(app)
#让服务器监听某个端口
server.listen(options.port)
#启动服务器
IOLoop.current().start()

