void setup() {
  Serial.begin(9600);   
  delay(1000);
  Serial.println("UART Communication Started");
}

void loop() {
  Serial.println("Hello from UART!");
  delay(2000);          
}
