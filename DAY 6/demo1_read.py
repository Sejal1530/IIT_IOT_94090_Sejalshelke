import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensor_readings",
    use_pure = True
    )

def fetch_readings():
    conn = mysql.connector.connect()
    cursor = conn.cursor()

    query = "SELECT * FROM sensor_readings"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()
