# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P34 verifier-guided-beam — PRM验证器引导计算

L0: 生成很多候选，用打分员挑最好的几个留下。
L1: 按 scorer 分数排 top-k。
L2: beam(cands, scorer, k) → top-k。
"""

def beam(cands, scorer, k=2):
    return sorted(cands, key=scorer, reverse=True)[:k]

def demo():
    print("[P34]", beam(["a","bb","ccc"], lambda s: len(s), 2))


if __name__ == "__main__":
    demo()
