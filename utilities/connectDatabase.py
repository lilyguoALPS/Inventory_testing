import pymysql


class Mysql:
    @staticmethod
    def get_conection():
        conn  = pymysql.connect(
        host='127.0.0.1',
        port=3305,
        user='root',
        password='alps20210329',
        db='vh_inventory_v5'
        )
        return conn   