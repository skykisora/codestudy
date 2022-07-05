# -*- coding:utf-8 -*-
import random

# 猜拳游戏：定义 石头=0，剪刀=1，布=2
wanjia = int(input("玩家出拳石头=0，剪刀=1，布=2："))
diannao = random.randint(0, 2)
print(diannao)
if (wanjia == 0 and diannao == 1) or (wanjia == 1 and diannao == 2) or (wanjia == 2 and diannao == 0):
    print("玩家获胜")
elif wanjia == diannao:
    print("是平局哦")
else:
    print("电脑获胜")

# 九九乘法表
m = 1
n = 1
while m <= 9:
    while n <= 9:
        s = m * n
        print(f'{m}*{n}={s}', end="\t")
        n += 1
    n = 1
    print(end="\n")
    m += 1

for i in range(1, 10):
    for j in range(1, 10):
        s = j * i
        print(f'{j}*{i}={s}', end="\t")
    print(end="\n")

