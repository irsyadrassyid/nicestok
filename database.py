import pymysql

def connect_to_database():
    connection = pymysql.connect(
        host="nama_host",
        user="nama_user",
        password="password_user",
        database="nama_database"
    )
    return connection

def execute_query(connection, query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result