"""
三千流小说生成器接口模块

此模块提供了将三千流生成器与主系统集成的接口函数，便于用户调用特定的生成功能。
"""

import os
import json
from typing import Dict, List, Optional, Union, Any

from core.sanqianliu_generator import SanQianLiuGenerator, create_sanqianliu_generator
from core.generator import NovelGenerator
from templates.prompts import (
    SANQIANLIU_EXPLOSION_POINTS,
    SANQIANLIU_CULTIVATION_SYSTEM,
    SANQIANLIU_MAGICAL_ITEMS,
    SANQIANLIU_SPECIAL_TRAITS,
    SANQIANLIU_CHAPTER_STRUCTURE
)

class SanQianLiuInterface:
    """三千流小说生成器接口类"""
    
    def __init__(self, api_key: str, model: str = "gemini-2.5-pro-exp-03-25"):
        """
        初始化三千流接口
        
        Args:
            api_key: API密钥
            model: 使用的模型名称
        """
        self.api_key = api_key
        self.model = model
        self.generator = None
        self.output_dir = "output/sanqianliu"
        self._ensure_output_dir()
        
    def _ensure_output_dir(self) -> None:
        """确保输出目录存在"""
        os.makedirs(self.output_dir, exist_ok=True)
        
    def initialize_generator(self, target_length: int = 5000000, explosion_interval: int = 5) -> None:
        """
        初始化三千流生成器
        
        Args:
            target_length: 目标字数
            explosion_interval: 爆点间隔章节数
        """
        self.generator = create_sanqianliu_generator(self.api_key, self.model)
        # 重新设置参数
        self.generator.target_length = target_length
        self.generator.explosion_interval = explosion_interval
        # 重新初始化计划
        self.generator.total_chapters = self.generator._calculate_total_chapters()
        self.generator.chapter_plan = self.generator._create_chapter_plan()
        print(f"已初始化三千流生成器，目标字数: {target_length}，爆点间隔: 每{explosion_interval}章")
        
    def generate_novel_outline(self) -> Dict:
        """生成小说大纲"""
        if not self.generator:
            self.initialize_generator()
            
        outline = {
            "书名": "三千流",
            "主角": "尤川",
            "总字数": self.generator.target_length,
            "总章节数": self.generator.total_chapters,
            "修炼体系": SANQIANLIU_CULTIVATION_SYSTEM,
            "法宝系统": SANQIANLIU_MAGICAL_ITEMS,
            "特殊体质与血脉": SANQIANLIU_SPECIAL_TRAITS,
            "章节结构": {}
        }
        
        # 添加详细章节结构
        current_chapter = 1
        for phase in SANQIANLIU_CHAPTER_STRUCTURE:
            phase_chapters = []
            for chapter_info in self.generator.chapter_plan:
                if chapter_info["phase"] == phase:
                    phase_chapters.append({
                        "章节号": chapter_info["chapter_number"],
                        "事件": chapter_info["event"],
                        "是否爆点章节": chapter_info["is_explosion_point"],
                        "爆点类型": chapter_info["explosion_type"] if chapter_info["is_explosion_point"] else None,
                        "修为境界": chapter_info["cultivation_progress"]
                    })
            outline["章节结构"][phase] = phase_chapters
            
        # 保存大纲到文件
        outline_path = os.path.join(self.output_dir, "novel_outline.json")
        with open(outline_path, "w", encoding="utf-8") as f:
            json.dump(outline, f, ensure_ascii=False, indent=2)
            
        print(f"小说大纲已生成并保存至 {outline_path}")
        return outline
    
    def generate_character_system(self) -> Dict:
        """生成小说角色体系"""
        if not self.generator:
            self.initialize_generator()
            
        # 基于当前章节规划创建对应的角色系统
        characters = {
            "主角": {
                "名称": "尤川",
                "身份": "被欺凌的家族庶子",
                "特质": "坚韧不拔，心思缜密，隐忍复仇",
                "体质": "流光体 - 天生契合《三千流》",
                "武器": "流光剑 - 随主角修为提升而成长的本命法器",
                "成长轨迹": [
                    {"阶段": "开篇引入", "境界": "凡体境·淬体期", "主要成就": "开始修炼《三千流》"},
                    {"阶段": "初步崛起", "境界": "后天境·引气期", "主要成就": "初次展露锋芒"},
                    {"阶段": "踏入修真界", "境界": "先天境·筑基期", "主要成就": "加入流云宗"},
                    {"阶段": "实力提升", "境界": "先天境·金丹期", "主要成就": "炼制第一件真正法宝"},
                    {"阶段": "仇敌浮现", "境界": "通玄境·化神期", "主要成就": "发现害母真凶"},
                    {"阶段": "最终决战", "境界": "流天境·真流期", "主要成就": "为母报仇"},
                    {"阶段": "新的征程", "境界": "流天境·道流期", "主要成就": "开创新的修真体系"}
                ]
            },
            "重要角色": self._generate_important_characters(),
            "敌对势力": self._generate_enemy_factions(),
            "盟友势力": self._generate_ally_factions()
        }
        
        # 保存角色系统到文件
        character_path = os.path.join(self.output_dir, "character_system.json")
        with open(character_path, "w", encoding="utf-8") as f:
            json.dump(characters, f, ensure_ascii=False, indent=2)
            
        print(f"角色体系已生成并保存至 {character_path}")
        return characters
    
    def _generate_important_characters(self) -> List[Dict]:
        """生成重要角色信息"""
        return [
            {
                "名称": "叶清雨",
                "身份": "流云宗天才弟子，女主角",
                "特质": "聪慧灵动，心地善良，武道天赋异禀",
                "体质": "太阴体 - 对月华有特殊亲和力",
                "武器": "月影扇 - 可攻可守的上品法宝",
                "与主角关系": "生死之交，后成为道侣"
            },
            {
                "名称": "老者李道玄",
                "身份": "隐世强者，《三千流》秘籍前任持有者",
                "特质": "深不可测，行事神秘，对主角有特殊期望",
                "体质": "普通体质，但修为通天",
                "武器": "无形剑气 - 不需外物，以气御剑",
                "与主角关系": "授业恩师，指引方向"
            },
            {
                "名称": "林晓风",
                "身份": "流云宗大师兄，剑道天才",
                "特质": "光明磊落，重情重义，剑术无双",
                "体质": "剑骨体 - 天生适合修剑道",
                "武器": "青锋剑 - 祖传宝剑，锋利无比",
                "与主角关系": "先敌后友，生死兄弟"
            },
            {
                "名称": "尤夫人（慕容雪）",
                "身份": "主角母亲，尤家庶妾",
                "特质": "温婉贤惠，蕙质兰心，隐藏实力",
                "体质": "普通体质",
                "武器": "无",
                "与主角关系": "血脉相连，是主角复仇的原因"
            },
            {
                "名称": "黑袍人",
                "身份": "神秘强者，身份成谜",
                "特质": "行踪不定，实力强大，目的不明",
                "体质": "不明",
                "武器": "不明",
                "与主角关系": "若即若离，时助时阻"
            }
        ]
    
    def _generate_enemy_factions(self) -> List[Dict]:
        """生成敌对势力信息"""
        return [
            {
                "势力名称": "尤家",
                "势力类型": "家族",
                "势力地位": "当地望族，有一定影响力",
                "核心人物": [
                    {"名称": "尤青山", "身份": "家主，主角伯父", "实力": "先天境·金丹期"},
                    {"名称": "尤天佑", "身份": "大少爷，主角堂兄", "实力": "后天境·练气期"},
                    {"名称": "尤老太爷", "身份": "前任家主，幕后操控者", "实力": "通玄境·化神期"}
                ],
                "与主角矛盾": "迫害主角母亲，欺凌主角，觊觎《三千流》秘籍"
            },
            {
                "势力名称": "万毒门",
                "势力类型": "邪派宗门",
                "势力地位": "修真界一流势力，以毒术闻名",
                "核心人物": [
                    {"名称": "墨千毒", "身份": "门主", "实力": "通玄境·大乘期"},
                    {"名称": "墨七", "身份": "少门主", "实力": "通玄境·合道期"},
                    {"名称": "百毒老人", "身份": "炼毒长老", "实力": "通玄境·返虚期"}
                ],
                "与主角矛盾": "觊觎《三千流》秘籍，与尤家勾结迫害主角母亲"
            },
            {
                "势力名称": "天机阁",
                "势力类型": "特殊势力，掌管天机",
                "势力地位": "超然势力，不参与纷争但影响巨大",
                "核心人物": [
                    {"名称": "天机子", "身份": "阁主", "实力": "流天境·御流期"},
                    {"名称": "白眉老者", "身份": "预言长老", "实力": "流天境·真流期"},
                    {"名称": "黑衣算命人", "身份": "执行者", "实力": "通玄境·渡劫期"}
                ],
                "与主角矛盾": "预言主角将扰乱天道平衡，欲阻止其崛起"
            }
        ]
    
    def _generate_ally_factions(self) -> List[Dict]:
        """生成盟友势力信息"""
        return [
            {
                "势力名称": "流云宗",
                "势力类型": "正派宗门",
                "势力地位": "修真界顶级势力之一，底蕴深厚",
                "核心人物": [
                    {"名称": "流云子", "身份": "宗主", "实力": "流天境·合流期"},
                    {"名称": "叶长老", "身份": "执法长老，叶清雨之父", "实力": "通玄境·渡劫期"},
                    {"名称": "剑痴老人", "身份": "剑道长老", "实力": "通玄境·大乘期"}
                ],
                "与主角关系": "主角加入的宗门，提供修炼资源和庇护"
            },
            {
                "势力名称": "百草谷",
                "势力类型": "中立势力，以医术和炼丹著称",
                "势力地位": "二流势力，但因医术精湛受人尊敬",
                "核心人物": [
                    {"名称": "谷主药老", "身份": "谷主，炼丹大师", "实力": "通玄境·合道期"},
                    {"名称": "小药童", "身份": "天才炼丹师", "实力": "先天境·元丹期"},
                    {"名称": "采药长老", "身份": "负责收集珍稀药材", "实力": "通玄境·化神期"}
                ],
                "与主角关系": "主角曾救谷主药老，结为盟友，提供丹药支持"
            },
            {
                "势力名称": "流浪剑客联盟",
                "势力类型": "松散联盟，由各方剑修组成",
                "势力地位": "人数众多但缺乏统一领导，整体实力不俗",
                "核心人物": [
                    {"名称": "断剑老人", "身份": "联盟精神领袖", "实力": "通玄境·返虚期"},
                    {"名称": "林晓风", "身份": "年轻一代领军人物", "实力": "通玄境·化神期"},
                    {"名称": "醉剑仙", "身份": "神秘剑客，行踪不定", "实力": "通玄境·大乘期"}
                ],
                "与主角关系": "主角在危机时刻救过多位剑客，结为生死之交"
            }
        ]
    
    def generate_chapter(self, chapter_number: int) -> str:
        """
        生成特定章节
        
        Args:
            chapter_number: 章节号
            
        Returns:
            生成的章节内容
        """
        if not self.generator:
            self.initialize_generator()
            
        if chapter_number < 1 or chapter_number > self.generator.total_chapters:
            raise ValueError(f"章节号 {chapter_number} 超出范围 (1-{self.generator.total_chapters})")
            
        # 生成章节提示词
        prompt = self.generator.generate_chapter_prompt(chapter_number)
        
        # 使用基础生成器生成内容
        chapter_content = self.generator.base_generator.generate_content(
            prompt=prompt,
            temperature=0.75
        )
        
        # 保存章节到文件
        chapter_filename = f"第{chapter_number}章.txt"
        chapter_path = os.path.join(self.output_dir, chapter_filename)
        
        with open(chapter_path, "w", encoding="utf-8") as f:
            f.write(chapter_content)
            
        print(f"章节已生成并保存至 {chapter_path}")
        return chapter_content
        
    def generate_novel_batch(self, start_chapter: int = 1, num_chapters: int = 10) -> None:
        """
        批量生成小说章节
        
        Args:
            start_chapter: 起始章节号
            num_chapters: 要生成的章节数量
        """
        if not self.generator:
            self.initialize_generator()
            
        end_chapter = min(start_chapter + num_chapters - 1, self.generator.total_chapters)
        
        print(f"开始生成第 {start_chapter} 至 {end_chapter} 章...")
        
        for chapter_num in range(start_chapter, end_chapter + 1):
            print(f"正在生成第 {chapter_num} 章...")
            self.generate_chapter(chapter_num)
            
        print(f"批量生成完成，共生成 {end_chapter - start_chapter + 1} 章")
    
    def generate_cultivation_chart(self) -> None:
        """生成修炼境界图表"""
        if not self.generator:
            self.initialize_generator()
            
        chart_data = {
            "境界体系": SANQIANLIU_CULTIVATION_SYSTEM,
            "主角修炼路线": []
        }
        
        # 主角修炼路线
        phases = list(SANQIANLIU_CHAPTER_STRUCTURE.keys())
        for phase_idx, phase in enumerate(phases):
            # 每个阶段取中间的章节作为代表
            phase_chapters = [c for c in self.generator.chapter_plan if c["phase"] == phase]
            if phase_chapters:
                mid_chapter = phase_chapters[len(phase_chapters) // 2]
                chart_data["主角修炼路线"].append({
                    "阶段": phase,
                    "章节": mid_chapter["chapter_number"],
                    "境界": mid_chapter["cultivation_progress"]
                })
                
        # 保存到文件
        chart_path = os.path.join(self.output_dir, "cultivation_chart.json")
        with open(chart_path, "w", encoding="utf-8") as f:
            json.dump(chart_data, f, ensure_ascii=False, indent=2)
            
        print(f"修炼境界图表已生成并保存至 {chart_path}")
    
    def export_story_summary(self) -> str:
        """
        导出小说概要
        
        Returns:
            概要文本
        """
        if not self.generator:
            self.initialize_generator()
            
        summary = f"""《三千流》小说概要

【基本信息】
书名：三千流
主角：尤川
类型：玄幻武侠修仙小说
预计字数：{self.generator.target_length//10000}0万字
预计章节数：{self.generator.total_chapters}章

【核心故事】
主角尤川从小体弱多病，在家族中备受欺凌，因母亲是妾室而地位低下。在目睹家族谋害其母亲后，尤川性格大变，为苟活而隐忍承担家族事务，暗中修炼《三千流》秘籍。《三千流》是一本包含各类武功和法宝炼制方法的神秘功法，主角通过逐步领悟其中奥秘，不断突破自身极限，为母报仇，最终登临修真界巅峰。

【修炼体系】
《三千流》设定了五大境界：凡体境、后天境、先天境、通玄境和流天境，每个境界又分为五个小阶段。修炼者需要逐步突破这些境界，最终达到道流期，近乎长生不老。

【故事亮点】
1. 复仇主线：主角为母报仇的坚定信念贯穿全文
2. 修炼成长：详细描绘修炼过程，展现主角实力逐步提升
3. 人物塑造：重要角色性格鲜明，各具特色
4. 爆点设计：每隔{self.generator.explosion_interval}章安排一个重要爆点，保持读者新鲜感
5. 法宝系统：精心设计的法器、法宝、灵宝、神器体系，丰富世界观
6. 特殊体质：多种体质和血脉设定，增加故事可能性

【主要阶段】
"""
        
        # 添加各阶段简介
        for phase in SANQIANLIU_CHAPTER_STRUCTURE:
            events = SANQIANLIU_CHAPTER_STRUCTURE[phase]
            summary += f"\n{phase}：" + "、".join(events)
            
        # 保存到文件
        summary_path = os.path.join(self.output_dir, "story_summary.txt")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)
            
        print(f"小说概要已生成并保存至 {summary_path}")
        return summary


def get_interface(api_key: str, model: str = "gemini-2.5-pro-exp-03-25") -> SanQianLiuInterface:
    """获取三千流接口实例"""
    return SanQianLiuInterface(api_key, model) 