# 📋 Resume Analyzer - AI 简历分析与评估技能

> 🤖 一个基于 AI Agent 的智能简历分析技能，支持批量读取 PDF 简历，按照多维度对候选人进行评分，并自动生成结构化的 Excel 评估报告。

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PDF](https://img.shields.io/badge/PDF-pdfplumber-red?logo=adobe&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-openpyxl-green?logo=microsoftexcel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ 功能特性

- 🔍 **智能简历解析** — 自动提取 PDF 简历中的关键信息（姓名、学历、技能、经历等）
- 📊 **多维度评分** — 从学历背景、工作经验、技能匹配、项目经验、稳定性、发展潜力六个维度打分
- 🎯 **岗位匹配** — 内置多个岗位要求模板，根据特定岗位标准精准评估候选人
- 📁 **批量处理** — 支持单个简历文件和整个文件夹的批量分析
- 📈 **Excel 报告** — 自动生成带格式化样式、颜色标注和汇总统计的专业评估报告
- 🏷️ **推荐分级** — 根据总分自动给出「推荐 / 待定 / 不推荐」结论

---

## 📂 项目结构

```
resume-analyzer/
├── 📄 SKILL.md                      # 技能核心文档（AI Agent 读取此文件执行任务）
├── 📄 README.md                     # 项目说明文档
├── 📂 scripts/                      # Python 工具脚本
│   ├── 🐍 read_pdf.py              # PDF 简历读取工具
│   └── 🐍 write_excel.py           # Excel 报告写入工具
└── 📂 resources/                    # 岗位要求文档
    ├── 📋 产品经理.md
    ├── 📋 前端开发.md
    ├── 📋 Java工程师.md
    ├── 📋 测试工程师.md
    └── 📋 项目经理.md
```

---

## 🚀 快速开始

### 环境准备

```bash
# 安装 Python 依赖
pip install pdfplumber openpyxl
```

### 使用方式

本技能设计为 **AI Agent 技能（Skill）**，配合支持技能系统的 AI 编程助手使用。将 `resume-analyzer` 文件夹放入你的技能目录后，只需用自然语言对 AI 说：

```
帮我分析 d:\resumes 文件夹下的简历，目标岗位是前端开发
```

AI 将自动执行以下流程：

1. 📥 读取指定路径下的所有 PDF 简历
2. 📖 加载对应岗位的要求文档
3. 🧠 逐份分析评分并给出综合评价
4. 📊 生成格式化的 Excel 评估报告

### 单独使用脚本

也可以独立运行 Python 脚本：

```bash
# 读取简历（输出 JSON）
python scripts/read_pdf.py /path/to/resumes/

# 写入 Excel 报告
python scripts/write_excel.py output.xlsx --input results.json
```

---

## 📊 评分体系

满分 **100 分**，由以下六个维度组成：

| 维度 | 分值 | 评分要点 |
|:---:|:---:|:---|
| 🎓 学历背景 | **15分** | 学历层次、院校水平、专业相关性 |
| 💼 工作经验 | **20分** | 相关领域年限、岗位匹配度、职级成长 |
| 🛠️ 技能匹配 | **25分** | 核心技术栈与岗位要求的匹配程度 |
| 📁 项目经验 | **20分** | 项目复杂度、承担角色、成果产出 |
| ⚖️ 稳定性 | **10分** | 平均任职时长、跳槽频率 |
| 🚀 发展潜力 | **10分** | 学习能力、成长速度、额外认证 |

### 推荐等级

| 等级 | 分数范围 | 含义 |
|:---:|:---:|:---|
| ✅ **推荐** | ≥ 75 分 | 候选人综合素质优秀，建议进入面试 |
| ⏳ **待定** | 60 - 74 分 | 候选人有一定潜力，建议进一步评估 |
| ❌ **不推荐** | < 60 分 | 候选人与岗位要求差距较大 |

---

## 🏢 内置岗位模板

| 岗位 | 文件 | 核心评估维度 |
|:---|:---|:---|
| 产品经理 | `resources/产品经理.md` | 需求分析、产品规划、项目推动、数据分析 |
| 前端开发 | `resources/前端开发.md` | React/Vue、TypeScript、CSS、工程化、性能优化 |
| Java工程师 | `resources/Java工程师.md` | JVM、Spring生态、数据库、分布式、微服务 |
| 测试工程师 | `resources/测试工程师.md` | 测试方法论、自动化测试、接口测试、性能测试 |
| 项目经理 | `resources/项目经理.md` | 项目管理、敏捷实践、团队管理、沟通协调 |

> 💡 **自定义岗位**：在 `resources/` 目录下新建 `岗位名称.md` 文件，参照已有模板编写岗位要求即可。

---

## 📈 Excel 报告预览

生成的 Excel 报告包含以下特性：

- 🎨 **专业配色** — 蓝色标题栏、橙色评分表头、绿/黄/红推荐状态
- 📊 **完整信息** — 基本信息 + 六维评分 + 综合评价 + 推荐结论
- 📋 **汇总统计** — 底部自动统计推荐/待定/不推荐人数
- 📐 **自适应列宽** — 各列宽度根据内容类型预设优化

---

## 🔧 脚本说明

### `scripts/read_pdf.py` — PDF 读取工具

```bash
# 读取单个 PDF
python scripts/read_pdf.py /path/to/resume.pdf

# 读取文件夹中所有 PDF
python scripts/read_pdf.py /path/to/folder/
```

**输出格式**：JSON，包含文件路径、文件名、提取文本、页数等信息。

### `scripts/write_excel.py` — Excel 写入工具

```bash
# 从 JSON 文件读取
python scripts/write_excel.py output.xlsx --input results.json

# 从标准输入读取
echo '{"position":"前端开发","candidates":[...]}' | python scripts/write_excel.py output.xlsx

# 指定岗位名称
python scripts/write_excel.py output.xlsx --input results.json --position "Java工程师"
```

**输入格式**：参见 [SKILL.md](SKILL.md) 中的 JSON 数据格式说明。

---

## 📝 示例

`emp_sample/` 目录下包含测试用的示例文件：

- 5 份模拟的前端开发岗位简历 PDF
- `analysis_results.json` — AI 分析评分结果
- `简历分析报告.xlsx` — 生成的 Excel 评估报告

---

## 📄 许可证

本项目采用 MIT 许可证开源。
