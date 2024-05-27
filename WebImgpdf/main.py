"""
@File : main.py
@Author : mr
@Description :
1.根据URL下载到images文件夹下边
2.下载成功会显示
@Time : 2024
"""
import os
import requests

# 图片存储目录
image_dir = './images'

# 创建目录（如果不存在）
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# 图片范围
start_number = 1
end_number = 26

# 图片基本URL
base_url = 'https://study.liuzehe.top/ADMIN/DAY01/COURSE/LINUXNSD_V01ADMINDAY01_'


# 下载图片函数
def download_image(image_number):
    image_url = f"{base_url}{str(image_number).zfill(3)}.png"
    image_path = os.path.join(image_dir, f"LINUXNSD_V01ADMINDAY01_{str(image_number).zfill(3)}.png")

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(image_path, 'wb') as image_file:
            for chunk in response.iter_content(chunk_size=8192):
                image_file.write(chunk)

        print(f"Downloaded {image_path}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")


# 下载指定范围内的图片
for image_number in range(start_number, end_number + 1):
    # 实时下载显示
    download_image(image_number)
