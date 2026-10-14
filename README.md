# 版本实验室 · sun-alan-life-lab

把孙宇晨、邵艾伦及抖音相关讨论，转成适合个人的行动与复盘。

这是一个第三方独立整理的 Agent Skill。它包含开放主题索引和实践指令，适合交给支持 `SKILL.md` 的 Agent 使用。当前版本 **0.2.0**，原索引核对 **2026-10-12**，最近增量核对 **2026-10-14**。

[GitHub 仓库](https://github.com/huixiaodou123/sun-alan-life-lab) · [版本与下载](https://github.com/huixiaodou123/sun-alan-life-lab/releases)

## 孙哥、邵艾伦：热门讨论怎么交给 AI 用

从孙学、开图、小我，到薄肌、黄毛、英语、创作、大水和过日子，按你的问题查来源、找用法。**自更新由调用 Skill 的 Agent 执行**：开始新应用任务时检查本人新公开内容，核对后补进知识库；观点变化保留记录。没有配置常驻任务时，不声称全天即时监控。

[新版视频](https://github.com/huixiaodou123/sun-alan-life-lab/releases/download/v0.2.0/version-lab-v4.mp4) · [大嘴配音](https://github.com/huixiaodou123/sun-alan-life-lab/releases/download/v0.2.0/version-lab-v4-dazui.wav) · [可选字幕](https://github.com/huixiaodou123/sun-alan-life-lab/releases/download/v0.2.0/optional-captions-v4.srt) · [可编辑工程](https://github.com/huixiaodou123/sun-alan-life-lab/releases/download/v0.2.0/version-lab-v4-editable.zip)

视频 v4（约78秒）：粗黑体大字、短句分段、绿色关键词、直接切换；安装与调用口令采用易读的短行卡片。按用户要求，结尾追加“遥遥领先，让友商永远追不上。”，沿用“大嘴”配音。

视频使用用户指定的 ComfyUI 保存音色“大嘴”，仅保留主体动效文字，完整旁白字幕单独提供，默认不烧录。两人的姓名用于识别讨论对象，不表示本人为这个第三方 Skill 背书。

## 能帮你做什么

- 查观点：找到来源，分清本人表达、社区延伸、传播梗和本项目设计。
- 做选择：比较方向、时间与成本，设计一次能退出的小验证。
- 开始行动：按身体与恢复、英语学习、表达与关系、创作、生活取舍或 AI 上下文进入具体任务。
- 持续复盘：根据实际产物和反馈调整，避免每次重新写一份宏大计划。

目前索引发现 **29 个主题条目**，包括开图、小我、全球需求、版本变化、自由、创造与消费、睡眠、注意力、SMV、人脉、风口、自媒体、大水、过日子和情绪稳定等。这个数字是当前索引规模，不代表已证实的 29 条理论；标题、二创和梗均有标记。后续按来源继续增补、合并和修订。

## 自更新已经实际做了什么

0.2.0 已核对两人近期本人公开文字，新增自媒体作为机会入口、学习与学历、AI 智能体与支付基础设施三条来源记录；创作模块已补充一处带出处的实践说明。仍保留29个主题，不把每条帖子都增算成新理论。见 [最新增量](references/latest-updates.md) 和 [更新流程](references/updates.md)。

## 快速使用

把完整的 `sun-alan-life-lab` 文件夹放入所用 Agent 的技能目录，保留 `SKILL.md`、`agents/` 和 `references/` 的相对位置。Codex 本地技能通常放在 `~/.codex/skills/`；重新开始一个会话后调用：

```text
用 $sun-alan-life-lab 帮我把一直想做的视频缩成今天能录的一个小样。
我已经有工具演示，今天有 40 分钟，不想再收集一堆理论。
```

检查更新：

```text
用 $sun-alan-life-lab 检查孙哥和邵艾伦的新内容，核对后更新这个 Skill 和我的知识库，再说明有什么变化。
```

也可以直接给新的原始链接，它会比较旧观点、去重、必要时更新模块并留档。

其他入口：

```text
用 $sun-alan-life-lab 解释黄毛、SMV 和边界的关系，说明哪些读到了原始内容。

用 $sun-alan-life-lab 研究大水、过日子和女性版本等抖音延伸，先核对作者，别只局限于已有名单。

用 $sun-alan-life-lab 练习用英文介绍我的作品。我没有雅思考试需求。

用 $sun-alan-life-lab 复盘上周的实验：只完成了一次，原因是动作太大。
```

## 文件入口

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | Agent 的任务识别、模块路由与执行规则 |
| [主题索引](references/topic-map.md) | 当前发现的主题、核对状态与扩展流程 |
| [来源登记](references/sources.md) | 原始入口、作者归属与实际阅读范围 |
| [理念映射](references/principles.md) | 将讨论转成实践问题的方式 |
| [使用示例](examples.md) | 演示输入与可检查的预期行为 |
| [更新流程](references/updates.md) | 调用时查新、来源核对、模块修改与记录 |
| [验证说明](VALIDATION.md) | 本次检查范围与仍需验证的部分 |

## 资料边界

本项目尚未完整听校全部视频、直播和课程，不提供“全网所有理论已收齐”的承诺。健康、考试和其他事实需要独立核验；个人观点、标题和热度无法证明效果。没有实际记录时不能报告进步、收入、提分或体型变化。

执行流程、练习设计和模块分类是本项目原创。来源、改写及第三方授权见 [sources.md](references/sources.md)。本项目原创指令采用 [MIT License](LICENSE)；注明来自 wousp112 整理的改编主题归纳按 CC BY 4.0 保留署名与许可。MIT 不覆盖链接指向的原视频、字幕、课程与其他第三方作品。发布包不携带这些原始内容或个人数据。
