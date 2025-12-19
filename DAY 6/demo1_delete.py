import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "sensor_readings",
    use_pure = True
    )

def delete_reading(reading_id):
    conn = mysql.connector.connect()
    cursor = conn.cursor()

    query = "DELETE FROM sensor_readings WHERE id = %s"
    cursor.execute(query, (reading_id,))
    conn.commit()

    print("Record deleted successfully")

    cursor.close()
    conn.close()

