import os
import random
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

def get_random_image_from_directory(directory):
    images = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('png', 'jpg', 'jpeg'))]
    return random.choice(images)

def process_image(a_directory, b_directory, output_directory, index):
    # 디렉토리에서 랜덤 이미지 선택
    image_a_path = get_random_image_from_directory(a_directory)
    image_b_path = get_random_image_from_directory(b_directory)
    
    # 이미지 불러오기
    image_a = Image.open(image_a_path).convert("RGBA")
    image_b = Image.open(image_b_path).convert("RGBA")
    
    # 이미지 B의 크기를 랜덤한 비율로 조정 (50% - 150%)
    scale_factor = random.uniform(0.5, 1.5)
    new_width = int(image_b.width * scale_factor)
    new_height = int(image_b.height * scale_factor)
    image_b = image_b.resize((new_width, new_height), Image.ANTIALIAS)
    
    # 이미지 B를 랜덤하게 회전
    angle = random.randint(0, 360)
    image_b = image_b.rotate(angle, expand=True)
    
    # A 이미지 크기
    a_width, a_height = image_a.size
    # B 이미지 크기 (크기 조정 및 회전 후)
    b_width, b_height = image_b.size
    
    # B 이미지를 랜덤한 위치에 배치
    random_x = random.randint(0, a_width - b_width)
    random_y = random.randint(0, a_height - b_height)
    
    # 투명 마스크 생성
    image_b_mask = image_b if image_b.mode == 'RGBA' else None
    
    # A 이미지에 B 이미지를 붙이기
    image_a.paste(image_b, (random_x, random_y), image_b_mask)
    
    # 결과 이미지를 저장
    output_path = os.path.join(output_directory, f'output_image_{index+1}.png')
    image_a.save(output_path, format="PNG")
    print(f"Result {index+1} saved to {output_path}")

def overlay_images_randomly(a_directory, b_directory, output_directory, num_images=100):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_image, a_directory, b_directory, output_directory, i) for i in range(num_images)]
        for future in futures:
            future.result()  # 결과를 기다리기 (옵션: 예외를 잡기 위해)

# 예제 사용
a_directory = r'C:\Users\WONJANGHO\Desktop\samples\yolo\base'
b_directory = r'C:\Users\WONJANGHO\Desktop\samples\yolo\template'
output_directory = r'C:\Users\WONJANGHO\Desktop\samples\yolo\results2'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

overlay_images_randomly(a_directory, b_directory, output_directory, num_images=100)