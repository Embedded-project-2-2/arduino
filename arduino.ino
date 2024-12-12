#include <Servo.h>


Servo servo_9;
Servo servo_10;

// 핀 번호와 전역 변수 선언
int motorPin_9 = 9;
int motorPin_10 = 10;
int inputnumber = 0;

void move_servo_p(Servo &servo, int start, int last);
void move_servo_m(Servo &servo, int start, int last);

const int buttonPin = 2;  // 버튼이 연결된 핀
int buttonState = 0;       // 버튼 상태 변수

void setup() {
  // 시리얼 통신 시작
  Serial.begin(9600);
  servo_9.attach(9, 500, 2500);
  servo_10.attach(10, 500, 2500);
  
  // 버튼 핀을 입력으로 설정
  pinMode(buttonPin, INPUT);
}

void loop() {
  // 버튼의 상태를 읽음
  buttonState = digitalRead(buttonPin);
  
  // 버튼이 눌렸다면
  if (buttonState == HIGH) {
    // "on"을 시리얼로 전송
    Serial.println("on");
    
    // 버튼이 떼어졌을 때까지 기다리기 (디바운싱)
    while (digitalRead(buttonPin) == HIGH) {
      delay(10);
    }
  }

  // 잠시 대기
  delay(100);
  if (Serial.available())
  {
    int cmd = Serial.parseInt();
    if(cmd == 2) {
      move_servo_p(servo_9, 90, 125);
      move_servo_p(servo_10, 90, 150);
    } else if (cmd == 3) {
      move_servo_p(servo_9, 90, 125);
      move_servo_m(servo_10, 90, 30);
    } else if (cmd == 1) {
      move_servo_m(servo_9, 90, 60);
    }
  }
  
}

void move_servo_p(Servo &servo, int start, int last) {
  for (int pos = start; pos <= last; pos += 1) {
    servo.write(pos);
    if (pos == last) {
      delay(1000);
    }
    delay(10); 
  }
  for (int pos = last; pos >= start; pos -= 1) {
    servo.write(pos);
    if (pos == last) {
      delay(1000);
    }
    delay(10); 
  }
}

void move_servo_m(Servo &servo, int start, int last) {
  for (int pos = start; pos >= last; pos -= 1) { // 조건 수정
    servo.write(pos);
    if (pos == last) {
      delay(1000);
    }
    delay(10);
  }
  for (int pos = last; pos <= start; pos += 1) { // 조건 수정
    servo.write(pos);
    if (pos == last) {
      delay(1000);
    }
    delay(10);
  }
}
