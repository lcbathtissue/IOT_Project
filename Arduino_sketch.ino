#include <SoftwareSerial.h>

#define DHTPIN A0

SoftwareSerial btSerial(4, 5); // TX, RX

void setup() {
  btSerial.begin(9600);
  Serial.begin(9600);
  btSerial.flush();
  Serial.flush();
}

void loop() {
  int sensorValue = analogRead(A0); 
  btSerial.println(sensorValue);
  delay(1000); // Send data every 10 seconds
}
