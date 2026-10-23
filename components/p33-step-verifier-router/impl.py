# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P33 step-verifier-router — PRM验证器引导计算

L0: 某步分数低就多展开想想，分数高就直接过。
L1: score>=thr → prune(过)，否则 expand(展开)。
L2: route(score, thr) → 'prune'/'expand'。
"""

def route(score, thr=0.7):
    return "prune" if score >= thr else "expand"

def demo():
    print("[P33]", [route(s) for s in (0.9, 0.4)])


if __name__ == "__main__":
    demo()
