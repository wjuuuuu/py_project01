# -------------------- 函数 - 变量的作用域 -------------------- #
# 全局变量： 在函数外部或函数内部都是可以访问的 ；
num = 100
num1 = 10

# 定义函数
def circle_area(r):
    # 局部变量: 只能在函数内部使用
    pi = 3.14
    area = pi * r * r

    num = 10000
    print("num = ", num)
    global num1  # global关键字：可以在函数中使用全局变量,使得可以在函数内部修改全局变量的值;先声明再使用；
    num1 = 1000
    print("num1 = ", num1)

    return area


# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ", num)
print("num1 = ", num1)

# -------------------- 函数 - 传参方式 -------------------- #
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 传参方式一：位置传参
stu = reg_stu("张三", 18, "男", "北京")
print(stu)

# 传参方式二：关键字参数
stu = reg_stu(name = "王林", age = 28, gender = "男", city = "北京")
print(stu)

stu = reg_stu(age = 18, gender = "女", city = "北京",name = "李慕婉")
print(stu)

# 传参方式三：位置参数 + 关键字参数 ---> 位置参数在前，关键字参数在后
stu = reg_stu("王林", 28, gender = "男", city = "北京")
print(stu)


# -------------------- 函数 - 默认参数 -------------------- #
# 定义函数
def reg_stu2(name, age, gender = "男", city = "北京"):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
reg_stu2("王林",20)

reg_stu2("李慕婉", "18","女")

reg_stu2("韩立", "20",city = "上海")

# -------------------- 函数 - 不定长参数（位置参数 *args --> 元组） --------------------  #
# 需求：根据传入的这批数据，计算这批数据的最小值，最大值，平均值
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    return min_data, max_data, round(avg_data, 1)

# 调用函数
print(calc_data(2, 7, 9, 10, 45))

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))

# -------------------- 函数 - 不定长参数（关键字参数 **kwargs --> 字典） -------------------- #
# 需求：根据传入的这批数据，计算这批数据的最小值，最大值，平均值
def calc_data(*args, **kwargs):
    """
    根据传入的这批数据，计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算这批数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数个数
        print: 是否打印输出
    :return: 最小值， 最大值， 平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"min = {min_data}, max = {max_data}, avg = {avg_data}")

    return min_data, max_data, round(avg_data, 1)

# 调用函数
print(calc_data(2, 7, 9, 10, 45, round = 3, print = True))

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, round = 3, print = True))
