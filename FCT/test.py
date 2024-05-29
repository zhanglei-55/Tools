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
        下一个版本添加 pdf转为ppt => 非简单化将图片放入

     当前存在的问题 ：
       1. 如果 选择路径为D:\PPTtest 目标路径为 D:\  这样转换不会开始 而且也没有pdf生成  幽灵时间
       2. 如果 选择路径为D:\PPTtest 目标路径为 D:\Work 或者桌面 等其他类似的 进度条一直跑 而pdf实际已经生成完毕了
"""
import os
import re
import img2pdf
from gooey import Gooey, GooeyParser


def extract_number(filename):
    """
    从文件名中提取数字。

    参数:
    filename: 字符串，包含一个或多个字符，期望其中包含至少一个数字。

    返回值:
    如果找到数字，则返回整型数字。如果没有找到数字，返回正无穷大（float('inf')）。
    """
    # 使用正则表达式在文件名中搜索第一个数字
    match = re.search(r'\d+', filename)

    # 如果找到数字，转换为整数并返回；否则，返回正无穷大
    return int(match.group()) if match else float('inf')


@Gooey(program_name="图片转换为PDF工具", default_size=(600, 400), language='chinese')
def main():
    """
    图片转换为PDF工具的主函数。

    使用Gooey装饰器将命令行界面转换为图形用户界面，用户可以通过图形界面选择图片文件夹，
    指定输出位置和文件名，然后将选择的图片转换为一个PDF文件。

    参数:
    - 无

    返回值:
    - 无
    """
    # 创建解析器并设置程序描述
    parser = GooeyParser(description="选择图片文件夹并转换为PDF")

    # 添加输入图片文件夹的参数
    parser.add_argument(
        'folder_path',
        metavar='图片文件夹',
        help='请选择包含图片的文件夹',
        widget='DirChooser',
    )

    # 添加输出文件夹的参数
    parser.add_argument(
        'output_folder',
        metavar='保存位置',
        help='请选择保存PDF文件的位置',
        widget='DirChooser'
    )

    # 添加输出文件名的参数，设置默认值为output.pdf
    parser.add_argument(
        'output_filename',
        metavar='输出文件名',
        help='请输入输出PDF文件的文件名',
        default='output.pdf'
    )

    # 解析命令行参数
    args = parser.parse_args()

    # 获取用户选择的文件夹路径和输出路径
    folder_path = args.folder_path
    output_folder = args.output_folder
    output_filename = args.output_filename

    # 收集文件夹中的所有图片文件并按文件名中的数字排序
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                   f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    image_files.sort(key=lambda x: extract_number(os.path.basename(x)))  # 按文件名中的数字排序

    # 如果没有找到图片文件，打印错误信息并退出
    if not image_files:
        print("没有找到图片文件！")
        return

    # 生成输出PDF文件的完整路径
    output_pdf_path = os.path.join(output_folder, output_filename)

    try:
        # 将图片转换为PDF并保存到指定路径 2进制写入
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_files))
        print(f"PDF文件已保存到: {output_pdf_path}")
    except Exception as e:
        print(f"转换过程中发生错误: {e}")


if __name__ == "__main__":
    main()
