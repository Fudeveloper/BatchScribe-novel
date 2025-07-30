# AI小说生成器

一个基于AI的小说生成工具，可以生成各种类型的小说，支持批量生成、续写等功能。

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-4.1.3-orange.svg)](VERSION)

## 📄 开源协议

本项目采用 **GNU Affero General Public License v3.0 (AGPL-3.0)** 开源协议。

### 重要声明：
- **禁止商业用途**：本软件仅供学习和研究使用，禁止任何商业用途
- **强制开源**：任何修改后的代码也必须采用相同的开源协议
- **网络服务条款**：如果通过网络提供服务，必须提供源代码访问

详细协议内容请查看 [LICENSE](LICENSE) 文件。

## 🌟 功能特点

- **多种小说类型**：支持奇幻冒险、科幻未来、武侠仙侠等14种类型
- **多AI模型支持**：兼容GPT、Claude、Gemini、Moonshot等多种高级模型
- **自定义参数**：可调整温度、核采样、生成长度等参数
- **批量生成**：同时生成多篇不同类型的小说
- **续写功能**：继续创作已有的小说
- **自动保存**：生成过程中自动保存内容，防止数据丢失
- **自定义提示词**：为AI提供个性化创作指导
- **智能重试**：网络问题时自动重试，确保生成过程不中断
- **小说摘要**：自动生成小说摘要，便于管理长篇内容
- **现代界面**：直观的用户界面，简化使用流程

## 📋 系统要求

- Python 3.7 或更高版本
- Windows 10/11, macOS, 或 Linux
- 最小屏幕分辨率: 1200x800
- 内存: 最小 4GB，推荐 8GB+
- 磁盘空间: 最小 500MB（不含生成的小说内容）

## 💻 安装指南

### 方法1: 从源码安装

1. 确保已安装 Python 3.7+
2. 克隆仓库：

   ```bash
   git clone https://github.com/yourusername/novel_generator.git
   cd novel_generator
   ```
3. 安装依赖项：

   ```bash
   pip install -r requirements.txt
   ```
4. 运行程序：

   ```bash
   python main.py
   ```

### 方法2: 使用预编译版本

从 [Releases](https://github.com/yourusername/novel_generator/releases) 页面下载最新版本。

## 🚀 快速开始

1. 首次启动程序时，会提示输入API密钥，请输入有效的AI服务API密钥
2. 在主界面上选择小说类型、目标字数和其他基本参数
3. 如需更详细的控制，点击"高级设置"按钮
4. 点击"开始生成"按钮开始创作
5. 生成过程中可以随时"暂停"或"停止"
6. 完成后，生成的小说将保存在输出目录中

## 📁 项目结构

```
novel_generator/
├── main.py                # 主程序入口
├── main_wrapper.py        # 启动包装器
├── core/                  # 核心功能
│   ├── generator.py       # 小说生成器核心逻辑
│   └── model_manager.py   # 模型管理功能
├── ui/                    # 用户界面
│   ├── app.py             # 主应用界面
│   ├── dialogs.py         # 各种对话框
│   └── assets/            # 界面资源
├── utils/                 # 工具函数
│   ├── config.py          # 配置管理
│   ├── common.py          # 通用工具函数
│   └── logging.py         # 日志功能
├── templates/             # 模板文件
│   └── prompts.py         # 小说生成提示词模板
├── novel_generator_app/   # 移动端应用
└── resources/             # 资源文件
```

## ⚙️ 配置说明

配置项保存在 `novel_generator_config.json`文件中，主要配置项包括：

| 配置项       | 说明                 | 默认值           |
| ------------ | -------------------- | ---------------- |
| API密钥      | 用于访问AI服务的密钥 | -                |
| 模型         | 使用的AI模型         | gemini-2.0-flash |
| 语言         | 生成小说的语言       | 中文             |
| 小说类型     | 生成的小说类型       | 奇幻冒险         |
| 目标字数     | 生成小说的字数       | 20000            |
| 并行数       | 同时生成的小说数量   | 3                |
| 自动保存间隔 | 自动保存的秒数       | 60               |

## 🤝 贡献指南

我们欢迎社区贡献！在贡献代码之前，请确保：

1. **遵守开源协议**：所有贡献的代码必须遵循AGPL-3.0协议
2. **代码质量**：确保代码符合项目编码规范
3. **测试覆盖**：新功能需要包含相应的测试
4. **文档更新**：更新相关文档和注释

### 贡献流程：

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📝 开发说明

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/novel_generator.git
cd novel_generator

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 运行开发版本
python main.py
```

### 代码规范

- 使用 Python 3.7+ 语法
- 遵循 PEP 8 编码规范
- 添加适当的类型注解
- 编写清晰的文档字符串

## 🐛 问题反馈

如果您发现了bug或有功能建议，请通过以下方式反馈：

1. 在 [Issues](https://github.com/yourusername/novel_generator/issues) 页面创建新issue
2. 详细描述问题或建议
3. 提供复现步骤（如果是bug）

## 📄 许可证

本项目采用 GNU Affero General Public License v3.0 开源协议。详见 [LICENSE](LICENSE) 文件。

## 👨‍💻 作者

**许丙南** - 初始开发者

- 邮箱：your.email@example.com
- GitHub：[@yourusername](https://github.com/yourusername)

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！

## ⚠️ 免责声明

本软件仅供学习和研究使用。使用者需要：

1. 遵守相关法律法规
2. 尊重知识产权
3. 不得用于商业用途
4. 对使用本软件产生的任何后果自行承担责任

---

**注意**：使用本软件即表示您同意遵守AGPL-3.0开源协议的所有条款。
