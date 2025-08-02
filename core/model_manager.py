import os
import sys
import requests
from typing import List, Dict, Any, Optional

# 修复导入问题
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# 尝试使用相对导入（作为模块导入时）
try:
    from ..templates.prompts import MODEL_DESCRIPTIONS, SUPPORTED_MODELS
except ImportError:
    from templates.prompts import MODEL_DESCRIPTIONS, SUPPORTED_MODELS

def get_model_list(api_key=None):
    """获取可用模型列表"""
    # 返回支持的模型列表
    return SUPPORTED_MODELS

def get_model_info(model_name: str) -> Dict[str, Any]:
    """获取特定模型的详细信息"""
    # 这里可以添加获取模型详细信息的代码
    # 暂时返回一些基本信息
    
    model_info = {
        "name": model_name,
        "max_tokens": 4000,
        "pricing": "未知",
        "capabilities": []
    }
    
    # 根据不同模型设置不同的属性
    if "claude" in model_name:
        model_info["max_tokens"] = 4000
        model_info["capabilities"] = ["文本生成", "内容理解", "多语言支持"]
    elif "gpt" in model_name:
        model_info["max_tokens"] = 4000
        model_info["capabilities"] = ["文本生成", "内容理解", "代码生成"]
        
    return model_info

def check_api_key_validity(api_key: str) -> bool:
    """检查API密钥是否有效"""
    # 这里应该添加实际的API密钥验证逻辑
    # 目前简单返回True
    return True if api_key and len(api_key) > 10 else False 