# 一元二次方程式 ax^2 + bx + c = 0
# 公式：x = (-b ± sqrt(b^2 - 4ac)) / (2a)

import math

# 輸入 a, b, c
a = 1
b = -3
c = 2

# 計算判別式
discriminant = b**2 - 4*a*c
print(f"判別式 = {discriminant}")

if discriminant > 0:
    # 兩個實根
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"有兩個實根: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    # 一個實根
    x = -b / (2*a)
    print(f"有一個實根: x = {x}")
else:
    # 無實根，為複數根
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"有兩個複數根: x1 = {real}+{imag}i, x2 = {real}-{imag}i")
