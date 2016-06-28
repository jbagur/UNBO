#include <stdlib.h>
#include <VirtualWire.h>

const int ledPin = 13;
const int buttonPin1 = 7;
const int buttonPin2 = 8;

int buttonState1 = 0;
int buttonState2 = 0;

void setup() {
  vw_setup(2000);
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
}

void loop() {
  
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  
  if (buttonState1 == LOW) {
    sendData("id=001$status=1");
    digitalWrite(ledPin, HIGH);    
  } else if (buttonState2 == LOW) {
    sendData("id=001$status=0");
    digitalWrite(ledPin, LOW);
  }   
}

void sendData(char *message) {
  vw_send((uint8_t *)message, strlen(message));
  vw_wait_tx();
  Serial.println(message);
}
