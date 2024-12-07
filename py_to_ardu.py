import serial
import time
import random

arduino_port = 'COM3'  # 아두이노 연결 포트 확인
baud_rate = 9600  # 아두이노와 동일한 Baud Rate
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # 연결 안정화 대기

try:
    while True:
        # 1~5 사이의 랜덤 숫자 생성
        random_number = random.randint(1, 5)
        
        # 숫자를 아두이노로 전송
        arduino.write(f"{random_number}\n".encode())
        print(f"Sent to Arduino: {random_number}")
        
        # 아두이노로부터 응답 대기
        response = arduino.readline().decode().strip()
        if response:
            print(f"Arduino Response: {response}")
        
        time.sleep(1)  # 1초 대기
except KeyboardInterrupt:
    print("Program stopped by user.")
finally:
    arduino.close()
