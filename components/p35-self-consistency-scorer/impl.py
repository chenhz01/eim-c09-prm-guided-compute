# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P35 self-consistency-scorer — PRM验证器引导计算

L0: 同一个问题问好几遍，答案多数一致才可信。
L1: 多数投票 + 一致率。
L2: score(answers) → (majority, agreement)。
"""

def score(answers):
    from collections import Counter
    if not answers: return (None, 0.0)
    c = Counter(answers); maj, n = c.most_common(1)[0]
    return maj, round(n/len(answers), 2)

def demo():
    print("[P35]", score(["42","42","41"]))


if __name__ == "__main__":
    demo()
