# 创建数据类型 ---> type() 获取指定字面量或变量的类型
print("Hello")
print(type("Hello"))


print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

num = -100
print(type(num))

# 常见数据类型 ---> isinstance(数据， 类型) ---> bool值 ---> 判定指定数据是否是指定的类型，如果是：True，否则:False
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))


# 字符串
# 定义字符串的三种方式
s1 = "Hello"  # 双引号定义
s2 = 'Python' # 单引号定义
s3 = """
Hello:
    吴同学                 
    王同学
"""  # 三引号定义

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))


# 定义字符串 ---> It's very good
#转义字符 \' \" \n \t
msg = 'It\'s very good'
print(msg)

msg2 = "It's very good"
print(msg2)

msg3 = "hello 的意思是\"你好\""
print(msg3)

msg4 = 'hello 的意思是"你好"'
print(msg4)

msg5 = "\t吴同学\n\t王同学"
print(msg5)

# 字符串拼接
s1 = "人生苦短" "我用 Python"
print(s1)

msg1 = "人生苦短"
msg2 = "我用 Python"
print("龟叔说：" + msg1 + " , " + msg2)

#案例 ---> str(int数字) ---> 将int类型的数字转换为字符串
name = "吴同学"
age = 18
pro = "计算机科学"
hobby = "Python"
print("大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro + "， 爱好是" + hobby)

#字符串格式化 ---> 案例一 ---> %s 占位符
name = "吴同学"
age = 18
pro = "计算机科学"
hobby = "Python"
print("大家好，我是%s，今年%s岁，学习的专业是%s， 爱好是%s"%(name,age,pro,hobby))

#字符串格式化 ---> 案例二 ---> f"...{变量名/表达式}..." ---> 推荐方式
name = "吴同学"
age = 18
pro = "计算机科学"
hobby = "Python"
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{pro}， 爱好是{hobby}")

