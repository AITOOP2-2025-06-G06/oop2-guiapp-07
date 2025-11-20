import os
import subprocess

def open_image_directory():
    # 画像が保存されているディレクトリのパス
    image_dir = "./output_images"
    
    # ディレクトリを開く
    if os.path.exists(image_dir):
        subprocess.run(["open", image_dir])
    else:
        print("ディレクトリが存在しません")