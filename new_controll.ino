#include <Servo.h>

Servo servo1;  // 서보모터 1
Servo servo2;  // 서보모터 2

void setup() {
  // 서보모터 핀 초기화
  servo1.attach(10);  // 9번 핀에 서보모터 1 연결
  servo2.attach(11); // 10번 핀에 서보모터 2 연결
}

void loop() {
  // 9번 핀 서보모터 0도에서 180도로 이동
  
  servo1.write(0);   // 9번 핀 서보모터를 0도로 이동
  servo2.write(180); // 10번 핀 서보모터를 180도로 이동
  delay(3500);        // 1초 대기

  // 9번 핀 서보모터 180도에서 0도로 이동
  servo1.write(180); // 9번 핀 서보모터를 180도로 이동
  servo2.write(0);   // 10번 핀 서보모터를 0도로 이동
  delay(1000);        // 1초 대기
}
