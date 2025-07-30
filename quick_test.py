"""
小说生成器bug修复快速测试
"""

# 模拟问题场景，测试修复是否有效

def safe_replace(text, placeholder, value):
    """
    模拟_safe_replace方法
    """
    try:
        if text is None:
            return ""
            
        if placeholder not in text:
            return text
            
        if value is None:
            str_value = ""
        elif isinstance(value, (list, tuple)):
            try:
                str_value = "、".join([str(item) for item in value if item is not None])
            except:
                str_value = str(value)
        else:
            str_value = str(value)
        
        return text.replace(placeholder, str_value)
    except Exception as e:
        print(f"替换文本时出错: {e}")
        return text if text is not None else ""

def get_prompt_fixed(novel_setup, current_text=""):
    """
    模拟已修复的get_prompt方法
    """
    # 初始化base_prompt为空字符串，确保它不会是None
    base_prompt = ""
    
    # 根据小说类型获取模板
    novel_type = novel_setup.get("genre", "奇幻冒险")
    
    # 这里模拟GENRE_SPECIFIC_PROMPTS字典
    # 故意不包含"童话重塑"类型
    genre_prompts = {
        "奇幻冒险": "这是一个[PROTAGONIST_NAME]的奇幻故事",
        "科幻未来": "这是一个[PROTAGONIST_NAME]的科幻故事"
    }
    
    # 尝试获取提示词模板
    if novel_type in genre_prompts:
        base_prompt = genre_prompts[novel_type]
    else:
        # 模板不存在，设置为None以模拟bug
        base_prompt = None
    
    # 模拟修复 - 检查base_prompt是否为None
    if base_prompt is None:
        base_prompt = ""
        print(f"警告：无法找到适用于 {novel_type} 类型的提示词模板，使用空模板")
    
    # 替换变量
    if "protagonist" in novel_setup and novel_setup["protagonist"]:
        protagonist = novel_setup["protagonist"]
        base_prompt = safe_replace(base_prompt, "[PROTAGONIST_NAME]", protagonist.get("name"))
    
    # 添加语言指导
    base_prompt += "\n\n请用中文创作。"
    
    return base_prompt

def get_prompt_buggy(novel_setup, current_text=""):
    """
    模拟原有bug的get_prompt方法
    """
    # 根据小说类型获取模板
    novel_type = novel_setup.get("genre", "奇幻冒险")
    
    # 这里模拟GENRE_SPECIFIC_PROMPTS字典
    # 故意不包含"童话重塑"类型
    genre_prompts = {
        "奇幻冒险": "这是一个[PROTAGONIST_NAME]的奇幻故事",
        "科幻未来": "这是一个[PROTAGONIST_NAME]的科幻故事"
    }
    
    # 尝试获取提示词模板
    if novel_type in genre_prompts:
        base_prompt = genre_prompts[novel_type]
    else:
        # 模板不存在，设置为None以模拟bug
        base_prompt = None
    
    # 不检查None值，直接使用 (这会导致bug)
    
    # 替换变量
    if "protagonist" in novel_setup and novel_setup["protagonist"]:
        protagonist = novel_setup["protagonist"]
        base_prompt = safe_replace(base_prompt, "[PROTAGONIST_NAME]", protagonist.get("name"))
    
    # 添加语言指导 - 这里会出错，如果base_prompt是None
    base_prompt += "\n\n请用中文创作。"
    
    return base_prompt

def test_fixes():
    """
    测试修复前后的区别
    """
    print("===== 测试bug修复效果 =====")
    
    # 创建一个测试小说设置
    test_setup = {
        "genre": "童话重塑",  # 测试不存在的类型
        "language": "中文",
        "protagonist": {
            "name": "测试角色",
        },
    }
    
    # 测试修复后的版本
    print("\n测试修复后的版本:")
    try:
        prompt = get_prompt_fixed(test_setup)
        print(f"成功生成提示词: '{prompt}'")
        print("测试通过!")
    except Exception as e:
        print(f"修复后的版本仍然出错: {e}")
        print("测试失败!")
    
    # 测试有bug的版本
    print("\n测试原始有bug的版本:")
    try:
        prompt = get_prompt_buggy(test_setup)
        print(f"成功生成提示词: '{prompt}'")
        print("应该会出错但没有，请检查模拟bug是否正确!")
    except Exception as e:
        print(f"如预期一样出错: {e}")
        print("测试符合预期，证明修复有效!")

if __name__ == "__main__":
    test_fixes() 