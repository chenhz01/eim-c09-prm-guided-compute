# C09 · PRM-Guided Compute

> **机制簇**：PRM验证器引导计算 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
别把算力平均撒在每一步，把力气花在「最可能出错的那一步」。

**L1 · 机制本质**
用过程评分给每步打分，把预算非均匀分配给低分步（重采样、验证、回溯）。

**L2 · 怎么用上**
step-scorer 打分；budget-allocator 按分数分配；verifier-loop 触发重采样与回溯。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c09-prm-guided-compute.git && cd eim-c09-prm-guided-compute
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p32-prm-compute-allocator/impl.py        # 看 demo 输出
python components/p32-prm-compute-allocator/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P32` | prm-compute-allocator | 按步得分归一化后分配算力预算。 | `components/p32-prm-compute-allocator/` |
| `P33` | step-verifier-router | score>=thr → prune(过)，否则 expand(展开)。 | `components/p33-step-verifier-router/` |
| `P34` | verifier-guided-beam | 按 scorer 分数排 top-k。 | `components/p34-verifier-guided-beam/` |
| `P35` | self-consistency-scorer | 多数投票 + 一致率。 | `components/p35-self-consistency-scorer/` |

## 该用 / 不该用 / 常见误用

**该用**
长链推理、数学/代码生成，总算力受限且步骤可分。

**不该用**
极短的单步任务（分配开销大于收益）；无法切分步骤的黑盒模型。

**常见误用（这条最重要）**
用最终答案分数当过程分。稀疏信号会让预算分配失去分辨率，退化成均匀撒。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C09 · PRM-Guided Compute © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
