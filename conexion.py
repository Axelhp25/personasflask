import pymysql


def obtener_conexion():
    return pymysql.connect(host='us-cdbr-east-06.cleardb.net',
                                user='bf634860d1d9e4',
                                password='4f71f2c1',
                                db='heroku_0052a0298a2abce')