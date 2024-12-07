import serial
import numpy as np
import matplotlib.pyplot as plt
import clip
import torch
import joblib
from torchvision import transforms
from PIL import Image
import time

# 시리얼 포트 설정 (포트는 실제 사용 중인 포트로 변경)
ser = serial.Serial('COM8', baudrate=115200, timeout=1)  # 타임아웃 추가

# 이미지 크기 설정 (예: 320x240)
width, height = 320, 240

# 이미지 데이터를 저장할 배열
image_data = np.zeros((height, width), dtype=np.uint8)

# 이미지 데이터를 시리얼로 받기
for y in range(height):
    for x in range(width):
        if ser.in_waiting > 0:  # 데이터가 있을 때만 읽기
            pixel = ser.read(1)
            image_data[y, x] = ord(pixel)

# 이미지 출력
plt.imshow(image_data, cmap='gray')
plt.show()

# 이미지 저장
image_path = 'image.png'
plt.savefig(image_path)

# CLIP 모델 및 전처리 불러오기
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)

# Logistic Regression 모델 불러오기
classifier = joblib.load('model.pkl')

# 이미지 전처리 및 CLIP 모델 특징 추출
image = Image.open(image_path)
image = image.convert("RGB")  # 알파 채널 제거 후 RGB로 변환

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),  # CLIP 모델에 맞게 크기 조정
    transforms.ToTensor(),
    transforms.Normalize((0.48145466, 0.4578275, 0.40821073),
                         (0.26862954, 0.26130258, 0.27577711))  # 정규화
])

image_tensor = preprocess(image).unsqueeze(0).to(device)

with torch.no_grad():
    image_features = model.encode_image(image_tensor).cpu().numpy()

# 예측
prediction = classifier.predict(image_features)
categories = ["binil", "cans", "glass", "other_ps", "p_bowls", "pets"]
predicted_category = categories[prediction[0]]  # 예측된 레이블로 카테고리 이름 가져오기
print(f"해당 이미지는 '{predicted_category}' 카테고리로 분류되었습니다.")

# 시리얼 포트로 결과 전송
command = categories.index(predicted_category)  # 카테고리 인덱스를 전송
ser.write(bytes([command]))  # 명령어를 바이트로 전송
print(f"보낸 명령어: {command}")

# 응답 받기
time.sleep(1)
if ser.in_waiting > 0:  # 데이터가 있을 때만 읽기
    response = ser.readline()
    print("응답:", response.decode().strip())

# 시리얼 포트 닫기
ser.close()
