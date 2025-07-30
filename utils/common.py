import os
import json
import time
import webbrowser
from typing import Optional

def get_timestamp() -> int:
    """获取当前时间戳"""
    return int(time.time())

def get_output_dir(timestamp: Optional[int] = None) -> str:
    """获取输出目录路径"""
    if timestamp is None:
        timestamp = get_timestamp()
    
    output_dir = f"novel_output_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def open_file(filepath: str) -> None:
    """打开文件（使用系统默认应用）"""
    try:
        os.startfile(filepath)
    except AttributeError:
        # 非Windows系统
        webbrowser.open(filepath)
    except Exception as e:
        print(f"无法打开文件 {filepath}: {e}")

def open_directory(dirpath: str) -> None:
    """打开目录（使用系统文件浏览器）"""
    try:
        if os.path.exists(dirpath):
            os.startfile(dirpath)
        else:
            print(f"目录不存在: {dirpath}")
    except AttributeError:
        # 非Windows系统
        try:
            import subprocess
            subprocess.Popen(['xdg-open', dirpath])
        except Exception:
            webbrowser.open(dirpath)
    except Exception as e:
        print(f"无法打开目录 {dirpath}: {e}")

def count_characters(text: str) -> int:
    """计算文本字符数"""
    return len(text)

def estimate_completion_time(current_length: int, target_length: int, elapsed_time: float) -> float:
    """估计完成时间（秒）"""
    if current_length == 0 or elapsed_time == 0:
        return 0
        
    rate = current_length / elapsed_time  # 每秒生成的字符数
    remaining_chars = target_length - current_length
    
    if rate > 0:
        return remaining_chars / rate
    return 0

def format_time(seconds: float) -> str:
    """将秒数格式化为时:分:秒"""
    if seconds <= 0:
        return "--:--"
        
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

def truncate_text(text: str, max_length: int = 100) -> str:
    """截断文本，添加省略号"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def ensure_directory_exists(directory: str) -> None:
    """确保目录存在，如不存在则创建"""
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def export_custom_prompt(prompt, filename=None):
    """导出自定义提示词到文件
    
    Args:
        prompt (str): 自定义提示词
        filename (str, optional): 文件名。默认为None，使用时间戳生成
        
    Returns:
        str: 导出文件的路径
    """
    if not prompt:
        return None
        
    # 设置默认文件名
    if not filename:
        timestamp = get_timestamp()
        filename = f"custom_prompt_{timestamp}.txt"
    
    # 确保文件有.txt后缀
    if not filename.endswith(".txt"):
        filename += ".txt"
        
    # 添加提示词文件夹
    prompt_dir = "custom_prompts"
    os.makedirs(prompt_dir, exist_ok=True)
    
    # 完整文件路径
    filepath = os.path.join(prompt_dir, filename)
    
    # 写入文件
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(prompt)
        return filepath
    except Exception as e:
        print(f"导出提示词失败: {e}")
        return None

def import_custom_prompt(filepath):
    """从文件导入自定义提示词
    
    Args:
        filepath (str): 文件路径
        
    Returns:
        str: 导入的提示词，失败则返回None
    """
    if not os.path.exists(filepath):
        print(f"文件不存在: {filepath}")
        return None
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            prompt = f.read()
        return prompt
    except Exception as e:
        print(f"导入提示词失败: {e}")
        return None

def list_custom_prompts():
    """列出所有自定义提示词文件
    
    Returns:
        list: 提示词文件列表
    """
    prompt_dir = "custom_prompts"
    
    if not os.path.exists(prompt_dir):
        os.makedirs(prompt_dir, exist_ok=True)
        return []
        
    prompts = []
    for file in os.listdir(prompt_dir):
        if file.endswith(".txt"):
            prompts.append(os.path.join(prompt_dir, file))
            
    return prompts

def get_prompt_preview(filepath, max_length=100):
    """获取提示词文件的内容预览
    
    Args:
        filepath (str): 文件路径
        max_length (int): 最大预览长度
        
    Returns:
        str: 提示词预览
    """
    prompt = import_custom_prompt(filepath)
    if not prompt:
        return ""
        
    # 截断长提示词
    if len(prompt) > max_length:
        return prompt[:max_length] + "..."
    
    return prompt 