#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
这是AI小说生成器的主要入口点包装脚本。
它确保所有必要的模块可以被正确导入，无论是在开发环境还是打包环境中。
"""

import os
import sys
import importlib.util

def setup_environment():
    """设置运行环境，确保所有模块可以被正确导入"""
    # 获取应用程序运行目录
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 打包后的运行环境
        base_dir = sys._MEIPASS
    else:
        # 开发环境
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 确保当前目录在导入路径中
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)
    
    # 添加可能的模块路径
    paths = [
        os.path.join(base_dir, 'ui'),
        os.path.join(base_dir, 'core'),
        os.path.join(base_dir, 'utils'),
        os.path.join(base_dir, 'templates'),
    ]
    
    for path in paths:
        if os.path.exists(path) and path not in sys.path:
            sys.path.insert(0, path)
    
    # 输出调试信息
    print(f"当前工作目录: {os.getcwd()}")
    print(f"系统路径: {sys.path}")
    
    # 检查ui模块是否可以被导入
    try:
        spec = importlib.util.find_spec('ui')
        if spec is not None:
            print("ui模块可以被导入")
        else:
            print("警告: ui模块不可用")
            
        spec = importlib.util.find_spec('ui.app')
        if spec is not None:
            print("ui.app模块可以被导入")
        else:
            print("警告: ui.app模块不可用")
    except Exception as e:
        print(f"检查模块导入时出错: {str(e)}")

def main():
    """主函数，导入并运行原始main脚本"""
    # 设置环境
    setup_environment()
    
    try:
        # 导入并执行原始main模块
        import main
        if hasattr(main, 'main'):
            main.main()
        else:
            print("错误: main模块中没有main函数")
    except Exception as e:
        import traceback
        print(f"运行main模块时出错: {str(e)}")
        print(traceback.format_exc())
        input("按Enter键退出...")
        sys.exit(1)

if __name__ == "__main__":
    main() 