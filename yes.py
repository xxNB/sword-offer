# from tornado import gen
# from tornado.web import RequestHandler
# from tornado.httpclient import AsyncHTTPClient
#
#
# class GenAsyncHandler(RequestHandler):
#     @gen.coroutine
#     def get(self):
#         http_client = AsyncHTTPClient()
#         response = yield http_client.fetch("http://example.com")
#         do_something_with_response(response)
#         self.render("template.html")
#
#
# def do_something_with_response(response):
#     pass
#

from flask import Flask

app = Flask(__name__)

@app.route("/")
def func():
    return "The world is bad"

app.run()

