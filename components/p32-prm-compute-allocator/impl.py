# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P32 prm-compute-allocator — PRM验证器引导计算

L0: 每步值不值得多想，用'打分员'给分来决定。
L1: 按步得分归一化后分配算力预算。
L2: allocate(scores, budget) → 每步预算。
"""

def allocate(scores, budget=1000, floor=20):
    s = sum(scores) or 1
    return [max(floor, int(budget*x/s)) for x in scores]

def demo():
    print("[P32]", allocate([0.9, 0.2, 0.6], 900))


if __name__ == "__main__":
    demo()
