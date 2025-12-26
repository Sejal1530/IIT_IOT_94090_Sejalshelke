#include <WiFi.h>
#include <PubSubClient.h>

// WiFi Credentials
const char* ssid = "Realme 12";
const char* password = "vobt0457";

const char* mqtt_server = "broker.hivemq.com"; 
const int mqtt_port = 1883;

const char* topic = "sensor/data";

WiFiClient espClient;
PubSubClient client(espClient);

// Connect to WiFi
void setup_wifi() {
  delay(10);
  Serial.print("Connecting to WiFi");

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
}

// Reconnect MQTT
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();

  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Example sensor values 
  float temperature = 29.3;
  float humidity = 62.8;

  String payload = "{";
  payload += "\"temperature\":" + String(temperature) + ",";
  payload += "\"humidity\":" + String(humidity);
  payload += "}";

  Serial.print("Publishing: ");
  Serial.println(payload);

  client.publish(topic, payload.c_str());

  delay(5000); 
}
