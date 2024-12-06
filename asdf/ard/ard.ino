#include <Servo.h>

Servo servo1;
Servo servo2;
int motorPin1 = 8;
int motorPin2 = 7;

void setup() {
  Serial.begin(9600);
  servo1.attach(motorPin1);
  servo2.attach(motorPin2);
}

void loop() {
  for (int i = 0; i <= 170; i++) {
    servo1.write(i);
    Serial.println(i);
    servo2.write(i);
    Serial.println(i);
    delay(10);
  }
  delay(1000);
}