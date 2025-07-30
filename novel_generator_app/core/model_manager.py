import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('model_manager')

# 支持的模型列表
SUPPORTED_MODELS = [
    {
        "id": "gpt-3.5-turbo",
        "name": "GPT-3.5 Turbo",
        "description": "快速且经济的模型，适合一般性文本生成任务",
        "context_length": 16000,
        "max_tokens": 4000
    },
    {
        "id": "gpt-4",
        "name": "GPT-4",
        "description": "强大的大型语言模型，能够理解和生成复杂的文本",
        "context_length": 8000,
        "max_tokens": 4000
    },
    {
        "id": "gpt-4.5-preview",
        "name": "GPT-4.5 预览版",
        "description": "最新的OpenAI大型语言模型，提供最佳的文本生成能力",
        "context_length": 100000,
        "max_tokens": 4000
    }
]

def get_model_list():
    """
    获取可用模型列表
    
    Returns:
        list: 模型ID列表
    """
    return [model["id"] for model in SUPPORTED_MODELS]

def get_model_info(model_id):
    """
    获取指定模型的详细信息
    
    Args:
        model_id (str): 模型ID
        
    Returns:
        dict: 模型信息字典，如果未找到则返回None
    """
    for model in SUPPORTED_MODELS:
        if model["id"] == model_id:
            return model
    
    logger.warning(f"未找到模型信息: {model_id}")
    return None

def get_recommended_model():
    """
    获取推荐的默认模型
    
    Returns:
        str: 推荐模型的ID
    """
    return "gpt-4.5-preview" 