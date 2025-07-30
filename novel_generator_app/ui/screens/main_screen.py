from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os
import sys

# 导入新的弹窗
from ui.popups.multi_type_popup import MultiTypePopup

# 临时导入
# 在实际应用中，这些应该来自现有项目的core和utils模块
try:
    from core.model_manager import get_model_list
    from utils.config import load_config, save_config
    from templates.prompts import NOVEL_TYPES  # 修正：从prompts而不是novel_types导入
except ImportError:
    # 模拟功能，实际应用中应直接从原项目复制
    def get_model_list():
        return ["gpt-3.5-turbo", "gpt-4", "gpt-4.5-preview"]
    
    def load_config():
        return {}
    
    def save_config(config):
        print("配置已保存:", config)
    
    # 完整的小说类型列表（从原项目复制）
    NOVEL_TYPES = {
        "中文": [
            "玄幻小说", "修真小说", "武侠小说", "都市小说", "历史小说", "军事小说", "游戏小说", 
            "体育小说", "科幻小说", "悬疑小说", "推理小说", "恐怖小说", "灵异小说", "言情小说", 
            "青春小说", "儿童小说", "古言小说", "现言小说", "仙侠小说", "奇幻小说", "校园小说", 
            "职场小说", "商战小说", "官场小说", "娱乐小说", "宫斗小说", "穿越小说", "重生小说", 
            "种田小说", "系统小说", "网游小说", "竞技小说", "末世小说", "架空小说", "宅斗小说", 
            "女强小说", "女尊小说", "纯爱小说", "百合小说", "耽美小说", "异能小说", "灵魂转换小说", 
            "精灵小说", "搞笑小说", "冒险小说", "智斗小说", "悲情小说", "正剧小说", "轻小说", 
            "短篇小说", "中篇小说", "长篇小说", "微小说", "童话故事", "散文随笔", "戏剧小说", 
            "诗歌小说", "外国小说", "民国小说", "清穿小说", "民国言情小说", "洪荒小说", "历史架空小说", 
            "东方玄幻小说", "西方奇幻小说", "历史穿越小说", "都市异能小说", "青春校园小说", "都市言情小说", 
            "古代言情小说", "宫廷小说", "黑道小说", "黑帮小说", "警匪小说", "侦探小说", "商战职场小说", 
            "宗教小说", "吸血鬼小说", "医疗小说", "婚恋小说", "美食小说", "破案小说", "宝宝小说", 
            "复仇小说", "豪门小说", "扮猪吃虎小说", "星际小说", "乡村小说", "虐恋小说", "姐弟恋小说", 
            "年代小说", "婆媳小说", "宅男小说", "宅女小说", "总裁小说", "腹黑小说"
        ]
    }

# 实现高级设置对话框类
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox

class AdvancedSettingsPopup(Popup):
    """高级设置弹窗"""
    
    def __init__(self, main_screen, **kwargs):
        try:
            # 确保先调用父类初始化
            super(AdvancedSettingsPopup, self).__init__(
                title="高级设置",
                size_hint=(0.8, 0.9),
                auto_dismiss=False,
                **kwargs
            )
            
            self.main_screen = main_screen
            
            # 创建内容
            try:
                content_layout = self._create_content()
                self.content = content_layout
            except Exception as e:
                print(f"创建高级设置内容失败: {e}")
                # 如果创建内容失败，显示错误信息
                error_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
                error_label = Label(text="创建设置界面失败，请重试")
                close_button = Button(text="关闭", size_hint_y=None, height=50)
                close_button.bind(on_release=self.dismiss)
                
                error_layout.add_widget(error_label)
                error_layout.add_widget(close_button)
                self.content = error_layout
                
        except Exception as e:
            print(f"初始化高级设置弹窗失败: {e}")
            import traceback
            traceback.print_exc()
    
    def _create_content(self):
        """创建弹窗内容"""
        try:
            # 创建主布局
            content_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
            
            # 创建滑块区域
            try:
                # 直接在这里创建滑块，而不是调用MainScreen的方法
                self.sliders = {}
                sliders_layout = self._create_sliders()
                content_layout.add_widget(sliders_layout)
            except Exception as e:
                print(f"创建滑块区域失败: {e}")
                error_label = Label(text="创建滑块设置失败")
                content_layout.add_widget(error_label)
            
            # 创建写作风格选择区域
            try:
                style_label = Label(text="写作风格:", size_hint_y=None, height=30, halign="left")
                content_layout.add_widget(style_label)
                
                style_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                self.writing_style = Spinner(
                    text='标准',
                    values=('标准', '简洁', '详细', '学术', '诗意', '幽默', '正式', '非正式'),
                    size_hint=(1, None),
                    height=40
                )
                style_layout.add_widget(self.writing_style)
                content_layout.add_widget(style_layout)
            except Exception as e:
                print(f"创建写作风格选择失败: {e}")
                error_label = Label(text="创建写作风格选择失败")
                content_layout.add_widget(error_label)
            
            # 按钮区域
            try:
                buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
                
                cancel_button = Button(text="取消")
                cancel_button.bind(on_release=self.dismiss)
                
                save_button = Button(text="保存")
                save_button.bind(on_release=self._on_save)
                
                buttons_layout.add_widget(cancel_button)
                buttons_layout.add_widget(save_button)
                content_layout.add_widget(buttons_layout)
            except Exception as e:
                print(f"创建按钮区域失败: {e}")
                # 如果按钮创建失败，至少添加一个关闭按钮
                close_button = Button(text="关闭", size_hint_y=None, height=50)
                close_button.bind(on_release=self.dismiss)
                content_layout.add_widget(close_button)
            
            # 加载保存的设置
            try:
                self._load_settings()
            except Exception as e:
                print(f"加载设置失败: {e}")
            
            return content_layout
        except Exception as e:
            print(f"创建内容时出错: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # 如果创建内容失败，返回一个简单的错误布局
            error_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
            error_label = Label(text="创建设置界面失败，请重试")
            close_button = Button(text="关闭", size_hint_y=None, height=50)
            close_button.bind(on_release=self.dismiss)
            
            error_layout.add_widget(error_label)
            error_layout.add_widget(close_button)
            return error_layout

    def _on_save(self, instance):
        """保存高级设置"""
        try:
            # 获取主屏幕的配置
            config = self.main_screen.config
            
            # 获取滑块值
            try:
                # 从主屏幕获取滑块实例
                sliders = self.main_screen.sliders
                if sliders:
                    advanced_settings = {}
                    
                    if 'temperature' in sliders:
                        advanced_settings['temperature'] = sliders['temperature'].value
                        
                    if 'top_p' in sliders:
                        advanced_settings['top_p'] = sliders['top_p'].value
                        
                    if 'max_tokens' in sliders:
                        advanced_settings['max_tokens'] = int(sliders['max_tokens'].value)
                        
                    if 'creativity' in sliders:
                        advanced_settings['creativity'] = sliders['creativity'].value
                        
                    if 'formality' in sliders:
                        advanced_settings['formality'] = sliders['formality'].value
                        
                    if 'detail_level' in sliders:
                        advanced_settings['detail_level'] = sliders['detail_level'].value
                        
                    if 'genre_influence' in sliders:
                        advanced_settings['genre_influence'] = sliders['genre_influence'].value
                    
                    # 获取写作风格
                    advanced_settings['writing_style'] = self.writing_style.text
                    
                    # 更新配置
                    config['advanced_settings'] = advanced_settings
                    
                    # 保存配置
                    if hasattr(self.main_screen, 'save_config') and callable(self.main_screen.save_config):
                        self.main_screen.save_config()
                    else:
                        from core.config import save_config
                        save_config(config)
                    
                    print("高级设置已保存:", advanced_settings)
            except Exception as e:
                print(f"获取滑块值失败: {e}")
                import traceback
                traceback.print_exc()
            
            # 关闭弹窗
            self.dismiss()
            
        except Exception as e:
            print(f"保存高级设置失败: {e}")
            import traceback
            traceback.print_exc()
            
            # 显示错误提示
            error_popup = Popup(
                title="保存失败",
                content=Label(text=f"保存设置失败: {e}"),
                size_hint=(0.6, 0.3)
            )
            error_popup.open()

    def _load_settings(self):
        """从配置中加载设置"""
        try:
            config = self.main_screen.config
            advanced_settings = config.get('advanced_settings', {})
            
            # 获取滑块
            sliders = getattr(self, 'sliders', {})
            if not sliders:
                print("警告: 滑块尚未初始化，无法加载设置")
                return
                
            # 设置滑块值
            if 'temperature' in sliders and 'temperature' in advanced_settings:
                sliders['temperature'].value = advanced_settings['temperature']
                
            if 'top_p' in sliders and 'top_p' in advanced_settings:
                sliders['top_p'].value = advanced_settings['top_p']
                
            if 'max_tokens' in sliders and 'max_tokens' in advanced_settings:
                sliders['max_tokens'].value = advanced_settings['max_tokens']
                
            if 'creativity' in sliders and 'creativity' in advanced_settings:
                sliders['creativity'].value = advanced_settings['creativity']
                
            if 'formality' in sliders and 'formality' in advanced_settings:
                sliders['formality'].value = advanced_settings['formality']
                
            if 'detail_level' in sliders and 'detail_level' in advanced_settings:
                sliders['detail_level'].value = advanced_settings['detail_level']
                
            if 'genre_influence' in sliders and 'genre_influence' in advanced_settings:
                sliders['genre_influence'].value = advanced_settings['genre_influence']
            
            # 设置写作风格
            if hasattr(self, 'writing_style') and 'writing_style' in advanced_settings:
                # 确保写作风格在可选值列表中
                if advanced_settings['writing_style'] in self.writing_style.values:
                    self.writing_style.text = advanced_settings['writing_style']
                
            print("已加载高级设置")
        except Exception as e:
            print(f"加载设置失败: {e}")
            import traceback
            traceback.print_exc()
    
    def open_popup(self):
        """打开高级设置弹窗"""
        try:
            self.open()
        except Exception as e:
            print(f"打开高级设置弹窗失败: {e}")
            import traceback
            traceback.print_exc()

class CustomPromptPopup(Popup):
    """自定义提示词弹窗"""
    def __init__(self, config, callback=None, **kwargs):
        # 创建内容
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # 说明标签
        explanation = Label(
            text="在这里输入自定义提示词，用于指导AI生成小说。\n这将覆盖默认的提示词模板。",
            size_hint_y=None, 
            height=60,
            halign='left',
            valign='top'
        )
        explanation.bind(size=explanation.setter('text_size'))
        
        # 提示词输入框
        self.prompt_input = TextInput(
            text=config.get("custom_prompt", ""),
            multiline=True,
            hint_text="例如：写一个关于{主角}在{设定}中冒险的故事，风格要{风格}...",
            size_hint=(1, 1)
        )
        
        # 占位符说明
        placeholders = Label(
            text="可用占位符: {主角}, {性别}, {设定}, {风格}, {类型}",
            size_hint_y=None,
            height=30,
            halign='left'
        )
        placeholders.bind(size=placeholders.setter('text_size'))
        
        # 按钮区域
        buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        # 重置按钮
        reset_btn = Button(text="重置为默认", size_hint_x=0.5)
        reset_btn.bind(on_release=self.reset_prompt)
        
        # 取消和保存按钮
        btn_box = BoxLayout(size_hint_x=0.5, spacing=10)
        cancel_btn = Button(text="取消")
        cancel_btn.bind(on_release=self.dismiss)
        
        save_btn = Button(text="保存", background_color=(0.3, 0.7, 0.3, 1))
        save_btn.bind(on_release=self.save_prompt)
        
        btn_box.add_widget(cancel_btn)
        btn_box.add_widget(save_btn)
        
        buttons.add_widget(reset_btn)
        buttons.add_widget(btn_box)
        
        # 添加所有组件
        content.add_widget(explanation)
        content.add_widget(self.prompt_input)
        content.add_widget(placeholders)
        content.add_widget(buttons)
        
        # 保存回调和配置
        self.config = config
        self.callback = callback
        
        # 初始化弹窗
        super(CustomPromptPopup, self).__init__(
            title="自定义提示词",
            content=content,
            size_hint=(0.9, 0.8),
            **kwargs
        )
    
    def reset_prompt(self, instance):
        """重置为默认提示词"""
        self.prompt_input.text = ""
    
    def save_prompt(self, instance):
        """保存自定义提示词"""
        custom_prompt = self.prompt_input.text.strip()
        if custom_prompt:
            self.config["custom_prompt"] = custom_prompt
        elif "custom_prompt" in self.config:
            del self.config["custom_prompt"]
            
        save_config(self.config)
        
        if self.callback:
            self.callback(custom_prompt)
            
        self.dismiss()

class MainScreen(Screen):
    # 默认使用中文小说类型列表
    novel_types = ListProperty([])
    # 存储多类型选择结果
    selected_novel_types = ListProperty([])
    
    def __init__(self, **kwargs):
        # 在调用super()之前先初始化config属性
        self.config = load_config()
        # 初始化小说类型列表
        language = self.config.get("language", "中文")  # 从配置获取语言
        if isinstance(NOVEL_TYPES, dict) and language in NOVEL_TYPES:
            self.novel_types = NOVEL_TYPES[language]
        elif isinstance(NOVEL_TYPES, list):
            self.novel_types = NOVEL_TYPES
        super(MainScreen, self).__init__(**kwargs)
        
    def on_kv_post(self, base_widget):
        """KV文件加载完成后触发"""
        self.load_saved_config()
        
    def update_novel_types(self, language="中文"):
        """更新小说类型列表"""
        if isinstance(NOVEL_TYPES, dict) and language in NOVEL_TYPES:
            self.novel_types = NOVEL_TYPES[language]
        elif isinstance(NOVEL_TYPES, list):
            self.novel_types = NOVEL_TYPES
        
        # 如果界面已加载，更新Spinner
        if hasattr(self, 'ids') and self.ids and 'novel_type' in self.ids:
            current_type = self.ids.novel_type.text
            self.ids.novel_type.values = self.novel_types
            
            # 如果当前选择的类型不在新列表中，重置为默认值
            if current_type not in self.novel_types:
                self.ids.novel_type.text = "选择小说类型"
                
    def load_saved_config(self):
        """从配置文件加载保存的设置"""
        if not hasattr(self, 'ids') or not self.ids:
            # 延迟加载，确保ids已可用
            return
            
        # 更新小说类型列表
        language = self.config.get("language", "中文")
        self.update_novel_types(language)
            
        # 设置API密钥（确保清理掉任何空白字符）
        if "api_key" in self.config:
            api_key = self.config.get("api_key", "").strip()
            self.ids.api_key.text = api_key
            # 同时更新配置中的值，确保它是干净的
            self.config["api_key"] = api_key
            
        # 设置模型
        if "model" in self.config:
            self.ids.model_selection.text = self.config.get("model", "gpt-4.5-preview")
        
        # 设置多种类型选择
        if "selected_novel_types" in self.config:
            self.selected_novel_types = self.config.get("selected_novel_types")
            # 更新UI以反映多类型选择
            self._update_ui_after_type_selection()
        # 如果没有多选，则设置单选类型
        elif "novel_type" in self.config and self.config["novel_type"] in self.novel_types:
            self.ids.novel_type.text = self.config.get("novel_type")
            
        # 设置其他配置项
        if "target_length" in self.config:
            self.ids.target_length.text = str(self.config.get("target_length", 20000))
            
        if "auto_summary" in self.config:
            self.ids.auto_summary.active = self.config.get("auto_summary", True)
            
        if "create_ending" in self.config:
            self.ids.create_ending.active = self.config.get("create_ending", False)
    
    def on_enter(self):
        """屏幕进入时加载配置"""
        self.load_saved_config()
    
    def open_advanced_settings(self, *args):
        """打开高级设置弹窗"""
        try:
            if not hasattr(self, 'advanced_settings_popup'):
                self.advanced_settings_popup = AdvancedSettingsPopup(main_screen=self)
            self.advanced_settings_popup.open_popup()
        except Exception as e:
            print(f"无法打开高级设置: {e}")
            import traceback
            traceback.print_exc()
            
            # 显示错误提示
            error_popup = Popup(
                title="错误",
                content=Label(text=f"无法打开高级设置: {e}"),
                size_hint=(0.6, 0.3)
            )
            error_popup.open()
        
    def open_multi_type_popup(self):
        """打开多类型选择弹窗"""
        language = self.config.get("language", "中文")
        # 将当前已选择的类型传递给弹窗
        popup = MultiTypePopup(language=language, current_selection=self.selected_novel_types)
        popup.parent_screen = self # 将当前屏幕实例传递给弹窗，用于回调
        popup.open()
        
    def update_selected_types(self, selected_types):
         """弹窗关闭后，更新主屏幕的选择结果"""
         self.selected_novel_types = selected_types
         print(f"主屏幕更新选择: {self.selected_novel_types}")
         # 更新界面显示
         self._update_ui_after_type_selection()
    
    def _update_ui_after_type_selection(self):
        """更新UI以反映多类型选择"""
        multi_type_btn = self.ids.get('multi_type_btn')
        if multi_type_btn:
            if self.selected_novel_types:
                multi_type_btn.text = f"已选 {len(self.selected_novel_types)} 种"
            else:
                multi_type_btn.text = "多种类型"
        
        # 更新单选类型下拉框状态
        if hasattr(self, 'ids') and 'novel_type' in self.ids:
            self.ids.novel_type.disabled = bool(self.selected_novel_types)
            
        # 保存选择到配置
        if self.selected_novel_types:
            self.config["selected_novel_types"] = self.selected_novel_types
        elif "selected_novel_types" in self.config:
            del self.config["selected_novel_types"]
        save_config(self.config)

    def open_custom_prompt(self):
        """打开自定义提示词弹窗"""
        try:
            print("打开自定义提示词弹窗")
            popup = CustomPromptPopup(self.config)
            popup.open()
        except Exception as e:
            print(f"打开自定义提示词弹窗错误: {str(e)}")
            import traceback
            traceback.print_exc()
    
    def start_generation(self):
        """开始生成小说"""
        # 保存当前配置
        self.save_current_config()
        
        # 验证输入
        if not self.validate_inputs():
            return
            
        # 切换到生成屏幕
        self.manager.current = 'generation'
        gen_screen = self.manager.get_screen('generation')
        
        # 清理API密钥，确保没有空白字符和控制字符
        api_key = self.ids.api_key.text.strip()
        
        # 获取生成类型：优先使用多选结果，否则使用单选结果
        novel_type_to_generate = self.selected_novel_types if self.selected_novel_types else [self.ids.novel_type.text]
        
        # 获取高级设置
        advanced_settings = self.config.get("advanced_settings", {})
        
        # 获取自定义提示词
        custom_prompt = self.config.get("custom_prompt", "")
        
        # 传递参数到生成屏幕
        params = {
            'api_key': api_key,
            'model': self.ids.model_selection.text,
            'novel_types': novel_type_to_generate, # 传递类型列表
            'target_length': int(self.ids.target_length.text),
            'auto_summary': self.ids.auto_summary.active,
            'create_ending': self.ids.create_ending.active,
            'num_novels': len(novel_type_to_generate) if self.selected_novel_types else 1, # 生成数量
            'language': self.config.get("language", "中文"), # 传递语言设置
            'advanced_settings': advanced_settings, # 传递高级设置
            'custom_prompt': custom_prompt # 传递自定义提示词
        }
        
        gen_screen.start_novel_generation(**params)
    
    def validate_inputs(self):
        """验证用户输入"""
        # 清理API密钥
        api_key = self.ids.api_key.text.strip()
        self.ids.api_key.text = api_key  # 更新文本框中的值
        
        if not api_key:
            self.show_error("请输入API密钥")
            return False
            
        # 检查小说类型：优先检查多类型选择，如果没有则检查单选下拉框
        if not self.selected_novel_types and self.ids.novel_type.text == "选择小说类型":
            self.show_error("请选择小说类型")
            return False
            
        try:
            target_length = int(self.ids.target_length.text)
            if target_length < 1000:
                self.show_error("目标字数不能小于1000")
                return False
        except ValueError:
            self.show_error("请输入有效的目标字数")
            return False
            
        return True
    
    def show_error(self, message):
        """显示错误消息"""
        popup = Popup(
            title='错误',
            content=Label(text=message),
            size_hint=(0.8, 0.3)
        )
        popup.open()
        
    def change_language(self, language):
        """切换语言"""
        if language in ["中文", "English"] and language != self.config.get("language", "中文"):
            self.config["language"] = language
            self.update_novel_types(language)
            save_config(self.config)
    
    def save_current_config(self):
        """保存当前配置到配置文件"""
        # 去除API密钥中的空白字符和控制字符
        api_key = self.ids.api_key.text.strip()
        self.config["api_key"] = api_key
        
        self.config["model"] = self.ids.model_selection.text
        self.config["novel_type"] = self.ids.novel_type.text
        self.config["target_length"] = int(self.ids.target_length.text)
        self.config["auto_summary"] = self.ids.auto_summary.active
        self.config["create_ending"] = self.ids.create_ending.active
        
        # 确保语言设置被保存
        if "language" not in self.config:
            self.config["language"] = "中文"
            
        # 保存多类型选择
        if self.selected_novel_types:
            self.config["selected_novel_types"] = self.selected_novel_types
        elif "selected_novel_types" in self.config:
            del self.config["selected_novel_types"]
            
        save_config(self.config) 

    def _create_sliders(self):
        """创建所有滑块控件"""
        try:
            sliders_layout = BoxLayout(orientation='vertical', spacing=10)
            
            # 创建温度滑块
            try:
                temp_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                temp_label = Label(text="温度:", size_hint_x=0.3, halign="left")
                temp_slider = Slider(min=0.1, max=1.0, value=0.8, size_hint_x=0.6)
                temp_value = Label(text=f"{temp_slider.value:.1f}", size_hint_x=0.1)
                
                def on_temp_change(instance, value):
                    temp_value.text = f"{value:.1f}"
                
                temp_slider.bind(value=on_temp_change)
                self.sliders['temperature'] = temp_slider
                
                temp_layout.add_widget(temp_label)
                temp_layout.add_widget(temp_slider)
                temp_layout.add_widget(temp_value)
                sliders_layout.add_widget(temp_layout)
            except Exception as e:
                print(f"创建温度滑块失败: {e}")
            
            # 创建Top-P滑块
            try:
                top_p_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                top_p_label = Label(text="Top-P:", size_hint_x=0.3, halign="left")
                top_p_slider = Slider(min=0.1, max=1.0, value=0.9, size_hint_x=0.6)
                top_p_value = Label(text=f"{top_p_slider.value:.1f}", size_hint_x=0.1)
                
                def on_top_p_change(instance, value):
                    top_p_value.text = f"{value:.1f}"
                
                top_p_slider.bind(value=on_top_p_change)
                self.sliders['top_p'] = top_p_slider
                
                top_p_layout.add_widget(top_p_label)
                top_p_layout.add_widget(top_p_slider)
                top_p_layout.add_widget(top_p_value)
                sliders_layout.add_widget(top_p_layout)
            except Exception as e:
                print(f"创建Top-P滑块失败: {e}")
            
            # 创建最大tokens滑块
            try:
                max_tokens_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                max_tokens_label = Label(text="最大tokens:", size_hint_x=0.3, halign="left")
                max_tokens_slider = Slider(min=1000, max=8000, value=4000, step=100, size_hint_x=0.6)
                max_tokens_value = Label(text=str(int(max_tokens_slider.value)), size_hint_x=0.1)
                
                def on_max_tokens_change(instance, value):
                    max_tokens_value.text = str(int(value))
                
                max_tokens_slider.bind(value=on_max_tokens_change)
                self.sliders['max_tokens'] = max_tokens_slider
                
                max_tokens_layout.add_widget(max_tokens_label)
                max_tokens_layout.add_widget(max_tokens_slider)
                max_tokens_layout.add_widget(max_tokens_value)
                sliders_layout.add_widget(max_tokens_layout)
            except Exception as e:
                print(f"创建最大tokens滑块失败: {e}")
            
            # 创建创造力滑块
            try:
                creativity_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                creativity_label = Label(text="创造力:", size_hint_x=0.3, halign="left")
                creativity_slider = Slider(min=0.1, max=1.0, value=0.7, size_hint_x=0.6)
                creativity_value = Label(text=f"{creativity_slider.value:.1f}", size_hint_x=0.1)
                
                def on_creativity_change(instance, value):
                    creativity_value.text = f"{value:.1f}"
                
                creativity_slider.bind(value=on_creativity_change)
                self.sliders['creativity'] = creativity_slider
                
                creativity_layout.add_widget(creativity_label)
                creativity_layout.add_widget(creativity_slider)
                creativity_layout.add_widget(creativity_value)
                sliders_layout.add_widget(creativity_layout)
            except Exception as e:
                print(f"创建创造力滑块失败: {e}")
            
            # 创建正式程度滑块
            try:
                formality_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                formality_label = Label(text="正式程度:", size_hint_x=0.3, halign="left")
                formality_slider = Slider(min=0.0, max=1.0, value=0.5, size_hint_x=0.6)
                formality_value = Label(text=f"{formality_slider.value:.1f}", size_hint_x=0.1)
                
                def on_formality_change(instance, value):
                    formality_value.text = f"{value:.1f}"
                
                formality_slider.bind(value=on_formality_change)
                self.sliders['formality'] = formality_slider
                
                formality_layout.add_widget(formality_label)
                formality_layout.add_widget(formality_slider)
                formality_layout.add_widget(formality_value)
                sliders_layout.add_widget(formality_layout)
            except Exception as e:
                print(f"创建正式程度滑块失败: {e}")
            
            # 创建细节程度滑块
            try:
                detail_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                detail_label = Label(text="细节程度:", size_hint_x=0.3, halign="left")
                detail_slider = Slider(min=0.1, max=1.0, value=0.6, size_hint_x=0.6)
                detail_value = Label(text=f"{detail_slider.value:.1f}", size_hint_x=0.1)
                
                def on_detail_change(instance, value):
                    detail_value.text = f"{value:.1f}"
                
                detail_slider.bind(value=on_detail_change)
                self.sliders['detail_level'] = detail_slider
                
                detail_layout.add_widget(detail_label)
                detail_layout.add_widget(detail_slider)
                detail_layout.add_widget(detail_value)
                sliders_layout.add_widget(detail_layout)
            except Exception as e:
                print(f"创建细节程度滑块失败: {e}")
            
            # 创建类型特征强度滑块
            try:
                genre_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                genre_label = Label(text="类型特征强度:", size_hint_x=0.3, halign="left")
                genre_slider = Slider(min=0.1, max=1.0, value=0.8, size_hint_x=0.6)
                genre_value = Label(text=f"{genre_slider.value:.1f}", size_hint_x=0.1)
                
                def on_genre_change(instance, value):
                    genre_value.text = f"{value:.1f}"
                
                genre_slider.bind(value=on_genre_change)
                self.sliders['genre_influence'] = genre_slider
                
                genre_layout.add_widget(genre_label)
                genre_layout.add_widget(genre_slider)
                genre_layout.add_widget(genre_value)
                sliders_layout.add_widget(genre_layout)
            except Exception as e:
                print(f"创建类型特征强度滑块失败: {e}")
            
            return sliders_layout
        except Exception as e:
            print(f"创建滑块时出错: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # 如果滑块创建失败，返回一个简单的标签
            error_label = Label(text="创建设置控件失败，请重试")
            return BoxLayout(orientation='vertical').add_widget(error_label) 