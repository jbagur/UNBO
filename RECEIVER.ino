
#include <VirtualWire.h>
byte message[VW_MAX_MESSAGE_LEN]; // INCOMING BUFFER
byte messageLength = VW_MAX_MESSAGE_LEN; // INCOMING MESSAGE SIZE

void setup() {
  Serial.begin(9600);
  Serial.println("Device is ready");
  
  // INITIALIZE IO AND ISR
  vw_setup(2000); // BIT PER SECOND
  vw_rx_start();  // -INITIALIZE RF RECEIVER
}

void loop() {
  if (vw_get_message(message, &messageLength)) {
    Serial.print("Received: ");
    for (int i = 0; i < messageLength; i++) {
      Serial.write(message[i]);
    }
    Serial.println();
  }
}
