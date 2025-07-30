import sys
import os
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("test_new_models")

# 添加项目路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    # 导入模板模块
    from templates.prompts import SUPPORTED_MODELS, MODEL_DESCRIPTIONS
    
    # 测试新模型是否在支持的模型列表中
    new_models = ["chatgpt-4o-latest", "gemini-2.5-pro-exp-03-25"]
    
    logger.info("测试新模型是否已添加到支持列表中")
    for model in new_models:
        if model in SUPPORTED_MODELS:
            logger.info(f"成功: 模型 {model} 已添加到SUPPORTED_MODELS列表中")
        else:
            logger.error(f"失败: 模型 {model} 未添加到SUPPORTED_MODELS列表中")
    
    # 测试新模型是否有描述
    logger.info("测试新模型是否有描述")
    for model in new_models:
        if model in MODEL_DESCRIPTIONS:
            logger.info(f"成功: 模型 {model} 已添加到MODEL_DESCRIPTIONS中")
            logger.info(f"模型描述: {MODEL_DESCRIPTIONS[model]}")
        else:
            logger.error(f"失败: 模型 {model} 未添加到MODEL_DESCRIPTIONS中")
    
    logger.info("测试完成")
    
except ImportError as e:
    logger.error(f"导入模块失败: {str(e)}")
except Exception as e:
    logger.error(f"测试过程中出现错误: {str(e)}")

if __name__ == "__main__":
    print("新模型测试完成，请查看日志输出") 