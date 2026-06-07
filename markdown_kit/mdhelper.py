#!/usr/bin/env python3
"""
markdown-kit - Markdown 文档辅助工具
功能：CSV转Markdown表格、表格格式化、目录生成、批量替换
用法：markdown-kit csv2table [csv文件] [输出文件(可选)]
      markdown-kit toc [markdown文件]
      markdown-kit table-align [markdown文件]
"""
import sys
import csv
import re
from pathlib import Path
from io import StringIO


def csv_to_table(csv_file, output_file=None, header=True):
    """将CSV文件转换为Markdown表格"""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        print(f"错误：读取CSV文件失败: {e}")
        return False

    if not rows:
        print("错误：CSV文件为空")
        return False

    # 构建Markdown表格
    md_lines = []

    for i, row in enumerate(rows):
        # 转义管道符
        row = [col.replace('|', '\\|') for col in row]

        md_lines.append("| " + " | ".join(row) + " |")

        if header and i == 0:
            # 表头分隔行
            separator = "| " + " | ".join(["---"] * len(row)) + " |"
            md_lines.append(separator)

    result = "\n".join(md_lines) + "\n"

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Markdown 表格已保存到: {output_file}")
        print(f"共 {len(rows)} 行 x {len(rows[0])} 列")
    else:
        print(result)

    return True


def _extract_tables(text):
    """从Markdown文本中提取表格"""
    tables = []
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('|') and line.strip().endswith('|'):
            table_start = i
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i])
                i += 1
            if len(table_lines) >= 2:  # 至少表头+分隔行
                tables.append((table_start, table_lines))
        else:
            i += 1
    return tables, lines


def align_tables(md_file, output_file=None):
    """对齐Markdown表格为等宽格式"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"错误：读取文件失败: {e}")
        return False

    tables, lines = _extract_tables(text)

    if not tables:
        print("未找到Markdown表格")
        return False

    print(f"找到 {len(tables)} 个表格")

    for start_idx, table_lines in tables:
        # 解析列数
        cols_counts = [len(re.findall(r'\|', l)) - 1 for l in table_lines]
        num_cols = max(cols_counts) if cols_counts else 0
        if num_cols < 2:
            continue

        # 计算每列最大宽度
        col_widths = [0] * num_cols
        parsed_table = []
        for line in table_lines:
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            # 补齐列数
            while len(cells) < num_cols:
                cells.append('')
            parsed_table.append(cells)
            for i, cell in enumerate(cells):
                col_widths[i] = max(col_widths[i], len(cell))

        # 重建对齐后的表格
        aligned = []
        for row_idx, cells in enumerate(parsed_table):
            aligned_row = "|"
            for i, cell in enumerate(cells):
                w = max(col_widths[i], 3)
                if row_idx == 1:  # 分隔行
                    aligned_row += " " + "-" * w + " |"
                else:
                    aligned_row += " " + cell.ljust(w) + " |"
            aligned.append(aligned_row)

        # 替换原行
        for j, line in enumerate(aligned):
            lines[start_idx + j] = line

    result = '\n'.join(lines)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"已保存到: {output_file}")
    else:
        print(result)

    return True


def generate_toc(md_file, output_file=None):
    """生成Markdown文件的目录（TOC）"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"错误：读取文件失败: {e}")
        return False

    toc_lines = ["# 目录\n", "\n"]
    found_headers = False

    for line in lines:
        match = re.match(r'^(#{2,4})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            indent = "  " * (level - 2)
            anchor = title.lower()
            anchor = re.sub(r'[^\w\u4e00-\u9fff ]', '', anchor)
            anchor = anchor.replace(' ', '-')
            toc_lines.append(f"{indent}- [{title}](#{anchor})\n")
            found_headers = True

    if not found_headers:
        print("未找到二级及以上标题（##, ###, ####）")
        return False

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(toc_lines)
        print(f"目录已保存到: {output_file}")
    else:
        print(''.join(toc_lines))

    print(f"共生成 {len(toc_lines) - 2} 条目")
    return True


def _show_promotion():
    print("\n" + "=" * 55)
    print("  🔧 markdown-kit - Markdown 文档辅助工具")
    print("  📦 pip install markdown-kit")
    print("  ☕ 如果帮到了您，欢迎打赏支持:")
    print("     USDT(TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa")
    print("  ⭐ https://github.com/BoiledSaltedDuck/markdown-kit")
    print("=" * 55)


def main():
    if len(sys.argv) < 3:
        print("用法:")
        print("  CSV转表格:   markdown-kit csv2table [csv文件] [输出文件(可选)]")
        print("  目录生成:    markdown-kit toc [markdown文件] [输出文件(可选)]")
        print("  表格对齐:    markdown-kit table-align [markdown文件] [输出文件(可选)]")
        print()
        print("示例:")
        print("  markdown-kit csv2table data.csv table.md")
        print("  markdown-kit toc README.md TOC.md")
        print("  markdown-kit table-align doc.md")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "csv2table":
        if len(sys.argv) < 3:
            print("用法: markdown-kit csv2table [csv文件] [输出文件(可选)]")
            sys.exit(1)
        output = sys.argv[3] if len(sys.argv) > 3 else None
        success = csv_to_table(sys.argv[2], output)

    elif command == "toc":
        if len(sys.argv) < 3:
            print("用法: markdown-kit toc [markdown文件] [输出文件(可选)]")
            sys.exit(1)
        output = sys.argv[3] if len(sys.argv) > 3 else None
        success = generate_toc(sys.argv[2], output)

    elif command == "table-align":
        if len(sys.argv) < 3:
            print("用法: markdown-kit table-align [markdown文件] [输出文件(可选)]")
            sys.exit(1)
        output = sys.argv[3] if len(sys.argv) > 3 else None
        success = align_tables(sys.argv[2], output)

    else:
        print(f"错误：不支持的命令 '{command}'")
        sys.exit(1)

    if success:
        _show_promotion()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
