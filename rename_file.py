import os

def rename_files(directory, new_name_format):
    # 디렉토리가 존재하는지 확인
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return

    # 디렉토리 내의 모든 파일 가져오기
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    # 파일 이름 변경
    for i, filename in enumerate(files, start=1):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{new_name_format}_{i}{file_extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed {filename} to {new_name}")
# 사용 예시
directory_path = r'C:\Users\WONJANGHO\Desktop\samples\yolo\id'
new_name_format = "id"
rename_files(directory_path, new_name_format)
