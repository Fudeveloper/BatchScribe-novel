# AI小说生成器 - 移动版

## 简介

AI小说生成器移动版是原PC版AI小说生成器的Android/iOS适配版本，使用Kivy框架开发，保留了原版所有核心功能。

## 功能特点

- 支持多种AI模型（GPT-3.5、GPT-4、GPT-4.5等）
- 可生成多种类型的小说内容
- 自定义生成参数（温度、创造性等）
- 实时显示生成进度和内容预览
- 暂停/继续/停止生成控制
- 移动设备优化界面

## 安装方法

### Android安装包

1. 下载最新的APK安装包
2. 在Android设备上安装
3. 首次运行时需要配置API密钥

### 从源代码构建

#### 准备环境

```bash
# 安装Python和依赖
pip install kivy buildozer plyer

# Android开发环境（仅在Linux上构建安卓版时需要）
# 请参考Buildozer文档配置Android SDK和NDK
```

#### 构建Android版本

Linux环境下：

```bash
cd novel_generator_app
buildozer -v android debug
```

构建成功后，APK文件将位于`bin`目录下。

## 使用说明

1. 启动应用后，首先输入您的API密钥
2. 选择AI模型和小说类型
3. 设置目标字数
4. 根据需要调整高级设置
5. 点击"开始生成"按钮开始生成小说
6. 生成过程中可以实时查看内容，也可以暂停或停止生成

## 开发者信息

- 基于原PC版AI小说生成器开发
- 使用Kivy框架实现跨平台移动支持
- 支持Android 5.0+设备

## 注意事项

- 需要稳定的网络连接
- 生成过程中耗电较多，建议连接电源使用
- 首次使用请确保正确配置API密钥

## 许可证

与原PC版相同 