#include <Wire.h>

#define SLAVE_ADDR 0x08

void setup() {
  Wire.begin(SLAVE_ADDR);       // Start as I2C Slave with address 0x08
  Wire.onRequest(requestEvent); // Register callback for data request
}

void loop() {
  // Can perform other tasks here
}

void requestEvent() {
  int dataToSend = 123;         // Example data
  Wire.write(dataToSend);       // Send single byte of data to Pi
}
