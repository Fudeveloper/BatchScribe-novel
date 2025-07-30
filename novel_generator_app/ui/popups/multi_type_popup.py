from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.lang import Builder
import os

# 尝试从项目中导入NOVEL_TYPES
try:
    from templates.prompts import NOVEL_TYPES
except ImportError:
    # 如果导入失败，使用备用列表（与main_screen.py中的一致）
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
        ],
         "English": [ # 简单添加一些英文示例
            "Fantasy Adventure", "Science Fiction", "Mystery", "Horror Thriller", "Romance"
        ]
    }

# 加载KV文件 (确保KV文件与Python文件在同一级或指定路径)
kv_path = os.path.join(os.path.dirname(__file__), '../kv/multi_type_popup.kv')
if os.path.exists(kv_path):
    Builder.load_file(kv_path)
else:
    # 尝试在其他可能的路径加载，或者提供错误信息
    kv_path_alt = os.path.join(os.path.dirname(__file__), 'kv/multi_type_popup.kv')
    if os.path.exists(kv_path_alt):
         Builder.load_file(kv_path_alt)
    else:
         print(f"错误: 找不到KV文件 multi_type_popup.kv at {kv_path} or {kv_path_alt}")


class MultiTypePopup(Popup):
    grid_layout = ObjectProperty(None)
    search_input = ObjectProperty(None)
    selection_label = ObjectProperty(None)
    all_types = ListProperty([])
    filtered_types = ListProperty([])
    type_checkboxes = {} # 用于存储Checkbox实例
    language = StringProperty("中文") # 默认为中文
    selected_count = 0

    def __init__(self, language="中文", current_selection=[], **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.current_selection = current_selection or [] # 存储传入的当前已选类型，确保不是None
        print(f"多类型选择弹窗初始化，当前语言：{language}，已选类型数：{len(self.current_selection)}")
        
    def on_open(self):
        """弹窗打开时初始化界面"""
        try:
            print("多类型选择弹窗已打开，开始初始化")
            # 确保grid_layout正确引用
            self.grid_layout = self.ids.grid_layout
            self.search_input = self.ids.search_input
            self.selection_label = self.ids.selection_label
            print(f"控件引用状态: grid_layout={bool(self.grid_layout)}, search_input={bool(self.search_input)}, selection_label={bool(self.selection_label)}")
            # 加载类型列表
            self._load_types()
            # 更新计数
            self._update_selection_count()
            print("多类型选择弹窗初始化完成")
        except Exception as e:
            print(f"多类型选择弹窗初始化错误: {str(e)}")
            import traceback
            traceback.print_exc()
        
    def _load_types(self):
        """根据语言加载小说类型"""
        if isinstance(NOVEL_TYPES, dict) and self.language in NOVEL_TYPES:
            self.all_types = sorted(NOVEL_TYPES[self.language])
        elif isinstance(NOVEL_TYPES, list) and self.language == "中文": # 兼容旧格式
             self.all_types = sorted(NOVEL_TYPES)
        else:
            self.all_types = [] # 或者显示错误
        self.filtered_types = self.all_types[:] # 初始显示所有类型
        self.display_types()
        # 恢复之前的选择
        self._restore_selection()

    def display_types(self):
        """在GridLayout中显示类型复选框"""
        try:
            # 确保有要显示的类型列表
            if not self.filtered_types:
                print("没有类型可显示")
                return
                
            # 清空现有内容
            if self.grid_layout:
                self.grid_layout.clear_widgets()
                
            self.type_checkboxes.clear()
            self.selected_count = 0 # 重置计数

            # 添加类型复选框
            for novel_type in self.filtered_types:
                box = BoxLayout(size_hint_y=None, height=30)
                is_active = novel_type in self.current_selection # 检查是否已选
                checkbox = CheckBox(size_hint_x=None, width=40, active=is_active)
                checkbox.bind(active=self._on_checkbox_active)
                
                label = Label(text=novel_type, halign='left', valign='middle')
                label.bind(size=label.setter('text_size')) # 自动调整文本大小
                
                box.add_widget(checkbox)
                box.add_widget(label)
                self.grid_layout.add_widget(box)
                self.type_checkboxes[novel_type] = checkbox
                if is_active:
                    self.selected_count += 1
            
            # 调整GridLayout的高度以适应内容
            self.grid_layout.height = len(self.filtered_types) * 35 # 稍微增加每行的高度
            
            print(f"显示了 {len(self.filtered_types)} 种类型，已选 {self.selected_count} 种")
        except Exception as e:
            print(f"显示类型出错: {str(e)}")
            import traceback
            traceback.print_exc()

    def filter_types(self, search_term):
        """根据搜索词过滤类型"""
        search_term = search_term.lower()
        if not search_term:
            self.filtered_types = self.all_types[:]
        else:
            self.filtered_types = [t for t in self.all_types if search_term in t.lower()]
        self.display_types() # 重新显示过滤后的类型

    def clear_search(self):
        """清除搜索框"""
        try:
            print("清除搜索...")
            # 确保search_input已绑定
            if not hasattr(self, 'search_input') or not self.search_input:
                self.search_input = self.ids.get('search_input')
                
            if self.search_input:
                self.search_input.text = ""
                self.filter_types("")
                print("搜索已清除")
            else:
                print("错误: 无法找到搜索输入框")
        except Exception as e:
            print(f"清除搜索出错: {str(e)}")
            import traceback
            traceback.print_exc()

    def _on_checkbox_active(self, checkbox, value):
        """复选框状态改变时更新计数"""
        if value:
            self.selected_count += 1
        else:
            self.selected_count -= 1
        self._update_selection_count()

    def _update_selection_count(self):
        """更新已选择数量标签"""
        if not hasattr(self, 'selection_label') or not self.selection_label:
            try:
                self.selection_label = self.ids.selection_label
            except:
                return
                
        if self.selection_label:
            self.selection_label.text = f"已选择: {self.selected_count}"

    def _restore_selection(self):
         """恢复上次打开时的选中状态"""
         self.selected_count = 0
         for novel_type, checkbox in self.type_checkboxes.items():
              if novel_type in self.current_selection:
                   checkbox.active = True
                   self.selected_count +=1
              else:
                   checkbox.active = False
         self._update_selection_count()


    def select_all(self, select=True):
        """全选或取消全选当前显示的类型"""
        try:
            print(f"{'全选' if select else '取消全选'}当前显示的类型...")
            count_before = self.selected_count
            
            # 更新所有复选框
            for novel_type in self.filtered_types:
                if novel_type in self.type_checkboxes:
                    checkbox = self.type_checkboxes[novel_type]
                    if checkbox.active != select:
                        checkbox.active = select
            
            # 因为是批量操作，直接重新计算总数
            self.selected_count = sum(1 for nt in self.filtered_types if self.type_checkboxes.get(nt) and self.type_checkboxes[nt].active)
            self._update_selection_count()
            
            print(f"已{'选中' if select else '取消'} {self.selected_count} 种类型 (之前: {count_before})")
        except Exception as e:
            print(f"{'全选' if select else '取消全选'}出错: {str(e)}")
            import traceback
            traceback.print_exc()


    def get_selected_types(self):
        """获取所有选中的类型列表"""
        return [novel_type for novel_type, checkbox in self.type_checkboxes.items() if checkbox.active]

    def on_ok(self):
        """确认按钮回调"""
        try:
            print("确认选择...")
            selected = self.get_selected_types()
            print(f"已选择 {len(selected)} 种类型: {selected[:3]}...")
            
            # 触发回调
            if hasattr(self, 'parent_screen') and self.parent_screen and hasattr(self.parent_screen, 'update_selected_types'):
                print("正在调用父屏幕回调...")
                self.parent_screen.update_selected_types(selected)
                print("回调完成")
            else:
                print("警告: 无法找到父屏幕回调")
                
            self.dismiss()
        except Exception as e:
            print(f"确认选择出错: {str(e)}")
            import traceback
            traceback.print_exc()

    def on_cancel(self):
        """取消按钮回调"""
        try:
            print("取消选择")
            self.dismiss()
        except Exception as e:
            print(f"取消出错: {str(e)}")
            import traceback
            traceback.print_exc()

# 示例用法 (通常这个弹窗会从其他Screen中调用)
if __name__ == '__main__':
    from kivy.app import App

    class TestApp(App):
        def build(self):
            # 创建一个按钮来触发弹窗
            button = Button(text="打开多类型选择")
            
            # 将按钮添加到布局中
            layout = BoxLayout()
            layout.add_widget(button)

            # 绑定按钮事件
            def open_popup(instance):
                 popup = MultiTypePopup(language="中文", current_selection=["玄幻小说", "都市小说"])
                 # 假设父屏幕是App本身，用于回调
                 popup.parent_screen = self 
                 popup.open()
            
            button.bind(on_release=open_popup)
            return layout

        def update_selected_types(self, selected_types):
            print("主屏幕收到选择结果:", selected_types)

    TestApp().run() 