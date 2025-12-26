#include <WiFi.h>
#include <PubSubClient.h>

// WiFi Credentials
const char* ssid = "Realme 12";
const char* password = "vobt0457";

const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;

const char* ledTopic = "device/led/control";

// LED Pin
#define LED_PIN 2   

WiFiClient espClient;
PubSubClient client(espClient);

// Callback when message arrives
void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived: ");

  String msg;
  for (int i = 0; i < length; i++) {
    msg += (char)message[i];
  }

  Serial.println(msg);

  if (msg == "ON") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED ON");
  } 
  else if (msg == "OFF") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED OFF");
  }
}

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
    if (client.connect("ESP32_LED_Client")) {
      Serial.println("Connected");
      client.subscribe(ledTopic);
      Serial.println("Subscribed to LED topic");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  setup_wifi();

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
