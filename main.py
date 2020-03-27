import web
import sys

urls = (
    '/', 'index',
    '/test', 'test',
)

app = web.application(urls, globals())

class index:
    def GET(self):
        params = web.input()
        userid = params.get('userid', '')
        return userid

class test:
    def GET(self):
        print web.input()
        return '222'

if __name__ == "__main__":
    app.run()
