# AI Novel Generator (BatchScribe)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)]()

**Languages**: [中文](README.md) | **English**

An AI-powered novel generation tool that can create various types of novels with batch generation, continuation, and other advanced features. Currently supports Windows only.

## 📖 Detailed User Guide
For complete usage instructions and updates, please refer to: [AI Novel Generator Official Documentation](https://ccnql5c7kjke.feishu.cn/wiki/FXp9wHkozi8a3YkH3lRcw5EBn3f)

## 📄 Open Source License

This project is licensed under **GNU Affero General Public License v3.0 (AGPL-3.0)**.

### ⚠️ Important Notice

- **No Commercial Use**: This software is for learning and research purposes only, commercial use is prohibited
- **Mandatory Open Source**: Any modified code must also adopt the same open source license
- **Network Service Terms**: If providing services through the network, source code access must be provided

For detailed license terms, please see the [LICENSE](LICENSE) file.

### 💰 Commercialization Journey & Open Source Reflection

#### 📖 Making Money with AI Novel Writing on Xianyu in One Month (Not Selling Courses!)

**💡 The Inspiration**

About a month ago, I saw a sentence on the subway: "Instead of writing novels yourself, let AI write them and you be the director." That sparked an idea. Although I'm not a professional writer and my writing skills aren't great, I know what readers want to see, plus I'm familiar with the AI space. So I thought: **Can I create an automatic novel writing software?**

I got to work immediately, used some open-source models with fine-tuning, spent about two weeks, and created a demo with a clean interface that could quickly generate chapters.

**🧪 What Kind of Results Can It Achieve?**

I set up several popular novel templates, like "CEO + Substitute + Sweet Angst" and "Supernatural + Plot Twist + Short Addictive Fiction". Honestly, the AI-generated content isn't ready for direct publication on major platforms, but for second-hand platforms like Xianyu, it's completely sufficient!

Readers don't demand exceptional writing skills; as long as the plot is engaging and fast-paced, they're willing to pay for downloads.

**🤔 Why Choose Xianyu Instead of Other Platforms?**

Because I didn't want too much publicity, and I wasn't trying to build a big IP. I discovered:
- Promoting on WeChat, Xiaohongshu, and Bilibili is too "heavy" - requires persona building, video editing, copywriting
- Xianyu is a "light buying and selling" environment where people aren't too picky about content
- As long as you "solve their problems" like "can't find good novels/writer's block/don't want to write yourself", they're willing to pay!

My listings were simple: "Custom novel outlines/Auto-generate novels" "AI assistant helps you start writing quickly", and the response was surprisingly good!

**📌 Why Not Write Novels Myself to Make Money?**

This is particularly realistic. Writing novels is not only time-consuming but requires persistence. After the initial traffic bonus disappears, it's easy to get buried. But this tool "serves" those who write novels, meaning: **Don't be a novelist, be a "tool person" for novel writing.**

**💰 Commercialization Results**
- Half a year of development, solo independent development
- No investment, just an old computer and creativity
- Buddhist sales strategy, 30,000 yuan revenue in 3 months
- Proved the market value and commercial viability of AI novel generation tools

#### 😢 The Real Reason for Forced Open Source

**The Painful Experience of Technology Theft**:

Just when things were picking up, someone reverse-engineered it for commercialization. The model was exactly the same as mine, even the copy was stolen. I spent months working on compliance and applying for software copyright, but before it came through, they had already promoted it everywhere.

I really regret not adding reverse-engineering protection to the MVP!

**The Decision to Go Open Source**:
- Project was reverse-engineered, core technology leaked
- Chose to go open source proactively to protect intellectual property and developer rights
- Adopted AGPL-3.0 license to ensure any commercial use must be open source
- Made technology transparent to prevent malicious copying and unfair competition

#### 📎 What I Learned from This Experience

1. **Don't underestimate the commercial potential of "non-mainstream platforms"** - Xianyu isn't just for selling second-hand goods
2. **AI tools don't have to be about technical showing off** - they have value when used for "specific needs"
3. **Individual projects can also go "light"** - find your own small pond and you can live comfortably
4. **Technical protection is important** - consider intellectual property protection strategies before going open source

**Post-Open Source Monetization Suggestions**:
1. **Technical Services**: Provide customized development, technical consulting, system integration services
2. **SaaS Model**: Build cloud services based on open source code, charge subscription fees (must comply with AGPL license)
3. **Training & Education**: Conduct training courses on AI writing, prompt engineering, etc.
4. **Peripheral Products**: Develop supporting tools, template libraries, material packages, and other value-added products
5. **Community Operations**: Establish paid member communities, provide advanced features and professional support
6. **Licensing Partnerships**: Cooperate with publishers, content platforms, and other institutions for technical licensing

> **Note**: Any commercialization based on this project must strictly comply with the AGPL-3.0 license, ensuring code remains open source.

## 🌟 Features

- **Multiple Novel Types**: Supports 14 types including fantasy adventure, sci-fi future, martial arts, modern urban, mystery, etc.
- **Multi-AI Model Support**: Compatible with GPT, Claude, Gemini, Moonshot, and other advanced models
- **Custom Parameters**: Adjustable temperature, nucleus sampling, generation length, and other parameters
- **Batch Generation**: Generate multiple novels of different types simultaneously
- **Continuation Feature**: Continue creating existing novels
- **Auto-save**: Automatically saves content during generation to prevent data loss
- **Custom Prompts**: Provide personalized creative guidance for AI
- **Smart Retry**: Automatically retries on network issues to ensure uninterrupted generation
- **Novel Summaries**: Automatically generates novel summaries for easy management of long content
- **Modern Interface**: Intuitive user interface that simplifies the workflow
- **Media Generation**: Supports generating novel illustrations and audio
- **Multi-language Support**: Supports Chinese, English, and other languages

## 📋 System Requirements

- Python 3.7 or higher
- Windows 10/11, macOS, or Linux
- Minimum screen resolution: 1200x800
- Memory: Minimum 4GB, recommended 8GB+
- Disk space: Minimum 500MB (excluding generated novel content)

## 💻 Installation Guide

### Method 1: Install from Source

1. Ensure Python 3.7+ is installed

2. Clone the repository:
```bash
git clone https://github.com/147227/BatchScribe.git
cd BatchScribe
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the program:
```bash
python main.py
```

### Method 2: Use Pre-compiled Version
Download the latest version from the Releases page.

## 🚀 Quick Start

### Recommended AI Model Configuration
**Highly recommended**: `gemini-2.0-flash-exp`
- Excellent performance with high generation quality
- Fast speed, low cost
- API Key acquisition: Register at aiapi.space

### Usage Steps

1. **Configure API Key**: Enter the API key obtained from aiapi.space when starting the program for the first time
2. **Select Model**: Choose the recommended model
3. **Set Parameters**: Select novel type, target word count, and other basic parameters in the main interface
4. **Advanced Settings**: Click "Advanced Settings" to adjust temperature, nucleus sampling, and other parameters for detailed control
5. **Start Generation**: Click "Start Generation" to begin creation
6. **Real-time Monitoring**: You can "Pause" or "Stop" at any time during generation
7. **View Results**: Upon completion, generated novels will be automatically saved in the output directory

## 📁 Project Structure

```
novel_generator/
├── main.py                # Main program entry
├── main_wrapper.py        # Startup wrapper
├── core/                  # Core functionality
│   ├── generator.py       # Novel generator core logic
│   ├── model_manager.py   # Model management functionality
│   ├── media_generator.py # Media content generation
│   └── sanqianliu_*.py    # Sanqianliu interface support
├── ui/                    # User interface
│   ├── app.py             # Main application interface
│   ├── dialogs.py         # Various dialogs
│   └── assets/            # Interface resources
├── utils/                 # Utility functions
│   ├── config.py          # Configuration management
│   ├── common.py          # Common utility functions
│   └── logging.py         # Logging functionality
├── templates/             # Template files
│   └── prompts.py         # Novel generation prompt templates
├── dist/                  # Release versions
│   ├── AI小说生成器_v4.1.3/  # Executable program
│   ├── 更新日志_v4.1.3.txt   # Version update log
│   └── 发布说明_v4.1.3.md    # Release notes
├── novel_generator_app/   # Mobile app
├── resources/             # Resource files
└── docs/                  # Documentation
    ├── SOFTWARE_COPYRIGHT.md # Software copyright application document
    └── *.html             # Other technical documents
```

## 🏗️ Software Architecture

### Overall Architecture Design

This software adopts a modular architecture following high cohesion and low coupling design principles:

```
┌─────────────────────────────────────┐
│            main.py                  │
│      Program entry, environment init │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│             UI Layer (ui/)          │
│     User interface, parameter setup  │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│           Core Layer (core/)        │
│     Novel generation logic, AI calls│
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│          Data Layer (utils/)        │
│    Config management, file ops, logs│
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│        Template Layer (templates/)  │
│      Prompt templates, type defs    │
└─────────────────────────────────────┘
```

### Core Technical Features

1. **Advanced Prompt Engineering**: Multi-level prompt template system optimized for different novel types
2. **Asynchronous Concurrent Processing**: Efficient concurrent processing based on asyncio, supporting simultaneous generation of multiple novels
3. **Intelligent Context Management**: Dynamic management of AI model context windows ensuring coherence in long-form creation
4. **Modern GUI Design**: Modern interface based on Tkinter with high DPI display support
5. **Robust Error Handling**: Comprehensive error handling and automatic recovery mechanisms

## 🔬 Technical Principles Explained

### 🧠 AI Model Integration Architecture

#### Multi-Model Adapter Layer
```python
# Unified model interface design
class ModelManager:
    def __init__(self):
        self.models = {
            'openai': OpenAIAdapter(),
            'anthropic': ClaudeAdapter(), 
            'google': GeminiAdapter(),
            'moonshot': MoonshotAdapter()
        }
    
    async def generate(self, prompt, model_name, **kwargs):
        adapter = self.models[model_name]
        return await adapter.generate(prompt, **kwargs)
```

#### Intelligent Prompt Engineering

**Layered Prompt Architecture**:
- **System Layer**: Defines AI's role and basic rules
- **Type Layer**: Specialized instructions for different novel types
- **Context Layer**: Dynamic prompts maintaining story coherence
- **Optimization Layer**: Automatically adjusts parameters based on generation quality

```python
# Prompt template example
PROMPT_TEMPLATE = {
    'system': 'You are a seasoned novelist skilled at creating engaging stories',
    'genre_specific': {
        'Fantasy Adventure': 'Focus on world-building and logical magic systems',
        'Mystery': 'Emphasize clue placement and logical reasoning'
    },
    'context_management': 'Based on previous content: {previous_content}, continue creating...',
    'quality_optimization': 'Ensure smooth writing, tight plot, vivid characters'
}
```

### ⚡ Asynchronous Concurrent Processing Mechanism

#### Task Queue Management
```python
import asyncio
from asyncio import Queue, Semaphore

class NovelGenerator:
    def __init__(self, max_concurrent=3):
        self.semaphore = Semaphore(max_concurrent)
        self.task_queue = Queue()
        
    async def generate_batch(self, novel_configs):
        tasks = []
        for config in novel_configs:
            task = asyncio.create_task(
                self._generate_single(config)
            )
            tasks.append(task)
        
        return await asyncio.gather(*tasks, return_exceptions=True)
    
    async def _generate_single(self, config):
        async with self.semaphore:
            # Limit concurrency to avoid API limits
            return await self._call_ai_model(config)
```

#### Smart Retry Mechanism
```python
import backoff

@backoff.on_exception(
    backoff.expo,
    (aiohttp.ClientError, asyncio.TimeoutError),
    max_tries=3,
    max_time=300
)
async def _call_ai_model(self, prompt, **kwargs):
    """Smart retry with exponential backoff"""
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            self.api_url,
            json=self._build_request(prompt, **kwargs),
            timeout=aiohttp.ClientTimeout(total=60)
        )
        return await response.json()
```

### 🧩 Context Management Algorithm

#### Dynamic Window Management
```python
class ContextManager:
    def __init__(self, max_tokens=4000):
        self.max_tokens = max_tokens
        self.context_window = []
    
    def add_content(self, content):
        """Intelligently add content, auto-manage window size"""
        tokens = self._count_tokens(content)
        
        # If exceeding limit, intelligently trim important content
        while self._total_tokens() + tokens > self.max_tokens:
            self._remove_least_important()
        
        self.context_window.append({
            'content': content,
            'tokens': tokens,
            'importance': self._calculate_importance(content)
        })
    
    def _calculate_importance(self, content):
        """Calculate importance score based on content features"""
        score = 0
        # Dialogue and key plot points have higher weight
        if '"' in content or '「' in content:
            score += 2
        # Character descriptions and world-building have high weight
        if any(keyword in content for keyword in ['description', 'setting', 'background']):
            score += 1.5
        return score
```

## ⚙️ Configuration

Configuration items are saved in the `novel_generator_config.json` file. Main configuration items include:

| Configuration | Description | Recommended Value | Default Value |
| ------------- | ----------- | ----------------- | ------------- |
| API Key | Key for accessing AI services | Get from aiapi.space | - |
| Model | AI model to use | gemini-2.0-flash-exp | gemini-2.0-flash |
| Language | Language for novel generation | Chinese | Chinese |
| Novel Type | Type of novel to generate | Choose based on needs | Fantasy Adventure |
| Target Words | Word count for novel | 20000-50000 | 20000 |
| Concurrency | Number of novels to generate simultaneously | 2-3 (avoid API limits) | 3 |
| Auto-save Interval | Auto-save interval in seconds | 30-60 | 60 |
| Temperature | Creativity control | 0.7-0.9 | 0.8 |
| Nucleus Sampling | Randomness control | 0.9-0.95 | 0.9 |

### API Key Acquisition

1. Visit [aiapi.space](https://aiapi.space)
2. Register an account and complete verification
3. Get API key from the console
4. Enter the key in the software configuration

### Model Selection Recommendations

- **Beginner Recommended**: `gemini-2.0-flash-exp` - Balanced performance and cost
- **Quality Priority**: `claude-3-5-sonnet-20241022` - Highest literary quality
- **Speed Priority**: `gemini-2.0-flash` - Fastest generation speed
- **Logic Strong**: `gemini-2.0-flash-thinking-exp` - Suitable for complex plots

## 🤝 Contributing

We welcome all forms of contributions! Please follow these steps:

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## 📚 Technical Documentation

### Software Copyright Documentation

For detailed technical implementation and architecture design, please refer to: [Software Copyright Application Document](SOFTWARE_COPYRIGHT.md)

This document contains:
- Complete software architecture design
- Detailed functional specifications
- Core code analysis
- Data structures and algorithms
- Testing processes and results

### Development Environment Setup

```bash
# Clone repository
git clone https://github.com/147227/BatchScribe.git
cd BatchScribe

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run development version
python main.py
```

### Core Technology Stack

- **Programming Language**: Python 3.7+
- **Asynchronous Processing**: asyncio, aiohttp
- **GUI Framework**: Tkinter
- **AI Interfaces**: OpenAI, Anthropic, Google, Moonshot APIs
- **Packaging Tool**: PyInstaller

### Code Standards

- Use Python 3.7+ syntax
- Follow PEP 8 coding standards
- Add appropriate type annotations
- Write clear docstrings

## 👨‍💻 Author

- **GitHub**: [147227](https://github.com/147227)
- **Project URL**: [BatchScribe](https://github.com/147227/BatchScribe)
- **Official Documentation**: [Feishu Documentation](https://ccnql5c7kjke.feishu.cn/wiki/FXp9wHkozi8a3YkH3lRcw5EBn3f)
- **Technical Support**: Welcome to submit Issues or Pull Requests
- **Business Cooperation**: For technical consulting or custom development, please contact through GitHub

### 🎯 Project Vision

Although the project is open source, we believe **open source doesn't mean free, technology has value, service has value**. We hope to benefit more people through the power of the open source community while creating sustainable value for developers.

## 🙏 Acknowledgments

Thanks to all contributors and the open source community for their support.

Special thanks to:
- OpenAI, Anthropic, Google, Moonshot for providing excellent AI models
- The Python community for powerful development tools
- All users for their valuable feedback and suggestions

## 📞 Support

If you encounter any issues during use, please:
1. Check the [User Guide](USER_GUIDE.md)
2. Search existing [Issues](https://github.com/147227/BatchScribe/issues)
3. Submit a new Issue describing the problem in detail

---

⭐ If this project helps you, please give it a Star!
💡 Have commercialization ideas? Welcome to discuss cooperation and explore the infinite possibilities of AI writing together!

**Note**: Using this software indicates your agreement to comply with all terms of the AGPL-3.0 open source license.