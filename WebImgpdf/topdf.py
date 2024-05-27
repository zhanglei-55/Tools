"""
@File : topdf.py
@Author : mr
@Description : 
"""
import os
import img2pdf

# 图片存储目录
image_dir = 'images'

# 输出PDF文件路径
pdf_path = 'output/images.pdf'

# 检查图片存储目录是否存在
if not os.path.exists(image_dir):
    print("图片存储目录不存在，请先下载图片。")
    exit()

# 获取图片文件列表
image_files = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith('.png')]

# 如果图片文件列表为空，则无法生成PDF
if not image_files:
    print("图片文件列表为空，无法生成PDF。")
    exit()

# 创建输出目录（如果不存在）
output_dir = os.path.dirname(pdf_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 将图片转换为PDF
with open(pdf_path, "wb") as pdf_file:
    pdf_file.write(img2pdf.convert(image_files))

print(f"所有图片已转换并保存为 {pdf_path}")
