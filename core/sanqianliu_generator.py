"""
三千流小说生成器模块 - 专为500万字玄幻武侠修仙小说优化

此模块包含针对"三千流"类型小说的专用生成逻辑，包括：
1. 爆点控制系统 - 确保每隔一定章节出现吸引人的爆点内容
2. 长篇章节规划 - 管理500万字的长篇结构
3. 修真体系设计 - 提供一致的修真境界和法宝系统
4. 人物关系网络 - 设计复杂的人物关系和势力分布
"""

import os
import random
import json
import time
from typing import Dict, List, Tuple, Optional, Any, Union

from templates.prompts import (
    SANQIANLIU_EXPLOSION_POINTS,
    SANQIANLIU_CULTIVATION_SYSTEM,
    SANQIANLIU_MAGICAL_ITEMS, 
    SANQIANLIU_SPECIAL_TRAITS,
    SANQIANLIU_CHAPTER_STRUCTURE
)

from core.generator import NovelGenerator
from core.import import GENRE_PROMPTS

class SanQianLiuGenerator:
    """三千流小说专用生成器类"""
    
    def __init__(self, 
                 base_generator: NovelGenerator,
                 target_length: int = 5000000,
                 explosion_interval: int = 5):
        """
        初始化三千流小说生成器
        
        Args:
            base_generator: 基础小说生成器实例
            target_length: 目标字数，默认500万字
            explosion_interval: 爆点间隔章节数，默认每5章
        """
        self.base_generator = base_generator
        self.target_length = target_length
        self.explosion_interval = explosion_interval
        self.current_chapter = 0
        self.total_chapters = self._calculate_total_chapters()
        self.protagonist = {"name": "尤川", "current_level": "淬体期"}
        self.story_phase = "开篇引入"
        self.explosion_points_used = []
        self.chapter_plan = self._create_chapter_plan()
        
    def _calculate_total_chapters(self) -> int:
        """计算总章节数"""
        # 假设平均每章1万字
        return self.target_length // 10000
    
    def _create_chapter_plan(self) -> List[Dict]:
        """创建整体章节规划"""
        # 将500万字分为7个主要阶段
        phases = list(SANQIANLIU_CHAPTER_STRUCTURE.keys())
        phase_chapters = self._distribute_chapters(phases)
        
        chapter_plan = []
        current_chapter = 1
        
        for phase_idx, phase in enumerate(phases):
            phase_length = phase_chapters[phase_idx]
            phase_events = SANQIANLIU_CHAPTER_STRUCTURE[phase]
            
            # 将每个阶段进一步细分为多个事件
            event_chapters = self._distribute_chapters(phase_events, total=phase_length)
            
            for event_idx, event in enumerate(phase_events):
                event_length = event_chapters[event_idx]
                
                # 为每个事件创建具体章节
                for i in range(event_length):
                    # 判断是否应该在本章安排爆点
                    is_explosion_point = (current_chapter % self.explosion_interval == 0)
                    explosion_type = None
                    explosion_content = None
                    
                    if is_explosion_point:
                        explosion_type, explosion_content = self._select_explosion_point()
                    
                    chapter = {
                        "chapter_number": current_chapter,
                        "phase": phase,
                        "event": event,
                        "is_explosion_point": is_explosion_point,
                        "explosion_type": explosion_type,
                        "explosion_content": explosion_content,
                        "cultivation_progress": self._calculate_cultivation_progress(current_chapter)
                    }
                    
                    chapter_plan.append(chapter)
                    current_chapter += 1
        
        return chapter_plan
    
    def _distribute_chapters(self, items: List[str], total: Optional[int] = None) -> List[int]:
        """将章节数量分配给多个项目"""
        if total is None:
            total = self.total_chapters
            
        # 先给每个项目分配一个基础数量
        base_amount = total // len(items)
        distribution = [base_amount] * len(items)
        
        # 分配剩余的章节
        remaining = total - (base_amount * len(items))
        
        # 为重要的前期和后期阶段多分配一些章节
        importance_weights = []
        for i in range(len(items)):
            # 给开头和结尾的项目分配更高的权重
            if i == 0 or i == len(items) - 1:
                importance_weights.append(3)
            # 给第二个和倒数第二个项目分配次高的权重
            elif i == 1 or i == len(items) - 2:
                importance_weights.append(2)
            else:
                importance_weights.append(1)
        
        # 根据权重分配剩余章节
        total_weight = sum(importance_weights)
        for i in range(len(items)):
            item_share = int((importance_weights[i] / total_weight) * remaining)
            distribution[i] += item_share
        
        # 处理由于四舍五入导致的微小差异
        current_sum = sum(distribution)
        if current_sum < total:
            distribution[-1] += (total - current_sum)
        
        return distribution
    
    def _select_explosion_point(self) -> Tuple[str, str]:
        """选择一个爆点类型和内容"""
        # 获取所有可用的爆点类型
        available_types = list(SANQIANLIU_EXPLOSION_POINTS.keys())
        
        # 如果当前阶段有特定的爆点类型偏好，给予更高权重
        phase_preferences = {
            "开篇引入": ["奇遇机缘"],
            "初步崛起": ["修为突破", "奇遇机缘"],
            "踏入修真界": ["身份揭露", "击败强敌"],
            "实力提升": ["修为突破", "奇遇机缘"],
            "仇敌浮现": ["身份揭露", "击败强敌"],
            "最终决战": ["强势复仇", "修为突破"],
            "新的征程": ["修为突破", "奇遇机缘"]
        }
        
        weights = []
        for explosion_type in available_types:
            # 基础权重
            weight = 1
            
            # 如果是当前阶段的偏好类型，增加权重
            if explosion_type in phase_preferences.get(self.story_phase, []):
                weight += 2
                
            # 如果最近已经使用过，降低权重
            if explosion_type in self.explosion_points_used[-3:]:
                weight -= 0.5
                
            weights.append(max(0.1, weight))  # 确保权重至少为0.1
            
        # 按权重随机选择爆点类型
        selected_type = random.choices(available_types, weights=weights, k=1)[0]
        
        # 从选定类型中随机选择一个具体爆点内容
        available_contents = SANQIANLIU_EXPLOSION_POINTS[selected_type]
        selected_content = random.choice(available_contents)
        
        # 记录使用过的爆点类型
        self.explosion_points_used.append(selected_type)
        
        return selected_type, selected_content
    
    def _calculate_cultivation_progress(self, chapter_number: int) -> str:
        """根据章节号计算修炼进度"""
        # 将境界扁平化处理
        all_levels = []
        for realm, levels in SANQIANLIU_CULTIVATION_SYSTEM.items():
            for level in levels:
                level_name = level.split(' - ')[0]
                all_levels.append(level_name)
                
        # 确定当前应该在哪个境界
        total_levels = len(all_levels)
        progress_ratio = chapter_number / self.total_chapters
        
        # 在最终决战前必须达到较高境界
        if progress_ratio > 0.8:
            level_index = int(total_levels * 0.9)
        elif progress_ratio > 0.6:
            level_index = int(total_levels * 0.7)
        else:
            # 前期进展较慢，中期加快
            if progress_ratio < 0.3:
                adjusted_ratio = progress_ratio * 0.5
            else:
                adjusted_ratio = 0.15 + (progress_ratio - 0.3) * 0.85
                
            level_index = int(adjusted_ratio * total_levels)
        
        # 确保索引在有效范围内
        level_index = max(0, min(level_index, total_levels - 1))
        
        return all_levels[level_index]
    
    def generate_chapter_prompt(self, chapter_number: int) -> str:
        """生成特定章节的提示词"""
        if chapter_number > len(self.chapter_plan):
            raise ValueError(f"章节号 {chapter_number} 超出了计划章节范围")
            
        chapter_info = self.chapter_plan[chapter_number - 1]
        self.current_chapter = chapter_number
        self.story_phase = chapter_info["phase"]
        self.protagonist["current_level"] = chapter_info["cultivation_progress"]
        
        # 构建核心提示词
        prompt = f"""
请创作《三千流》小说的第{chapter_number}章，这是一部500万字的玄幻武侠修仙爽文。

当前故事阶段: {chapter_info['phase']}
当前事件重点: {chapter_info['event']}
主角修为境界: {chapter_info['cultivation_progress']}

章节要求:
1. 字数控制在8000-12000字之间
2. 语言风格苍劲有力，富有古风韵味
3. 保持情节连贯，与前面章节保持一致性
"""

        # 如果是爆点章节，添加爆点要求
        if chapter_info["is_explosion_point"]:
            prompt += f"""
本章是重要爆点章节，需要包含以下类型的爆点情节:
爆点类型: {chapter_info["explosion_type"]}
具体内容: {chapter_info["explosion_content"]}

爆点应该是章节的高潮部分，要细致描写，渲染气氛，建立张力，让读者感受到强烈的代入感和爽感。
"""
        
        # 添加修真体系相关内容
        current_level = chapter_info["cultivation_progress"]
        for realm, levels in SANQIANLIU_CULTIVATION_SYSTEM.items():
            for level in levels:
                if current_level in level:
                    prompt += f"""
当前修真境界: {realm} - {level}
"""
                    break
        
        # 添加故事背景提示
        prompt += """
故事背景:
主角尤川从小体弱多病，在家族中备受欺凌，因母亲是妾室而地位低下。在目睹家族谋害其母亲后，尤川性格大变，为苟活而隐忍承担家族事务，暗中修炼《三千流》秘籍。《三千流》是一本包含各类武功和法宝炼制方法的神秘功法，主角通过逐步领悟其中奥秘，不断突破自身极限，为母报仇，最终登临修真界巅峰。
"""
        
        return prompt
    
    def generate_novel(self, start_chapter: int = 1, end_chapter: Optional[int] = None) -> Dict:
        """生成指定范围的章节"""
        if end_chapter is None:
            end_chapter = len(self.chapter_plan)
            
        novel_content = {}
        
        for chapter_num in range(start_chapter, end_chapter + 1):
            chapter_prompt = self.generate_chapter_prompt(chapter_num)
            
            # 使用基础生成器生成内容
            chapter_content = self.base_generator.generate_content(
                prompt=chapter_prompt,
                temperature=0.75,  # 稍微降低随机性，保持风格一致
                max_tokens=self.base_generator.max_tokens
            )
            
            # 添加章节信息
            chapter_info = self.chapter_plan[chapter_num - 1]
            novel_content[f"第{chapter_num}章"] = {
                "content": chapter_content,
                "metadata": chapter_info
            }
            
            # 每生成10章保存一次
            if chapter_num % 10 == 0:
                self._save_checkpoint(novel_content, start_chapter, chapter_num)
                
        return novel_content
    
    def _save_checkpoint(self, content: Dict, start_chapter: int, current_chapter: int) -> None:
        """保存当前进度"""
        timestamp = int(time.time())
        checkpoint_dir = "checkpoints"
        os.makedirs(checkpoint_dir, exist_ok=True)
        
        filename = f"{checkpoint_dir}/sanqianliu_ch{start_chapter}-{current_chapter}_{timestamp}.json"
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
            
        print(f"已保存章节 {start_chapter}-{current_chapter} 到 {filename}")

def create_sanqianliu_generator(api_key: str, model: str = "gemini-2.5-pro-exp-03-25") -> SanQianLiuGenerator:
    """创建一个三千流生成器实例"""
    # 创建基础生成器
    base_generator = NovelGenerator(
        api_key=api_key,
        model=model,
        language="中文",
        novel_type="三千流",
        target_length=5000000,
        temperature=0.7,
        top_p=0.9,
        max_tokens=8000,
        context_length=20000
    )
    
    # 创建并返回三千流专用生成器
    return SanQianLiuGenerator(base_generator=base_generator) 