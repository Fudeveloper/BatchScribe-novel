# 贡献指南

感谢您对AI小说生成器项目的关注！我们欢迎所有形式的贡献，包括但不限于：

- 🐛 Bug报告
- 💡 功能建议
- 📝 文档改进
- 🔧 代码贡献
- 🌟 测试用例

## 📋 贡献前准备

在开始贡献之前，请确保：

1. **阅读开源协议**：本项目采用AGPL-3.0协议，所有贡献必须遵循该协议
2. **了解项目结构**：熟悉代码库的组织结构
3. **设置开发环境**：确保本地开发环境正常运行

## 🚀 快速开始

### 1. Fork 项目

1. 访问 [项目主页](https://github.com/yourusername/novel_generator)
2. 点击右上角的 "Fork" 按钮
3. 选择您的GitHub账户作为目标

### 2. 克隆您的Fork

```bash
git clone https://github.com/YOUR_USERNAME/novel_generator.git
cd novel_generator
```

### 3. 设置上游仓库

```bash
git remote add upstream https://github.com/yourusername/novel_generator.git
```

### 4. 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

## 🔧 开发环境设置

### 安装依赖

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖
pip install pytest black flake8 mypy
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_generator.py

# 生成覆盖率报告
pytest --cov=core --cov-report=html
```

### 代码质量检查

```bash
# 代码风格检查
flake8 .

# 代码格式化
black .

# 类型检查
mypy .
```

## 📝 贡献类型

### Bug报告

如果您发现了bug，请：

1. 在 [Issues](https://github.com/yourusername/novel_generator/issues) 页面创建新issue
2. 使用 "Bug report" 模板
3. 提供详细的复现步骤
4. 包含错误信息和系统环境

**Bug报告模板：**

```markdown
## Bug描述
简要描述bug的内容

## 复现步骤
1. 打开程序
2. 点击...
3. 观察错误

## 预期行为
描述应该发生什么

## 实际行为
描述实际发生了什么

## 环境信息
- 操作系统：
- Python版本：
- 程序版本：

## 错误信息
粘贴完整的错误信息
```

### 功能建议

如果您有新功能建议，请：

1. 在Issues页面创建新issue
2. 使用 "Feature request" 模板
3. 详细描述功能需求和用例
4. 讨论实现方案

### 代码贡献

#### 代码规范

- **Python版本**：使用Python 3.7+语法
- **编码规范**：遵循PEP 8
- **类型注解**：为新函数添加类型注解
- **文档字符串**：为所有公共函数添加文档字符串
- **测试覆盖**：新功能需要包含测试用例

#### 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

类型说明：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

示例：
```
feat: 添加新的小说类型支持

- 新增科幻小说类型
- 添加相应的提示词模板
- 更新用户界面选项

Closes #123
```

#### 代码审查

1. **自检**：提交前运行测试和代码检查
2. **小步提交**：每个提交专注于一个功能或修复
3. **清晰描述**：提交信息要清晰描述变更内容
4. **响应反馈**：及时响应代码审查意见

## 🔄 工作流程

### 1. 同步上游代码

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### 2. 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

### 3. 开发功能

- 编写代码
- 添加测试
- 更新文档
- 运行测试确保通过

### 4. 提交代码

```bash
git add .
git commit -m "feat: 添加新功能描述"
git push origin feature/your-feature-name
```

### 5. 创建Pull Request

1. 访问您的GitHub仓库
2. 点击 "Compare & pull request"
3. 填写PR描述，使用PR模板
4. 等待代码审查

### 6. 代码审查

- 响应审查意见
- 修复发现的问题
- 重新提交（如果需要）

## 📚 文档贡献

### 文档类型

- **README.md**：项目介绍和使用说明
- **API文档**：代码接口说明
- **用户指南**：详细使用教程
- **开发者文档**：技术实现说明

### 文档规范

- 使用清晰的标题结构
- 提供代码示例
- 包含截图（如果需要）
- 保持文档的时效性

## 🧪 测试贡献

### 测试类型

- **单元测试**：测试单个函数或类
- **集成测试**：测试模块间的交互
- **端到端测试**：测试完整功能流程

### 测试规范

- 测试文件名以 `test_` 开头
- 测试函数名以 `test_` 开头
- 使用描述性的测试名称
- 包含正面和负面测试用例

## 🎯 贡献优先级

### 高优先级

- 安全性修复
- 严重bug修复
- 核心功能改进

### 中优先级

- 新功能开发
- 性能优化
- 用户体验改进

### 低优先级

- 文档改进
- 代码重构
- 测试覆盖

## 🤝 社区准则

### 行为准则

- 尊重所有贡献者
- 保持专业和友善的交流
- 接受建设性的批评
- 帮助新贡献者

### 沟通渠道

- **Issues**：问题报告和功能讨论
- **Pull Requests**：代码审查和合并
- **Discussions**：一般性讨论（如果启用）

## 📞 获取帮助

如果您在贡献过程中遇到问题：

1. 查看 [Issues](https://github.com/yourusername/novel_generator/issues) 页面
2. 搜索是否有类似问题
3. 创建新issue描述您的问题
4. 在issue中详细描述您遇到的问题

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！您的贡献让这个项目变得更好。

---

**记住**：每个贡献，无论大小，都是宝贵的。感谢您的参与！ 