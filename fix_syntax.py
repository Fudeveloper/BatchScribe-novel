#!/usr/bin/env python
# 这个脚本用于修复core/generator.py中的语法错误

def fix_syntax_error():
    filepath = "core/generator.py"
    
    # 读取文件内容
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    # 检查并修复英文部分代码
    english_problematic_line = 938 - 1  # 0-indexed
    if "protagonist\\'s" in content[english_problematic_line]:
        print("修复英文部分第939行的f-string问题...")
        # 如果前一行没有定义act1_default变量，则添加
        if "act1_default" not in content[english_problematic_line-1]:
            content.insert(english_problematic_line, '                    act1_default = "Establish the protagonist\'s ordinary world, introduce main characters and settings"\n')
            # 替换问题行
            content[english_problematic_line + 1] = '                    base_prompt += f"Act 1: {structure.get(\'act1\', act1_default)}\\n"\n'
    
    # 检查并修复中文部分代码
    chinese_problematic_line = 784 - 1  # 0-indexed
    for i in range(chinese_problematic_line-5, chinese_problematic_line+5):
        if i < len(content) and "protagonist\\'s" in content[i]:
            print(f"修复中文部分第{i+1}行的f-string问题...")
            # 如果前一行没有定义act1_default变量，则添加
            if "act1_default" not in content[i-1]:
                content.insert(i, '                    act1_default = "Establish the protagonist\'s ordinary world, introduce main characters and settings"\n')
                # 替换问题行
                content[i + 1] = '                    base_prompt += f"Act 1: {structure.get(\'act1\', act1_default)}\\n"\n'
    
    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(content)
    
    print("语法错误已修复!")

if __name__ == "__main__":
    fix_syntax_error() 