# 媒体生成功能最终版本

## 功能概述

已为AI小说生成器添加了封面图片和音乐生成功能，支持在小说生成完成后自动生成配套的封面图片和背景音乐。

## 主要特性

### ✅ **智能等待机制**
- **等待时间**：图片生成10分钟，音乐生成10分钟
- **检查频率**：每10秒自动查询一次任务状态
- **进度显示**：实时显示任务进度、已等待时间、剩余时间
- **不会提前报错**：只有超过10分钟才会显示超时

### ✅ **详细状态反馈**
```
[时间] 正在生成封面图片，提示词：fantasy adventure...
[时间] 封面图片 1 任务提交成功，任务ID: 1234567890
[时间] 等待图片任务完成: 1234567890，最长等待10分钟
[时间] 图片任务进度: 25%, 状态: IN_PROGRESS, 已等待: 60秒, 剩余: 540秒
[时间] 图片任务进度: 50%, 状态: IN_PROGRESS, 已等待: 120秒, 剩余: 480秒
[时间] 图片任务进度: 100%, 状态: SUCCESS, 已等待: 180秒, 剩余: 420秒
[时间] 图片任务 1234567890 完成！耗时: 180秒
```

### ✅ **智能提示词生成**
根据小说类型自动生成合适的提示词：
- **系统流**: fantasy adventure, magical world, epic landscape
- **都市言情**: modern romance, city background, elegant atmosphere  
- **玄幻修真**: cultivation fantasy, ancient chinese style, mystical energy
- **悬疑推理**: mystery thriller, dark atmosphere, suspenseful mood
- **科幻未来**: science fiction, futuristic technology, cyberpunk style
- **历史军事**: historical military, ancient battlefield, heroic spirit
- **女频文**: romantic fantasy, beautiful heroine, dreamy atmosphere

### ✅ **优雅错误处理**
- API调用失败时显示详细错误信息
- 媒体生成失败不影响小说正常生成和保存
- 超时时提供任务ID供用户后续查询

## 使用方法

### 1. 界面设置
在主界面的"媒体生成"区域：
- ☑️ **生成封面图片** - 勾选启用封面生成
- **封面数量**: 设置生成图片数量（1-5张）
- ☑️ **生成音乐** - 勾选启用音乐生成

### 2. API配置
确保在"API密钥"字段中填入有效的aiapi.space API密钥。

### 3. 生成流程
1. 配置小说生成参数（类型、字数等）
2. 勾选需要的媒体生成选项
3. 点击"开始生成"
4. 小说生成完成后，自动开始媒体生成
5. 耐心等待，系统会每10秒更新一次进度

### 4. 结果查看
- 生成的媒体信息保存在小说输出目录的 `media_info.json` 文件中
- 包含下载链接、任务状态、提示词等详细信息

## 技术实现

### 等待机制优化
- **图片生成**: 最长等待10分钟，每10秒检查状态
- **音乐生成**: 最长等待10分钟，每10秒检查状态
- **状态轮询**: 自动检测 `SUBMITTED` → `IN_PROGRESS` → `SUCCESS`
- **进度追踪**: 显示百分比进度和剩余时间

### API集成
- **MidJourney API**: `/mj/submit/imagine` 提交任务，`/mj/task/list-by-condition` 查询状态
- **Suno API**: `/suno/submit/music` 提交任务，`/suno/fetch` 查询状态
- **错误处理**: 详细的API响应日志和错误信息

### 文件结构
```
novel_output_xxx/
├── novel_xxx.txt           # 小说正文
├── novel_xxx_meta.json     # 小说元数据
├── media_info.json         # 媒体信息（新增）
└── summary.txt             # 小说摘要
```

## 示例输出

### media_info.json 文件内容
```json
{
  "novel_info": {
    "genre": "系统流",
    "protagonist": {
      "name": "林逸",
      "age": 27
    },
    "background": "现代都市"
  },
  "cover_images": [
    {
      "index": 1,
      "task_id": "1234567890",
      "status": "SUCCESS",
      "image_url": "https://cdn.aiapi.space/images/xxx.jpg",
      "prompt": "fantasy adventure, magical world...",
      "progress": "100%"
    }
  ],
  "music": {
    "task_id": "0987654321",
    "status": "complete",
    "audio_url": "https://cdn.aiapi.space/audio/xxx.mp3",
    "video_url": "https://cdn.aiapi.space/video/xxx.mp4",
    "title": "Epic Orchestral Theme",
    "prompt": "Epic orchestral music"
  },
  "generated_at": "2025-07-13 23:15:30"
}
```

## 注意事项

### 💰 **费用说明**
- 封面生成：每张图片约 $0.3-1.5
- 音乐生成：每首音乐约 $1.0-1.5
- 费用从aiapi.space账户余额扣除

### ⏱️ **时间预期**
- **封面图片**：通常1-5分钟，复杂图片可能需要8-10分钟
- **音乐生成**：通常2-8分钟，高质量音乐可能需要10分钟

### 🔧 **故障排除**
1. **API密钥无效**：检查aiapi.space账户余额和密钥有效性
2. **生成超时**：记录任务ID，可稍后手动查询
3. **生成失败**：查看详细错误信息，通常是余额不足或服务暂时不可用

## 更新日志

### v2.0 (最终版本)
- ✅ 将等待时间延长到10分钟
- ✅ 优化等待逻辑，每10秒检查一次
- ✅ 添加详细的进度显示（已等待时间、剩余时间）
- ✅ 移除复杂的任务管理界面，简化用户体验
- ✅ 超时时提供任务ID供手动查询
- ✅ 完善错误处理和状态反馈

### v1.0 (初始版本)
- ✅ 基础媒体生成功能
- ✅ 任务管理器和查询界面
- ✅ API集成和错误处理

## 文件清单

**核心文件**:
- `core/media_generator.py` - 媒体生成核心逻辑
- `core/media_task_manager.py` - 任务管理器（保留用于调试）
- `core/generator.py` - 集成媒体生成到小说生成流程
- `ui/app.py` - UI界面集成

**配置文件**:
- 媒体生成设置已集成到现有配置系统中

这个版本专注于用户体验，提供了稳定可靠的媒体生成功能，让用户可以轻松为小说生成配套的封面和音乐。 