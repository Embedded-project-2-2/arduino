import serial
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')        

# 시리얼 포트 설정 (포트는 실제 사용 중인 포트로 변경)
ser = serial.Serial('COM3', baudrate=1000000)  # COM3 포트, 1M baud rate

# 이미지 크기 설정 (예: 320x240)
width, height = 320, 240

# 이미지 데이터를 저장할 배열
image_data = np.zeros((height, width), dtype=np.uint8)

# 이미지를 시리얼로 받기
for y in range(height):
    for x in range(width):
        # 시리얼로부터 1 byte 받기
        pixel = ser.read(1)
        # 받은 값은 bytes로 오므로, 정수형으로 변환
        image_data[y, x] = ord(pixel)

# 이미지 출력
plt.imshow(image_data, cmap='gray')
plt.show()

ser.close()
