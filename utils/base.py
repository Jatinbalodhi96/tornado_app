from tornado.web import RequestHandler
from tornado.gen import coroutine
import asyncio


class BaseHandler(RequestHandler):

    def initialize(self, model):
        self.model = model

    async def prepare(self):
        await asyncio.sleep(0.01)
        self.conn = await self.application.db.acquire()
        setattr(self.model, 'conn', self.conn)

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Content-Type", "application/json")

    async def options(self):
        self.set_status(204)
        await self.finish()

    @coroutine
    def on_finish(self):
        yield self.application.db.release(self.conn)
