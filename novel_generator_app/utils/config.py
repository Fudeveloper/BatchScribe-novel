import os
import json
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('novel_generator_config')

# 配置文件路径
CONFIG_FILE = 'novel_generator_config.json'

def load_config():
    """
    加载配置文件，如果不存在则创建默认配置
    
    Returns:
        dict: 配置字典
    """
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                logger.info("配置文件加载成功")
                return config
        else:
            logger.info("配置文件不存在，创建默认配置")
            default_config = create_default_config()
            save_config(default_config)
            return default_config
    except Exception as e:
        logger.error(f"加载配置文件时出错: {str(e)}")
        return create_default_config()

def save_config(config):
    """
    保存配置到文件
    
    Args:
        config (dict): 要保存的配置字典
    """
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
            logger.info("配置已保存")
    except Exception as e:
        logger.error(f"保存配置文件时出错: {str(e)}")

def create_default_config():
    """
    创建默认配置
    
    Returns:
        dict: 默认配置字典
    """
    return {
        "api_key": "",
        "model": "gpt-4.5-preview",
        "language": "中文",
        "novel_type": "玄幻小说",
        "target_length": 20000,
        "auto_summary": True,
        "auto_summary_interval": 2000,
        "create_ending": False,
        "advanced_settings": {
            "temperature": 0.8,
            "top_p": 0.9,
            "max_tokens": 4000,
            "context_length": 100000,
            "autosave_interval": 60,
            "creativity": 0.7,
            "formality": 0.5,
            "detail_level": 0.6,
            "writing_style": "平衡"
        }
    } 