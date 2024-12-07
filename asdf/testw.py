import serial
import time
import take_a_photo

# 아두이노와 연결된 포트 설정 (예: 'COM5', '/dev/ttyUSB0' 등)
ser = serial.Serial('COM3', 9600)  # 아두이노가 연결된 포트로 바꿔주세요

while True:
    if ser.in_waiting > 0:  # 시리얼 데이터가 있을 때
        try:
            # 바이트 데이터를 UTF-8로 디코딩하고 오류가 발생하면 무시
            data = ser.readline().decode('utf-8', errors='ignore').strip()  # 오류 무시
            
            if data == "1":  # 버튼이 눌렸을 때
                print("버튼이 눌렸습니다. 출력: 1")
            elif data == "0":  # 버튼을 떼었을 때
                print("버튼이 눌리지 않았습니다. 출력: 0")
        except UnicodeDecodeError:
            print("디코딩 오류가 발생했습니다. 데이터가 손상되었을 수 있습니다.")
    
    time.sleep(0.3)  # 0.3초 대기
