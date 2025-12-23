import paho.mqtt.client as mqtt

# ---------- THRESHOLDS ----------
PULSE_THRESHOLD = 100
SPO2_THRESHOLD = 92

# ---------- MQTT CALLBACK ----------
def on_message(client, userdata, msg):
    try:
        value = int(msg.payload.decode().strip())

        if msg.topic == "health/pulse":
            print(f"Received Pulse Rate: {value} bpm")

            if value > PULSE_THRESHOLD:
                alert = f"ALERT! High Pulse Rate: {value} bpm"
                client.publish("health/alert", alert)
                print(alert)

        elif msg.topic == "health/spo2":
            print(f"Received SpO2 Level: {value}%")

            if value < SPO2_THRESHOLD:
                alert = f"ALERT! Low SpO2 Level: {value}%"
                client.publish("health/alert", alert)
                print(alert)

    except ValueError:
        print("Invalid data received:", msg.payload.decode())
    except Exception as e:
        print("Error:", e)

# ---------- MQTT CLIENT ----------
client = mqtt.Client(client_id="health_monitor")
client.on_message = on_message

try:
    client.connect("localhost", 1883, 60)
except Exception as e:
    print("MQTT connection failed:", e)
    exit()

client.subscribe("health/pulse")
client.subscribe("health/spo2")

print("Healthcare Monitoring System Running...\n")

client.loop_forever()
