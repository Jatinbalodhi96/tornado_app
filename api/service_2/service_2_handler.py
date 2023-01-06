from tornado.web import RequestHandler
from tornado.gen import coroutine


class Service_2_Handler(RequestHandler):

    @coroutine
    def get(self):
        self.write("Hello, world")
