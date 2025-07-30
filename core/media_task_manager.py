#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
媒体任务管理器 - 负责管理媒体生成任务的持久化存储和查询
"""

import json
import os
import time
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger("novel_generator")

class MediaTaskManager:
    """媒体任务管理器"""
    
    def __init__(self, tasks_file: str = "media_tasks.json"):
        self.tasks_file = tasks_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self) -> Dict[str, Any]:
        """加载任务数据"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"加载任务文件失败: {e}")
        return {"image_tasks": {}, "music_tasks": {}}
    
    def _save_tasks(self):
        """保存任务数据"""
        try:
            with open(self.tasks_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"保存任务文件失败: {e}")
    
    def add_image_task(self, task_id: str, novel_info: Dict[str, Any], 
                       prompt: str, output_dir: str) -> str:
        """
        添加图片生成任务
        
        Args:
            task_id: 任务ID
            novel_info: 小说信息
            prompt: 生成提示词
            output_dir: 输出目录
            
        Returns:
            str: 本地任务标识
        """
        local_id = f"img_{int(time.time())}_{len(self.tasks['image_tasks'])}"
        
        task_info = {
            "local_id": local_id,
            "api_task_id": task_id,
            "type": "image",
            "status": "submitted",
            "prompt": prompt,
            "novel_info": novel_info,
            "output_dir": output_dir,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "result": None,
            "error": None
        }
        
        self.tasks["image_tasks"][local_id] = task_info
        self._save_tasks()
        
        logger.info(f"已保存图片任务: {local_id} (API ID: {task_id})")
        return local_id
    
    def add_music_task(self, task_id: str, novel_info: Dict[str, Any], 
                       prompt: str, output_dir: str) -> str:
        """
        添加音乐生成任务
        
        Args:
            task_id: 任务ID
            novel_info: 小说信息
            prompt: 生成提示词
            output_dir: 输出目录
            
        Returns:
            str: 本地任务标识
        """
        local_id = f"music_{int(time.time())}_{len(self.tasks['music_tasks'])}"
        
        task_info = {
            "local_id": local_id,
            "api_task_id": task_id,
            "type": "music",
            "status": "submitted",
            "prompt": prompt,
            "novel_info": novel_info,
            "output_dir": output_dir,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "result": None,
            "error": None
        }
        
        self.tasks["music_tasks"][local_id] = task_info
        self._save_tasks()
        
        logger.info(f"已保存音乐任务: {local_id} (API ID: {task_id})")
        return local_id
    
    def update_task_status(self, local_id: str, status: str, result: Optional[Dict] = None, 
                          error: Optional[str] = None):
        """
        更新任务状态
        
        Args:
            local_id: 本地任务ID
            status: 新状态
            result: 任务结果
            error: 错误信息
        """
        task = self.get_task(local_id)
        if task:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            
            if result:
                task["result"] = result
            if error:
                task["error"] = error
            
            # 更新到对应的任务列表中
            if task["type"] == "image":
                self.tasks["image_tasks"][local_id] = task
            else:
                self.tasks["music_tasks"][local_id] = task
            
            self._save_tasks()
            logger.info(f"任务 {local_id} 状态更新为: {status}")
    
    def get_task(self, local_id: str) -> Optional[Dict[str, Any]]:
        """获取任务信息"""
        if local_id in self.tasks["image_tasks"]:
            return self.tasks["image_tasks"][local_id]
        elif local_id in self.tasks["music_tasks"]:
            return self.tasks["music_tasks"][local_id]
        return None
    
    def get_pending_tasks(self) -> List[Dict[str, Any]]:
        """获取所有待处理的任务"""
        pending = []
        
        for task in self.tasks["image_tasks"].values():
            if task["status"] in ["submitted", "queued", "running", "in_progress"]:
                pending.append(task)
        
        for task in self.tasks["music_tasks"].values():
            if task["status"] in ["submitted", "queued", "running", "in_progress"]:
                pending.append(task)
        
        return pending
    
    def get_completed_tasks(self) -> List[Dict[str, Any]]:
        """获取所有已完成的任务"""
        completed = []
        
        for task in self.tasks["image_tasks"].values():
            if task["status"] in ["success", "complete"]:
                completed.append(task)
        
        for task in self.tasks["music_tasks"].values():
            if task["status"] in ["success", "complete"]:
                completed.append(task)
        
        return completed
    
    def get_failed_tasks(self) -> List[Dict[str, Any]]:
        """获取所有失败的任务"""
        failed = []
        
        for task in self.tasks["image_tasks"].values():
            if task["status"] in ["failure", "error", "timeout"]:
                failed.append(task)
        
        for task in self.tasks["music_tasks"].values():
            if task["status"] in ["failure", "error", "timeout"]:
                failed.append(task)
        
        return failed
    
    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """获取所有任务"""
        all_tasks = []
        all_tasks.extend(self.tasks["image_tasks"].values())
        all_tasks.extend(self.tasks["music_tasks"].values())
        
        # 按创建时间排序
        all_tasks.sort(key=lambda x: x["created_at"], reverse=True)
        return all_tasks
    
    def clean_old_tasks(self, days: int = 7):
        """清理旧任务（默认7天前的）"""
        cutoff_time = time.time() - (days * 24 * 60 * 60)
        
        # 清理图片任务
        to_remove = []
        for local_id, task in self.tasks["image_tasks"].items():
            created_timestamp = datetime.fromisoformat(task["created_at"]).timestamp()
            if created_timestamp < cutoff_time:
                to_remove.append(local_id)
        
        for local_id in to_remove:
            del self.tasks["image_tasks"][local_id]
            logger.info(f"已清理旧图片任务: {local_id}")
        
        # 清理音乐任务
        to_remove = []
        for local_id, task in self.tasks["music_tasks"].items():
            created_timestamp = datetime.fromisoformat(task["created_at"]).timestamp()
            if created_timestamp < cutoff_time:
                to_remove.append(local_id)
        
        for local_id in to_remove:
            del self.tasks["music_tasks"][local_id]
            logger.info(f"已清理旧音乐任务: {local_id}")
        
        if to_remove:
            self._save_tasks()
    
    def export_tasks(self, filename: str = None) -> str:
        """导出任务数据"""
        if not filename:
            filename = f"media_tasks_export_{int(time.time())}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            logger.info(f"任务数据已导出到: {filename}")
            return filename
        except Exception as e:
            logger.error(f"导出任务数据失败: {e}")
            return ""
    
    def get_task_summary(self) -> Dict[str, int]:
        """获取任务统计摘要"""
        summary = {
            "total": 0,
            "pending": 0,
            "completed": 0,
            "failed": 0,
            "image_tasks": len(self.tasks["image_tasks"]),
            "music_tasks": len(self.tasks["music_tasks"])
        }
        
        all_tasks = self.get_all_tasks()
        summary["total"] = len(all_tasks)
        
        for task in all_tasks:
            status = task["status"]
            if status in ["submitted", "queued", "running", "in_progress"]:
                summary["pending"] += 1
            elif status in ["success", "complete"]:
                summary["completed"] += 1
            elif status in ["failure", "error", "timeout"]:
                summary["failed"] += 1
        
        return summary 