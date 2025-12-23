import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

# DATABASE CONNECTION
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="home_automation_db"
    )

#MQTT CALLBACK
def on_message(client, userdata, msg):
    appliance = msg.topic.split("/")[1].upper()
    status = msg.payload.decode().upper()

    if status not in ["ON", "OFF"]:
        print("Invalid command received")
        return

    con = get_db_connection()
    cur = con.cursor()

    query = """
    UPDATE appliance_status
    SET status = %s, last_updated = %s
    WHERE appliance_name = %s
    """
    cur.execute(query, (status, datetime.now(), appliance))

    con.commit()
    cur.close()
    con.close()

    print(f"{appliance} turned {status}")

#MQTT CLIENT 
client = mqtt.Client(client_id="home_controller")
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("home/light")
client.subscribe("home/fan")

client.loop_forever()
