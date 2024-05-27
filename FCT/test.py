#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File    : test.py
@Author  : zhanglei-55
@Contact : jxz911911@qq.com
@Time    : 2024/5/26 21:52
@Desc    : 
    描述: This is a Format conversion tool
         这是一个UI界面的格式转换工具
    
    用法: 用户根据需求 进行相应的UI操作
    
    示例:
    示例1:
        描述: 描述第一个示例
        命令: python test.py --example1
        
    示例2:
        描述: 描述第二个示例
        命令: python test.py --example2

    注意: 在这里你可以列出使用这个脚本时需要注意的事项，比如特殊依赖、环境配置等。
    
    版本历史:
        test v1.0: 初始版本  实现了将图片文件夹转为PDF
        test v1.1: 修改默认语言为中文
        v1.2: 修复了一些错误

    作者备注: 
        使用 gooey 进行开发
"""
import os
import re
import img2pdf
from gooey import Gooey, GooeyParser


def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')


@Gooey(program_name="图片转换为PDF工具", default_size=(600, 400),
       language='chinese'
       )
def main():
    parser = GooeyParser(description="选择图片文件夹并转换为PDF")

    parser.add_argument(
        'folder_path',
        metavar='图片文件夹',
        help='请选择包含图片的文件夹',
        widget='DirChooser',
    )

    parser.add_argument(
        'output_folder',
        metavar='保存位置',
        help='请选择保存PDF文件的位置',
        widget='DirChooser'
    )

    parser.add_argument(
        'output_filename',
        metavar='输出文件名',
        help='请输入输出PDF文件的文件名',
        default='output.pdf'
    )

    args = parser.parse_args()

    folder_path = args.folder_path
    output_folder = args.output_folder
    output_filename = args.output_filename

    # 获取文件夹中的所有图片文件并排序
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                   f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    image_files.sort(key=lambda x: extract_number(os.path.basename(x)))  # 按文件名中的数字排序

    if not image_files:
        print("没有找到图片文件！")
        return

    # 生成PDF文件路径
    output_pdf_path = os.path.join(output_folder, output_filename)

    try:
        # 将图片转换为PDF并保存
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_files))
        print(f"PDF文件已保存到: {output_pdf_path}")
    except Exception as e:
        print(f"转换过程中发生错误: {e}")


if __name__ == "__main__":
    main()
