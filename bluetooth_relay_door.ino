#include <SoftwareSerial.h>
SoftwareSerial BT(10, 11); 
// creates a "virtual" serial port/UART
// connect BT module TX to D10
// connect BT module RX to D11
// connect BT Vcc to 5V, GND to GND

int relay_pin = 6;
char command = '2';

void setup() {
  Serial.begin(9600);
  // set digital pin to control as an output
  pinMode(13, OUTPUT);
  // set the data rate for the SoftwareSerial port
  BT.begin(9600);
  // Send test message to other device
  BT.println("Hello from Arduino");

  pinMode(relay_pin, OUTPUT);

  digitalWrite(relay_pin, HIGH);

  Serial.println("hello");
}

void loop() {
  if (BT.available())
  // if text arrived in from BT serial...
  {
    command = (BT.read());
    if (command == '1')
    {
      BT.println("ON");
      Serial.println("1");
      digitalWrite(relay_pin, LOW);
      delay(500);      
      digitalWrite(relay_pin, HIGH);
    }
    // you can add more "if" statements with other characters to add more commands
  }
}
