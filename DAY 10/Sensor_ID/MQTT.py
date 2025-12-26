from flask import Flask, request
import mysql.connector
from datetime import datetime
import paho.mqtt.publish as publish

# Create Flask app
app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="agro_iot_system"
)
cursor = db.cursor()

# Threshold value
THRESHOLD = 300

# MQTT details
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "iit/moisture/alert"

@app.route("/add_moisture")
def add_moisture():

    sensor_id = request.args.get("sensor_id")
    moisture = request.args.get("moisture")

    if sensor_id is None or moisture is None:
        return "ERROR: Missing sensor_id or moisture"

    moisture = int(moisture)

    # Current date and time
    now = datetime.now()
    date = now.date()
    time = now.time()

    # Insert into database
    sql = "INSERT INTO moisture_data VALUES (%s, %s, %s, %s)"
    values = (sensor_id, moisture, date, time)
    cursor.execute(sql, values)
    db.commit()

    # Check threshold
    if moisture < THRESHOLD:
        alert_msg = f"ALERT: Sensor {sensor_id} Moisture LOW ({moisture})"
        publish.single(MQTT_TOPIC, alert_msg, hostname=MQTT_BROKER)
        return alert_msg + " | Stored + MQTT Alert Sent"

    return "Moisture Stored Successfully"

if __name__ == "__main__":
    app.run(debug=True)
