from aiomysql import DictCursor
from utils.base import BaseHandler
from tornado.escape import json_encode
from tornado.web import RequestHandler

class Service_1_Handler(BaseHandler):

    async def get(self):
        result = await self.model.getdata()
        # async with self.application.db.acquire() as conn:
        #     cursor = await conn.cursor(DictCursor)
        #     await cursor.execute('select productline, count(1) as cnt from sales.sales_data group by productline')
        #     result = await cursor.fetchall()
        # print(result)
        self.write(json_encode(result))
