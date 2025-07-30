# AI小说生成器 - 媒体生成功能使用指南

## 功能概述

AI小说生成器现已支持为每篇生成的小说自动创建封面图片和主题音乐。这些功能使用用户提供的API密钥调用相关服务，为小说增加视觉和听觉元素。

## 主要特性

### 📖 封面生成
- **自动化生成**：根据小说类型、主角信息和世界设定自动生成封面提示词
- **多张生成**：支持为每篇小说生成1-4张不同的封面选择
- **风格适配**：根据小说类型自动调整封面风格（奇幻、都市、科幻等）
- **高质量输出**：使用MidJourney API生成高质量4K封面图片

### 🎵 音乐生成
- **主题音乐**：根据小说类型和主题自动生成背景音乐
- **风格匹配**：不同类型小说生成对应风格的音乐
- **情感表达**：根据小说主题（爱情、友情、冒险等）调整音乐情感
- **专业品质**：使用Suno API生成专业级音乐作品

## 使用方法

### 1. 启用媒体生成功能

在主界面的设置区域中：

1. **生成封面图片**：勾选"生成封面图片"选项
2. **封面数量**：设置要生成的封面数量（1-4张）
3. **生成主题音乐**：勾选"生成主题音乐"选项

### 2. 开始生成

1. 设置其他小说生成参数（类型、字数等）
2. 点击"开始生成"按钮
3. 系统会先生成小说文本，然后自动生成封面和音乐

### 3. 查看结果

生成完成后，在输出目录中会找到：
- `小说文本.txt` - 小说正文
- `小说文本_meta.json` - 小说元数据
- `media_info.json` - 媒体文件信息（包含封面和音乐的下载链接）

## 技术细节

### API调用

#### 封面生成（MidJourney API）
```python
# 提交图片生成任务
POST /mj/submit/imagine
{
    "prompt": "fantasy adventure, magical world, epic landscape, handsome young man, book cover design, high quality",
    "botType": "MID_JOURNEY"
}

# 查询任务状态
POST /mj/task/list-by-condition
{
    "ids": ["task_id"]
}
```

#### 音乐生成（Suno API）
```python
# 提交音乐生成任务
POST /suno/submit/music
{
    "gpt_description_prompt": "Epic fantasy orchestral music with adventure themes",
    "make_instrumental": false,
    "mv": "chirp-v4"
}

# 查询任务状态
GET /suno/fetch/{task_id}
```

### 提示词生成逻辑

#### 封面提示词构成
1. **基础风格**：根据小说类型映射对应的视觉风格
2. **角色信息**：包含主角的性别、年龄等特征
3. **世界设定**：融入小说的背景设定
4. **艺术要求**：添加"book cover design"、"high quality"等质量要求

#### 音乐提示词构成
1. **音乐风格**：根据小说类型选择对应的音乐风格
2. **情感主题**：根据小说主题添加情感关键词
3. **乐器选择**：某些类型会指定特定乐器（如武侠的传统乐器）

## 类型映射表

### 封面风格映射
| 小说类型 | 封面风格 |
|---------|----------|
| 奇幻冒险 | fantasy adventure, magical world, epic landscape |
| 都市言情 | modern city, romantic atmosphere, urban lifestyle |
| 玄幻修真 | cultivation, immortal world, mystical mountains |
| 科幻未来 | futuristic, sci-fi technology, space age |
| 悬疑推理 | mystery, dark atmosphere, detective theme |
| 历史穿越 | historical, time travel, ancient architecture |
| 武侠江湖 | martial arts, ancient China, warriors |
| 恐怖灵异 | horror, supernatural, dark gothic |

### 音乐风格映射
| 小说类型 | 音乐风格 |
|---------|----------|
| 奇幻冒险 | Epic fantasy orchestral music with adventure themes |
| 都市言情 | Romantic modern pop music, soft and emotional |
| 玄幻修真 | Traditional Chinese instruments mixed with epic orchestral |
| 科幻未来 | Electronic synthwave music, futuristic sounds |
| 悬疑推理 | Dark mysterious music, tension building |
| 历史穿越 | Classical orchestral with historical instruments |
| 武侠江湖 | Traditional Chinese martial arts music |
| 恐怖灵异 | Horror ambient music, dark and scary |

## 注意事项

### 💰 费用说明
- 媒体生成功能会消耗额外的API费用
- 封面生成：每张图片约消耗相应的MidJourney API费用
- 音乐生成：每首音乐约消耗相应的Suno API费用

### ⏱️ 生成时间
- 封面生成：通常需要1-3分钟
- 音乐生成：通常需要2-5分钟
- 系统会自动等待生成完成，无需手动操作

### 🔧 故障排除
- 如果生成失败，请检查API密钥是否有效
- 确保账户有足够的API额度
- 网络连接问题可能导致生成超时

## 文件结构

生成完成后的文件结构示例：
```
novel_output_20241201_123456/
├── novel_1_奇幻冒险_林逸.txt          # 小说正文
├── novel_1_奇幻冒险_林逸_meta.json    # 小说元数据
└── media_info.json                    # 媒体信息
```

### media_info.json 文件格式
```json
{
  "novel_info": {
    "title": "小说标题",
    "genre": "奇幻冒险",
    "protagonist": {
      "name": "林逸",
      "gender": "男",
      "age": "青年"
    }
  },
  "cover_images": [
    {
      "index": 1,
      "url": "https://example.com/cover1.jpg",
      "task_id": "mj_task_123",
      "prompt": "fantasy adventure, magical world..."
    }
  ],
  "music": {
    "url": "https://example.com/music.mp3",
    "title": "主题音乐",
    "task_id": "suno_task_456",
    "prompt": "Epic fantasy orchestral music..."
  },
  "generated_at": "2024-12-01 12:34:56"
}
```

## 配置选项

在配置文件中，媒体生成相关的设置包括：
- `generate_cover`: 是否生成封面（true/false）
- `generate_music`: 是否生成音乐（true/false）
- `num_cover_images`: 封面图片数量（1-4）

## 更新日志

### v4.0.0 新增功能
- ✅ 支持自动生成封面图片
- ✅ 支持自动生成主题音乐
- ✅ 智能提示词生成
- ✅ 多种小说类型适配
- ✅ 媒体信息保存

---

**注意**：此功能需要有效的API密钥和足够的API额度。建议在使用前先进行小规模测试，确保功能正常工作。 