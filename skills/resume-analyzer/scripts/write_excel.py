#!/usr/bin/env python3
"""
简历分析结果Excel写入工具
用途: 将简历分析和评分结果写入格式化的Excel文件。

依赖: pip install openpyxl

用法:
    # 从stdin读取JSON数据并写入Excel
    echo '{"data": [...]}' | python write_excel.py /path/to/output.xlsx

    # 从JSON文件读取数据并写入Excel
    python write_excel.py /path/to/output.xlsx --input /path/to/results.json

    # 指定目标岗位名称（显示在表头）
    python write_excel.py /path/to/output.xlsx --input results.json --position "前端开发"

输入JSON格式:
{
    "position": "岗位名称",
    "candidates": [
        {
            "name": "姓名",
            "file_name": "源文件名",
            "basic_info": {
                "gender": "性别",
                "age": "年龄",
                "education": "学历",
                "school": "毕业院校",
                "major": "专业",
                "work_years": "工作年限",
                "phone": "联系电话",
                "email": "邮箱"
            },
            "scores": {
                "education_score": 0,
                "experience_score": 0,
                "skill_match_score": 0,
                "project_score": 0,
                "stability_score": 0,
                "potential_score": 0,
                "total_score": 0
            },
            "evaluation": "综合评价文本",
            "recommendation": "推荐/待定/不推荐"
        }
    ]
}
"""

import argparse
import json
import sys
from pathlib import Path


def write_results_to_excel(data: dict, output_path: str):
    """
    将简历分析结果写入Excel文件。

    Args:
        data: 包含岗位信息和候选人分析结果的字典
        output_path: 输出Excel文件的路径
    """
    try:
        from openpyxl import Workbook
        from openpyxl.styles import (
            Alignment,
            Border,
            Font,
            PatternFill,
            Side,
        )
        from openpyxl.utils import get_column_letter
    except ImportError:
        print("错误: 请先安装 openpyxl: pip install openpyxl", file=sys.stderr)
        sys.exit(1)

    wb = Workbook()
    ws = wb.active

    position = data.get("position", "未指定岗位")
    ws.title = f"{position}-简历分析报告"

    # ========== 样式定义 ==========
    # 标题样式
    title_font = Font(name="微软雅黑", size=16, bold=True, color="FFFFFF")
    title_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
    title_alignment = Alignment(horizontal="center", vertical="center")

    # 表头样式
    header_font = Font(name="微软雅黑", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # 评分表头（橙色）
    score_header_fill = PatternFill(start_color="ED7D31", end_color="ED7D31", fill_type="solid")

    # 数据样式
    data_font = Font(name="微软雅黑", size=10)
    data_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    eval_alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # 推荐状态颜色
    recommend_colors = {
        "推荐": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
        "待定": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"),
        "不推荐": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"),
    }
    recommend_fonts = {
        "推荐": Font(name="微软雅黑", size=10, bold=True, color="006100"),
        "待定": Font(name="微软雅黑", size=10, bold=True, color="9C5700"),
        "不推荐": Font(name="微软雅黑", size=10, bold=True, color="9C0006"),
    }

    # 边框
    thin_border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )

    # ========== 标题行 ==========
    # 定义列
    columns = [
        ("序号", 6),
        ("姓名", 10),
        ("性别", 6),
        ("年龄", 6),
        ("学历", 10),
        ("毕业院校", 16),
        ("专业", 14),
        ("工作年限", 10),
        ("联系电话", 14),
        ("邮箱", 24),
        ("学历评分\n(15分)", 10),
        ("经验评分\n(20分)", 10),
        ("技能匹配\n(25分)", 10),
        ("项目经验\n(20分)", 10),
        ("稳定性\n(10分)", 10),
        ("发展潜力\n(10分)", 10),
        ("总分\n(100分)", 10),
        ("综合评价", 50),
        ("推荐结果", 10),
        ("源文件", 20),
    ]

    # 合并标题行
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(columns))
    title_cell = ws.cell(row=1, column=1, value=f"📋 {position} - 简历分析评估报告")
    title_cell.font = title_font
    title_cell.fill = title_fill
    title_cell.alignment = title_alignment
    ws.row_dimensions[1].height = 40

    # ========== 表头行 ==========
    for col_idx, (header, width) in enumerate(columns, 1):
        cell = ws.cell(row=2, column=col_idx, value=header)
        cell.font = header_font
        cell.alignment = header_alignment
        cell.border = thin_border

        # 评分列使用橙色表头
        if col_idx >= 11 and col_idx <= 17:
            cell.fill = score_header_fill
        else:
            cell.fill = header_fill

        # 设置列宽
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    ws.row_dimensions[2].height = 35

    # ========== 数据行 ==========
    candidates = data.get("candidates", [])
    for row_idx, candidate in enumerate(candidates, 3):
        basic = candidate.get("basic_info", {})
        scores = candidate.get("scores", {})

        row_data = [
            row_idx - 2,  # 序号
            candidate.get("name", "未知"),
            basic.get("gender", "-"),
            basic.get("age", "-"),
            basic.get("education", "-"),
            basic.get("school", "-"),
            basic.get("major", "-"),
            basic.get("work_years", "-"),
            basic.get("phone", "-"),
            basic.get("email", "-"),
            scores.get("education_score", 0),
            scores.get("experience_score", 0),
            scores.get("skill_match_score", 0),
            scores.get("project_score", 0),
            scores.get("stability_score", 0),
            scores.get("potential_score", 0),
            scores.get("total_score", 0),
            candidate.get("evaluation", ""),
            candidate.get("recommendation", "待定"),
            candidate.get("file_name", ""),
        ]

        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = data_font
            cell.border = thin_border

            if col_idx == 18:  # 综合评价列左对齐
                cell.alignment = eval_alignment
            else:
                cell.alignment = data_alignment

            # 推荐结果列特殊样式
            if col_idx == 19:
                rec = str(value)
                if rec in recommend_colors:
                    cell.fill = recommend_colors[rec]
                    cell.font = recommend_fonts[rec]

            # 总分列加粗
            if col_idx == 17:
                cell.font = Font(name="微软雅黑", size=11, bold=True, color="C00000")

        ws.row_dimensions[row_idx].height = 60

    # ========== 汇总行 ==========
    if candidates:
        summary_row = len(candidates) + 3
        ws.merge_cells(
            start_row=summary_row, start_column=1,
            end_row=summary_row, end_column=10
        )
        summary_cell = ws.cell(
            row=summary_row, column=1,
            value=f"共 {len(candidates)} 位候选人 | "
                  f"推荐: {sum(1 for c in candidates if c.get('recommendation') == '推荐')} 人 | "
                  f"待定: {sum(1 for c in candidates if c.get('recommendation') == '待定')} 人 | "
                  f"不推荐: {sum(1 for c in candidates if c.get('recommendation') == '不推荐')} 人"
        )
        summary_cell.font = Font(name="微软雅黑", size=11, bold=True)
        summary_cell.alignment = Alignment(horizontal="left", vertical="center")

    # 保存文件
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    wb.save(output_path)
    print(f"✅ Excel文件已保存至: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="简历分析结果Excel写入工具"
    )
    parser.add_argument(
        "output_path",
        help="输出Excel文件路径（.xlsx）",
    )
    parser.add_argument(
        "--input",
        help="输入JSON文件路径（不指定则从stdin读取）",
    )
    parser.add_argument(
        "--position",
        help="岗位名称（会覆盖JSON中的position字段）",
    )

    args = parser.parse_args()

    # 读取输入数据
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    # 覆盖岗位名称
    if args.position:
        data["position"] = args.position

    write_results_to_excel(data, args.output_path)


if __name__ == "__main__":
    main()
