#include <WiFi.h>

// Wi-Fi credentials
const char* ssid = "Realme 12";
const char* password = "vobt0457";

void setup() {
  Serial.begin(115200);
  delay(2000);   

  Serial.println();
  Serial.println("Starting ESP32...");
  
  // Set Wi-Fi mode explicitly
  WiFi.mode(WIFI_STA);
  WiFi.disconnect(true);
  delay(1000);

  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);

  int retryCount = 0;

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    retryCount++;

    if (retryCount > 20) {   
      Serial.println("\nFailed to connect to Wi-Fi");
      return;
    }
  }

  Serial.println("\nWi-Fi connected successfully!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {

}
