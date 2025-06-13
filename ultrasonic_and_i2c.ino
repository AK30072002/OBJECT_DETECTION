#include <Wire.h>
#define SLAVE_ADDR 0x08
#define TRIG_PIN 9
#define ECHO_PIN 10

volatile int latestDistance = 0;  // Use volatile for ISR safety

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Wire.begin(SLAVE_ADDR);
  Wire.onRequest(requestEvent);
}

void loop() {
  long duration;
  float distance;

  // Trigger ultrasonic sensor
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read echo time
  duration = pulseIn(ECHO_PIN, HIGH, 25000);  // timeout in 25ms
  distance = duration * 0.0343 / 2;

  latestDistance = (int)round(distance);

  Serial.print("Distance: ");
  Serial.print(latestDistance);
  Serial.println(" cm");

  delay(100);  // Small delay to avoid too frequent readings
}

void requestEvent() {
  Wire.write((uint8_t*)&latestDistance, sizeof(latestDistance));
}
