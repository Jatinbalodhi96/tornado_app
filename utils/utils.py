import aiomysql


async def get_connection_pool():
    return await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='sales', autocommit=True,
                                      minsize=50, maxsize=100)
