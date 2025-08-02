import os
import sys
import logging
import traceback
import importlib.util

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('novel_generator.log', encoding='utf-8')
    ]
)
logger = logging.getLogger("novel_generator")

# 添加调试信息
logger.info(f"当前工作目录: {os.getcwd()}")

# 检测是否在打包环境中运行
is_frozen = getattr(sys, 'frozen', False)
if is_frozen:
    # 运行在PyInstaller打包的环境中
    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    logger.info(f"运行在打包环境中，基础目录: {base_dir}")
else:
    # 运行在开发环境中
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logger.info(f"运行在开发环境中，基础目录: {base_dir}")

# 添加项目根目录到Python路径，确保导入正常工作
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# 确保当前目录也在路径中
paths_to_add = [
    current_dir, 
    parent_dir,
    os.path.join(base_dir, 'ui'),
    os.path.join(base_dir, 'core'),
    os.path.join(base_dir, 'utils'),
    os.path.join(base_dir, 'templates')
]

for path in paths_to_add:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)
        logger.info(f"添加路径到sys.path: {path}")

logger.info(f"Python路径: {sys.path}")

# 添加ctypes导入，用于设置应用ID和去除黑窗口
try:
    import ctypes
    if sys.platform.startswith('win'):
        # 设置应用ID，使任务栏图标正确显示
        app_id = 'novel_generator.app'
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
            logger.info("已设置Windows应用ID")
        except Exception as e:
            logger.warning(f"设置Windows应用ID失败: {str(e)}")
except ImportError:
    logger.warning("无法导入ctypes模块")

# 检查ui模块是否存在
def check_module(module_name):
    """检查模块是否可以导入"""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            logger.info(f"模块 {module_name} 可以被导入")
            return True
        else:
            logger.warning(f"模块 {module_name} 不可用")
            return False
    except Exception as e:
        logger.error(f"检查模块 {module_name} 时出错: {str(e)}")
        return False

# 检查关键模块
check_module('ui')
check_module('ui.app')

# 直接导入UI模块
try:
    # 尝试不同的导入方式
    try:
        from ui.app import NovelGeneratorApp
        logger.info("成功导入UI模块 (从ui.app)")
    except ImportError:
        # 尝试直接导入
        if is_frozen:
            # 在打包环境中尝试绝对导入
            sys.path.insert(0, os.path.join(base_dir, 'ui'))
            import app
            NovelGeneratorApp = app.NovelGeneratorApp
            logger.info("成功导入UI模块 (从app)")
        else:
            # 其他情况下重新抛出异常
            raise
except ImportError as e:
    logger.error(f"无法导入UI模块: {traceback.format_exc()}")
    # 在控制台显示错误信息
    print("错误：无法导入UI模块")
    print(f"当前Python路径: {sys.path}")
    print(f"错误详情: {str(e)}")
    print("请尝试使用python main_wrapper.py启动程序")
    
    # 在GUI中显示错误（如果可能）
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        messagebox.showerror("导入错误", 
                             f"无法导入UI模块。\n\n错误详情: {str(e)}\n\n请联系开发者获取支持。")
    except:
        pass
    
    # 等待用户按键后退出
    input("按Enter键退出...")
    sys.exit(1)

def main():
    """
    主程序入口，启动GUI应用
    """
    import tkinter as tk
    from tkinter import messagebox
    
    logger.info("AI小说生成器启动")
    
    try:
        root = tk.Tk()
        # 设置窗口尺寸
        root.geometry("1280x860")  
        root.minsize(1200, 800)    
        
        # 设置窗口图标
        try:
            # 尝试多个可能的图标路径
            icon_paths = [
                os.path.join(os.path.dirname(__file__), "resources", "icon.ico"),
                os.path.join(base_dir, "resources", "icon.ico"),
                "resources/icon.ico"
            ]
            
            icon_found = False
            for icon_path in icon_paths:
                if os.path.exists(icon_path):
                    root.iconbitmap(icon_path)
                    logger.info(f"已设置应用图标: {icon_path}")
                    icon_found = True
                    break
            
            if not icon_found:
                import warnings
                warnings.warn("未找到可用的应用图标")
        except Exception as e:
            logger.warning(f"设置应用图标失败: {str(e)}")

        # 创建应用实例
        app = NovelGeneratorApp(root)
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        logger.info("应用界面已初始化")
        
        root.mainloop()
        logger.info("应用已关闭")
    except Exception as e:
        error_msg = f"应用运行出错: {str(e)}"
        logger.error(f"{error_msg}\n{traceback.format_exc()}")
        
        try:
            messagebox.showerror("错误", error_msg)
        except:
            print(error_msg)
            
        input("按Enter键退出...")
        sys.exit(1)

if __name__ == "__main__":
    main() 