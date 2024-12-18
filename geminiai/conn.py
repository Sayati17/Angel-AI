import mysql.connector
import config

def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=config.db_user,
        password="",
        database=config.mysql_db,
    )
    cursor = conn.cursor()
    cursor.execute(config.query)
    data = cursor.fetchall()
    conn.close()
    return data