from random import random
from time import perf_counter
from math import sqrt

Points = int(input("請輸入點數n(點越多結果越準確，計算時間也越長): "))
# 統計圓內的點
cnt = 0

# 開始計時
start = perf_counter()
print("計算中，請稍後...")
for i in range(Points):
    x, y = random(), random()
    dis = sqrt(x**2 + y**2)
    if dis <= 1.0:
        cnt += 1

# 計算PI
pi = 4*cnt/Points
print("{:.6f}".format(pi))
print("執行時間: {:.6f}".format(perf_counter() - start))

