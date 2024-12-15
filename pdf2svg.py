#!/bin/python
import fitz  # PyMuPDF
import os
import argparse

def pdf_to_svg(pdf_path, output_dir):
    # 打开PDF文件
    doc = fitz.open(pdf_path)

    # 创建输出目录，如果不存在的话
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历每一页并导出为SVG
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # 加载页码为page_num的页面
        svg_file_path = os.path.join(output_dir, f"page_{page_num + 1}.svg")  # 生成SVG文件路径
        # 将pdf导出的svg分辨率放大，插入word时就能自动占满页面
        scale = 3
        svg_data = page.get_svg_image(matrix=fitz.Matrix(scale, scale))  # 获取该页的SVG数据

        # 保存为SVG文件
        with open(svg_file_path, "w", encoding="utf-8") as svg_file:
            svg_file.write(svg_data)
        
        print(f"Page {page_num + 1} exported as SVG.")

    print("PDF to SVG conversion completed.")

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Convert each page of a PDF to a separate SVG file.")
    parser.add_argument("pdf_path", help="The path to the input PDF file")
    parser.add_argument(
        "output_dir", 
        nargs="?",  # 该参数是可选的
        help="The directory to save the output SVG files. If not provided, a folder with the same name as the PDF will be created."
    )

    # 解析命令行参数
    args = parser.parse_args()

    # 如果没有指定输出目录，则根据PDF文件路径自动生成输出目录
    if not args.output_dir:
        pdf_directory = os.path.dirname(args.pdf_path)  # 获取PDF文件所在的目录
        pdf_filename = os.path.splitext(os.path.basename(args.pdf_path))[0]  # 获取PDF文件名（去除扩展名）
        args.output_dir = os.path.join(pdf_directory, pdf_filename)  # 使用同名文件夹作为输出目录

    # 调用pdf_to_svg函数进行转换
    pdf_to_svg(args.pdf_path, args.output_dir)

if __name__ == "__main__":
    main()
