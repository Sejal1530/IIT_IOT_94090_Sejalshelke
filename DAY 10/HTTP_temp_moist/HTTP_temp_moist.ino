#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Realme 12";
const char* password = "vobt0457";

const char* serverURL = "http://192.168.1.100:5000/update";  // Change IP & port

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    float temperature = 28.5;
    float humidity = 65.2;

    // JSON payload
    String postData = "{";
    postData += "\"temperature\":" + String(temperature) + ",";
    postData += "\"humidity\":" + String(humidity);
    postData += "}";

    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");

    int httpResponseCode = http.POST(postData);

    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Server response:");
      Serial.println(response);
    } else {
      Serial.println("Error sending POST request");
    }

    http.end();
  }

  delay(5000); 
}
