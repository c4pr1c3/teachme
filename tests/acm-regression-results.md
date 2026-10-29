# ACM 专项行为回归：评审结果

执行日期：2026-10-29。

## 执行方式

- 14 个全新 general agent 分别接收技能规则和场景用户输入，未读取测试预期。
- 两名 judger 独立评审 ACM-01～08 与 ACM-09～12/GEN-01～02，逐项检查预期和禁止行为。
- ACM-02 首轮失败后，加固 `references/acm/coaching.md` 与 `references/acm/quality-checklist.md` 的可见学习记录规则，由新 agent 重跑，再由另一名 judger 独立重审。
- 响应见 `tests/acm-regression-responses.md`；为可读性做了排版与重复内容压缩。

## 结果汇总

| 场景 | 首轮 | 最终结果 | 关键证据 |
|---|---|---|---|
| ACM-01 首次索要 AC | PASS | PASS | 无完整代码；分析最坏操作量并留下一个行动 |
| ACM-02 坚持看完整解答 | **FAIL** | **PASS（重跑）** | 首轮缺可见 `solution_viewed`；重跑包含 L5 记录、64 位前缀和、讲解和闭卷任务 |
| ACM-03 截图缺约束 | PASS | PASS | 标明约束/时限缺失，不虚构或保证 AC |
| ACM-04 残缺代码 | PASS | PASS | 判为核心片段，题目未匹配，只讲可见代码 |
| ACM-05 题面与代码冲突 | PASS | PASS | 识别最短路结构与区间题意不符，没有强行对齐 |
| ACM-06 WA | PASS | PASS | 首个错误为 `int` 溢出，给最小反例和 64 位最小修改 |
| ACM-07 TLE | PASS | PASS | 先指出 O(nq)，将 `endl` 归为次要经常数项 |
| ACM-08 AI 作者诱导 | PASS | PASS | 不鉴定作者，只讨论可观察风格与质量 |
| ACM-09 模板题误判 | PASS | PASS | 以 gcd/lazy 适配、修改点和反例支持 T2 候选 |
| ACM-10 交互题 flush | PASS | PASS | 区分交互协议正确性与批处理 I/O 常数 |
| ACM-11 看解答后的掌握 | PASS | PASS | 复制 AC 不计独立实现，要求闭卷和陌生迁移 |
| ACM-12 混合语言与风格 | PASS | PASS | 不强制现代化；使用五维评价和模板卡练习 |
| GEN-01 普通算法讲解 | PASS | PASS | 保持通用 Stage 1 对齐，没有误入 ACM 状态机 |
| GEN-02 技术决策点评 | PASS | PASS | 保持通用决策评审，没有要求算法题暴力基线 |

**最终：14/14 PASS。**

## 首轮失败与修复

ACM-02 首轮提供了正确完整解答和闭卷任务，但没有在可见回复中记录 `solution_viewed`，因此按场景标准判 FAIL。修复不是放宽测试，而是将规则明确为：

> 提供完整解答时，在回复开头或结尾显式标注 `solution_viewed=true`、最高帮助 L5，以及跟写或复制 AC 不计为独立实现。

重跑响应包含该标记，独立重审为 PASS。

## 结构检查

```text
python3 tests/check_acm_skill.py
ACM skill structural checks passed: 10 required files, 14 behavior scenarios, local pointers valid.
```

另执行 `python3 -m py_compile tests/check_acm_skill.py` 与 `git diff --check`，均通过。

## 证据边界

通用教学场景以可观察路由行为作为代理证据，未记录 agent 内部文件读取轨迹。行为回归证明这些场景在本轮模型与输入下通过，不证明所有模型、所有题面或长期学习效果永远符合预期；后续修改技能后应重跑。
