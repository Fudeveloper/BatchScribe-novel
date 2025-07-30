#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AI小说生成器 - 媒体生成功能简化演示
"""

import os
import sys
import json
import time

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def demo_media_generation():
    """演示媒体生成功能"""
    
    print("🎨 AI小说生成器 - 媒体生成功能演示")
    print("=" * 50)
    
    # 模拟小说设置
    novel_setup = {
        "genre": "奇幻冒险",
        "title": "魔法世界的冒险",
        "protagonist": {
            "name": "林逸",
            "gender": "男",
            "age": "青年",
            "background": "来自普通世界的少年，意外获得魔法力量"
        },
        "world_building": {
            "setting": "一个充满魔法和神秘生物的奇幻世界",
            "time_period": "中世纪奇幻时代",
            "location": "艾泽拉斯大陆"
        },
        "themes": ["友情", "成长", "冒险", "正义", "勇气"]
    }
    
    print("📋 小说设置:")
    print(json.dumps(novel_setup, ensure_ascii=False, indent=2))
    
    print("\n" + "=" * 50)
    
    # 演示封面提示词生成
    print("🖼️  封面提示词生成演示:")
    cover_prompt = generate_cover_prompt(novel_setup)
    print(f"生成的封面提示词: {cover_prompt}")
    
    print("\n" + "-" * 30)
    
    # 演示音乐提示词生成
    print("🎵 音乐提示词生成演示:")
    music_prompt = generate_music_prompt(novel_setup)
    print(f"生成的音乐提示词: {music_prompt}")
    
    print("\n" + "=" * 50)
    
    # 创建输出目录并保存演示结果
    output_dir = f"demo_output_{int(time.time())}"
    os.makedirs(output_dir, exist_ok=True)
    
    # 模拟生成结果
    mock_image_results = [
        {
            "index": 1,
            "url": "https://example.com/cover_1.jpg",
            "task_id": "demo_image_1",
            "prompt": cover_prompt
        },
        {
            "index": 2,
            "url": "https://example.com/cover_2.jpg",
            "task_id": "demo_image_2",
            "prompt": cover_prompt
        }
    ]
    
    mock_music_result = {
        "url": "https://example.com/theme_music.mp3",
        "title": "魔法世界的冒险 - 主题音乐",
        "task_id": "demo_music_1",
        "prompt": music_prompt
    }
    
    # 保存媒体信息
    media_info = {
        "novel_info": {
            "title": novel_setup.get("title", ""),
            "genre": novel_setup.get("genre", ""),
            "protagonist": novel_setup.get("protagonist", {})
        },
        "cover_images": mock_image_results,
        "music": mock_music_result,
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # 保存到JSON文件
    media_file = os.path.join(output_dir, "media_info.json")
    with open(media_file, 'w', encoding='utf-8') as f:
        json.dump(media_info, f, ensure_ascii=False, indent=2)
    
    print(f"💾 媒体信息已保存到: {media_file}")
    
    # 显示媒体信息内容
    print(f"\n📋 媒体信息内容:")
    print(json.dumps(media_info, ensure_ascii=False, indent=2))
    
    print("\n" + "=" * 50)
    print("🎉 演示完成！")
    print(f"📁 输出目录: {os.path.abspath(output_dir)}")

def generate_cover_prompt(novel_setup):
    """根据小说设置生成封面提示词"""
    genre = novel_setup.get("genre", "奇幻冒险")
    protagonist = novel_setup.get("protagonist", {})
    world_building = novel_setup.get("world_building", {})
    
    # 基础提示词
    prompt_parts = []
    
    # 添加类型相关的风格
    genre_styles = {
        "奇幻冒险": "fantasy adventure, magical world, epic landscape",
        "都市言情": "modern city, romantic atmosphere, urban lifestyle",
        "玄幻修真": "cultivation, immortal world, mystical mountains",
        "科幻未来": "futuristic, sci-fi technology, space age",
        "悬疑推理": "mystery, dark atmosphere, detective theme",
        "历史穿越": "historical, time travel, ancient architecture",
        "武侠江湖": "martial arts, ancient China, warriors",
        "恐怖灵异": "horror, supernatural, dark gothic",
        "军事战争": "military, war scene, battlefield",
        "商业职场": "business, office, professional"
    }
    
    style = genre_styles.get(genre, "fantasy adventure")
    prompt_parts.append(style)
    
    # 添加主角信息
    if protagonist.get("name"):
        gender = protagonist.get("gender", "男")
        age = protagonist.get("age", "青年")
        
        gender_desc = "handsome young man" if gender == "男" else "beautiful young woman"
        prompt_parts.append(f"{gender_desc}, {age}")
    
    # 添加世界设定
    if world_building.get("setting"):
        setting = world_building["setting"]
        prompt_parts.append(f"background: {setting}")
    
    # 添加艺术风格
    prompt_parts.extend([
        "book cover design",
        "high quality",
        "detailed illustration",
        "cinematic lighting",
        "4K resolution"
    ])
    
    return ", ".join(prompt_parts)

def generate_music_prompt(novel_setup):
    """根据小说设置生成音乐提示词"""
    genre = novel_setup.get("genre", "奇幻冒险")
    themes = novel_setup.get("themes", [])
    
    # 基础音乐风格映射
    music_styles = {
        "奇幻冒险": "Epic fantasy orchestral music with adventure themes, magical atmosphere",
        "都市言情": "Romantic modern pop music, soft and emotional, urban vibes",
        "玄幻修真": "Traditional Chinese instruments mixed with epic orchestral, mystical and powerful",
        "科幻未来": "Electronic synthwave music, futuristic sounds, space ambient",
        "悬疑推理": "Dark mysterious music, tension building, detective thriller soundtrack",
        "历史穿越": "Classical orchestral with historical instruments, time travel themes",
        "武侠江湖": "Traditional Chinese martial arts music, heroic and powerful",
        "恐怖灵异": "Horror ambient music, dark and scary, supernatural themes",
        "军事战争": "Military march music, heroic and powerful, war themes",
        "商业职场": "Modern corporate music, motivational and professional"
    }
    
    base_style = music_styles.get(genre, "Epic orchestral music")
    
    # 添加主题相关的音乐元素
    if themes:
        theme_keywords = []
        for theme in themes:
            if "爱情" in theme:
                theme_keywords.append("romantic")
            elif "友情" in theme:
                theme_keywords.append("friendship")
            elif "成长" in theme:
                theme_keywords.append("inspiring")
            elif "冒险" in theme:
                theme_keywords.append("adventurous")
            elif "正义" in theme:
                theme_keywords.append("heroic")
        
        if theme_keywords:
            base_style += f", {', '.join(theme_keywords)} themes"
    
    return base_style

def show_api_examples():
    """显示API调用示例"""
    print("\n🔧 API调用示例:")
    print("=" * 30)
    
    print("\n📸 MidJourney API (封面生成):")
    print("```python")
    print("# 提交图片生成任务")
    print("POST /mj/submit/imagine")
    print("{")
    print('    "base64Array": [],')
    print('    "notifyHook": "",')
    print('    "prompt": "fantasy adventure, magical world, epic landscape",')
    print('    "state": "",')
    print('    "botType": "MID_JOURNEY"')
    print("}")
    print("```")
    
    print("\n🎵 Suno API (音乐生成):")
    print("```python")
    print("# 提交音乐生成任务")
    print("POST /suno/submit/music")
    print("{")
    print('    "gpt_description_prompt": "Epic fantasy orchestral music",')
    print('    "make_instrumental": false,')
    print('    "mv": "chirp-v4",')
    print('    "prompt": "Fantasy Adventure Theme"')
    print("}")
    print("```")

def show_feature_overview():
    """显示功能概览"""
    print("\n📖 媒体生成功能概览:")
    print("=" * 30)
    
    features = [
        ("🖼️  封面生成", "根据小说类型和内容自动生成封面图片"),
        ("🎵 音乐生成", "为小说创作配套的主题音乐"),
        ("🎨 智能提示词", "基于小说元素自动生成高质量提示词"),
        ("📊 多种类型", "支持奇幻、都市、科幻等多种小说类型"),
        ("⚙️  灵活配置", "可自定义封面数量和生成选项"),
        ("💾 完整保存", "自动保存媒体文件信息和下载链接")
    ]
    
    for title, desc in features:
        print(f"{title}: {desc}")
    
    print("\n🔧 支持的API服务:")
    print("  • MidJourney API - 高质量图片生成")
    print("  • Suno API - 专业音乐创作")
    
    print("\n📋 支持的小说类型:")
    types = [
        "奇幻冒险", "都市言情", "玄幻修真", "科幻未来",
        "悬疑推理", "历史穿越", "武侠江湖", "恐怖灵异"
    ]
    for i, novel_type in enumerate(types, 1):
        print(f"  {i}. {novel_type}")

if __name__ == "__main__":
    show_feature_overview()
    print("\n" + "=" * 50)
    demo_media_generation()
    show_api_examples() 