def takeit():

    import serial
    import numpy as np
    from PIL import Image
    import os  # 파일 처리 관련 모듈

    # 시리얼 포트 설정 (포트는 실제 사용 중인 포트로 변경)
    ser = serial.Serial('COM5', baudrate=1000000)  # COM8 포트, 1M baud rate

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

    # 파일 경로 설정
    file_path = "./received_image.png"

    # 파일이 이미 존재하면 삭제
    if os.path.exists(file_path):
        os.remove(file_path)

    # 이미지 파일로 저장 (예: "received_image.png"로 저장)
    image = Image.fromarray(image_data)
    image.save(file_path)

    # 이미지 출력 (선택사항)
    image.show()

    # 시리얼 포트 닫기
    ser.close()
