# if条件判断：如果分数超过 680，我就去清华读书
score = 600
if score >= 680:
    print("欢迎你来清华读书")
    print("也恭喜你即将踏入精彩的大学生活")
print("--------------------------------")

# if案例：结合前面学习的输入输出及 if 条件判断的知识，完成 B 站的登录功能的实现（正确账号和密码为 188888888/666888）
#正确的账号和密码
ok_account = "188888888"
ok_password = "666888"
# 1.接受用户输入的账号和密码
account = input("请输入您的B站账号：")
password = input("请输入您的B站密码：")

# 2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入 B 站首页
if account == ok_account and password == ok_password:
    print("登录成功~")
    print("进入B站首页~")
else:
    print("登录失败!")
    print("账号或密码错误!")

# 案例 1：根据用户输入的年份，判断一年是闰年还是平年（非正百年份，且能被 4 整除的是闰年；整百年份（如 1900，2000）必须被 400整除才是闰年）
year = int(input("请输入需要判定的年份："))

# 如果是 非正百年份，且能被 4 整除的 是闰年；整百年份 必须被 400 整除 才是闰年
if (year % 4 == 0 and year % 100 != 0) or year %400 == 0:
    print(f"{year}是闰年！")
else:
    print(f"{year}是平年！")

# if...elif...else 案例：根据用户输入的数字判断数字是正数，还是负数还是 0
num = int(input("请输入数字"))

if num > 0:
    print(f"{num}是正数！")
elif num < 0:
    print(f"{num}是负数！")
else:
    print(f"{num}是0！")

