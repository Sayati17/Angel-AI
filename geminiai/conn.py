import mysql.connector

def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="user",
        password="",
        database="table_name",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT InjectionId, InjectionName, InjectionDescription FROM tablepromptinjection")
    data = cursor.fetchall()
    conn.close()
    return data