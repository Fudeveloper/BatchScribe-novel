# AI小说生成器 - PyQt6现代界面

## 简介

PyQt6界面是AI小说生成器的一个现代化UI选项，提供更美观、更流畅的用户体验。这个界面与原始的Tkinter界面功能完全相同，但具有以下优势：

- 现代化的外观和感觉
- 更丰富的视觉效果
- 更好的跨平台一致性
- 更流畅的用户交互
- 更好的高DPI显示支持

## 安装

要使用PyQt6界面，您需要先安装PyQt6依赖：

```bash
pip install PyQt6 PyQt6-Qt6 PyQt6-sip
```

## 启动方式

### 方法1：使用启动器（推荐）

运行启动器，可以在Tkinter和PyQt界面之间选择：

```bash
python launcher.py
```

### 方法2：直接启动PyQt界面

```bash
python launcher.py --pyqt
```

### 方法3：通过模块直接启动

```bash
python -m ui.qt_app
```

## 界面切换

- 如果您在使用过程中想要切换回原始界面，可以通过启动器重新选择，或直接运行：

```bash
python launcher.py --tkinter
```

## 注意事项

1. 所有配置文件和数据与原始界面共享，切换界面不会影响您的设置和生成结果
2. 如果您在PyQt界面中遇到问题，可以随时切换回Tkinter界面
3. PyQt版本仍在优化中，欢迎提供反馈和建议

## 截图对比

### PyQt6现代界面
(PyQt界面截图位置)

### 原始Tkinter界面
(Tkinter界面截图位置)

## 反馈

如果您有任何问题或建议，请通过以下方式联系我们：

- 提交GitHub问题
- 发送邮件至（您的邮箱）

感谢您使用AI小说生成器！ 