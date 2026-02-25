#!/usr/bin/env python3
"""
简历PDF读取工具
用途: 读取单个PDF文件或文件夹中所有PDF文件，提取文本内容。

依赖: pip install pdfplumber

用法:
    # 读取单个PDF文件
    python read_pdf.py /path/to/resume.pdf

    # 读取文件夹中所有PDF文件
    python read_pdf.py /path/to/resumes_folder/

    # 指定输出编码（默认utf-8）
    python read_pdf.py /path/to/resume.pdf --encoding utf-8

输出: JSON格式，包含每个文件的路径、文件名和提取的文本内容。
"""

import argparse
import json
import os
import sys
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> dict:
    """
    从单个PDF文件中提取文本内容。

    Args:
        pdf_path: PDF文件的绝对路径

    Returns:
        dict: 包含文件信息和提取文本的字典
            - file_path: 文件完整路径
            - file_name: 文件名（不含扩展名）
            - text: 提取的全文文本
            - pages: 每页的文本列表
            - page_count: 总页数
            - success: 是否成功
            - error: 错误信息（如果失败）
    """
    try:
        import pdfplumber
    except ImportError:
        print("错误: 请先安装 pdfplumber: pip install pdfplumber", file=sys.stderr)
        sys.exit(1)

    result = {
        "file_path": str(pdf_path),
        "file_name": Path(pdf_path).stem,
        "text": "",
        "pages": [],
        "page_count": 0,
        "success": False,
        "error": None,
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            result["page_count"] = len(pdf.pages)
            all_text = []
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                result["pages"].append(page_text)
                all_text.append(page_text)
            result["text"] = "\n".join(all_text)
            result["success"] = True
    except Exception as e:
        result["error"] = str(e)

    return result


def read_pdfs(input_path: str) -> list[dict]:
    """
    读取指定路径的PDF文件。支持单个文件或文件夹。

    Args:
        input_path: PDF文件路径或包含PDF文件的文件夹路径

    Returns:
        list[dict]: 所有PDF文件的提取结果列表
    """
    path = Path(input_path)
    results = []

    if path.is_file():
        if path.suffix.lower() == ".pdf":
            results.append(extract_text_from_pdf(str(path)))
        else:
            print(f"警告: {path} 不是PDF文件，已跳过", file=sys.stderr)
    elif path.is_dir():
        pdf_files = sorted(path.glob("*.pdf"))
        if not pdf_files:
            print(f"警告: 文件夹 {path} 中没有找到PDF文件", file=sys.stderr)
        for pdf_file in pdf_files:
            print(f"正在读取: {pdf_file.name}", file=sys.stderr)
            results.append(extract_text_from_pdf(str(pdf_file)))
    else:
        print(f"错误: 路径 {input_path} 不存在", file=sys.stderr)
        sys.exit(1)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="简历PDF读取工具 - 提取PDF文件中的文本内容"
    )
    parser.add_argument(
        "input_path",
        help="PDF文件路径或包含PDF文件的文件夹路径",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="输出编码格式（默认: utf-8）",
    )

    args = parser.parse_args()
    results = read_pdfs(args.input_path)

    # 输出JSON结果
    output = json.dumps(results, ensure_ascii=False, indent=2)
    print(output)

    # 汇总信息输出到stderr
    success_count = sum(1 for r in results if r["success"])
    fail_count = sum(1 for r in results if not r["success"])
    print(f"\n读取完成: 成功 {success_count} 个, 失败 {fail_count} 个", file=sys.stderr)


if __name__ == "__main__":
    main()
