# 社区调研与内化来源

核验日期：2026-10-29。stars/forks 只表示公开采用信号，不证明教学质量；论文试点也不自动外推到 ACM 长期训练效果。

本轮未发现同时覆盖 ACM/CCPC/ICPC、渐进提示、完整代码审查、常数优化、模板识别和个人风格训练，并具有充分采用与学习效果证据的单一开放项目。因此本专项采用**方法借鉴、独立表达、按需整合**。

## 1. 直接相关技能与教练系统

### acm-coach

- 来源：[仓库](https://github.com/jojo-yin/acm-coach)、[SKILL.md](https://github.com/jojo-yin/acm-coach/blob/main/.claude/skills/acm-coach/SKILL.md)
- 采用信号：核验时 2 stars、21 commits；作者明确称个人项目、非专业维护。
- 借鉴：READ–THINK–CODE–VERIFY 的分析顺序；诊断优先于替换；竞赛代码不做无意义风格挑刺；对拍与弱项记录。
- 局限：采用证据有限，不能据此宣称学习效果已验证。
- 许可证：README 声明 **CC BY-SA 4.0**。本专项不复制其完整提示词或代码；如未来引入实质表达或代码，需另行处理署名和相同方式共享要求。

### oi-coach

- 来源：[SKILL.md](https://github.com/tangyixiao/tangyixiao-skills/blob/main/oi-coach/SKILL.md)
- 采用信号：所在仓库本轮约 2 stars，属于新近个人技能。
- 借鉴：缺前置时直接示范、避免永远反问；分级提示；教学代码不计独立实现；用陌生任务和延迟复测区分接触与掌握。
- 局限：主要面向 OI/CSP/NOIP，规则存在不等于长期成绩已改善。
- 许可证：SKILL 声明 **MIT**。仍按方法内化并独立表达。

### Algo Sensei

- 来源：[仓库](https://github.com/karanb192/algo-sensei)、[Hint Mode](https://github.com/karanb192/algo-sensei/blob/main/modes/hint-mode.md)
- 采用信号：核验时 299 stars、62 forks；是直接技能中相对较强的采用信号。
- 借鉴：观察、模式、方向、具体技术、伪代码的渐进提示；从特征识别模式；正确性/复杂度/边界审查。
- 局限：主要面向 LeetCode/面试，不含完整 ACM 对拍、赛场协议和常数优化；“10x”等宣传不能当作研究结论。
- 许可证：**MIT**。

### Coach Mo / voidhub-cp-coach-skill

- 来源：[COACHING.md](https://github.com/adhamahmedyousef/voidhub-cp-coach-skill/blob/main/skills/voidhub-cp-coach/references/COACHING.md)
- 采用信号：本轮约 1 star、16 commits，采用证据有限。
- 借鉴：帮助级别记账；首次索要完整解答先给提示选择；`solution_viewed` 与独立完成分离；看过答案后安排闭卷重做和陌生迁移。
- 局限：绑定特定题库与状态存储，其教学判断仍需独立评估。
- 许可证：调研时仓库声明 **MIT**；题目内容与服务条款另行适用。

### SHARP / Ask Codey

- 来源：[论文](https://ceur-ws.org/Vol-4287/short2.pdf)、[代码](https://github.com/Snail664/coding-tutor)
- 证据：CSEDM 2026 短文；论文报告 benchmark 与 42 名中学生探索性试点。
- 借鉴：先定位学生当前里程碑，再生成通向下一里程碑的短提示，而不是固定从同一级开始。
- 局限：主要验证 K–12 多 bug 调试；课堂试点无对照组，未测长期收益，不能外推为 ACM 完整教练效果。
- 许可证：论文页面标注 **CC BY 4.0**；代码仓库未明确声明许可证，不复制其实现。

## 2. 相邻高质量训练资源

### USACO Guide

- 来源：[How to Practice](https://usaco.guide/general/practicing)、[How to Debug](https://usaco.guide/general/debugging-checklist)、[Fast I/O](https://usaco.guide/general/fast-io)、[仓库](https://github.com/cpinitiative/usaco-guide)
- 采用信号：核验时约 1.9k stars、684 forks。
- 借鉴：难度应落在需要挣扎但缺口有限的位置；分步读题解、代码作为最后手段是一种有效选择；调试、对拍与 I/O 常数需要具体证据。
- 重要差异：页面对“渐进提示是否优于直接读完整题解”保留不同优秀选手观点，因此本专项采用自适应支架，而非宣称提示永远最好。
- 许可证：**CC BY-NC-SA 4.0**。不复制其段落；未来若引入实质内容，需重新审查非商业与相同方式共享条件。

### KACTL

- 来源：[仓库](https://github.com/kth-competitive-programming/kactl)
- 采用信号：KTH ICPC 队伍模板库；核验时约 3.6k stars、1.0k forks，带 stress tests。
- 借鉴：模板应短、够快、经过测试并容易按题修改；个人模板卡同时记录适用条件、复杂度和测试状态。
- 局限：它是模板库而非教学技能，采用量不能证明某个模板适合所有 judge 环境。
- 许可证：逐文件存在差异且部分不明确，不能把整个库视为统一自由许可；本专项不复制其代码。

## 3. 内化原则

1. 只吸收可迁移的教学思想、验证方法和评价维度，重新组织为本项目自己的协议。
2. 不复制外部完整 prompt、代码或大段文档，不用来源拼接替代针对本需求的设计。
3. 外部事实在运行时仍需核对原题、官方环境和当前许可证。
4. 本文件是来源记录，不改变本仓库整体许可证；新增实质外部内容前必须重新审查授权。
