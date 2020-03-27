import web
import sys

urls = (
    '/', 'index',
    '/test/', 'test',
)
app = web.application(urls, globals())

class index:
    def GET(self):
        print web.input()
        return 'Hello world!'


if __name__ == "__main__":
    app.run()
