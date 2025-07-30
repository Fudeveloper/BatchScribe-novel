import sys
import os
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("test_female_fantasy")

# 添加项目路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    # 导入模板模块
    from templates.prompts import NOVEL_TYPES, GENRE_SPECIFIC_PROMPTS, PROMPT_TEMPLATES
    
    # 测试女频玄幻是否在小说类型列表中
    logger.info("测试女频玄幻是否在小说类型列表中")
    if "女频玄幻" in NOVEL_TYPES["中文"]:
        logger.info("成功: 女频玄幻已添加到小说类型列表中")
    else:
        logger.error("失败: 女频玄幻未添加到小说类型列表中")
    
    # 测试女频玄幻是否有提示词定义
    logger.info("测试女频玄幻是否有提示词定义")
    if "女频玄幻" in GENRE_SPECIFIC_PROMPTS:
        logger.info("成功: 女频玄幻已添加到提示词定义中")
        logger.info(f"女频玄幻提示词: {GENRE_SPECIFIC_PROMPTS['女频玄幻'][:100]}...")
    else:
        logger.error("失败: 女频玄幻未添加到提示词定义中")
    
    # 测试女频玄幻是否有写作风格模板
    logger.info("测试女频玄幻是否有写作风格模板")
    if "女频玄幻" in PROMPT_TEMPLATES["中文"]:
        logger.info("成功: 女频玄幻已添加到写作风格模板中")
        logger.info(f"女频玄幻写作风格模板: {PROMPT_TEMPLATES['中文']['女频玄幻']}")
    else:
        logger.error("失败: 女频玄幻未添加到写作风格模板中")
    
    # 测试是否有玄幻小说情节示例
    logger.info("测试是否有女频玄幻小说情节示例")
    try:
        # 尝试不同的编码方式读取文件
        encodings = ['utf-8', 'gbk', 'utf-16', 'latin-1', 'cp936']
        content = None
        
        for encoding in encodings:
            try:
                with open("female_fantasy.txt", "r", encoding=encoding) as f:
                    content = f.read()
                    logger.info(f"成功使用 {encoding} 编码读取文件")
                    break
            except UnicodeDecodeError:
                continue
        
        if content:
            if "水云天司命殿的花神小兰花" in content:
                logger.info("成功: 女频玄幻小说情节示例已添加")
            else:
                logger.error("失败: 女频玄幻小说情节示例未添加")
        else:
            logger.error("无法读取female_fantasy.txt文件，尝试了多种编码都失败")
    except Exception as e:
        logger.error(f"读取female_fantasy.txt文件失败: {str(e)}")
    
    logger.info("测试完成")
    
except ImportError as e:
    logger.error(f"导入模块失败: {str(e)}")
except Exception as e:
    logger.error(f"测试过程中出现错误: {str(e)}")

if __name__ == "__main__":
    print("女频玄幻小说类型测试完成，请查看日志输出") 