# 版本信息
__version__ = "4.1.2"
__author__ = "147229"
__blog__ = "https://147227.xyz"

# 支持的模型列表（固定值）
SUPPORTED_MODELS = [
    "deepseek-chat",
    "deepseek-r1",
    "qwq-32b",
    "deepseek-r1-searching",
    "gpt-4.5-preview",
    "o3-mini-2025-01-31",
    "o1-2024-12-17",
    "o3-mini-all",
    "claude-3-7-sonnet-20250219",
    "claude-3-7-sonnet-thinking",
    "claude-3-7-sonnet-latest",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite-preview-02-05",
    "gemini-2.0-pro-exp-02-05",
    "gemini-1.5-pro-latest",
    "gemini-2.5-pro-exp-03-25",
    "gemini-2.5-pro-preview-03-25",
    "chatgpt-4o-latest",
    "moonshot-v1-128k",
    "deepseek-r1-2025-01-20",
    "deepseek-v3",
    "deepseek-v3-0324",
    "glm-4-airx",
    "qwen-max-2025-01-25",
    "qwen-max",
    "qwen-plus-latest",
    "qwq-32b-preview",
    "qwq-plus",
    "ERNIE-4.0-8K",
    "doubao-1-5-pro-256k-250115",
    "grok-3",
    "Phi-4",
    "gpt-4.1-2025-04-14",
    "o4-mini"
]

# 模型说明
MODEL_DESCRIPTIONS = {
    "deepseek-chat": "DeepSeek公司的对话模型，消耗8倍字数",
    "deepseek-r1": "DeepSeek公司的强大模型，消耗8倍字数",
    "qwq-32b": "QWQ公司的高级模型，消耗4倍字数",
    "deepseek-r1-searching": "DeepSeek公司的搜索增强模型，消耗8倍字数",
    "gpt-4.5-preview": "高级模型，消耗100倍字数",
    "o3-mini-2025-01-31": "Anthropic公司的轻量模型，消耗1/2倍字数",
    "o1-2024-12-17": "Anthropic公司的最新模型，消耗20倍字数",
    "o3-mini-all": "Anthropic公司的轻量模型，消耗4倍字数",
    "claude-3-7-sonnet-20250219": "Anthropic公司的高级模型，消耗8倍字数",
    "claude-3-7-sonnet-thinking": "Anthropic公司带思维链的高级模型，消耗8倍字数",
    "claude-3-7-sonnet-latest": "Anthropic公司的最新模型，消耗8倍字数",
    "gemini-2.0-flash": "Google的快速响应模型，消耗1倍字数",
    "gemini-2.0-flash-lite-preview-02-05": "Google的轻量快速模型，消耗1/3倍字数",
    "gemini-2.0-pro-exp-02-05": "Google的专业模型，消耗4倍字数",
    "gemini-1.5-pro-latest": "Google的专业模型新版本，消耗1倍字数",
    "gemini-2.5-pro-exp-03-25": "Google新模型，超级推荐！消耗3倍字数",
    "gemini-2.5-pro-preview-03-25": "Google新模型预览版，特性可能不稳定，消耗3倍字数",
    "chatgpt-4o-latest": "OpenAI的最新多模态模型，消耗8倍字数",
    "moonshot-v1-128k": "登月公司的高级模型，消耗10倍字数",
    "deepseek-r1-2025-01-20": "DeepSeek公司的优化模型，消耗8倍字数",
    "deepseek-v3": "DeepSeek公司的第三代模型，消耗4倍字数",
    "deepseek-v3-0324": "DeepSeek公司的第三代最新模型，消耗5倍字数",
    "glm-4-airx": "智谱AI的高级模型，消耗1倍字数",
    "qwen-max-2025-01-25": "阿里通义千问的高级大模型，消耗8倍字数",
    "qwen-max": "阿里通义千问的高级大模型，消耗8倍字数",
    "qwen-plus-latest": "阿里通义千问的高级模型，消耗4倍字数",
    "qwq-32b-preview": "QWQ公司的高级预览模型，消耗4倍字数",
    "qwq-plus": "QWQ公司的高级模型，消耗2倍字数",
    "ERNIE-4.0-8K": "百度文心一言的高级模型，消耗4倍字数",
    "doubao-1-5-pro-256k-250115": "豆包的高级版本，消耗2倍字数",
    "grok-3": "xAI公司的高级模型，消耗4倍字数",
    "Phi-4": "微软的轻量但高能力模型，消耗1倍字数",
    "gpt-4.1-2025-04-14": "OpenAI最新版GPT-4.1模型，性能优异，消耗12倍字数",
    "o4-mini": "Anthropic公司全新轻量高效模型，提供优秀的性能，消耗3倍字数"
}

# 添加通用标准提示词模板
STANDARD_PROMPT_TEMPLATE = """
请创作一篇引人入胜的小说，展现人物丰满的性格特点、独特的世界观和引人入胜的情节发展。

主角设定：
姓名：[PROTAGONIST_NAME]
性别：[PROTAGONIST_GENDER]
年龄：[PROTAGONIST_AGE]
性格特点：[PROTAGONIST_TRAITS]
外貌描述：[PROTAGONIST_APPEARANCE]
背景故事：[PROTAGONIST_BACKGROUND]

世界观设定：
背景设定：[WORLD_SETTING]
世界规则：[WORLD_RULES]
历史背景：[WORLD_HISTORY]
文化特点：[WORLD_CULTURE]

故事结构：
开场设计：[STORY_HOOK]
情节发展：[STORY_PLOT]
主要冲突：[STORY_CONFLICT]
高潮部分：[STORY_CLIMAX]
剧情转折：[STORY_TWIST]
结局解决：[STORY_RESOLUTION]

核心主题：
主题列表：[THEMES_LIST]
主题探索：[THEMES_EXPLORATION]

写作要求：
1. 保持内容连贯，情节发展符合逻辑
2. 人物刻画要立体，有成长和变化
3. 对话自然流畅，符合角色性格
4. 场景描写生动具体，有画面感
5. 情感表达真实深刻，避免过度煽情
6. 保持适当的叙事节奏，张弛有度
7. 语言风格统一，避免表达不一致
"""

# 小说类型特定提示词
GENRE_SPECIFIC_PROMPTS = {
    "奇幻冒险": "这是一个充满魔法、神秘生物和壮丽景观的世界。故事应包含主角踏上冒险之旅，面对各种挑战和敌人，最终实现成长和目标的过程。应深入描绘奇幻世界的独特魔法体系、种族特性和地理环境，构建丰富完整的世界观。主角应有明确的成长轨迹，从普通人逐渐掌握力量，最终在关键时刻展现英雄气概。冒险过程中应穿插扣人心弦的战斗场景、解谜环节和情感纠葛，让读者沉浸其中。故事应严格限制在奇幻世界设定内，避免引入现代科技或其他题材元素。魔法系统要保持内部一致性，遵循既定规则，不随意改变。",
    "科幻未来": "这是一个高科技、未来世界的故事，可能涉及太空旅行、人工智能、虚拟现实或其他先进技术。故事应探索科技对人类社会和个体的影响，并提出关于人性、伦理和存在的深刻问题。应塑造一个逻辑自洽的未来世界，包括社会结构、政治体系和经济模式，使其既富有想象力又具有一定科学合理性。主角的冒险不仅是物理上的探索，更应是对人类命运和科技边界的思考。可以融入关于人与机器关系、基因改造伦理、太空殖民等前沿话题，反映当代科技发展的忧虑与希望。科技设定应保持连贯性和合理性，不应违背基本物理法则或自相矛盾。避免引入纯魔法或超自然元素，除非有科学解释。",
    "校园文": "这是一个以学校为主要舞台的青春故事，聚焦校园生活的方方面面。故事必须严格限制在校园环境中展开，包括教室、操场、图书馆、食堂、社团活动室、宿舍等学校场景。应细致描绘校园日常：上课互动、课间交流、社团活动、考试压力、同学关系等，让读者真实感受校园氛围。主角的成长应紧密结合学校生活，通过学业挑战、人际关系、自我认知等校园特有的经历实现自我发展。情感线索应自然融入校园背景，如同窗情谊、师生互动、校园恋情，避免脱离校园环境的剧情发展。每个场景转换都应保持在学校范围内，只有极少数情节（如假期、外出）可暂时离开校园，但很快要回归。节奏上应避免大幅跳跃，保持日常生活的连贯性和细节刻画。",
    "悬疑推理": "这是一个围绕谜团和侦破过程展开的故事。故事核心必须包含一个或多个精心设计的谜题，贯穿始终。应精心设计线索链，确保每条线索都有其逻辑作用，既不能太过明显也不能无迹可寻。叙事节奏应重视悬念的营造和线索的逐步展开，避免过早揭示真相。人物塑造应为悬疑服务，包括可疑人物的动机和行为逻辑，侦探型角色的思维方式和调查手段。环境描写应强调氛围营造，使用光影、声音、天气等元素增强紧张感和神秘感。结局必须对所有关键线索做出合理解释，真相应在逻辑上自洽，避免出现硬伤或逻辑漏洞。整个故事应保持理性思维框架，即使有超自然元素，也要符合故事内部逻辑。",
    "浪漫爱情": "这是一个以情感关系为核心的故事，聚焦两人之间情感的萌发、发展、考验与结局。故事应细致描绘主角间的情感变化，包括心理活动、肢体语言、对话交流等微妙表现。必须设计合理的相遇场景和情感发展契机，避免关系发展过于突兀。应塑造有深度的感情阻碍或考验，可以是性格差异、环境限制、价值观冲突或外部干涉等。角色应有独特的情感需求和成长轨迹，在爱情中实现自我认知与成长。环境和场景应为情感氛围服务，创造浪漫、温馨或感人的氛围。节奏把控应重视情感铺垫，避免感情发展过快或无由头的剧情转折。对话设计应真实自然，反映角色性格和关系动态。整体风格应保持一致，避免爱情主线被其他元素过度稀释或偏离。",
    "穿越重生": "这是一个主角穿越到异世界或重生回过去的故事。故事核心在于主角如何利用现代知识或前世记忆，在新环境中创造不同命运。应详细描绘穿越/重生的机制和原因，以及主角面对身份变化的心理调适过程。主角应善用先知先觉的优势，但也要面对预知带来的责任和改变历史可能引发的蝴蝶效应。情节需要平衡爽感与挑战，既展现主角凭借现代知识或经验取得成功的快感，也设置原有时空规则带来的限制和阻碍。可探讨命运、选择与责任的哲学问题，以及人物在第二次人生中的成长与救赎。穿越规则应保持一致性，不应随剧情需要随意改变。对历史事件或异世界设定的改变应考虑连锁反应，保持逻辑合理性。",
    "玄幻修真": "这是一个以修真、修仙为核心的东方玄幻故事。故事应构建一个等级分明、规则清晰的修真体系，包括功法、境界、丹药、法宝等元素。主角从微末起步，通过历练、机缘和顿悟，一步步提升境界，最终问鼎巅峰。应描绘丰富多样的宗门势力、修真家族和秘境遗迹，以及它们之间的矛盾与争斗。修真之旅不仅是力量的提升，还应包含道法自然、寻求大道的哲学思考。战斗场景需具体描写功法运用和能量变化，营造出视觉冲击力。可融入仙家法器、飞行术、炼丹炼器等特色元素，增强东方玄幻韵味。修真体系需保持内部一致性，设定规则后不应随意更改。功法威力和境界提升应符合既定规则，避免无理由的突破或降级。",
    "现代言情": "这是一个以当代都市为背景，聚焦于恋爱关系发展的故事。故事应描绘当代年轻人的爱情观念、生活方式和价值追求。主角通常是现代都市青年，有自己的事业和生活目标。情节应紧扣现代生活场景，如写字楼、咖啡厅、高档餐厅、时尚街区等。感情发展要符合现代人相处模式，包括社交媒体互动、约会方式、沟通模式等现代元素。故事可融入职场竞争、家庭关系、闺蜜/兄弟情谊等辅助情节，丰富故事层次。对话应现代化、生活化，反映当代年轻人的语言特点。应刻画细腻的情感心理变化，展现当代情感关系中的矛盾和成长。现代言情应保持时代感，可适当融入流行文化、科技元素和社会热点，使故事更贴近当下生活。",
    "言情霸道总裁": "这是一个以强势成功的商业精英为男主角，讲述其与女主角之间情感发展的故事。男主角必须是商业帝国的掌控者，拥有显赫的社会地位、惊人的财富和卓越的商业才能。他的性格应强势、专制而自信，在商场上所向披靡，但在情感上可能有隐藏的柔软或伤痛。女主角通常普通但有特质，能打动高高在上的男主角。故事应包含男主角对女主角的强势追求或命运般的相遇，以及随之而来的地位差异、家族阻碍、商业纷争等冲突。商业场景描写要专业而精准，体现男主角的能力与魅力。感情发展中，需展现男主角的专横与关怀并存，逐渐为爱情软化的过程。故事节奏上通常包含相遇、冲突、误会、和好、最终幸福的经典模式，但应避免过度俗套。总裁形象塑造要立体，既有强势霸道的一面，也有责任担当和内心成长的过程。",
    "扮猪吃虎": """这是一个主角隐藏真实实力或身份，以弱者形象出现，最终关键时刻展露锋芒的故事。故事核心在于主角的身份反差与实力反转，制造出强烈的爽感。应设置充分的伪装动机，如隐藏身世、避开仇敌、测试他人或执行秘密任务等。主角表演的弱者形象要合理自然，既能蒙蔽其他角色，又不会显得刻意做作。情节设计应包含多个层次的反转，让读者随着主角的假扮而体验"扮猪"的乐趣，又能在关键点享受主角"吃虎"的痛快。应精心安排主角暗中使用真实能力的场景，既不暴露身份，又能解决危机，体现智谋与谋略。剧情需要设置适当的对手和敌人，为主角最终揭露真相做铺垫。主角性格塑造要深入，展现其在伪装下的真实想法和内心矛盾。故事节奏把控要合理，既有伪装期的悬念，又有真相揭露后的高潮与爽感。""",
    "爽文": "这是一个以主角一路高歌猛进、快意恩仇为核心的故事，着重于满足读者的情感需求和代入感。故事主角必须具备明显优势，如超凡天赋、奇遇机缘、重生记忆或系统辅助等，使其能够在各种挑战中脱颖而出。情节应设计连续性的成长曲线，主角要不断遭遇挫折然后迅速翻盘，每次危机后都能获得更强大的能力。对手安排要层层递进，从弱到强，始终为主角提供展示实力的舞台。爽感设计要多样化，包括实力碾压、仇敌报复、美女倾心、敌人震惊等多种满足读者期待的情节点。可融入连续性的升级元素，如等级提升、装备获取、技能掌握等，给予读者清晰的成长感受。节奏把控上要张弛有度，既有高潮迭起的战斗和逆袭，也有低谷中蓄势的调整与准备。主角形象不应单薄，需要在爽感基础上增加人物立体感和情感厚度，避免流于脸谱化。",
    "都市日常": "这是一个聚焦于现代城市生活日常点滴的故事，着重描写人与人之间的情感连接和个人成长。故事必须严格限定在当代都市场景中，如公寓、写字楼、咖啡厅、公园等城市常见场所。情节应关注日常小事，如工作琐事、邻里往来、朋友聚会、家庭互动、购物休闲等普通人生活中的细节。人物塑造应真实生活化，主角通常是普通人，有正常的工作、家庭和社交圈，面对着常见的生活烦恼和喜悦。故事节奏应舒缓自然，避免过于戏剧化的冲突和不切实际的情节转折，保持生活的真实感。可融入当代都市生活元素，如互联网、外卖、共享单车、社交媒体等现代化便利与烦恼。情感内核应聚焦于人在都市中的归属感、孤独感、温暖与成长，表达对现代生活的思考。对话和内心活动描写要自然贴近生活，避免过于文学化或理想化的表达方式。",
    "都市多女主": "这是一个以一位男性角色与多位女性角色之间情感互动为主线的都市故事。故事应合理设计多位性格各异、背景不同的女性角色，如职场精英、邻家女孩、校园才女、海归精英等多种类型，避免千篇一律的形象塑造。每位女性角色都需要有完整的人物设定、独特的性格特点和个人故事线，不能沦为单纯的花瓶角色。情节设计需要为每位女性角色创造与主角相遇、互动和产生情感的合理契机，避免牵强附会。主角形象必须立体丰满，有足够的魅力、能力或特质吸引不同类型的女性，同时要避免塑造为完美无缺的人设。故事应平衡发展各条情感线索，避免某一角色过度抢戏或长期缺场。情感发展应考虑现实伦理观念，处理好角色间的情感纠葛和可能的冲突。都市场景描写要精准，融入现代生活元素和社会环境特点，增强故事代入感。",
    "都市高武": "这是一个在现代都市背景下融入武道、超能力等非凡元素的故事。故事应建构一个隐藏在普通社会之下的武道体系或超能力世界，如古武传承、秘密武馆、地下格斗场、特殊能力者协会等。主角通常是接触到这一隐秘世界的普通人，或已经身处其中的武道修习者。世界观设定要合理自洽，解释为何强大的武力或超能力在现代社会中保持隐秘，以及这些力量的来源和限制。剧情需平衡都市生活与高武元素，主角可能有普通的职业和社交圈，同时又在暗中习武或执行特殊任务。武力体系设计要有层次感和规则性，可融入传统武术概念、气功、内力或现代改良的武道理念。战斗场景描写要精彩动感，展现高于常人的武技对决，但应避免过度夸张到违背物理定律。可融入现代元素如科技辅助、当代武器、现代医学与古武结合等创新点。情节发展应超越单纯的武力较量，融入都市阴谋、家族纷争、正义与邪恶的对抗等深层次主题。",
    "言情霸道总裁穿越": "这是一个融合霸道总裁和穿越元素的言情故事。男主角必须同时具备霸道总裁的强势魅力和穿越者的独特优势。故事可以是现代商业精英穿越到古代/异世界，利用现代知识和商业头脑成为那个世界的霸主；也可以是古代/异世界强者穿越到现代，凭借特殊能力或思维方式在商界崛起。穿越设定要合理，解释清楚穿越的方式、原因和规则。时空差异应成为故事的重要元素，主角需要适应新环境的规则和文化，并利用这种差异获得独特优势。女主角形象要丰满，可以是协助适应新环境的向导，或是与主角产生文化冲突后逐渐理解接纳的伙伴。情感发展应融入穿越带来的特殊情境，如价值观差异、时空阻隔的忧虑等。剧情需要平衡霸道总裁的强势魅力和穿越者的文化冲击，创造独特的情感张力。应设置与穿越身份相关的危机和挑战，如身份暴露的风险、对原世界的怀念或责任等。商业或权力场景的描写要精彩，展现主角如何利用穿越优势在新环境中建立霸业。整体故事节奏应在强势逆袭、商场博弈和感情发展之间取得平衡。",
    "女频玄幻": "这是一部以《苍兰诀》世界观为基础，融合《云之羽》背景架构的女频玄幻小说。故事核心围绕女主小兰花（变身为'云为衫'）从水云天司命殿的花神被迫穿越至《云之羽》世界的冒险。女主角必须拥有天道系统，通过完成'拯救炮灰、净化瘴气'的任务来升级系统，逐步解封息山神力，以获得回归水云天的机会。男主角宫远徵是冷峻聪慧却内心孤独的宫门继承者，两人的情感升温始于公子羽试炼期间，关系发展需展示云为衫的体内灼热缓解和灵力增强的神秘联系。故事应构建多条隐藏线索与悬念：公子羽实为长恒仙君的灵魂碎片与东方青苍记忆纠缠；宫远徵逐渐觉醒与小兰花前世的因缘；天道系统背后隐藏更大的布局；东方青苍神魂现寄于《大奉打更人》的许七安体内。叙事结构应多线并行，每个任务阶段设计一个情感转折和小高潮，情节应设置反转与伏笔，对话自然流畅，场景描写细腻丰富。风格应情感细腻、幻想瑰丽、节奏紧凑、兼具甜虐与热血。主题应围绕命运重构与成长治愈展开。故事最终应实现女主完成系统最终升级，与宫远徵共同返回水云天，育有双胞胎儿女的圆满结局。",
    "三千流": "这是一部500万字的玄幻武侠修仙类爽文小说，需要每隔几章设计爆点内容，增强读者的代入感和爽感。主角尤川从小是家族中的废柴，因母亲是妾室而地位低下，经常被族中长老甚至同龄人欺凌打骂。在目睹家族谋害其母亲后，尤川性格大变，为苟活而隐忍承担家族事务，暗中修炼《三千流》秘籍。《三千流》是一本包含各类武功和法宝炼制方法的神秘功法，主角需通过逐步领悟其中奥秘，不断突破自身极限。故事应构建一个完整的修真体系，设计多个宗门势力、修真家族和秘境，以及它们之间的明争暗斗。剧情发展要设置连续的成长曲线，让主角在家族轻视和朋友背叛中逐渐崛起，复仇之路既要有智谋又要有实力的体现。爆点情节应包含：关键时刻实力突破、强势复仇场景、隐藏身份揭露、获得珍稀功法或法宝、击败强敌等。需要塑造多位有深度的配角，既有死忠追随者，也有明枪暗箭的敌人，还有道德立场模糊的灰色人物。修真世界观要丰富多元，包含不同层次的修行境界、各类天材地宝、多样的法术流派和独特的神通异能。叙事风格应苍劲有力，战斗场景描写激烈畅快，既要有快节奏的打斗，也要有修行感悟的沉淀。情节安排上要起伏跌宕，关键转折处设计出人意料又在情理之中的变化。最终主角不仅要为母亲复仇，还要登临修真界巅峰，实现自身的价值和追求。",
    "社会现实": "这是一个温暖而真实的当代生活故事，聚焦于普通人的成长历程和人生感悟。故事应展现现代社会中人与人之间的温情互动，如邻里友善、职场合作、家庭和睦、师生情谊等美好的人际关系。主角通常是积极向上的普通人，可能是努力工作的白领、勤奋学习的学生、热心助人的社区志愿者、敬业的教师或医生等，他们通过自己的努力和善良影响着周围的人。故事应展现人物在面对生活挑战时的坚韧不拔和乐观精神，强调通过努力奋斗、互帮互助来实现个人成长和社会进步。情节发展应真实自然，通过日常生活中的温馨细节和感人瞬间来推动故事进展。可以涉及温暖的家庭生活、和谐的职场环境、友善的社区氛围、积极的社会参与等正面内容。叙事风格应温暖励志，传递正能量和人文关怀，通过真实感人的故事激励读者。主题应积极向上，强调希望、奋斗、善良、互助等正面价值观，体现人性的美好和社会的温暖。故事结局应给人以希望和启发，展现美好生活的可能性和人生的意义。"
}

# 添加小说类型列表
NOVEL_TYPES = {
    "中文": [
        "奇幻冒险", "科幻未来", "悬疑推理", "恐怖惊悚", "浪漫爱情", 
        "历史架空", "武侠仙侠", "都市生活", "青春校园", "军事战争", 
        "职场商战", "体育竞技", "狼人言情", "玄幻修真", "末世求生",
        "宫廷权谋", "灵异鬼怪", "穿越重生", "异世大陆", "星际探索",
        "机甲战争", "美食烹饪", "游戏竞技", "家族传奇", "医疗人生",
        "探险寻宝", "时空穿梭", "超能力者", "黑暗奇幻", "生存挑战",
        "东方玄幻", "西方魔法", "蒸汽朋克", "赛博朋克", "古代传奇",
        "现代都市", "异能特工", "海盗冒险", "西部荒野", "童话重塑",
        "神话传说", "末日废土", "异形怪物", "心理惊悚", "复仇传奇",
        "地下世界", "魔法学院", "龙与骑士", "亡灵世界", "远古文明",
        "变形生物", "虚拟现实", "音乐传奇", "艺术人生", "侦探悬案",
        "间谍特工", "商业帝国", "政治博弈", "传媒风云", "法律正义",
        "犯罪黑帮", "灾难求生", "动物视角", "植物奇谈", "校园文",
        "文学小说", "黑色犯罪", "商业叙事", "新兴成人", "多元文化",
        "生态环保", "心理惊悚", "哲学思辨", "实验文学", "历史重构",
        "社会现实", "哥特风格", "幻想写实", "政治寓言", "女性主义",
        "民族志", "都市幻想", "海洋奇谭", "未来考古", "数字生存",
        "灵异鬼妻", "古代宅斗", "修真重生", "系统流", "无敌文",
        # 新增小说类型
        "现代言情", "言情霸道总裁", "扮猪吃虎", "爽文", "都市日常", 
        "都市多女主", "都市高武", "言情霸道总裁穿越", "女频玄幻",
        "三千流"
    ],
    "English": [
        "Fantasy Adventure", "Science Fiction", "Mystery", "Horror Thriller", "Romance", 
        "Historical Fiction", "Martial Arts", "Urban Life", "Young Adult", "Military War", 
        "Workplace Drama", "Sports", "Paranormal Romance", "Cultivation", "Post-Apocalyptic",
        "Court Intrigue", "Supernatural", "Time Travel", "Alternate World", "Space Exploration",
        "Mecha", "Culinary", "Gaming", "Family Saga", "Medical Drama",
        "Treasure Hunt", "Time Manipulation", "Superhero", "Dark Fantasy", "Survival",
        "Eastern Fantasy", "Western Magic", "Steampunk", "Cyberpunk", "Ancient Legend",
        "Modern Urban", "Supernatural Agent", "Pirate Adventure", "Wild West", "Fairy Tale Retelling",
        "Mythology", "Wasteland", "Alien Creature", "Psychological Thriller", "Revenge Saga",
        "Underground World", "Magic Academy", "Dragons and Knights", "Afterlife", "Ancient Civilization",
        "Shapeshifter", "Virtual Reality", "Music Legend", "Artistic Life", "Detective Mystery",
        "Spy Thriller", "Business Empire", "Political Game", "Media Storm", "Legal Justice",
        "Crime Syndicate", "Disaster Survival", "Animal Perspective", "Plant Tale",
        "Literary Fiction", "Noir Crime", "Business Narrative", "New Adult", "Multicultural",
        "Eco Fiction", "Psychological Thriller", "Philosophical", "Experimental", "Historical Revisionism",
        "Social Realism", "Gothic", "Magical Realism", "Political Allegory", "Feminist",
        "Ethnography", "Urban Fantasy", "Maritime Tale", "Future Archaeology", "Digital Existence"
    ]
}

# 添加提示词模板
PROMPT_TEMPLATES = {
    "standard": STANDARD_PROMPT_TEMPLATE,
    "中文": {
        "奇幻冒险": [
            "华丽唯美的文学风格，注重场景描写和情感表达",
            "紧凑刺激的冒险风格，注重动作描写和情节推进",
            "幽默诙谐的轻松风格，融入巧妙的笑点和俏皮对话"
        ],
        "科幻未来": [
            "硬科幻风格，注重科学细节和技术描写",
            "软科幻风格，注重人文关怀和哲学思考",
            "赛博朋克风格，描绘高科技低生活的反乌托邦世界"
        ],
        "校园文": [
            "青春活力风格，描写校园生活的朝气与活力，突出学生纯真与成长",
            "细腻心理风格，深入刻画校园人物内心世界与心理变化",
            "校园日常风格，专注于学校生活的日常细节与真实感",
            "校园社交风格，聚焦同学之间、师生之间的复杂人际关系",
            "纯美文艺风格，以优美文笔描绘校园生活中的细腻情感与青春美好"
        ],
        "悬疑推理": [
            "侦探视角风格，跟随侦探角色的思维与行动，层层推进破案过程",
            "多线叙事风格，交替展示多条故事线索，制造悬念与反转",
            "心理悬疑风格，深入刻画人物心理变化，通过心理描写制造紧张感",
            "冷静客观风格，以理性分析和细节观察为主，突出逻辑推理过程",
            "环境氛围风格，注重场景描写和氛围营造，以环境渲染强化悬疑感"
        ],
        "浪漫爱情": [
            "温馨甜蜜风格，以温暖浪漫的氛围为主，注重情感的美好与治愈",
            "情感深度风格，探索复杂情感世界，关注情感的深度和冲突",
            "日常细节风格，通过生活小事的描写展现爱情的真实与平凡之美",
            "戏剧冲突风格，设置引人入胜的情感障碍和矛盾，增强故事张力",
            "唯美浪漫风格，以优美意境和抒情笔调描绘爱情，注重感官描写"
        ],
        "末世求生": [
            "残酷写实的生存风格，描绘末日环境的危险与挣扎",
            "人文关怀的反思风格，探讨灾难中的人性与希望",
            "科技导向的重建风格，关注人类如何利用科技重建文明"
        ],
        "宫廷权谋": [
            "细腻精致的宫廷风格，描绘华丽场景和微妙人际关系",
            "紧张刺激的阴谋风格，突出权力斗争和政治博弈",
            "历史厚重的正剧风格，结合真实历史背景展开故事"
        ],
        "灵异鬼怪": [
            "恐怖惊悚的阴森风格，营造紧张恐怖的氛围",
            "民俗文化的传统风格，融入中国传统鬼怪传说和民间信仰",
            "悬疑推理的探索风格，主角调查超自然现象并揭开真相"
        ],
        "穿越重生": [
            "轻松幽默的爽文风格，主角凭借现代知识轻松改变历史",
            "严肃正剧的历史风格，主角谨慎行动避免改变历史进程",
            "温情感人的成长风格，主角在新的人生中寻找自我价值"
        ],
        "异世大陆": [
            "宏大史诗的世界构建风格，着重描绘异世界的地理、种族和文化",
            "冒险探索的旅行风格，主角穿越异世界各地区探索未知",
            "政治外交的权谋风格，主角参与异世界的国家纷争和种族冲突"
        ],
        "星际探索": [
            "硬科幻的太空冒险风格，注重科学准确性和太空环境描写",
            "文明交流的外交风格，描绘人类与外星文明的接触和交流",
            "军事战争的太空战争风格，展现星际舰队之间的战略战术对抗"
        ],
        "机甲战争": [
            "热血激昂的战斗风格，描绘精彩的机甲对决场景",
            "技术细节的硬核风格，详细描写机甲构造和作战原理",
            "人机情感的共生风格，探索驾驶员与机甲之间的特殊联系"
        ],
        "美食烹饪": [
            "感官享受的美食描写风格，生动描绘食物的色香味形",
            "职场竞争的厨艺比拼风格，展现厨师之间的技艺较量",
            "温情治愈的生活风格，通过美食连接人与人之间的情感"
        ],
        "文学小说": [
            "内省深刻的文学风格，注重人物心理和情感变化的细腻描写",
            "意象丰富的象征风格，通过精心选择的意象和符号传达深层主题",
            "叙事从容的写实风格，通过日常细节折射人性和社会真相"
        ],
        "黑色犯罪": [
            "冷硬简洁的硬汉风格，以简短有力的对话和直白描述展现暴力世界",
            "阴郁压抑的氛围营造，通过环境描写强化故事的黑暗基调",
            "道德模糊的灰色叙事，模糊善恶界限，展现人性复杂性"
        ],
        "商业叙事": [
            "紧凑节奏的商战风格，以快速对话和决策描写推动情节发展",
            "专业术语的行业风格，融入商业术语和流程，增强专业感",
            "心理博弈的谋略风格，深入描绘商场上的战略思考和权力较量"
        ],
        "新兴成人": [
            "自我探索的成长风格，聚焦主角对自我定位和人生方向的寻找",
            "情感丰富的关系风格，着重描写年轻人之间复杂多变的情感连接",
            "现实挣扎的转型风格，描绘年轻人面对独立生活和责任的适应过程"
        ],
        "多元文化": [
            "文化碰撞的交融风格，描绘不同文化背景人物的互动与理解",
            "传统探索的认同风格，聚焦角色对自身文化传统的重新发现和认同",
            "跨界融合的混合风格，展现多元文化环境中新的生活和思维方式"
        ],
        "生态环保": [
            "犀利批判的揭露风格，直面社会问题，不回避尖锐议题",
            "细腻观察的日常风格，通过平凡生活折射社会现实",
            "多声部的群像风格，通过不同阶层人物展现社会全貌"
        ],
        "心理惊悚": [
            "意识流的心理风格，通过内心独白和思维跳跃展现角色心理",
            "紧张递进的悬念风格，逐步加深紧张感，营造心理压力",
            "错觉迷惑的感知风格，模糊现实与幻觉的界限，制造阅读悬疑"
        ],
        "校园穿越": [
            "先知视角的轻松风格，主角凭借对未来的了解轻松解决校园难题和挑战",
            "鱼out水感的冲突风格，主角努力适应陌生的校园环境和时代背景",
            "双重时空的复杂风格，主角在过去/未来校园和原时空之间建立联系或对比"
        ],
        "灵异鬼妻": [
            "惊悚恐怖风格，营造阴森可怕的气氛和紧张感",
            "温情浪漫风格，主角与鬼妻之间的深情互动与感人故事",
            "悬疑推理风格，探索鬼妻身世之谜和背后真相"
        ],
        "古代宅斗": [
            "精致细腻风格，描绘宫廷闺阁间的勾心斗角和人情冷暖",
            "智谋博弈风格，主角以智慧应对各种明枪暗箭",
            "家族情感风格，在宅斗中也不忘亲情伦理的温暖"
        ],
        "修真重生": [
            "快节奏爽文风格，主角凭借重生优势快速崛起",
            "谨慎成长风格，主角吸取前世教训稳步提升",
            "人情世故风格，重生后更注重人际关系的经营"
        ],
        "系统流": [
            "轻松幽默风格，主角与系统的诙谐互动",
            "数据成长风格，注重能力数值提升的详细描写",
            "任务挑战风格，围绕系统发布的各类任务展开故事"
        ],
        "无敌文": [
            "强势碾压风格，主角实力远超同阶对手",
            "谋略为主风格，主角虽强但更依靠智谋取胜",
            "战斗特效风格，注重华丽战斗场面和招式描写"
        ],
        "社会现实": [
            "温暖治愈风格，通过细致入微的生活细节展现人情温暖",
            "励志成长风格，展现普通人通过努力实现梦想的正能量故事",
            "温情写实风格，描绘现代生活中的美好瞬间和感人情感",
            "多元和谐风格，从不同人群的角度展现社会的包容与进步",
            "朴实感人风格，用真诚的语言讲述温暖的人生故事"
        ],
        # 为新增小说类型添加模板
        "现代言情": [
            "都市生活风格，注重现代都市场景和生活细节的描写",
            "情感细腻风格，深入刻画角色内心情感变化和成长",
            "职场恋爱风格，在职场竞争中发展的爱情故事",
            "轻松幽默风格，以诙谐的语言和情节展现青春爱情"
        ],
        "言情霸道总裁": [
            "强势追求风格，霸道总裁对女主角的强势追求和保护",
            "商战情场风格，商业斗争与爱情发展并行",
            "身世秘密风格，围绕角色隐藏的身世之谜展开故事",
            "契约恋爱风格，从契约关系发展为真挚感情的过程"
        ],
        "扮猪吃虎": [
            "智谋为主风格，主角运用智慧和谋略解决问题",
            "反转惊喜风格，设置多重反转和意料之外的情节",
            "实力展现风格，关键时刻展现真实实力的爽快感",
            "身份神秘风格，围绕主角真实身份展开的悬念和探索"
        ],
        "爽文": [
            "连续升级风格，主角不断获取新能力和突破",
            "打脸报复风格，主角对昔日轻视者的强势反击",
            "奇遇连连风格，主角频获机缘和各种宝物",
            "横扫天下风格，主角战无不胜攻无不克的快感"
        ],
        "都市日常": [
            "温馨治愈风格，展现都市生活中的温情与感动",
            "生活百态风格，描绘多样化的都市人生百态",
            "成长蜕变风格，角色在都市生活中的成长与蜕变",
            "人情冷暖风格，展示都市中的人情冷暖与真情流露"
        ],
        "都市多女主": [
            "均衡发展风格，多位女性角色均衡发展的情感线",
            "才艺展示风格，不同女性角色各展所长的精彩故事",
            "团队协作风格，主角与多位女性角色共同应对挑战",
            "情感纠葛风格，多角色间复杂情感关系的处理"
        ],
        "都市高武": [
            "隐秘江湖风格，描写隐藏在现代都市下的武道世界",
            "古今结合风格，传统武道与现代社会的碰撞融合",
            "势力争锋风格，各大武道势力之间的较量与冲突",
            "武技详解风格，详细描写武功招式和内功心法"
        ],
        "言情霸道总裁穿越": [
            "时空反差风格，强调不同时空背景下的文化冲突与适应",
            "商业崛起风格，主角利用穿越优势在商场快速崛起",
            "双重身份风格，主角在两个世界中身份反差的故事",
            "文化震撼风格，展现穿越者对新世界的冲击与改变",
            "强势护爱风格，霸道总裁为爱不顾一切的深情表现"
        ],
        "玄幻修真": [
            "正统修真风格，注重修炼体系与境界提升，展现追求大道的历程",
            "江湖风格，重在人物纷争与势力冲突，融入江湖气息",
            "仙侠风格，融合修真与武侠元素，兼具飘逸灵动与侠义精神",
            "大气磅礴风格，宏大世界观与恢宏战斗场面，气势恢宏",
            "哲理思辨风格，通过修真历程探讨生命意义与天道规则"
        ],
        "女频玄幻": [
            "情感细腻风格，深入刻画人物内心情感变化，展现细腻情感纠葛",
            "瑰丽幻想风格，构建绚丽多彩的幻想世界，场景描写华美动人",
            "甜虐交织风格，甜蜜与虐心情节交替出现，情感起伏强烈",
            "成长治愈风格，聚焦角色内心创伤的治愈与自我成长历程",
            "隐喻寓意风格，通过穿越重生探讨命运、责任与自我认知"
        ],
        "三千流": [
            "玄幻武侠风格，融合奇幻与武侠元素，展现独特的修真世界",
            "爽文风格，情节紧凑，爽点密集，增强阅读快感",
            "修真体系丰富，包含多种武功和法宝，展现修真者的成长历程"
        ]
    },
    "English": {
        "Fantasy Adventure": [
            "Elegant literary style with focus on scenery and emotions",
            "Fast-paced adventure style with focus on action and plot",
            "Humorous and light-hearted style with clever jokes and witty dialogue"
        ],
        "Post-Apocalyptic": [
            "Harsh realistic survival style depicting the dangers and struggles of post-apocalyptic environments",
            "Humanistic reflective style exploring human nature and hope amidst disaster",
            "Technology-oriented rebuilding style focusing on how humans use technology to rebuild civilization"
        ],
        "Court Intrigue": [
            "Delicate and refined court style depicting gorgeous scenes and subtle interpersonal relationships",
            "Tense and exciting conspiracy style highlighting power struggles and political games",
            "Historically weighty drama style combining real historical backgrounds with fictional stories"
        ],
        "Literary Fiction": [
            "Introspective literary style with focus on nuanced character psychology and emotional development",
            "Symbolic style rich in imagery, conveying deeper themes through carefully chosen symbols",
            "Measured realistic style reflecting human nature and social truths through everyday details"
        ],
        "Noir Crime": [
            "Hard-boiled style with concise dialogue and straightforward descriptions of a violent world",
            "Gloomy atmospheric style enhancing the dark tone through environmental descriptions",
            "Morally ambiguous narrative blurring the lines between good and evil"
        ],
        "Business Narrative": [
            "Fast-paced business style with quick dialogue and decision-making driving the plot",
            "Industry-specific style incorporating business terminology and processes for authenticity",
            "Strategic style delving into business strategy and power dynamics"
        ]
    }
}

# 添加结局提示词
ENDING_PROMPTS = {
    "中文": {
        "奇幻冒险": [
            "创造一个圆满的结局，主角完成冒险并获得成长",
            "设计一个开放式结局，暗示新的冒险可能开始",
            "构建一个感人的结局，强调友情和牺牲的主题"
        ],
        "科幻未来": [
            "设计一个发人深省的结局，探讨科技与人性的关系",
            "创造一个令人惊讶的转折，揭示故事中隐藏的真相",
            "构建一个开放式结局，留下未来世界的无限可能"
        ],
        "校园文": [
            "毕业季结局，伴随着毕业典礼或毕业前的最后时光，展现成长与别离",
            "未来展望结局，角色们规划未来道路，表达对校园生活的不舍与对未来的期待",
            "情感圆满结局，主要感情线索得到圆满解决，带来温暖和满足感",
            "校园传承结局，角色们将自己的经验传递给学弟学妹，形成精神延续",
            "青春纪念结局，通过某个校园活动或仪式，总结校园生活的意义与收获"
        ],
        "悬疑推理": [
            "完美解谜结局，所有线索完美串联，谜题得到合理解释，展现侦探才智",
            "反转结局，最后一刻出现意料之外的真相反转，颠覆读者先前认知",
            "开放解读结局，提供多种可能的解释，留给读者思考和讨论空间",
            "正义实现结局，破案后邪恶得到惩罚，正义得到伸张，恢复社会秩序",
            "灰色地带结局，即使真相大白，但涉及的道德困境没有绝对答案"
        ],
        "浪漫爱情": [
            "幸福团圆结局，恋人克服障碍最终走到一起，获得圆满的爱情",
            "成长分离结局，双方因为各自成长需要而分开，但爱情使彼此都有所成长",
            "暂时别离重逢结局，经历一段分离后因缘际会再次相遇，爱情重获新生",
            "平凡相守结局，没有轰轰烈烈的表白，而是选择平淡踏实地相互陪伴",
            "开放式结局，爱情故事未完待续，为未来的可能性留下想象空间"
        ],
        "末世求生": [
            "创造一个希望的结局，主角找到新的生存家园或重建社会",
            "设计一个现实的结局，展现末世环境中的持续挣扎和适应",
            "构建一个反思性结局，探讨导致末世的原因和人类的未来"
        ],
        "宫廷权谋": [
            "设计一个成功的结局，主角在权力斗争中获胜并实现理想",
            "创造一个悲剧性结局，展现权力争夺的代价和无情",
            "构建一个和解的结局，对立方达成某种平衡或共识"
        ],
        "灵异鬼怪": [
            "创造一个解谜的结局，揭示所有超自然现象的真相或原理",
            "设计一个恐怖的结局，留下永恒的谜团或新的恐惧",
            "构建一个和解的结局，人与超自然存在达成某种理解或平衡"
        ],
        "文学小说": [
            "设计一个开放式结局，留下思考空间，不提供简单答案",
            "创造一个微妙的转变结局，角色内心达到某种顿悟或和解",
            "构建一个循环式结局，呼应开头，暗示生活的循环本质"
        ],
        "黑色犯罪": [
            "创造一个黑暗结局，主角最终未能逃脱命运，展现世界的残酷",
            "设计一个代价高昂的胜利，主角虽然达成目标但付出惨重代价",
            "构建一个道德模糊的结局，胜利与失败的界限变得不再清晰"
        ],
        "商业叙事": [
            "设计一个战略胜利结局，主角通过智慧和远见赢得商业竞争",
            "创造一个价值重估结局，主角重新思考成功的真正意义",
            "构建一个新起点结局，一个商业时代结束，新的机遇出现"
        ],
        "社会现实": [
            "创造一个微小改变结局，虽无法改变整个社会，但点燃希望火种",
            "设计一个清醒认知结局，主角接受现实局限但保持内心尊严",
            "构建一个集体行动结局，个体联合起来应对共同的社会挑战"
        ],
        "校园穿越": [
            "留在新世界结局，主角完全融入校园生活，放弃返回原世界的机会",
            "返回原点结局，主角完成使命后回到原来的时空，带着成长和收获",
            "双世界共存结局，主角找到在两个时空/世界之间自由穿梭的方法"
        ],
        "灵异鬼妻": [
            "创造一个超越生死的结局，主角与鬼妻之间的爱情突破阴阳界限",
            "设计一个温柔离别的结局，鬼妻最终解脱转世，留下美好回忆",
            "构建一个双世界共存的结局，主角找到方法在阴阳两界之间建立联系"
        ],
        "古代宅斗": [
            "设计一个权力掌控的结局，主角成功掌握家族大权，改变家族命运",
            "创造一个明哲保身的结局，主角选择退出权力争斗，寻求平静生活",
            "构建一个改革创新的结局，主角打破传统规则，建立新的家族秩序"
        ],
        "修真重生": [
            "创造一个完美逆转的结局，主角彻底改变前世悲剧，达成所有心愿",
            "设计一个超越命运的结局，主角不仅改变自己命运，还影响整个修真世界",
            "构建一个大道共存的结局，主角领悟天道规则，找到生命真谛和修真意义"
        ],
        "系统流": [
            "设计一个系统完成的结局，主角达成系统所有任务，获得终极奖励",
            "创造一个超越系统的结局，主角摆脱系统限制，获得真正自由",
            "构建一个融合进化的结局，主角与系统深度融合，创造全新的存在方式"
        ],
        "无敌文": [
            "创造一个称霸天下的结局，主角成为世界无可争议的最强者",
            "设计一个寻找对手的结局，主角踏上寻找能与自己一战的存在之路",
            "构建一个超越力量的结局，主角领悟无敌之外的人生真谛和责任"
        ]
    },
    "English": {
        "Fantasy Adventure": [
            "Create a satisfying ending where the protagonist completes the adventure and grows",
            "Design an open ending that hints at new adventures to come",
            "Build a touching ending that emphasizes themes of friendship and sacrifice"
        ],
        "Post-Apocalyptic": [
            "Create a hopeful ending where the protagonist finds a new home or rebuilds society",
            "Design a realistic ending showing continued struggle and adaptation in the post-apocalyptic environment",
            "Build a reflective ending exploring the causes of the apocalypse and humanity's future"
        ],
        "Court Intrigue": [
            "Design a successful ending where the protagonist wins the power struggle and achieves their goals",
            "Create a tragic ending that shows the high cost of power struggles and political games",
            "Build an open ending that leaves room for interpretation and future possibilities"
        ],
        "Literary Fiction": [
            "Design an open ending that leaves room for thought without providing simple answers",
            "Create a subtle transformation ending where characters reach an internal realization or reconciliation",
            "Build a circular ending that echoes the beginning, suggesting the cyclical nature of life"
        ],
        "Noir Crime": [
            "Create a dark ending where the protagonist fails to escape their fate, showing the cruelty of the world",
            "Design a pyrrhic victory where the protagonist achieves their goal but at terrible cost",
            "Build a morally ambiguous ending where the line between victory and defeat is blurred"
        ],
        "Business Narrative": [
            "Design a strategic victory ending where the protagonist outsmarts their competitors",
            "Create a value reevaluation ending where the protagonist rethinks the true meaning of success",
            "Build a new beginning ending where one business era ends and new opportunities emerge"
        ]
    }
}

# 添加新的结构化提示词分类
NARRATIVE_TECHNIQUES = {
    "中文": {
        "叙事视角": [
            "第一人称限制视角，通过主角的眼睛观察世界，增强代入感",
            "全知视角，深入每个角色的内心世界，展现全景式故事",
            "第三人称限制视角，聚焦于主角但保持一定客观性",
            "多视角交替，通过不同角色视角拼凑完整故事图景",
            "不可靠叙述者，叙述者的观点和记忆可能有误或有意欺骗"
        ],
        "叙事结构": [
            "线性叙事，按时间顺序推进故事，清晰明了",
            "非线性叙事，打乱时间顺序，通过闪回和预视构建故事",
            "框架叙事，故事中套故事，外层故事为内层故事提供背景",
            "平行叙事，同时展开多条故事线，最终交汇或相互映衬",
            "碎片化叙事，通过片段拼接构建整体，留给读者更多解读空间"
        ],
        "语言风格": [
            "简洁直白，用最精炼的语言传达最丰富的内容",
            "华丽修辞，运用丰富的比喻、排比等修辞手法增强文学性",
            "口语化叙述，接近日常对话，增强亲近感和现实感",
            "意识流，模拟人物思维流动，不受常规语法约束",
            "诗化语言，注重语言的韵律感和意象美，富有抒情性"
        ],
        "氛围营造": [
            "紧张悬疑，通过细节描写和节奏控制制造紧张感",
            "浪漫温馨，通过柔和意象和情感描写创造温暖氛围",
            "荒诞怪异，打破常规认知，制造陌生化效果",
            "史诗宏大，通过庞大场景和重大事件创造史诗感",
            "日常闲适，通过生活细节描写营造平和舒适的氛围"
        ],
        "主题表达": [
            "象征寓意，通过具体形象隐喻深层主题",
            "戏剧冲突，通过尖锐对立展现主题矛盾",
            "细节积累，通过日常小事的累积彰显主题",
            "对比映衬，通过人物或情境的对比突出主题",
            "开放讨论，呈现多种观点，不给出简单结论"
        ]
    },
    "English": {
        "Narrative Perspective": [
            "First-person limited perspective, viewing the world through the protagonist's eyes",
            "Omniscient perspective, delving into each character's inner world",
            "Third-person limited perspective, focusing on the protagonist while maintaining objectivity",
            "Multiple alternating perspectives, piecing together the complete story through different viewpoints",
            "Unreliable narrator, whose perspective and memories may be flawed or deliberately deceptive"
        ],
        "Narrative Structure": [
            "Linear narrative, progressing the story in chronological order",
            "Non-linear narrative, disrupting time sequence through flashbacks and foreshadowing",
            "Frame narrative, stories within stories, where outer stories provide context for inner ones",
            "Parallel narrative, developing multiple storylines simultaneously",
            "Fragmented narrative, constructing the whole through pieces, leaving room for interpretation"
        ],
        "Language Style": [
            "Concise and straightforward, conveying rich content with minimal language",
            "Ornate rhetoric, using rich metaphors and parallel structures to enhance literary quality",
            "Colloquial narration, close to everyday conversation for approachability",
            "Stream of consciousness, simulating the flow of thought without conventional grammar",
            "Poetic language, emphasizing rhythm and imagery, rich in lyricism"
        ]
    }
}

# 添加人物塑造提示词
CHARACTER_DEVELOPMENT = {
    "中文": {
        "性格类型": [
            "复杂矛盾型，内心充满冲突，行为不总是一致",
            "成长蜕变型，随着故事推进经历重大性格转变",
            "理想主义型，有强烈的理想和原则，不愿妥协",
            "实用主义型，注重实际利益，灵活适应环境",
            "反英雄型，有明显缺点但最终为正义事业奋斗",
            "悲剧英雄型，有致命弱点导致最终失败",
            "边缘人物型，处于社会边缘，有独特视角",
            "隐藏身份型，拥有秘密或双重身份，内外表现反差明显"
        ],
        "人物关系": [
            "亦敌亦友关系，敌对中包含尊重，冲突中孕育理解",
            "师徒关系，包含教导、成长与最终超越",
            "复杂家庭关系，爱与矛盾交织，影响人物核心性格",
            "对立互补关系，性格迥异但互相弥补不足",
            "三角关系，三方之间的复杂情感和权力动态",
            "群体归属关系，个体与集体认同间的张力",
            "孤独探索关系，主角与自我和解的内心旅程"
        ],
        "校园角色关系": [
            "同窗密友关系，共同经历学习生活的挚友，彼此支持鼓励",
            "班级对手关系，在学习成绩或特长方面的良性竞争者",
            "学长学妹关系，包含引导与仰慕，潜在的情感可能",
            "师生互动关系，严格要求与温暖鼓励并存的特殊情感",
            "同桌关系，朝夕相处产生的微妙情感与默契",
            "社团伙伴关系，因共同爱好或理想而凝聚的团队纽带",
            "暗恋情愫关系，青涩含蓄的情感表达与内心挣扎",
            "青梅竹马关系，童年玩伴发展为复杂情感的特殊羁绊",
            "班级小团体关系，校园中的小型社交圈与归属感",
            "校园情侣关系，纯真甜蜜但面临成长与未来的考验"
        ],
        "悬疑角色关系": [
            "侦探与助手关系，智慧引导与忠诚协助的互补配合",
            "侦探与嫌疑人关系，观察与反观察的心理较量",
            "侦探与受害者关系，通过调查形成的跨越生死的理解",
            "真凶与替罪羊关系，欺骗与被欺骗交织的复杂纠葛",
            "多重嫌疑人关系，共同隐藏秘密但各怀心思的复杂网络",
            "调查者与阻碍者关系，寻求真相与掩盖真相的对抗",
            "知情者与局外人关系，掌握部分真相与完全无知的信息差",
            "复仇者与目标关系，隐藏在案件背后的恩怨情仇"
        ],
        "爱情角色关系": [
            "初恋关系，纯真美好但经验不足导致的甜蜜与笨拙",
            "知己情侣关系，深度理解与欣赏成为感情基础",
            "欢喜冤家关系，表面对立但内心相互吸引的矛盾情感",
            "日久生情关系，从普通朋友或同事逐渐发展为恋人",
            "一见钟情关系，强烈的第一印象与吸引引发的感情",
            "重逢旧爱关系，曾经分离后再次相遇，面对过去与现在",
            "忘年恋关系，跨越年龄差距的爱情与理解",
            "跨文化恋情，不同背景与价值观碰撞中的互相适应",
            "三角恋关系，复杂的情感纠葛与选择困境",
            "双向暗恋关系，彼此暗恋却因误解或胆怯未能表达"
        ],
        "动机塑造": [
            "创伤驱动，过去的伤痛成为行动的隐性动力",
            "价值追求，对特定理念或价值的坚持推动行动",
            "关系纽带，为重要他人而行动的情感驱动",
            "自我超越，突破自身局限的成长欲望",
            "复仇动机，为报不公或伤害而采取行动",
            "生存本能，在极端环境中的求生意志",
            "好奇探索，对未知世界和知识的渴求",
            "使命担当，肩负特定历史或命运使命的责任感"
        ]
    },
    "English": {
        "Character Types": [
            "Complex and contradictory, full of internal conflicts with inconsistent behaviors",
            "Growth and transformation oriented, undergoing major personality changes as the story progresses",
            "Idealistic, with strong ideals and principles, unwilling to compromise",
            "Pragmatic, focused on practical benefits, adaptable to environments",
            "Anti-hero, with obvious flaws but ultimately fighting for justice",
            "Tragic hero, with fatal weaknesses leading to ultimate failure",
            "Marginal character, on the edge of society with unique perspectives"
        ],
        "Character Relationships": [
            "Frenemies, containing respect within enmity and understanding within conflict",
            "Mentor-student relationship, including teaching, growth and eventual surpassing",
            "Complex family relationships, interweaving love and contradictions",
            "Contrasting complementary relationships, vastly different but mutually compensating",
            "Triangle relationships, complex emotions and power dynamics between three parties",
            "Group belonging, tension between individual and collective identity",
            "Solitary exploration, the protagonist's inner journey toward self-reconciliation"
        ]
    }
}

# 添加情节发展提示词
PLOT_DEVELOPMENT = {
    "中文": {
        "开场设计": [
            "悬念型开场，以谜团或危机引出故事",
            "日常切入型开场，从平凡生活场景切入，暗示变化将至",
            "闪回型开场，以回忆或过去事件暗示故事主线",
            "场景描写型开场，以环境氛围描写设定故事基调",
            "对话型开场，通过角色间对话引出背景和冲突",
            "震撼转场型开场，主角突然被抛入全新环境，引发强烈对比"
        ],
        "冲突设计": [
            "内外双重冲突，主角同时面临内心挣扎和外部阻力",
            "逐层升级冲突，随故事推进冲突不断加深和复杂化",
            "价值观冲突，不同价值理念间的根本性对立",
            "身份认同冲突，角色对自我定位的质疑和重建",
            "关系冲突，角色间的信任、忠诚和理解的考验",
            "环境冲突，角色与自然、社会或科技环境的对抗",
            "时空冲突，不同时空或平行世界规则的碰撞与矛盾"
        ],
        "校园情节": [
            "入学适应，描写主角适应新学校环境、结交朋友的过程",
            "考试挑战，围绕重要考试展开的备考、临场发挥与结果",
            "社团活动，通过参与社团展现特长、建立友谊与面对挑战",
            "班级矛盾，处理班级内部分歧、误会或竞争的过程",
            "校园比赛，参与各类竞赛展示才能、团队协作与成长",
            "师生互动，与关键教师的互动对主角产生的重要影响",
            "青涩恋情，初恋情感的懵懂、表达与发展的细腻描写",
            "同窗友谊，深厚友情的建立、考验与成长的过程",
            "成长抉择，面对未来方向、价值观等重要人生选择",
            "校园活动，文化节、运动会等集体活动中的精彩故事",
            "学业困难，面对学习瓶颈或特定科目挑战的故事",
            "寝室生活，舍友相处、矛盾与和解的日常",
            "家校联动，家庭背景与学校生活相互影响的情节",
            "小小叛逆，在规则与自我表达间寻找平衡的成长经历",
            "特殊节日，在校园中度过的节日带来的特别经历与感受"
        ],
        "悬疑情节": [
            "初始谜团，一个引人入胜的谜题或案件作为故事起点",
            "线索发现，主角逐步收集和分析各种线索的过程",
            "调查访谈，通过与相关人物交谈获取信息和观察反应",
            "误导线索，设置误导读者和角色的假线索，增加破案难度",
            "危险探索，主角冒险进入危险区域收集关键证据",
            "关键证物，发现或理解决定性证据的关键时刻",
            "嫌疑人分析，深入挖掘各个嫌疑人的动机、机会和能力",
            "追踪跟踪，秘密观察嫌疑人或相关人物的行动",
            "真相预示，通过细微线索或巧妙暗示预告真相",
            "解谜时刻，主角将所有线索串联起来，解开谜团",
            "真相揭露，最终真相大白的戏剧性时刻",
            "罪犯对质，与真凶的最终对峙或智慧较量",
            "动机解析，深入探讨罪犯的心理和行为动机",
            "案后影响，案件解决后对各个角色的心理和生活影响"
        ],
        "爱情情节": [
            "初遇契机，安排独特而有意义的首次相遇场景",
            "相互吸引，通过细节描写展现两人之间的微妙吸引力",
            "日常互动，在平凡生活场景中的自然互动与了解",
            "情感萌芽，意识到对对方的特殊感情的微妙时刻",
            "误会冲突，因误解或外部因素导致的情感波折",
            "情感表白，真诚表达爱意的勇气与方式",
            "约会体验，共同经历特别活动或日常约会的温馨",
            "关系考验，面对家人反对、距离、第三者等挑战",
            "情感升温，关系逐渐深入，互相理解与依赖加深",
            "分离危机，因某种原因必须面临分离的困境",
            "和好重聚，克服障碍后的重新相聚与理解",
            "承诺时刻，对未来做出承诺的重要决定",
            "成长蜕变，通过爱情关系实现个人成长与改变",
            "平凡相守，在日常生活中建立稳定而温暖的关系"
        ],
        "转折设计": [
            "误解消除转折，关键信息揭示改变人物关系",
            "背叛反转转折，信任的人物出乎意料地背叛",
            "身份揭露转折，角色真实身份或过去的揭示",
            "环境变化转折，外部条件突变迫使计划改变",
            "内心醒悟转折，主角价值观或目标的根本性改变",
            "帮助出现转折，意外援助或新盟友的加入"
        ],
        "高潮设计": [
            "内外结合型高潮，内心抉择与外部行动同时达到顶点",
            "牺牲决断型高潮，主角为更大利益作出重大牺牲",
            "真相揭示型高潮，核心谜团解开带来认知冲击",
            "对决型高潮，与主要对手的最终正面较量",
            "绝境突围型高潮，在看似绝望情况下找到解决方案",
            "团队协作型高潮，多角色各展所长共同应对挑战"
        ]
    },
    "English": {
        "Opening Design": [
            "Mystery opening, introducing the story with an enigma or crisis",
            "Everyday life opening, starting from ordinary scenes, hinting at coming changes",
            "Flashback opening, using memories or past events to suggest the main storyline",
            "Scene description opening, setting the story tone through environment and atmosphere",
            "Dialogue opening, introducing background and conflict through character conversations"
        ],
        "Conflict Design": [
            "Internal-external dual conflicts, protagonist facing both inner struggles and external obstacles",
            "Escalating conflicts, continuously deepening and complicating as the story progresses",
            "Value conflicts, fundamental opposition between different value concepts",
            "Identity conflicts, characters questioning and rebuilding their self-positioning",
            "Relationship conflicts, testing trust, loyalty and understanding between characters",
            "Environmental conflicts, characters contending with natural, social or technological environments",
            "Temporal conflicts, collisions between different time sequences or parallel worlds"
        ]
    }
}

# 添加场景和环境提示词
SETTING_AND_ATMOSPHERE = {
    "中文": {
        "自然环境": [
            "荒芜沙漠，极端干旱环境下的生存考验",
            "茂密森林，神秘且充满生机的绿色世界",
            "辽阔草原，开放空间带来的自由与孤独",
            "险峻山脉，攀登和征服的象征",
            "汹涌海洋，未知深度和危险的代表",
            "极地冰原，极端寒冷下的纯净与危机",
            "湿润雨林，生物多样性与原始生命力的展现"
        ],
        "人工环境": [
            "繁华都市，现代文明的缩影，机遇与压力并存",
            "衰败小镇，过去辉煌的残影和现实的落寞",
            "古老城堡，历史重量和神秘氛围的载体",
            "高科技实验室，人类智慧和野心的集中地",
            "拥挤贫民区，社会不平等和生存韧性的写照",
            "学术殿堂，知识传承和思想碰撞的场所",
            "虚拟网络，数字时代的新型社交和生存空间"
        ],
        "悬疑场景": [
            "废弃建筑，残破不堪的墙壁、灰尘覆盖的家具、不明来源的噪音",
            "密室现场，封闭空间内的精心布置、关键线索的隐蔽放置、出入口的特殊设计",
            "暴风雨夜，闪电照亮的瞬间景象、雨声掩盖的动静、湿滑危险的地面",
            "阴森古宅，历史悠久的家族住所、老旧的装饰与照片、诡异的家族历史",
            "偏远小镇，与外界隔绝的社区、居民的异常行为、隐藏的秘密",
            "雾中景象，能见度极低的环境、模糊不清的轮廓、声音的诡异传播",
            "地下设施，复杂的走廊迷宫、特殊的照明条件、隐藏的机关与陷阱",
            "犯罪现场，精心保存的证据细节、现场重建的线索、专业法医的分析视角"
        ],
        "爱情场景": [
            "浪漫餐厅，柔和的烛光、精致的餐具摆设、窗外的城市夜景、轻柔的背景音乐",
            "城市公园，樱花飘落的季节、湖边长椅的私密空间、清晨的雾气与露珠",
            "海滩日落，金色阳光下的海浪、细软的沙滩、远处的地平线、彩霞满天",
            "下雨街道，共撑一把伞的亲密、雨水打湿的街道灯光、避雨亭下的偶遇",
            "摩天轮顶，城市全景尽收眼底、短暂停留的私密空间、灯光璀璨的夜色",
            "图书馆角落，书架间的偶遇、安静氛围中的窃窃私语、阳光透过窗户的温暖",
            "四季变换，春天的新绿、夏日的炎热、秋天的落叶、冬日的初雪，见证感情发展",
            "共同家庭，一起布置的新家、充满个人风格的装饰、创造共同生活记忆的空间"
        ],
        "时间背景": [
            "史前文明，人类早期社会的神秘与原始",
            "古代王朝，传统文化和宫廷政治的展现",
            "中世纪，骑士精神与宗教信仰的时代",
            "工业革命，技术变革与社会动荡的交织",
            "现代社会，全球化与信息爆炸的当下",
            "近未来，科技发展带来的机遇与担忧",
            "后末日，文明崩溃后的重建与反思"
        ],
        "氛围营造": [
            "紧张悬疑，通过节奏控制和线索设置制造不安",
            "浪漫唯美，通过感官描写和情感渲染创造梦幻感",
            "冷峻写实，直面现实的残酷与美丽，不加粉饰",
            "荒诞离奇，打破常规认知，建立异化视角",
            "哲学深沉，引发对存在本质和意义的思考",
            "幽默讽刺，以轻松笔触揭示深刻社会问题",
            "神秘超自然，模糊现实与非现实的界限"
        ],
        "特殊环境": [
            "现代校园，知识殿堂与青春情感的交织场所",
            "历史校园，反映特定时代教育理念和学生生活",
            "未来校园，融合高科技与创新教学方式的学习场所",
            "异界校园，具有魔法或超能力培训系统的奇幻学府",
            "虚拟校园，数字世界中的教育空间，规则可能被改写",
            "现实校园细节，包括教室黑板、课桌椅排列、走廊布告栏、操场跑道、食堂窗口、图书馆书架、社团活动室、宿舍床铺、校门口小摊、教师办公室等校园日常环境",
            "校园人文环境，包括班级文化、年级特色、社团氛围、校园传统、师生关系、班级荣誉、校园广播、晨读晚自习、课间活动等校园文化元素",
            "校园季节特色，包括开学典礼、期中考试、运动会、校园文化节、社团招新、校内比赛、毕业季等特殊时段的校园氛围变化"
        ]
    },
    "English": {
        "Natural Environment": [
            "Barren desert, survival test in extremely arid environments",
            "Dense forest, mysterious and vibrant green world",
            "Vast grassland, freedom and solitude brought by open spaces",
            "Treacherous mountains, symbols of climbing and conquest",
            "Turbulent ocean, representative of unknown depths and dangers",
            "Polar ice field, purity and crisis under extreme cold",
            "Humid rainforest, display of biodiversity and primitive vitality"
        ],
        "Artificial Environment": [
            "Bustling city, microcosm of modern civilization, where opportunities and pressures coexist",
            "Declining town, remnants of past glory and current desolation",
            "Ancient castle, carrier of historical weight and mysterious atmosphere",
            "High-tech laboratory, concentration of human wisdom and ambition",
            "Crowded slums, portrait of social inequality and survival resilience",
            "Academic halls, places for knowledge inheritance and ideological collision",
            "Virtual network, new social and survival space in the digital age"
        ]
    }
}

# 在这里添加其他从import.py中提取的提示词模板和常量
# ... 

# 三千流专属爆点生成系统
SANQIANLIU_EXPLOSION_POINTS = {
    "修为突破": [
        "主角在危机时刻突破修为，战胜强敌",
        "主角悟道顿悟，境界提升，引来天地异象",
        "主角吸收天材地宝，功力大增，震惊周围修士",
        "主角领悟《三千流》秘籍新篇章，获得全新能力",
        "主角在对战中被逼入绝境，触发血脉觉醒，实力暴增"
    ],
    "强势复仇": [
        "主角回到家族，以雷霆手段惩处迫害母亲的仇人",
        "主角击败曾经欺辱自己的族人，身份地位逆转",
        "主角设下连环计，让害母凶手自相残杀",
        "主角在众目睽睽之下揭穿家族长老的阴谋，名声大噪",
        "主角在家族大比中一鸣惊人，让所有轻视他的人震惊"
    ],
    "身份揭露": [
        "主角真实身世被揭露，原来与某位大能有关",
        "主角母亲临终前留下的信物揭示惊人真相",
        "主角体内隐藏的特殊体质被发现，引来各方势力争夺",
        "主角发现《三千流》秘籍与自己血脉相连，非他人可修炼",
        "主角被敌人认出真实身份，陷入重重危机"
    ],
    "奇遇机缘": [
        "主角误入古墓，获得绝世功法或法宝",
        "主角在危险秘境中获得天材地宝，实力大增",
        "主角救下神秘老者，获赠绝世武功或丹药",
        "主角偶然发现《三千流》秘籍中隐藏的更高境界修炼法",
        "主角在一处隐秘之地发现母亲留下的传承"
    ],
    "击败强敌": [
        "主角以弱胜强，击败修为高于自己的敌人",
        "主角智取敌方首领，令对方势力分崩离析",
        "主角在众人面前一战成名，震慑各方势力",
        "主角在生死之战中领悟武道真谛，击败宿敌",
        "主角不畏强权，挫败大势力阴谋，救下无辜之人"
    ]
}

# 三千流修真境界体系
SANQIANLIU_CULTIVATION_SYSTEM = {
    "凡体境": [
        "淬体期 - 炼化体内杂质，增强肌肉韧性",
        "锻骨期 - 强化骨骼，增加身体强度",
        "通脉期 - 打通经脉，为修炼真元做准备",
        "易筋期 - 改变筋脉质地，提升身体柔韧性",
        "洗髓期 - 洗涤骨髓，改变体质"
    ],
    "后天境": [
        "引气期 - 引导外界灵气入体，开始修炼真元",
        "聚气期 - 体内开始积累真元，有了一定修为",
        "凝气期 - 真元质变，可外放攻击",
        "化气期 - 真元与身体融合，增强各方面素质",
        "练气期 - 真元纯度提高，可使用简单法术"
    ],
    "先天境": [
        "筑基期 - 在体内建立真元基础，初步脱离凡俗",
        "聚核期 - 真元在丹田凝结成核，储存能量",
        "元丹期 - 元核化丹，修为大增",
        "金丹期 - 元丹化为金丹，寿命延长百年",
        "元婴期 - 金丹化婴，元神初成，可离体而存"
    ],
    "通玄境": [
        "化神期 - 元婴化神，神识增强，可远程控物",
        "返虚期 - 虚实转化，初步掌握空间之力",
        "合道期 - 与天道产生共鸣，领悟天地规则",
        "大乘期 - 道法大成，威能巨大",
        "渡劫期 - 经历天劫洗礼，踏入更高境界"
    ],
    "流天境": [
        "真流期 - 掌握三千流中的真流之力，可破虚空",
        "化流期 - 身化流光，速度无双",
        "御流期 - 操控流力，攻防一体",
        "合流期 - 与三千流融为一体，力量无穷",
        "道流期 - 成就流之大道，近乎长生"
    ]
}

# 三千流法宝系统
SANQIANLIU_MAGICAL_ITEMS = {
    "法器": [
        "初级法器 - 注入灵力可发挥一定威力，如飞剑、法印等",
        "中级法器 - 具有一定灵性，可与主人心意相通",
        "高级法器 - 具有特殊能力，威力强大"
    ],
    "法宝": [
        "初级法宝 - 可自主聚集灵力，攻击力强",
        "中级法宝 - 具有完整灵性，可自主行动",
        "高级法宝 - 蕴含特殊规则之力，威能惊人"
    ],
    "灵宝": [
        "初级灵宝 - 蕴含天地规则，可引动天象",
        "中级灵宝 - 拥有独立元神，堪比修士助力",
        "高级灵宝 - 可镇压一方天地，威能无穷"
    ],
    "神器": [
        "残缺神器 - 即使不完整也有惊人威力，可斩杀高阶修士",
        "完整神器 - 具有毁天灭地之能，可灭宗门",
        "先天神器 - 天地初开时形成，威能不可测"
    ]
}

# 三千流特殊体质与血脉
SANQIANLIU_SPECIAL_TRAITS = {
    "特殊体质": [
        "流光体 - 天生亲和《三千流》功法，修炼速度倍增",
        "太阴体 - 吸收月华之力，夜晚战力倍增",
        "太阳体 - 吸收日精之力，白天战力倍增",
        "不灭体 - 生命力顽强，恢复能力超群",
        "感知体 - 对危险有预感，战斗直觉敏锐"
    ],
    "特殊血脉": [
        "古神血脉 - 体内蕴含远古神明血脉，潜力无穷",
        "龙族血脉 - 具有操控水系能力，体魄强大",
        "凤凰血脉 - 火系能力强大，重伤后可浴火重生",
        "麒麟血脉 - 领悟能力极强，学习功法事半功倍",
        "混沌血脉 - 可同时掌握多种属性能力，变化多端"
    ],
    "特殊天赋": [
        "过目不忘 - 一眼记住所见功法，领悟速度快",
        "灵力亲和 - 吸收灵力速度快，质量高",
        "剑道天才 - 在剑道上有特殊悟性，剑技精湛",
        "丹道大师 - 炼丹天赋异禀，可炼制高品质丹药",
        "阵法宗师 - 领悟阵法奥义，布阵能力强"
    ],
    "特殊能力": [
        "预知未来 - 可模糊预见未来发生的危险",
        "通晓兽语 - 可与妖兽交流，易于收服",
        "心灵感应 - 可感知他人情绪，判断真假",
        "虚空移物 - 可隔空取物，战斗中出其不意",
        "元神出窍 - 灵魂可离体，进行侦查或暗杀"
    ]
}

# 三千流关键章节结构
SANQIANLIU_CHAPTER_STRUCTURE = {
    "开篇引入": [
        "主角身世介绍",
        "家族环境描述",
        "母亲遭害经过",
        "获得《三千流》秘籍",
        "开始修炼之路"
    ],
    "初步崛起": [
        "初步修炼成果",
        "家族内部矛盾",
        "初次展露锋芒",
        "结交初始盟友",
        "离开家族游历"
    ],
    "踏入修真界": [
        "接触更大世界",
        "加入宗门历练",
        "结交重要角色",
        "首次大型冒险",
        "名声初步建立"
    ],
    "实力提升": [
        "关键战斗历练",
        "探索奇遇秘境",
        "获得重要传承",
        "突破重要境界",
        "建立自身势力"
    ],
    "仇敌浮现": [
        "家族仇人现身",
        "阴谋逐渐揭露",
        "敌对势力冲突",
        "遭遇重大危机",
        "盟友离散聚合"
    ],
    "最终决战": [
        "回归复仇计划",
        "集结盟友力量",
        "突破最高境界",
        "大型宗门战争",
        "与最终Boss决战"
    ],
    "新的征程": [
        "尘埃落定后续",
        "建立新的秩序",
        "解决遗留问题",
        "更高层次修炼",
        "开启全新旅程"
    ]
}