# 🧰 AK Skills Sample — AI Agent 技能案例库

> 一个开源的 AI Agent 技能（Skill）案例集合，提供可直接使用的技能模板和最佳实践参考。  
> 每个技能都是独立的、可复用的功能模块，让 AI 编程助手获得专业领域的工作能力。

![Skills](https://img.shields.io/badge/技能数量-1-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 💡 什么是 Skill（技能）？

**Skill** 是一种可插拔的能力扩展包，用于增强 AI Agent 在特定领域的表现。每个 Skill 包含：

| 组成部分 | 说明 |
|:---|:---|
| `SKILL.md` | 核心指令文件，定义技能的触发条件、工作流程和操作规范 |
| `scripts/` | 可执行的工具脚本（Python/Bash 等），提供确定性的数据处理能力 |
| `resources/` | 领域知识文档，为 AI 提供专业参考依据 |

> 简单来说：**你告诉 AI「做什么」，Skill 教会 AI「怎么做」。**

---

## 📦 技能列表

| 技能 | 目录 | 描述 | 状态 |
|:---|:---|:---|:---:|
| 📋 [简历分析与评估](#-简历分析与评估-resume-analyzer) | `skills/resume-analyzer/` | 批量分析 PDF 简历，多维度打分，生成 Excel 报告 | ✅ 可用 |
| 🔜 *更多技能开发中...* | — | — | — |

---

## 📋 简历分析与评估 (resume-analyzer)

### 功能概述

自动读取 PDF 简历 → 根据岗位要求多维度评分 → 生成结构化 Excel 报告。

```
📄 简历 PDF ──→ 🧠 AI 分析评分 ──→ 📊 Excel 评估报告
                     ↑
               📋 岗位要求文档
```

### 核心能力

- 🔍 **智能解析** — 自动提取简历中的姓名、学历、技能、工作经历等关键信息
- 📊 **六维评分** — 学历背景(15分) + 工作经验(20分) + 技能匹配(25分) + 项目经验(20分) + 稳定性(10分) + 发展潜力(10分) = 满分100分
- 🎯 **岗位对标** — 内置 5 个岗位模板，支持自定义扩展
- 📁 **批量处理** — 支持单个文件或整个文件夹
- 📈 **专业报告** — 带格式化样式、颜色标注和汇总统计的 Excel 报告

### 内置岗位模板

| 岗位 | 核心考察点 |
|:---|:---|
| 产品经理 | 需求分析、产品规划、项目推动、数据分析 |
| 前端开发 | React/Vue、TypeScript、CSS、工程化、性能优化 |
| Java工程师 | JVM、Spring生态、数据库、分布式、微服务 |
| 测试工程师 | 测试方法论、自动化测试、接口测试、性能测试 |
| 项目经理 | 项目管理、敏捷实践、团队管理、沟通协调 |

> 💡 自定义岗位：在 `resources/` 下新建 `岗位名称.md`，参照已有模板编写即可。

### 推荐等级

| 等级 | 分数 | 含义 |
|:---:|:---:|:---|
| ✅ 推荐 | ≥ 75 | 综合素质优秀，建议进入面试 |
| ⏳ 待定 | 60-74 | 有一定潜力，建议进一步评估 |
| ❌ 不推荐 | < 60 | 与岗位要求差距较大 |

---

## 🚀 如何使用

### 1. 克隆仓库

```bash
git clone https://github.com/Angus221/ak.skills_sample.git
```

### 2. 安装依赖

```bash
pip install pdfplumber openpyxl
```

### 3. 将技能集成到你的 AI Agent 工具中

将 `skills/` 目录下的技能文件夹复制到你的 AI 编程助手的技能目录中。不同工具的技能目录位置可能不同，请参考对应文档。

### 4. 用自然语言触发

集成后，只需用自然语言对 AI 说：

```
帮我分析 D:\resumes 下的简历，目标岗位是前端开发
```

AI 将自动完成：读取简历 → 加载岗位要求 → 逐份打分 → 生成 Excel 报告。

### 5. 也可以单独使用脚本

```bash
# 读取 PDF 简历（输出 JSON）
python skills/resume-analyzer/scripts/read_pdf.py /path/to/resumes/

# 生成 Excel 报告
python skills/resume-analyzer/scripts/write_excel.py output.xlsx --input results.json
```

---

## 📂 项目结构

```
ak.skills_sample/
├── 📄 README.md                              # 项目说明
├── 📂 skills/                                # 技能集合
│   └── 📂 resume-analyzer/                   # 简历分析技能
│       ├── 📄 SKILL.md                       # 技能核心文档
│       ├── 📂 scripts/                       # 工具脚本
│       │   ├── 🐍 read_pdf.py               # PDF 读取工具
│       │   └── 🐍 write_excel.py            # Excel 写入工具
│       └── 📂 resources/                     # 岗位要求文档
│           ├── 产品经理.md
│           ├── 前端开发.md
│           ├── Java工程师.md
│           ├── 测试工程师.md
│           └── 项目经理.md
└── 📂 emp_sample/                            # 示例数据
    ├── 📄 5 份模拟简历 PDF
    ├── 📄 analysis_results.json              # AI 分析结果
    └── 📊 简历分析报告.xlsx                   # 生成的 Excel 报告
```

---

## 🤝 贡献

欢迎贡献新的技能！请参考以下规范：

1. 每个技能放在 `skills/技能名称/` 目录下
2. 必须包含 `SKILL.md` 文件，使用 YAML frontmatter 定义 `name` 和 `description`
3. 工具脚本放在 `scripts/`，参考文档放在 `resources/`
4. 提交 PR 时请附带示例数据和使用说明

---

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证开源。
