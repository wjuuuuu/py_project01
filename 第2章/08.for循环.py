# for循环：遍历输入的字符串

msg = input("请输入需要遍历的字符串：")

for s in msg:
    print(f"元素：{s}")
else:
    print ("遍历结束！")

# 案例1： 计算 1-100 之间所有的奇数之和
total = 0

for i in range(1,101,2):
        total += i

print("请输入 1-100之间奇数之和：",total)

# 案例 2：计算 100-500 之间所有 3 的倍数的数字之和
total = 0;

for i in range(100,501):
    if i % 3 == 0:
        total += i

print("100-500 之间所有3的倍数的数字之和：",total)

"""
    循环嵌套：根据输入的长方形的长度m，宽度 n，打印一个长方形；
    如下：是一个长度为 10，宽度为 5 的长方形
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    
    print("*")：自带换行效果，每一次执行都会输出新的一行；
    print("*",end="")):end表示的是每一次输出以什么结束；默认是\n，表示换行
"""

# 1. 接受键盘录入 m, n
# 长度
m = int(input("请输入长方形的长度:"))
# 宽度
n = int(input("请输入长方形的宽度:"))

# 2. 打印长方形
for i in range(n): # 控制行
    for j in range(m): # 控制列
        print("*", end=" ")
    print("")

# 案例：嵌套循环案例：打印99乘法表
for i in range(1,10): # 外层循环 - 控制行
    for j in range(1,i+1): # 内层循环 - 控制列
        print(f"{j} x {i} = {i * j}",end = "\t") # \t 制表符：等于按一下 tab，也可以用来对齐文字
    print()