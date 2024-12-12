import serial
import subprocess
import image_classify
import time

port = 'COM8'
baud_rate = 9600

try:
    # 시리얼 포트 초기화
    ser = serial.Serial(port, baudrate=baud_rate)
    print("시리얼 통신 시작. 버튼 상태를 기다립니다.")
    
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"버튼 상태: {data}")
            if data == "on":
                # 예시: 카메라 캡처 및 이미지 분류 호출
                predict_result = image_classify.imgage()
                predict_result = predict_result.encode('utf-8')
                print(predict_result)
                # 시리얼로 결과 전송
                ser.write(predict_result)
                time.sleep(2)

except serial.SerialException as e:
    print(f"시리얼 포트를 열 수 없습니다: {e}")
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")