# P34 · verifier-guided-beam

> 机制簇：**PRM验证器引导计算** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
生成很多候选，用打分员挑最好的几个留下。

**L1 · 机制本质**
按 scorer 分数排 top-k。

**L2 · 怎么用上**
beam(cands, scorer, k) → top-k。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P34] ['ccc', 'bb']
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 中间步骤可判定：数学推导、代码执行、形式化证明、结构化抽取。 |
| **不该用** | 主观创作、审美判断、无客观判据的开放任务。 |
| **常见误用** | 用未校准的弱验证器放大错误——验证器偏了，算力越多错得越系统。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P32` prm-compute-allocator · `P33` step-verifier-router · `P35` self-consistency-scorer
- 本仓是 **P34 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P34-verifier-guided-beam/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P34 · verifier-guided-beam © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
