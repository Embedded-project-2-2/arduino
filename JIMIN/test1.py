import qwer
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import clip
import torch
import joblib
from sympy.physics.units import current
from torchvision import transforms
from PIL import Image
import time
import os

# 시리얼 포트 설정 (포트는 실제 사용 중인 포트로 변경)
ser = serial.Serial('COM8', baudrate=115200)  # COM8 포트, 115200 baud rate

# 이미지 크기 설정 (예: 320x240)
width, height = 320, 240

# 이미지 데이터를 저장할 배열
image_data = np.zeros((height, width), dtype=np.uint8)

# 이미지 데이터를 시리얼로 받기
for y in range(height):
    for x in range(width):
        # 시리얼로부터 1 byte 받기
        if ser.in_waiting > 0:  # 데이터가 있을 때만 읽기
            pixel = ser.read(1)
            image_data[y, x] = ord(pixel)

# 이미지 출력
plt.imshow(image_data, cmap='gray')
plt.show()

# 현재 작업 디렉토리 확인 후 저장
current_path = os.getcwd()
os.chdir(current_path)
plt.savefig('image.png')

# 시리얼 포트 닫기
ser.close()



#변경하는 법

# os.chdir(current_path)
# plt.savefig('image.png')

# 1. CLIP 모델 및 전처리 불러오기
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)


# 2. Logistic Regression 모델 불러오기
classifier = joblib.load('model.pkl')

#ToDo 여기서 부터 while 추가
# 3. 단일 이미지 불러오기
image_path = "C:/Users/hongj/PycharmProjects/arduino/image.png"
image = Image.open(image_path)

# 알파 채널을 제거하고 RGB로 변환
image = image.convert("RGB")  # RGBA를 RGB로 변환

# 4. 이미지 전처리
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),  # CLIP 모델에 맞게 크기 조정
    transforms.ToTensor(),  # 텐서로 변환
    transforms.Normalize((0.48145466, 0.4578275, 0.40821073),
                         (0.26862954, 0.26130258, 0.27577711))  # 정규화
])

# 이미지 텐서로 변환 후 GPU/CPU로 전송
image_tensor = preprocess(image).unsqueeze(0).to(device)  # 이미지에 배치 차원 추가 후 GPU/CPU로 전송

# 5. CLIP 모델을 사용해 이미지 특징 추출
with torch.no_grad():
    image_features = model.encode_image(image_tensor).cpu().numpy()

# 6. Logistic Regression 모델을 사용하여 예측
prediction = classifier.predict(image_features)

# 7. 분류 결과 출력
categories = ["binil", "cans", "glass", "other_ps", "p_bowls", "pets"]
predicted_category = categories[prediction[0]]  # 예측된 레이블로 카테고리 이름 가져오기
print(f"해당 이미지는 '{predicted_category}' 카테고리로 분류되었습니다.")


py_serial = serial.Serial(
    port="COM8",

    baudrate=115200,
)

file_path = "C:/Users/hongj/PycharmProjects/arduino/image.png"

if os.path.exists(file_path):
    os.remove(file_path)


command = predicted_category

if command == "binil":
    command = "1"
elif command == "cans":
    command = "2"
elif command == "glass":
    command = "3"


py_serial.write(command.encode())
print("보냈습니다")
print(command)
time.sleep(1)

if py_serial.readable():
    response = py_serial.readline()
    print(response[:len(response) - 1].decode())

