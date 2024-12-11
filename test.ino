#include <Servo.h>

Servo servo_9;
Servo servo_10;

// 핀 번호와 전역 변수 선언
int motorPin_9 = 9;
int motorPin_10 = 10;
int inputnumber = 0;

void move_servo_p(Servo &servo, int start, int last);
void move_servo_m(Servo &servo, int start, int last);

void setup()
{
  Serial.begin(9600);
  servo_9.attach(9, 500, 2500);
  servo_10.attach(10, 500, 2500);
}

void loop() {
  inputnumber = (inputnumber + 1) % 3; // 0, 1, 2 반복
  delay(1000);

  switch (inputnumber) {
    case 0:
      Serial.println("0 case");
      servo_10.write(110);
      move_servo_p(servo_9, 90, 120);
      move_servo_p(servo_10, 160, 180);
      //servo_10.write(90);
      break;
    case 1:
      Serial.println("1 case");
      servo_10.write(110);
      move_servo_p(servo_9, 90, 120);
      move_servo_m(servo_10, 160, 180);
      //servo_10.write(90);
      break;
    case 2:
      Serial.println("2 case");
      servo_10.write(110);
      move_servo_p(servo_9, 90, 120);
      move_servo_m(servo_10, 160, 180);
      //servo_10.write(90);
      break;
    default:
      Serial.println("없는 내용");
      break;
  }
}
         
void move_servo_p(Servo &servo, int start, int last) {
  for (int pos = start; pos <= last; pos += 1) {
    servo.write(pos);
    delay(100); 
  }
  for (int pos = last; pos >= start; pos -= 1) {
    servo.write(pos);
    delay(100); 
  }
}

void move_servo_m(Servo &servo, int start, int last) {
  for (int pos = start; pos >= last; pos -= 1) { // 조건 수정
    servo.write(pos);
    delay(100);
  }
  for (int pos = last; pos <= start; pos += 1) { // 조건 수정
    servo.write(pos);
    delay(100);
  }
}