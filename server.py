import asyncio
import tornado.web

from utils.utils import get_connection_pool
from api.service_1.service_1_handler import Service_1_Handler
from api.service_2.service_2_handler import Service_2_Handler
from api.service_3.service_3_handler import Service_3_Handler
from api.service_1.service_1_model import Service_1_Model
# from api.service_2.service_2_model import Service_2_Model
# from api.service_3.service_3_model import Service_3_Model


class Application(tornado.web.Application):
    _routes = [
        tornado.web.url(r"/service1", Service_1_Handler, dict(model=Service_1_Model())),
        # tornado.web.url(r"/service1", Service_1_Handler),
        tornado.web.url(r"/service2", Service_2_Handler),
        tornado.web.url(r"/service3", Service_3_Handler),
    ]

    def __init__(self, db):
        self.db = db
        super(Application, self).__init__(self._routes)


async def main():
    pool = await get_connection_pool()
    async with pool as db:
        application = Application(db)
        application.listen(8888)
        shutdown_event = asyncio.Event()
        await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())