from aiomysql import DictCursor

class Service_1_Model():

    def __init__(self):
        self.query = 'select productline, count(1) as cnt from sales.sales_data group by productline'

    async def getdata(self):
        cursor = await self.conn.cursor(DictCursor)
        await cursor.execute(self.query)
        data = await cursor.fetchall()
        await cursor.close()
        return data
