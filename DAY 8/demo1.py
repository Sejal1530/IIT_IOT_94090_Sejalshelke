import paho.mqtt.client as mqtt
import mysql.connector
import json
import time
import random
from datetime import datetime

#THRESHOLDS
TEMP_THRESHOLD = 35      
LDR_THRESHOLD = 300      

#MQTT CALLBACK 
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    con = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="iot_smart_home_db"   
    )
    cur = con.cursor()

    if msg.topic == "sensor/ldr":
        value = data["intensity"]
        sensor = "LDR"
        status = "LIGHT ON" if value < LDR_THRESHOLD else "LIGHT OFF"

    elif msg.topic == "sensor/lm35":
        value = data["temperature"]
        sensor = "LM35"
        status = "FAN ON" if value > TEMP_THRESHOLD else "FAN OFF"

    cur.execute(
        "INSERT INTO sensor_data (sensor_type, value, timestamp) VALUES (%s, %s, %s)",
        (sensor, value, datetime.now())
    )

    con.commit()
    cur.close()
    con.close()

    print(f"{sensor} | Value: {value} | Status: {status}")

#MQTT SETUP
client = mqtt.Client(client_id="iot_smart_home")
client.connect("localhost", 1883, 60)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")
client.on_message = on_message

client.loop_start()

print("IoT Smart Home System Running...\n")

#PUBLISH SENSOR DATA 
while True:
    ldr_data = {"intensity": random.randint(0, 1023)}
    lm35_data = {"temperature": round(random.uniform(20, 45), 2)}

    client.publish("sensor/ldr", json.dumps(ldr_data))
    client.publish("sensor/lm35", json.dumps(lm35_data))

    time.sleep(5)
