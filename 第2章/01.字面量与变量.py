# 字面量的写法
print(100)
print(3.14)
print(True)
print(False)

print("Hello python")
print("-------------------")
print(None)

# bool类型本质上也是整数类型
print(True + 1) # 2
print(False - 1) # -1

#变量---->python中的变量是动态类型的，一个变量可以存储不同类型的数据（但是在项目开发的时候一般一个变量就存储一种类型的数据）
num = 1114.1
print(num)

num = num + 1
print(num)

num = "ok"
print(num)

a = 100
b = 200
print("a + b = ",a + b)

#案例
base = 20.7 # 基础播放量
incr = 50   # 每个月新增的播放量
print ("未来一个月的播放量:", base + incr)
print ("未来二个月的播放量:", base + incr + incr)

#案例 - 升级：一次性可以定义多个变量
base,incr = 20.7,50
print ("未来一个月的播放量:", base + incr)
print ("未来二个月的播放量:", base + incr + incr)










