# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_agricultures",
    use_pure = True
)

# form a query to be executed
sensor_id = int(input("Enter sensor_id whose moisture_lvl to be updated : "))
moisture_lvl = int(input("Enter new moisture_lvl : "))

query = f"update soil_moisture SET moisture_level = {moisture_lvl} where sensor_id = {sensor_id};"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()
