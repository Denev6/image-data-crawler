import os
from pathlib import Path

from PIL import Image

CWD = os.getcwd()
IMG_DIR = os.path.join(CWD, "result", "converted")  # 이미지 경로 변경하여 사용
SAVE_DIR = os.path.join(CWD, "result", "resized")  # 저장 경로 변경하여 사용
os.makedirs(SAVE_DIR, exist_ok=True)

IMG_SIZE = (100, 100)  # 이미지 크기 변경하여 사용


def specify_img_path(file_name):
    return os.path.join(IMG_DIR, file_name)


def specify_save_path(file_name):
    return os.path.join(SAVE_DIR, f"{Path(file_name).stem}.png")


imgs = os.listdir(IMG_DIR)
imgs = list(map(specify_img_path, imgs))

for img in imgs:
    with Image.open(img) as img_:
        resized = img_.resize(IMG_SIZE)
        resized.save(specify_save_path(img))
