import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensor_readings",
    use_pure = True
    )

def insert_reading(temperature, humidity):
    conn = mysql.connector.connect()
    cursor = conn.cursor()

    query = """
    INSERT INTO sensor_readings (temperature, humidity, timestamp)
    VALUES (%s, %s, NOW())
    """
    cursor.execute(query, (temperature, humidity))
    conn.commit()

    print("Record inserted successfully")

    cursor.close()
    conn.close()
