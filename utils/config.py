import os
import sys
import json
import configparser
from typing import Dict, Any, Optional

CONFIG_FILE = "novel_generator_config.ini"
JSON_CONFIG_FILE = "novel_generator_config.json"

def save_config(config: Dict[str, Any]) -> None:
    """保存配置到JSON配置文件
    
    Args:
        config: 包含配置项的字典
    """
    try:
        with open(JSON_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
            
        # 同时维护旧版配置文件的兼容性
        config_parser = configparser.ConfigParser()
        config_parser['DEFAULT'] = {
            'api_key': config.get('api_key', ''),
            'model': config.get('model', 'gpt-4.5-preview'),
            'language': config.get('language', '中文'),
            'max_workers': str(config.get('max_workers', 3)),
            'context_length': str(config.get('context_length', 100000))
        }
        
        with open(CONFIG_FILE, 'w', encoding='utf-8') as configfile:
            config_parser.write(configfile)
            
    except Exception as e:
        print(f"保存配置失败: {e}")
        import traceback
        print(traceback.format_exc())

def load_config() -> Dict[str, Any]:
    """加载配置文件，优先使用JSON格式，如果不存在则尝试使用INI格式
    
    Returns:
        Dict[str, Any]: 配置字典
    """
    defaults = {
        'api_key': '',
        'model': 'gpt-4.5-preview',
        'language': '中文',
        'max_workers': 3,
        'context_length': 100000,
        'novel_type': '奇幻冒险',
        'target_length': 20000,
        'num_novels': 1,
        'auto_summary': True,
        'auto_summary_interval': 10000
    }
    
    # 优先尝试读取JSON配置
    if os.path.exists(JSON_CONFIG_FILE):
        try:
            with open(JSON_CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config
        except Exception as e:
            print(f"读取JSON配置失败: {e}")
    
    # 如果JSON配置不存在或读取失败，尝试读取INI配置
    if os.path.exists(CONFIG_FILE):
        config = configparser.ConfigParser()
        try:
            config.read(CONFIG_FILE, encoding='utf-8')
            ini_config = {
                'api_key': config.get('DEFAULT', 'api_key', fallback=defaults['api_key']),
                'model': config.get('DEFAULT', 'model', fallback=defaults['model']),
                'language': config.get('DEFAULT', 'language', fallback=defaults['language']),
                'max_workers': config.getint('DEFAULT', 'max_workers', fallback=defaults['max_workers']),
                'context_length': config.getint('DEFAULT', 'context_length', fallback=defaults['context_length'])
            }
            # 使用默认值补充其他配置项
            for key, value in defaults.items():
                if key not in ini_config:
                    ini_config[key] = value
            return ini_config
        except Exception as e:
            print(f"读取INI配置失败: {e}")
    
    # 如果都不存在，返回默认配置
    return defaults 