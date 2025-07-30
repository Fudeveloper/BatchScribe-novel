#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试空行优化功能
验证新的内容合并和清理逻辑是否正常工作
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.generator import NovelGenerator

def test_content_cleaning():
    """测试内容清理功能"""
    print("=== 测试内容清理功能 ===")
    
    # 创建生成器实例
    generator = NovelGenerator(
        api_key="test_key",
        model="gpt-4.5-preview",
        status_callback=lambda msg: print(f"状态: {msg}")
    )
    
    # 测试用例1：多个连续空行
    test_content1 = """这是第一段内容。



这是第二段内容。




这是第三段内容。"""
    
    cleaned1 = generator._clean_content(test_content1)
    print("原始内容1:")
    print(repr(test_content1))
    print("清理后内容1:")
    print(repr(cleaned1))
    print(f"空行数量减少: {test_content1.count(chr(10)+chr(10))} -> {cleaned1.count(chr(10)+chr(10))}")
    
    # 测试用例2：带标记的内容
    test_content2 = """继续创作：这是故事的继续部分。

这里是正常的段落。


注意：这是一个标记行

这里应该被保留。"""
    
    cleaned2 = generator._clean_content(test_content2)
    print("\n原始内容2:")
    print(repr(test_content2))
    print("清理后内容2:")
    print(repr(cleaned2))
    
    return cleaned1, cleaned2

def test_smart_join():
    """测试智能合并功能"""
    print("\n=== 测试智能合并功能 ===")
    
    generator = NovelGenerator(
        api_key="test_key",
        model="gpt-4.5-preview",
        status_callback=lambda msg: print(f"状态: {msg}")
    )
    
    # 测试用例1：正常段落合并
    existing1 = "这是现有的内容。\n\n这是第二段。"
    new1 = "这是新生成的内容。\n\n这是新的第二段。"
    
    result1 = generator._smart_join_content(existing1, new1)
    print("现有内容1:", repr(existing1))
    print("新内容1:", repr(new1))
    print("合并结果1:", repr(result1))
    
    # 测试用例2：带引号的对话
    existing2 = "林逸看着远方，心中充满了决心。"
    new2 = '"我一定要变得更强！"他握紧了拳头。'
    
    result2 = generator._smart_join_content(existing2, new2)
    print("\n现有内容2:", repr(existing2))
    print("新内容2:", repr(new2))
    print("合并结果2:", repr(result2))
    
    # 测试用例3：空内容处理
    existing3 = ""
    new3 = "这是全新的内容。"
    
    result3 = generator._smart_join_content(existing3, new3)
    print("\n现有内容3:", repr(existing3))
    print("新内容3:", repr(new3))
    print("合并结果3:", repr(result3))
    
    return result1, result2, result3

def test_full_pipeline():
    """测试完整的清理和合并流程"""
    print("\n=== 测试完整流程 ===")
    
    generator = NovelGenerator(
        api_key="test_key",
        model="gpt-4.5-preview",
        status_callback=lambda msg: print(f"状态: {msg}")
    )
    
    # 模拟多次生成内容的过程
    existing_content = "林逸站在山峰之上，望着远方的云海。"
    
    # 第一次生成的内容（带多余空行）
    new_content1 = """


"这就是修真者的世界吗？"他喃喃自语。



突然，一道剑光从天而降。"""
    
    # 第二次生成的内容
    new_content2 = """


林逸迅速闪避，剑光擦身而过。

"什么人？"他警惕地环顾四周。"""
    
    # 逐步合并
    step1 = generator._clean_content(new_content1)
    result1 = generator._smart_join_content(existing_content, step1)
    print("第一次合并后:", repr(result1))
    
    step2 = generator._clean_content(new_content2)
    result2 = generator._smart_join_content(result1, step2)
    print("第二次合并后:", repr(result2))
    
    # 统计空行数量
    double_newlines = result2.count('\n\n')
    triple_newlines = result2.count('\n\n\n')
    
    print("\n最终内容:")
    print(result2)
    print(f"\n双空行数量: {double_newlines}")
    print(f"三空行数量: {triple_newlines}")
    
    return result2

if __name__ == "__main__":
    print("开始测试空行优化功能...")
    
    # 运行测试
    try:
        test_content_cleaning()
        test_smart_join()
        final_result = test_full_pipeline()
        
        print("\n=== 测试总结 ===")
        print("✅ 内容清理功能测试完成")
        print("✅ 智能合并功能测试完成") 
        print("✅ 完整流程测试完成")
        
        # 检查是否还有过多空行
        if final_result.count('\n\n\n') == 0:
            print("✅ 空行优化成功：没有发现三个或更多连续空行")
        else:
            print(f"⚠️  仍有过多空行：发现 {final_result.count(chr(10)+chr(10)+chr(10))} 处三空行")
            
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc() 