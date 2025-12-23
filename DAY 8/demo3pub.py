import paho.mqtt.client as mqtt
import time
import random

# ---------- MQTT CLIENT ----------
client = mqtt.Client(client_id="patient_device")

try:
    client.connect("localhost", 1883, 60)
except Exception as e:
    print("MQTT connection failed:", e)
    exit()

print("Patient health data publishing started...\n")

# ---------- PUBLISH SENSOR DATA ----------
try:
    while True:
        pulse = random.randint(55, 120)   # bpm
        spo2 = random.randint(88, 100)    # %

        client.publish("health/pulse", str(pulse))
        client.publish("health/spo2", str(spo2))

        print(f"Pulse: {pulse} bpm | SpO2: {spo2}%")

        time.sleep(5)

except KeyboardInterrupt:
    print("\nStopping patient device...")

finally:
    client.disconnect()
    print("MQTT client disconnected")
