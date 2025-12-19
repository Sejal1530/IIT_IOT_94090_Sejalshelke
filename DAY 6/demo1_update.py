import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensor_readings",
    use_pure = True
    )

def update_reading(reading_id, temperature, humidity):
    conn = mysql.connector.connect()
    cursor = conn.cursor()

    query = """
    UPDATE sensor_readings
    SET temperature = 20, humidity = 29
    WHERE id = 1
    """
    cursor.execute(query, (temperature, humidity, reading_id))
    conn.commit()

    print("Record updated successfully")

    cursor.close()
    conn.close()
