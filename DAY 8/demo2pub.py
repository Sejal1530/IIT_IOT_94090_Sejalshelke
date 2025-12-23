import paho.mqtt.client as mqtt
import time

# ---------- MQTT CLIENT ----------
client = mqtt.Client(client_id="remote_control")

try:
    client.connect("localhost", 1883, 60)
except Exception as e:
    print("MQTT connection failed:", e)
    exit()

print("Remote control started...")

# ---------- MENU LOOP ----------
try:
    while True:
        print("\n1. Light ON")
        print("2. Light OFF")
        print("3. Fan ON")
        print("4. Fan OFF")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            client.publish("home/light", "ON")
            print("Light turned ON")

        elif choice == "2":
            client.publish("home/light", "OFF")
            print("Light turned OFF")

        elif choice == "3":
            client.publish("home/fan", "ON")
            print("Fan turned ON")

        elif choice == "4":
            client.publish("home/fan", "OFF")
            print("Fan turned OFF")

        elif choice == "5":
            print("Exiting remote control...")
            break

        else:
            print("Invalid choice! Please try again.")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nRemote control stopped by user")

finally:
    client.disconnect()
    print("MQTT client disconnected")
