"""
测试小说生成器bug修复

执行此脚本来验证修复是否成功。
"""

import os
import sys
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("test_bug_fix")

# 修复导入问题
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 尝试使用相对导入（作为模块导入时）或使用绝对导入（直接运行时）
try:
    from core.generator import NovelGenerator
    from templates.prompts import PROMPT_TEMPLATES, GENRE_SPECIFIC_PROMPTS, NOVEL_TYPES
    logger.info("成功导入模块（相对路径）")
except ImportError as e:
    try:
        # 尝试绝对导入
        from core.generator import NovelGenerator
        from templates.prompts import PROMPT_TEMPLATES, GENRE_SPECIFIC_PROMPTS, NOVEL_TYPES
        logger.info("成功导入模块（绝对路径）")
    except ImportError as e2:
        logger.error(f"导入错误: {e2}")
        logger.error("请确保在正确的目录中运行此脚本")
        sys.exit(1)

def test_prompt_generation():
    """测试提示词生成是否正常"""
    
    # 创建一个测试小说设置
    test_setup = {
        "genre": "童话重塑",  # 测试一个可能不存在的类型
        "language": "中文",
        "protagonist": {
            "name": "测试角色",
            "gender": "男",
            "age": "30",
            "traits": None,  # 测试None值
            "appearance": None,
        },
        "world_building": None,  # 测试None值
        "story_structure": {
            "plot": "测试情节"
        },
        "themes": None  # 测试None值
    }
    
    # 创建生成器实例
    generator = NovelGenerator(
        api_key="test_key",
        model="gpt-3.5-turbo",
        novel_type="奇幻冒险",  # 默认类型，但测试会使用setup中的类型
        status_callback=lambda msg: logger.info(f"状态: {msg}")
    )
    
    # 尝试生成提示词
    try:
        prompt = generator.get_prompt(test_setup)
        logger.info("成功生成提示词!")
        logger.info(f"提示词长度: {len(prompt)}")
        return True
    except Exception as e:
        logger.error(f"生成提示词出错: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False

def main():
    """运行测试"""
    logger.info("开始测试bug修复...")
    
    success = test_prompt_generation()
    
    if success:
        logger.info("测试通过! 问题已修复.")
    else:
        logger.error("测试失败! 问题未完全修复.")
    
if __name__ == "__main__":
    main() 