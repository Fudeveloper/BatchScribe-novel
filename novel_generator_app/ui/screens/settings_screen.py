from kivy.uix.screenmanager import Screen
from kivy.properties import DictProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

try:
    from utils.config import load_config, save_config
except ImportError:
    # 模拟配置功能
    def load_config():
        return {}
    
    def save_config(config):
        print("配置已保存:", config)

class SettingsScreen(Screen):
    advanced_settings = DictProperty({
        "temperature": 0.8,
        "top_p": 0.9,
        "max_tokens": 4000,
        "context_length": 100000,
        "autosave_interval": 60,
        "auto_summary": True,
        "auto_summary_interval": 2000,
        "creativity": 0.7,
        "formality": 0.5,
        "detail_level": 0.6,
        "writing_style": "平衡"
    })
    
    def __init__(self, **kwargs):
        # 在调用super()之前初始化config
        self.config = load_config()
        super(SettingsScreen, self).__init__(**kwargs)
        self.load_settings()
    
    def on_enter(self):
        """屏幕进入时调用"""
        self.load_settings()
    
    def load_settings(self):
        """从配置文件加载设置"""
        if not hasattr(self, 'ids') or not self.ids:
            return
            
        # 加载高级设置
        if "advanced_settings" in self.config:
            self.advanced_settings.update(self.config.get("advanced_settings", {}))
        
        # 更新UI控件
        if hasattr(self.ids, 'temperature'):
            self.ids.temperature.value = self.advanced_settings["temperature"]
            self.ids.top_p.value = self.advanced_settings["top_p"]
            self.ids.max_tokens.value = self.advanced_settings["max_tokens"]
            self.ids.creativity.value = self.advanced_settings["creativity"]
            self.ids.formality.value = self.advanced_settings["formality"]
            self.ids.detail_level.value = self.advanced_settings["detail_level"]
            
            # 单选按钮组
            writing_style = self.advanced_settings["writing_style"]
            if writing_style == "平衡":
                self.ids.style_balanced.active = True
            elif writing_style == "简洁":
                self.ids.style_concise.active = True
            elif writing_style == "详细":
                self.ids.style_detailed.active = True
            elif writing_style == "文学":
                self.ids.style_literary.active = True
    
    def save_settings(self):
        """保存当前设置到配置文件"""
        # 获取UI控件的值
        self.advanced_settings["temperature"] = self.ids.temperature.value
        self.advanced_settings["top_p"] = self.ids.top_p.value
        self.advanced_settings["max_tokens"] = int(self.ids.max_tokens.value)
        self.advanced_settings["creativity"] = self.ids.creativity.value
        self.advanced_settings["formality"] = self.ids.formality.value
        self.advanced_settings["detail_level"] = self.ids.detail_level.value
        
        # 获取单选按钮组的值
        if self.ids.style_balanced.active:
            self.advanced_settings["writing_style"] = "平衡"
        elif self.ids.style_concise.active:
            self.advanced_settings["writing_style"] = "简洁"
        elif self.ids.style_detailed.active:
            self.advanced_settings["writing_style"] = "详细"
        elif self.ids.style_literary.active:
            self.advanced_settings["writing_style"] = "文学"
        
        # 保存到配置
        self.config["advanced_settings"] = self.advanced_settings
        save_config(self.config)
        
        # 显示保存成功提示
        self.show_message("设置已保存")
    
    def show_message(self, message):
        popup = Popup(
            title='提示',
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
    
    def go_back(self):
        """返回主屏幕"""
        self.manager.current = 'main' 