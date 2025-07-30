#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试媒体生成功能
"""

import os
import sys
import json

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from core.media_generator import MediaGenerator

def test_media_generation():
    """测试媒体生成功能"""
    
    # 测试用的API密钥（需要替换为实际的API密钥）
    api_key = "your_api_key_here"
    
    # 测试用的小说设置
    novel_setup = {
        "genre": "奇幻冒险",
        "title": "测试小说",
        "protagonist": {
            "name": "林逸",
            "gender": "男",
            "age": "青年"
        },
        "world_building": {
            "setting": "神秘的魔法世界，充满冒险和挑战"
        },
        "themes": ["友情", "成长", "冒险", "正义"]
    }
    
    # 创建媒体生成器
    def status_callback(message):
        print(f"[状态] {message}")
    
    media_generator = MediaGenerator(api_key, status_callback)
    
    print("开始测试媒体生成功能...")
    
    # 测试封面生成
    print("\n=== 测试封面生成 ===")
    cover_prompt = media_generator._generate_cover_prompt(novel_setup)
    print(f"生成的封面提示词: {cover_prompt}")
    
    # 测试音乐生成
    print("\n=== 测试音乐生成 ===")
    music_prompt = media_generator._generate_music_prompt(novel_setup)
    print(f"生成的音乐提示词: {music_prompt}")
    
    # 如果有有效的API密钥，可以测试实际的API调用
    if api_key != "your_api_key_here":
        print("\n=== 测试实际API调用 ===")
        
        # 测试生成1张封面
        print("测试生成封面...")
        image_ids = media_generator.generate_cover_images(novel_setup, 1)
        print(f"图片任务ID: {image_ids}")
        
        # 测试生成音乐
        print("测试生成音乐...")
        music_id = media_generator.generate_music(novel_setup)
        print(f"音乐任务ID: {music_id}")
        
        # 测试保存媒体信息
        output_dir = "test_output"
        os.makedirs(output_dir, exist_ok=True)
        
        # 模拟生成结果
        mock_image_results = [{
            "imageUrl": "https://example.com/image1.jpg",
            "id": "test_image_id",
            "prompt": cover_prompt
        }]
        
        mock_music_result = {
            "audio_url": "https://example.com/music.mp3",
            "title": "测试音乐",
            "id": "test_music_id",
            "gpt_description_prompt": music_prompt
        }
        
        media_generator.save_media_info(output_dir, novel_setup, mock_image_results, mock_music_result)
        print(f"媒体信息已保存到: {output_dir}/media_info.json")
    else:
        print("\n请设置有效的API密钥以测试实际的API调用功能")
    
    print("\n测试完成!")

if __name__ == "__main__":
    test_media_generation() 