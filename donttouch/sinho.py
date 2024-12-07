import serial

port = 'COM3'
baud_rate = 9600

try:
    with serial.Serial(port, baud_rate, timeout=1) as ser:
        print("시리얼 통신 시작. 버튼 상태를 기다립니다.")
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                print(f"버튼 상태: {data}")

except serial.SerialException as e:
    print(f"시리얼 포트를 열 수 없습니다: {e}")
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")