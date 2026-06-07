# markdown-kit Markdown 文档辅助工具

[![PyPI version](https://img.shields.io/pypi/v/markdown-kit)](https://pypi.org/project/markdown-kit/)
[![Downloads](https://img.shields.io/pypi/dm/markdown-kit)](https://pypi.org/project/markdown-kit/)
[![License](https://img.shields.io/pypi/l/markdown-kit)](https://github.com/BoiledSaltedDuck/markdown-kit/blob/main/LICENSE)

> **Office Tools Kit 系列** — 用AI写代码，用工具提效。一行命令搞定日常办公与开发杂务。

## 安装

```bash
pip install markdown-kit
```

## 用法

```bash
# CSV 转 Markdown 表格
markdown-kit csv2table data.csv table.md

# 生成 Markdown 目录（TOC）
markdown-kit toc README.md TOC.md

# 对齐 Markdown 表格格式
markdown-kit table-align doc.md
```

## 功能

### CSV 转表格 (csv2table)
- 将 CSV 文件转换为格式化 Markdown 表格
- 自动识别列数
- 支持管道符转义

### 目录生成 (toc)
- 自动提取 ##、###、#### 标题
- 生成锚点链接
- 支持中文标题

### 表格对齐 (table-align)
- 自动计算每列最大宽度
- 对齐为可读性更好的等宽格式
- 保持表头/分隔行/数据行的结构

## 特点

- 纯 Python，零依赖
- 支持中文内容
- 文件就地修改或输出到新文件

## 🧰 Office Tools Kit 系列工具

本工具属于 **Office Tools Kit 系列**，同类工具推荐：

| 工具 | 功能 | 安装 |
|------|------|------|
| [office-tools-kit](https://pypi.org/project/office-tools-kit/) | Excel合并拆分、PDF合并 | `pip install office-tools-kit` |
| [file-org-kit](https://pypi.org/project/file-org-kit/) | 文件智能分类整理 | `pip install file-org-kit` |
| [img-convert-kit](https://pypi.org/project/img-convert-kit/) | 图片格式批量转换 | `pip install img-convert-kit` |
| [img-resize-kit](https://pypi.org/project/img-resize-kit/) | 图片批量缩放与压缩 | `pip install img-resize-kit` |
| [json-tool-kit](https://pypi.org/project/json-tool-kit/) | JSON 文件处理 | `pip install json-tool-kit` |
| [markdown-kit](https://pypi.org/project/markdown-kit/) | Markdown 文档辅助 | `pip install markdown-kit` |
| [qr-code-kit](https://pypi.org/project/qr-code-kit/) | 二维码生成与解析 | `pip install qr-code-kit` |
| [text-clean-kit](https://pypi.org/project/text-clean-kit/) | 文本文件清洗处理 | `pip install text-clean-kit` |
| [unit-convert-kit](https://pypi.org/project/unit-convert-kit/) | 单位换算 | `pip install unit-convert-kit` |

> 📚 更多工具请访问 [BoiledSaltedDuck 工具主页](https://boiledsaltedduck.github.io/)

## 支持

如果 markdown-kit 帮到了您，欢迎打赏支持：

```
USDT (TRC20): TMPQygMkv42QPeyYnkxMkPwsqs7udbD2Aa
```

您的支持是开源项目持续发展的动力 ❤️
