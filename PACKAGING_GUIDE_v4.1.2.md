# AI小说生成器 v4.1.2 打包指南

## 📦 打包选项

### 1. 快速打包（推荐）
```bash
# Windows用户
build_simple.bat

# 或直接运行Python脚本
python build_simple.py
```

**特点**:
- 自动化程度高
- 稳定可靠
- 包含所有必要文件
- 自动复制文档和配置

### 2. 高级打包
```bash
# Windows用户
build_quick.bat

# 或直接运行Python脚本
python build_quick.py
```

**特点**:
- 包含版本信息
- 更详细的配置
- 更多自定义选项
- 适合开发者使用

### 3. 手动打包
```bash
# 使用spec文件
pyinstaller AI小说生成器_v4.1.2.spec

# 或使用原始build.py
python build.py
```

## 🛠️ 环境要求

### Python版本
- Python 3.8+
- 推荐 Python 3.11

### 必要依赖
```bash
pip install pyinstaller>=6.0.0
pip install aiohttp
pip install tkinter  # 通常Python自带
```

### 可选依赖
```bash
pip install pyarmor  # 代码混淆（高级打包）
pip install pillow   # 图标处理
```

## 📁 文件结构

### 打包前检查
确保以下文件/目录存在：
```
novel_generator/
├── main.py              # 主程序入口
├── core/                # 核心模块
├── ui/                  # 用户界面
├── templates/           # 提示词模板
├── resources/           # 资源文件
│   ├── icon.ico        # 应用图标
│   └── icon.png        # 备用图标
├── example_prompts/     # 示例提示词
└── requirements.txt     # 依赖列表
```

### 打包后结构
```
dist/
└── AI小说生成器_v4.1.2/
    ├── AI小说生成器_v4.1.2.exe    # 主程序
    ├── _internal/                   # 内部文件
    ├── resources/                   # 资源文件
    ├── templates/                   # 模板文件
    ├── example_prompts/             # 示例文件
    ├── novel_generator_config.json  # 配置文件
    ├── 使用说明.md                  # 使用文档
    ├── 更新说明.md                  # 更新日志
    └── 用户指南.md                  # 用户指南
```

## ⚙️ 打包配置

### 基本配置
- **模式**: 目录模式（--onedir）
- **界面**: 无控制台窗口（--windowed）
- **图标**: resources/icon.ico
- **名称**: AI小说生成器_v4.1.2

### 包含文件
- **数据文件**: resources, templates, example_prompts
- **隐藏导入**: aiohttp, tkinter, configparser等
- **排除模块**: matplotlib, numpy, scipy等大型库

### 版本信息
- **版本号**: 4.1.2.0
- **公司**: 147229
- **描述**: AI小说生成器 - 智能小说创作工具
- **版权**: Copyright (C) 2024 147229

## 🔧 常见问题

### 1. PyInstaller未安装
```bash
pip install pyinstaller
```

### 2. 缺少隐藏导入
如果运行时出现导入错误，在spec文件中添加：
```python
hiddenimports=['模块名']
```

### 3. 文件缺失
确保所有数据文件都在datas列表中：
```python
datas=[
    ('resources', 'resources'),
    ('templates', 'templates'),
]
```

### 4. 编码问题
Windows系统可能遇到编码问题，使用简化打包脚本：
```bash
python build_simple.py
```

### 5. 图标问题
如果ico文件有问题，可以：
- 使用png格式图标
- 删除--icon参数
- 使用在线工具转换图标格式

## 🚀 优化建议

### 1. 减小体积
- 排除不必要的模块
- 使用UPX压缩（--upx）
- 删除调试信息（--strip）

### 2. 提高性能
- 使用目录模式而非单文件模式
- 预编译Python文件
- 优化导入路径

### 3. 增强安全性
- 使用代码混淆（PyArmor）
- 清理敏感信息
- 添加数字签名

## 📋 打包检查清单

### 打包前
- [ ] 更新版本号
- [ ] 清理敏感信息
- [ ] 检查依赖完整性
- [ ] 验证主程序功能
- [ ] 确认资源文件存在

### 打包中
- [ ] 选择合适的打包脚本
- [ ] 监控打包过程
- [ ] 检查错误信息
- [ ] 确认文件包含完整

### 打包后
- [ ] 测试可执行文件
- [ ] 验证所有功能
- [ ] 检查文档完整性
- [ ] 测试不同环境
- [ ] 创建安装包（可选）

## 🎯 分发建议

### 1. 文件组织
```
AI小说生成器_v4.1.2_发布包/
├── AI小说生成器_v4.1.2/     # 主程序目录
├── 使用说明.md              # 使用文档
├── 更新说明.md              # 更新日志
├── 安装指南.txt             # 安装说明
└── README.txt               # 简要说明
```

### 2. 压缩打包
- 使用7-Zip或WinRAR压缩
- 压缩率选择"标准"
- 添加密码保护（可选）
- 创建自解压文件（可选）

### 3. 版本管理
- 使用语义化版本号
- 保留历史版本
- 提供升级路径
- 记录变更日志

---

**注意**: 本指南适用于AI小说生成器v4.1.2版本，其他版本可能有所不同。 