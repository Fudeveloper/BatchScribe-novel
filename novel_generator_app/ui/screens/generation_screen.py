from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import threading
import os
import time
import datetime

try:
    from core.generator import NovelGenerator
    from utils.config import load_config
except ImportError:
    # 模拟NovelGenerator功能
    class NovelGenerator:
        def __init__(self, api_key, model, **kwargs):
            self.api_key = api_key
            self.model = model
            self.novel_type = kwargs.get('novel_type', '')
            self.target_length = kwargs.get('target_length', 20000)
            self.is_running = False
            self.is_paused = False
            self.current_progress = 0
            self.current_content = ""
            
        def start_generation(self, callback=None, progress_callback=None):
            """模拟生成过程"""
            self.is_running = True
            self.current_progress = 0
            
            # 生成小说线程
            def generation_thread():
                while self.current_progress < 100 and self.is_running:
                    if not self.is_paused:
                        # 模拟生成内容
                        time.sleep(0.5)  # 减慢模拟速度
                        self.current_progress += 1
                        self.current_content += f"这是生成的小说内容，当前进度 {self.current_progress}%\n"
                        
                        if progress_callback:
                            progress_callback({
                                'progress': self.current_progress,
                                'current_length': len(self.current_content),
                                'target_length': self.target_length,
                                'status': 'generating'
                            })
                    
                    time.sleep(0.1)
                
                if self.is_running:  # 如果是正常完成而非被终止
                    if callback:
                        callback()
            
            # 启动线程
            threading.Thread(target=generation_thread, daemon=True).start()
        
        def stop_generation(self):
            """停止生成"""
            self.is_running = False
        
        def pause_generation(self):
            """暂停生成"""
            self.is_paused = True
        
        def resume_generation(self):
            """继续生成"""
            self.is_paused = False
        
        def get_current_content(self):
            """获取当前内容"""
            return self.current_content
            
    def load_config():
        return {
            "advanced_settings": {
                "temperature": 0.8,
                "top_p": 0.9,
                "max_tokens": 4000
            }
        }

class GenerationScreen(Screen):
    progress = NumericProperty(0)
    status = StringProperty("准备中")
    is_generating = BooleanProperty(False)
    is_paused = BooleanProperty(False)
    current_length = NumericProperty(0)
    target_length = NumericProperty(20000)
    elapsed_time = StringProperty("00:00:00")
    estimated_time = StringProperty("--:--:--")
    
    def __init__(self, **kwargs):
        # 确保在super()调用前初始化成员变量
        self.generator = None
        self.start_time = None
        self.timer = None
        self._temp_content = ""  # 临时存储内容，避免线程问题
        super(GenerationScreen, self).__init__(**kwargs)
        
    def on_enter(self):
        """屏幕进入时调用"""
        pass
    
    def start_novel_generation(self, **params):
        """开始生成小说"""
        self.is_generating = True
        self.is_paused = False
        self.progress = 0
        self.current_length = 0
        self._temp_content = ""
        self.target_length = params.get('target_length', 20000)
        self.status = "正在初始化..."
        
        if hasattr(self, 'ids') and self.ids and hasattr(self.ids, 'novel_content'):
            self.ids.novel_content.text = ""
        
        # 读取配置
        config = load_config()
        advanced_settings = config.get("advanced_settings", {})
        
        # 创建生成器
        self.generator = NovelGenerator(
            api_key=params.get('api_key', ''),
            model=params.get('model', 'gemini-2.5-flash-lite-preview-06-17'),
            novel_type=params.get('novel_type', ''),
            target_length=params.get('target_length', 20000),
            auto_summary=params.get('auto_summary', True),
            create_ending=params.get('create_ending', False),
            temperature=advanced_settings.get('temperature', 0.66),
            top_p=advanced_settings.get('top_p', 0.92),
            max_tokens=advanced_settings.get('max_tokens', 8000)
        )
        
        # 记录开始时间
        self.start_time = time.time()
        
        # 启动计时器
        self.timer = Clock.schedule_interval(self.update_timer, 1)
        
        # 更新状态
        self.status = "正在生成小说..."
        
        # 开始生成
        self.generator.start_generation(
            callback=self.generation_completed,
            progress_callback=self.safe_update_progress
        )
    
    def safe_update_progress(self, progress_data):
        """
        安全地更新进度（在主线程中）
        
        Args:
            progress_data (dict): 进度数据
        """
        # 保存内容到临时变量
        if 'content' in progress_data:
            self._temp_content = progress_data['content']
            
        # 使用Clock在主线程中调度UI更新
        Clock.schedule_once(lambda dt: self._do_update_progress(progress_data), 0)
    
    def _do_update_progress(self, progress_data):
        """
        在主线程中执行实际的UI更新
        
        Args:
            progress_data (dict): 进度数据
        """
        self.progress = progress_data.get('progress', 0)
        self.current_length = progress_data.get('current_length', 0)
        self.status = progress_data.get('status', '生成中')
        
        # 更新小说内容显示
        if hasattr(self, 'ids') and self.ids and hasattr(self.ids, 'novel_content'):
            if 'content' in progress_data:
                self.ids.novel_content.text = progress_data['content']
            elif self._temp_content:
                self.ids.novel_content.text = self._temp_content
            elif self.generator:
                self.ids.novel_content.text = self.generator.get_current_content()
    
    def update_timer(self, dt):
        """更新计时器"""
        if not self.start_time:
            return
            
        elapsed = time.time() - self.start_time
        self.elapsed_time = str(datetime.timedelta(seconds=int(elapsed)))
        
        # 估算剩余时间
        if self.progress > 0:
            total_time = elapsed / (self.progress / 100)
            remaining = total_time - elapsed
            self.estimated_time = str(datetime.timedelta(seconds=int(remaining)))
    
    def generation_completed(self):
        """生成完成时调用"""
        # 使用Clock确保在主线程中运行
        Clock.schedule_once(lambda dt: self._do_generation_completed(), 0)
    
    def _do_generation_completed(self):
        """在主线程中处理生成完成事件"""
        self.is_generating = False
        self.status = "生成完成"
        
        # 停止计时器
        if self.timer:
            self.timer.cancel()
            self.timer = None
        
        # 显示完成提示
        self.show_message("小说生成完成")
    
    def pause_generation(self):
        """暂停生成"""
        if self.generator and self.is_generating and not self.is_paused:
            self.generator.pause_generation()
            self.is_paused = True
            self.status = "已暂停"
    
    def resume_generation(self):
        """继续生成"""
        if self.generator and self.is_generating and self.is_paused:
            self.generator.resume_generation()
            self.is_paused = False
            self.status = "生成中"
    
    def stop_generation(self):
        """停止生成"""
        if self.generator and self.is_generating:
            self.generator.stop_generation()
            self.is_generating = False
            self.status = "已停止"
            
            # 停止计时器
            if self.timer:
                self.timer.cancel()
                self.timer = None
    
    def go_back(self):
        """返回主屏幕"""
        # 如果正在生成，先询问是否停止
        if self.is_generating:
            self.show_confirm_dialog(
                "确认返回", 
                "正在生成小说，返回将停止生成。确定要返回吗？",
                self.confirm_go_back
            )
        else:
            self.manager.current = 'main'
    
    def confirm_go_back(self):
        """确认返回"""
        self.stop_generation()
        self.manager.current = 'main'
    
    def show_message(self, message):
        """显示消息"""
        popup = Popup(
            title='提示',
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
    
    def show_confirm_dialog(self, title, message, callback):
        """显示确认对话框"""
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        
        buttons = BoxLayout(size_hint_y=None, height='50dp')
        
        # 取消按钮
        cancel_btn = Button(text='取消')
        cancel_btn.bind(on_release=lambda x: popup.dismiss())
        buttons.add_widget(cancel_btn)
        
        # 确认按钮
        confirm_btn = Button(text='确认')
        confirm_btn.bind(on_release=lambda x: [callback(), popup.dismiss()])
        buttons.add_widget(confirm_btn)
        
        content.add_widget(buttons)
        
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.8, 0.4),
            auto_dismiss=False
        )
        popup.open() 