# while 循环：打印 10遍“人生苦短，我用 Python～”

i = 0
while i < 10:
    print("人生苦短，我用 Python～")
    i += 1
else:
    print("循环正常结束")

# while案例：计算 1～100之间所有偶数的累加之和
total = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1~100之间的所有偶数之和：{total}")