[Awesome Agent](https://github.com/kyrolabs/awesome-agents)
# Frameworks
* llama-agentic-system: 就是一堆官方示例项目，用来告诉你“Llama Stack 这个东西可以怎么用”，给人看和参考的，不是拿来直接用的成品。你可以看代码学怎么接、怎么跑，但别指望直接改改就能上线或赚钱。 
* Transformers Agents: Transformers Agents 就是 Hugging Face 在 transformers 里做的一套现成代码，让大模型听懂你用人话说的任务后，自己决定要不要调用工具（比如计算、代码、别的模型）来把事情做完，而不是只回你一段文字。
* LlamaIndex: 这个库是一个 面向大语言模型（LLM）的数据接入与检索框架，它让你可以 将外部数据（如文档、数据库、API、Web 内容等）结构化地引入到 LLM 的上下文中，并基于这些数据构建查询/生成应用（例如问答系统、智能助理、RAG 应用）。LlamaIndex 核心目标是：让 LLM 能够有效地访问、理解并利用外部数据来增强生成（generation）能力。
它提供大量 reader/connectors，可以从多种数据源读取内容，例如： 文本/PDF/Word 数据库（SQL/NoSQL） Github 仓库、Issues 云存储、API Slack / Discord / Notion 等协作平台文档，将原始数据转成 LLM 能理解的文档格式。
可以构建不同的索引结构，如： 向量索引（Vector Index）：用于语义搜索 倒排索引（Inverted Index） 树状索引、关键词索引等复杂结构 索引可以将海量文本变为便于检索的形式，提高查询速度和相关性。
为用户提供统一的查询接口，将用户提问映射到索引查找，然后将检索到的数据片段传给 LLM 进行生成。 支持 检索增强生成（RAG, Retrieval-Augmented Generation），即结合外部知识片段与模型生成来提高回答准确性。
可以与不同 LLM（OpenAI、HuggingFace、Replicate 等）和向量数据库（Milvus、Pinecone 等）结合。 与其它工具（例如 LangChain）一起构成完整的智能应用栈。
* LangChain: LangChain 解决的是“如何把一个大语言模型，从一次性 Prompt 工具，工程化为可组合、可控制、可扩展的应用系统”的问题。LangChain 是一个 LLM 应用“控制层 / 编排层（Orchestration Layer）框架”。
原始的大语言模型（GPT、Claude、Llama 等）在工程层面存在几个根本痛点：LLM 原生能力是“一次性调用”。真实应用不是“问一句答一句”
真实系统通常需要： 多步骤任务（Plan → Execute → Verify） 条件分支、循环 调用外部系统（数据库、搜索、API、代码） 保持上下文记忆 可调试、可复现、可监控。裸 LLM API 无法直接支撑这些需求。
LangChain 解决的核心问题（拆解）：1. Prompt 不可复用、不结构化的问题、2. 多步骤推理与流程控制问题、工具调用与外部系统集成问题、状态与记忆问题（Memory）、5. Agent 行为不可控的问题
* Botpress: Botpress 解决的是：非 AI 团队、非研究团队，如何在真实业务环境中，低成本、可维护地“落地”对话型自动化系统的问题。
现实世界的真实痛点（不是论文里的问题）：
1️⃣ 需要“能用”的聊天机器人，而不是“聪明的模型”：企业要的是 客服机器人 售前咨询 FAQ 自动回复 流程引导（注册、报修、退款、预约） 多渠道统一接入（Web / WhatsApp / Slack / 微信），而不是聪明的模型。
2️⃣ 非技术人员必须能参与构建与维护
3️⃣ 聊天机器人必须“稳定、可控、合规”
Botpress 是一个“对话系统操作系统（Conversational OS）”，而不是一个 Agent 框架。
✅ 适合用 Botpress 的场景 企业客服 售前咨询 内部 IT / HR 机器人 标准化流程 合规要求高 人员结构复杂（非技术主导）。
❌ 不适合用 Botpress 的场景 自主 Agent 多步复杂推理 研究型 Agent 系统 Tool-heavy 的 AI Copilot 动态规划、探索型任务
* Haystack: 现实问题：人手里有一堆资料，但找不到“能直接用来回答问题的那一小段”。“我问一个问题，你帮我在资料里找到最相关的几段，然后基于它们回答。”
Haystack 就是一个“聪明的资料管理员 + 助理”。它干三件非常“人性化”的事： 把一堆杂乱资料整理好 帮你从里面找出最相关的几小段 让 AI 只基于这些内容回答。
✅ 非常适合 Haystack 的情况 你关心： 回答准不准 能不能追溯来源 能不能上线给别人用。你有：文档、知识库、明确的数据边界
❌ 不适合 Haystack 的情况 想做“会自己探索世界”的 Agent 复杂多步规划 游戏、自动化操作 创意写作、发散思考。Haystack 可以个人使用，也支持 Python，但它更偏“工程级工具”，而不是“个人玩具”。“上班场景”反而是 Haystack 这类工具最典型、最合适的使用场景。
* Semantic Kernel: Semantic Kernel 是一个“让 AI 按你写好的步骤办事”的工具。
它不是用来聊天的，而是用来把 AI 变成可控的“执行助手”。现实中的问题是： AI 很聪明 但太随性 同一个问题，每次回答不一样 很难嵌进已有系统 很难让它稳定地做同一件事 公司不是要“灵感”，是要“稳定执行”。
举一个外行能懂的例子：你对 AI 说： “帮我生成一份会议纪要。” 你真正想要的是： 先提取关键决策 再列待办事项 再总结风险 输出成固定格式，但普通聊天 AI 可能： 今天这样写 明天那样写 后天干脆跑题
Semantic Kernel 位于 Agent 世界的“执行与编排层”，不是“思考层”。Semantic Kernel 负责的是： “事情要按什么顺序、用什么工具、用什么格式做完。”，也就是规划流程，照着跑。
✅ 非常适合（现实工作中） 报告生成（固定结构） 数据分析流水线 文档处理（分类、抽取、总结） 自动化办公流程 AI 作为“系统模块”嵌入产品。不追求“聪明”，追求“一致、稳定、可复现”。Semantic Kernel 是“流程模板化工具”，
对个人来说，只有在你想把一件事“固化成机器”时才值得用。
* Agent-LLM:AGiXT 是一个“让 AI 能自己拆任务、自己执行、自己往下走”的框架。它的核心思想是： 你只说目标 中间步骤不用你盯着 AI 可以： 规划 调用工具 记住上下文 连续行动 👉 它不是“回答者”，而是“做事者”。
AGiXT 偏“自由行动”，风险比保守系统高。如果说 Haystack 是“不乱说话的 AI”， Semantic Kernel 是“按流程办事的 AI”， 那 AGiXT 就是“会自己动的 AI”。
AGiXT 适合个人开发者用，但只适合“愿意折腾、想要自动化、能接受不稳定”的那一类个人开发者。AGiXT 的目标是： 让 AI 自己继续做事
其实可以学着用用看，让ai持续做事，但调模型太花钱了。
* LLM Agents: 手langchain启发，比它更小型。这个库是一个非常简洁的示例工具，教人怎么利用大语言模型（LLM）来构建一个“智能代理”（Agent）。
它不是成品机器人，而是一个最简单、最基础的 Agent 实现模板。
✅ 适合的场景（现实、实用）：你想理解 Agent 的原理 它是一个结构简单、最基本的 Agent 示例，读代码就能看懂。 你正在学习如何把 LLM 变成会行动的系统 很适合初学者拆解 Agent 的控制循环（思考 → 动作 → 工具 → 反馈）。 GitHub 你想自己扩展自定义 Agent 比起直接用 LangChain/AGiXT 等成熟框架，这里是最小可运行版本，可以作为自己写 Agent 时的起点。
* e2b: E2B 是一个让 AI 代理（Agent）能在“安全、隔离的真实电脑环境”里工作，用真实工具、跑真实代码，而不是只在聊天框里胡乱说话的基础设施。
它适合什么样的场景？:✅ 1. AI 需要自己运行代码或真实执行任务
✅2. 需要把 AI 丢给“真实电脑”做事
✅ 3. 企业级 Agent 工作流部署和托管
E2B 从来不打算“帮你做 Agent”， 它假设：Agent 已经存在，现在只缺一个“真实、安全的执行环境”。
* Dust: Dust 是一个让企业和团队“创建智能 AI 助手/Agent” 的平台，目的是把分散在各种文件、聊天工具、知识库里的信息统一起来，让 AI 代理能真正“理解你的工作和数据”，并自动完成实际任务。Dust 是“让 AI 成为能干活的同事”。
Dust 是“企业级 AI 同事平台”，
AGiXT 是“给工程师用的 Agent 引擎 / 实验框架”。
“能做事”和“能把事交付”，是两件完全不同的事情。Dust “刻意牺牲了智能自由度”，换取了“结果可交付、可依赖、可复用”。
它们本质上都是：
我给一个目标 → AI 自己拆步骤 → 调工具 → 把任务完成；
只是 Dust 更强调“结果能不能长期、稳定、放心地用”。
* MetaGPT: MetaGPT 是一个“多智能体协作框架”。当一个任务非常复杂、需要多个角色协同完成时，一个 AI 不能单独干完全部事情。MetaGPT 让多个 AI 模型像一个“团队”一样，模拟不同角色（例如产品经理、架构师、工程师、项目经理）协同完成复杂任务。
现实中：开发一个完整的软件产品需要一支真实的团队（产品、设计、代码、测试、架构）协同工作。 MetaGPT 的目标是：让 AI 模拟这样的协同流程，从一句话需求 → 自动生成需求文档 → 设计 → 代码 → 项目交付。
MetaGPT 非常耗 token； 它天然更偏“企业 / 团队 / 研究展示”， 个人长期、高频使用的性价比并不高。
* AgentFlow: AgentFlow 就像一个“AI 任务流水线设计器 & 执行器”： 你定义好每一步要做什么，它负责按照顺序一步步让 AI 去做， 还可以调用工具、处理状态、返回结果。
区分：
AgentFlow 是“流程控制器”
MetaGPT 是“AI 虚拟团队”
AGiXT 是“自由探索型 AI 工具箱”
Dust 是“企业可交付 AI 员工系统”
这四个东西，看起来都是“给目标 → AI 去做事”，真正的区别在于：“谁在想、谁在管、谁在兜底、谁在交付”。
它们都在做“AI 调用工具完成任务”， 但分别把“控制权”放在不同地方： AgentFlow 把控制权交给【流程】 MetaGPT 把控制权交给【角色协作】 AGiXT 把控制权交给【Agent 自主智能】 Dust 把控制权交给【系统与交付约束】
* Lagent: Lagent 是一个用来构建“智能代理（AI Agents）”的轻量级开源框架。 简单来说，它让你 把大语言模型（LLM，如 GPT 或 InternLM 这些模型）包装成可编程、可行动的“机器人”，这些机器人能接收输入、调用工具（搜索、执行代码等）、记忆对话上下文，并根据需要做连续的思考与操作。
* Autogen: Autogen 是一个用来构建多智能体（Multi-Agent）AI 应用的编程框架。 它让开发者可以创建由多个“智能代理（Agent）”组成的系统，让这些代理互相对话、合作、调用工具、分工执行任务。Autogen 允许你创建多个“都能操作工具的 Agent”，并且让它们通过对话机制进行协作，自动完成复杂任务。
* AgentVerse:AgentVerse 是一个多智能体（Multi-Agent）框架，旨在让多个大语言模型（LLM）驱动的智能体在一个环境中协作、交互和解决问题，而不是单一模型孤立工作。
* Maestro: 自动把一个大目标分解成多个小子任务，然后让不同的智能体去执行这些子任务，最后把结果整理成最终输出。
* AgentScope: AgentScope = 一个让多个智能体一起协作、分工、执行任务的 Python 框架，它把通信、容错、部署这些复杂工程问题都帮你解决掉。
* CrewAI: 它提供了一个框架，让你可以构建多个能互相协作的 AI Agent 团队（Crew），这些 Agent 不仅能对话，还能调用工具、执行分配的任务、一起解决复杂任务。
* Swarm: Swarm 的核心目的是让多个 AI agent 协同工作、互相交接任务，并简化这种协作流程的构建方式。
* agency-swarm: Agency-Swarm 是一个专门用来构建“多个角色明确、像公司部门一样协作的 AI Agent 团队”的框架，适合复杂任务分工协作。
* Upsonic: Upsonic 是一个把 AI Agent 变成“可执行企业级自动化任务”的平台，重点是稳定运行、任务编排和真实业务落地。
* Mastra: Mastra 是一个偏产品化的 Agent 框架，目标是快速搭建可上线的 AI 应用而不是研究 Agent 本身。
* Vectara-agentic: 这是一个围绕 Vectara 搜索引擎打造的 Agent 示例库，专门用来做“基于企业数据的高质量问答和搜索”
* AgentDock: AgentDock 是一个帮你快速“拼装”不同 Agent、工具和模型的开发平台，更像 Agent 的 Docker。
* Modus: Modus 是一个让 Agent 直接跑在后端基础设施里的执行框架，目标是把 AI 逻辑变成真正的生产代码。
* Swarms Framework Swarms 是一个高度实验性的多 Agent 框架，用来探索大规模 Agent 协作和自组织行为。
* Strands Agents SDK: Strands SDK 是一个面向企业的 Agent 工具包，重点是把 Agent 嵌入现有系统和流程中，而不是单独玩 AI。
* AgentUp: AgentUp 在设计之初就以安全性、可扩展性和可伸缩性为核心基础，通过配置驱动的架构和丰富的插件生态，简化了 AI Agent 的开发流程。
* VoltAgent - 一个用于构建 AI 智能体的开源 TypeScript 框架，内置对大语言模型（LLM）的可观测性能力。
* Agentic Context Engine: 自我改进型智能体：能够从执行反馈中学习；并提供 LangChain 集成，使智能体能够自行整理和管理其上下文。
* Astron: 一个面向企业、适合商业落地的 Agent 工作流平台，用来打造下一代能力更强的超级 AI 智能体。
* Ailoy: 一个用于构建 AI 智能体的综合框架，支持在任何环境中运行，并且完整支持本地 AI 与 WASM（WebAssembly）。
# Testing and Evaluation
* Voice Lab: Voice Lab 是一个自动化评估语音/对话智能代理表现的测试框架，用来标准化对比不同模型、不同策略下的语音 Agent 输出质量，而不是用来构建这些 Agent。
* Open-RAG-Eval: open-rag-eval 是一个开源的 RAG 系统质量评估框架，让你在没有人工黄金答案的情况下，量化比较和改进检索增强生成应用的表现。
* EvoAgentX:EvoAgentX 是一个让多个 AI Agent 自动生成协作流程、自动评估并持续优化的多 Agent 工作流框架，用于让 AI 系统像一支会进化的团队一样高效完成复杂任务。
# Software Development
* MetaGPT: 多智能体框架：第一家 AI 软件公司，迈向自然语言编程。
* OpenHands:  OpenHands：少写代码，多做事情。（原名 OpenDevin），一个由 AI 驱动的软件开发智能体平台。
* GPT Pilot: GPT Pilot 是 Pythagora VS Code 扩展的核心技术，旨在打造第一个真正意义上的 AI 开发者伙伴。
* Aider: Aider 是一个运行在终端里的 AI 编程搭档。
* Devika: Devika是一种智能AI软件工程师，能够理解人类的高层次指令，将其分解为具体步骤，检索相关信息，并编写代码以实现既定目标。
* RepoAgent: 由大语言模型驱动的仓库代理，旨在帮助开发者和团队快速生成文档并快速了解代码仓库。
* DSPy: 用于对基础模型进行编程——而非仅仅提示——的框架。
* ThinkGPT: 将 Agent 技术用于增强你的大语言模型，并将其能力推向极限
* PyCodeAGI: 一个小型 AGI 实验：根据用户想要构建的应用，自动生成一个 Python 应用
* SuperAGI: 面向开发者优先的开源自主 AI Agent 框架
* Plandex: 用于处理复杂任务的 AI 编码引擎
* Codel: 一个完全自主的 AI Agent，可通过终端、浏览器和编辑器执行复杂任务和项目
* DB GPT: 使用本地 GPT 与你的数据和环境交互，无数据泄露，100% 私密，100% 安全
* Agency: 🕵️‍♂️一个为开发者设计的库，以简洁、高效且符合 Go 语言习惯的方式，探索大语言模型（LLM）及其他生成式 AI 的潜力
* TaskWeaver: 一个以代码为先的 Agent 框架，用于无缝规划和执行数据分析任务
* MicroAgent: 能够自我编辑其 Prompt 与 Python 代码的智能体
* SWE Agent: SWE-agent 可接收一个 GitHub issue，并使用 GPT-4 或你选择的语言模型尝试自动修复它
* AgentRun: 以最简单、最快速的方式安全运行 AI 生成的 Python 代码
* Claude Engineer: 一个交互式命令行界面（CLI），利用 Anthropic 的 Claude-3.5-Sonnet 模型能力来辅助软件开发任务
* Vision agent: 一个帮助你利用 Agent 框架生成代码以解决计算机视觉任务的库
* Nous: 基于 TypeScript 的 AI Agent 平台，包含自主 Agent、软件开发 Agent、AI 代码审查 Agent 等
* Cline: 一个开源的 AI 编码 Agent，为开发者提供对前沿模型的直接访问，并具备完全透明性
* OpenCode: 为终端而生的 AI 编码 Agent
# Research
* GPT Researcher: 一个为多种任务进行全面在线研究而设计的自主智能体
* BlockAGI: BlockAGI 通过迭代式、领域特定的研究，并输出详尽的叙事性报告来展示其研究发现
* data-to-paper: 从数据到可被人类验证的研究论文的 AI 驱动科研流程
* AI Scientist: 迈向完全自动化、开放式科学研究的 AI 科学家
* Storm: 一个由大语言模型驱动的知识策展系统，能够研究某一主题并生成带引用的完整长篇报告
* OpenLens AI: 面向健康信息学的完全自主研究智能体
* GenoMAS: 一个用于科学发现的多智能体框架，通过代码驱动的工作流自动化基因表达分析
* DeepAnalyze: 首个用于自主数据科学的 Agent 化大语言模型，支持具体的数据任务（数据准备、分析、建模、可视化与洞察），以及以数据为导向的深度研究（生成分析师级研究报告）
# Conversational / General Agents
* CollosalAI Chat: 基于 Colossal-AI 项目，实现结合 RLHF 的大语言模型
* RasaGPT: 首个构建于 Rasa 与 LangChain 之上的无界面（Headless）大语言模型聊天机器人平台
* SuperAgent: 将大语言模型智能体部署到生产环境
* BabyAGI UI: 让在 Web 应用中运行和开发 BabyAGI 变得更简单，体验类似 ChatGPT
* ix: 自主式 GPT-4 智能体平台
* DuetGPT: 一个对话式的半自主开发者助手，实现无需复制粘贴的 AI 结对编程
* Multi-Modal LangChain agents in Production: 将 LangChain 智能体部署到生产环境，并与 Telegram 进行连接
* Autonomous HR Chatbot: 一个能够利用现有工具自主回答人力资源相关问题的自治智能体
* LLama Cpp Agent: 一个用于便捷与大语言模型交互的 llama-cpp-agent 框架
* Memgpt: 创建具备长期记忆和自定义工具的大语言模型智能体
* GPT Agent: 用于计算机自动化的免费开源 AI 智能体
* joinly: 以语音为先的在线会议 AI 助手，能够在会议过程中主动参与并实时解决任务
* Gobii: 一个开源平台，用于通过对话式界面和 API 大规模部署与管理浏览器使用型智能体
# Game / Simulation
* Camel-AutoGPT: GPT-Agent（Camel-AutoGPT） 是一个 基于现有自动 agent 架构（如 AutoGPT / CAMEL）的框架示例，让多个自主 agent 可以互相对话与协作来解决目标任务。它在 agent 世界中属于 多 agent 协作层的实验/实现，适合用于 构建可配置的自主 agent 系统与角色协同解决任务场景。 一句结论：GPT-Agent 是一个能让多个自主 AI agent 协同工作、互相对话以完成目标的多 agent 协作实现。
* SkyAGI: SkyAGI 是一个 用于展示大模型模拟人类行为能力的 Python 包，实现了生成式智能体（generative agents）模拟逼真的角色行为与对话互动，在 agent 世界中属于 生成式行为模拟 / 交互式智能体演示，适用于 游戏 NPC、角色扮演交互、行为仿真等体验或研究场景。 一句结论：SkyAGI 是一个展示大模型如何生成“像人一样回应与行为”的智能角色行为模拟框架。
* Voyager: Voyager 是一个 在开放世界（Minecraft）中能自己探索、习得技能并持续成长的“具身智能体”，用于研究如何让大模型驱动的 agent 具备长期学习、计划与自我提升能力。它属于 具身智能 agent / 自主探索 AI 研究范式，适用于 长期任务学习、开放世界探索和智能体研究。 一句结论：Voyager 是一个能在 Minecraft 这样的虚拟世界中自主探索与学习技能的长期进化智能体。
# Knowledge Management
* Private GPT: PrivateGPT 是一个在本地安全运行、基于本地或开源 LLM 的文档问答系统，它通过检索增强生成（RAG）机制让你用自然语言问问题，数据永不离开本地，适合隐私敏感和离线环境。
* Local GPT: LocalGPT 是一个能在本地部署、完全私有地把你的文档变成智能问答知识库的开源项目，解决数据隐私与本地智能问答需求问题，在 agent 体系中它是知识检索与本地 RAG 能力模块，适用于有隐私要求或离线部署的文档智能交互场景。
* LLocalSearch: LLocalSearch 是一个可在本地运行的智能搜索系统，它利用本地 LLM Agent 自动搜索互联网并回答用户提问，解决了 LLM 无法获取实时信息且依赖外部 API 的问题。
* Second Brain AI Agent: Second Brain AI Agent 是一个把你个人笔记/文件自动整理、语义索引并让 AI 智能回答这些内容的个人知识管理助手。
# Automation
* DemoGPT: DemoGPT 是一个自动生成 LLM Agent 和相关应用代码的开发辅助库，它让你只用自然语言描述就能快速得到可运行的 LangChain/Streamlit 应用框架，适合快速原型构建和非程序员把想法转成代码的场景。
* RestGPT:RestGPT 是一个让大语言模型真正与现实世界 RESTful APIs 对接的 Agent 框架，它能自动规划、执行 API 调用并解析结果，从而让模型像软件一样完成复杂任务。
* XAgent: XAgent 是一个开源的自主智能体系统，通过任务规划、执行和工具调用让语言模型不仅会“说话”，还能自动完成复杂的多步任务，并在需要时与人协作。
* LLM Agents: mpaepper/llm_agents 是一个极简的 LLM Agent 库，用最少代码示范如何让大语言模型调用工具、循环推理并执行任务，适合入门学习和原型开发。
* uAgents: uAgents 是一个 Python 框架，帮助你快速创建拥有身份、通信、安全交易能力的自主 AI 代理，并让它们在去中心化网络中协同工作，解决真实世界中复杂、事件驱动和区块链集成的自动化任务。
* Maestro: 自动把一个大目标分解成多个小子任务，然后让不同的智能体去执行这些子任务，最后把结果整理成最终输出。
* llama-agents: Llama-agents（现 LlamaDeploy）是一个负责将多智能体 Agent 工作流工程化、部署到生产环境并提供服务级运行能力的框架。它通过： 提供一个部署和服务运行层、支持将 LLM Agent 工作流转换成可运行的服务、提供 HTTP API 访问、异步并发能力 支持可扩容、容错与监控运行状态来解决“Agent 在开发环境写好，却难以稳定运行在生产系统里”的现实问题。
* Phidata: Build AI Assistants with memory, knowledge and tools. 
* AgentK: AgentK 是一个开源的 “自我进化” AI 代理系统（AGI 框架），它希望解决现实世界里这样一个难题： 如何让一套 AI 系统不仅执行任务，还能自己生成新代理、扩展能力并协同工作，以处理复杂、开放式任务？
* ADAS: 这个仓库实现的是论文 “Automated Design of Agentic Systems（ADAS）” 的代码，它来自一篇发表在 ICLR 2025 的研究工作。该研究关注的是： 自动生成强大的智能体系统（agentic systems）设计，而不是由人类手工设计这些系统。ADAS 是一个让 AI 自动探索、自动生成、自动优化智能体系统设计的研究级框架，它通过“元 agent”自动发现更强的 agent 架构，从根本上减少人工手工设计智能体系统的工作量。
* Giselle: Giselle 是一个开源的 AI agent 与自动化工作流构建平台，通过可视化设计、跨模型组合和业务集成，让团队快速创建、部署和运行智能自动化流程
## Browser
* AgentGPT: AgentGPT 是一个浏览器里可视化创建与部署自主 AI 代理的平台，让用户简单定义目标后，AI 自动规划并执行整个任务，是从“只能回答问题”到“能独立完成目标”的跨越。
* OpenAgents:OpenAgents 是一个开源 “开箱即用”的 AI agent 平台，让普通用户和开发者通过 Web UI 调用多种智能代理（数据分析、插件调用、网页自动浏览）来完成现实任务，而不只是提供底层框架。
* WebQA-Agent: WebQA Agent 是一个自动化网页测试 Agent，它利用大语言模型控制浏览器模拟真实用户操作，自动审核网站的功能、性能和用户体验，并生成可视化测试报告，用来替代传统繁琐的人力网站 QA 测试。
## Multimodal
* Pipecat: Pipecat 是一个开源的 Python 框架，用于构建能“听、说、看、实时交互”的 AI 对话代理（agents）——特别是语音和多模态（不仅是文字，还包括音频、视频、图像等）对话机器人。让开发者不用从零开始应对语音识别、语音合成（TTS）、对话处理、网络传输、视觉输入等复杂组件的集成和实时协调工作，而是通过一个框架把这些模块串联起来，让 AI 代理可以如同现实中的助手一样实时听懂、理解并回应用户。
