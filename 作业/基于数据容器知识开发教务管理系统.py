"""
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
        1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
        4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5.列出所有学生:遍历所有学生信息并输出。
        6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
        7.退出系统。

        结构：students_information = {"李思" : {"chinese_score" : 92, "math_score" : 80, "english_score" : 78}, "张三" : {......}}

"""
students_information = {}

menu = """
###########################################################################################################
# 1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出所有学生信息  6. 统计班级成绩  7. 退出系统 #
###########################################################################################################
"""

print("欢迎使用教务管理系统")

while True:
    print(menu)

    choice = input("请输入您要执行的操作(1-7)：")

    match choice:
        case "1": # 添加学生信息
            student_name = input("请输入学生姓名：")

            if student_name in students_information:
                print("该学生已存在，请重新选择 ～")
                continue

            student_chinese_score = input("请输入语文成绩：")
            student_math_score = input("请输入数学成绩：")
            student_english_score = input("请输入英语成绩：")

            students_information[student_name] = {"chinese_score" : student_chinese_score, "math_score" : student_math_score, "english_score" : student_english_score }

            print("学生信息添加完毕 ～")

        case "2": # 修改学生信息
            student_name = input("请输入学生姓名：")

            if student_name not in students_information:
                print("该学生不存在，请重新选择 ～")
                continue

            student_chinese_score = input("请输入新的语文成绩：")
            student_math_score = input("请输入新的数学成绩：")
            student_english_score = input("请输入新的英语成绩：")

            students_information[student_name] = {"chinese_score": student_chinese_score, "math_score": student_math_score, "english_score": student_english_score}

            print("学生信息添加完毕 ～")

        case "3": # 删除学生信息
            student_name = input("请输入要删除的学生姓名：")

            if student_name not in students_information:
                print("该学生不存在，请重新选择 ～")
                continue
            else:
                del students_information[student_name]
                print("学生信息删除成功 ～")

        case "4": # 查询学生信息
            student_name = input("请输入要查询的学生信息：")

            if student_name not in students_information:
                print("没有您要查询的学生信息，请重新选择 ～")
                continue
            else:
                student = students_information[student_name]
                print(f"学生姓名 : {student_name}, 语文成绩 : {student["chinese_score"]}, 数学成绩 : {student["math_score"]}, 英语成绩 : {student["english_score"]}")

        case "5": # 列出所有学生信息
            for student_name in students_information:
                student = students_information[student_name]
                print(f"学生姓名 : {student_name}\t\t语文成绩 : {student["chinese_score"]}\t\t数学成绩 : {student["math_score"]}\t\t英语成绩 : {student["english_score"]}")

        case "6": # 统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
            chinese_score_list = [int(students_information[student]["chinese_score"]) for student in students_information]
            math_score_list = [int(students_information[student]["math_score"]) for student in students_information]
            english_score_list = [int(students_information[student]["english_score"]) for student in students_information]

            student_chinese_max = []
            student_math_max = []
            student_english_max = []
            student_chinese_min = []
            student_math_min = []
            student_english_min = []

            for student in students_information:
                if int(students_information[student]["chinese_score"]) == max(chinese_score_list):
                    student_chinese_max.append(student)
                if int(students_information[student]["chinese_score"]) == min(chinese_score_list):
                    student_chinese_min.append(student)
                if int(students_information[student]["math_score"]) == max(math_score_list):
                    student_math_max.append(student)
                if int(students_information[student]["math_score"]) == min(math_score_list):
                    student_math_min.append(student)
                if int(students_information[student]["english_score"]) == max(english_score_list):
                    student_english_max.append(student)
                if int(students_information[student]["english_score"]) == min(english_score_list):
                    student_english_min.append(student)

            print(f"语文最高分：{max(chinese_score_list)}")
            print(f"语文得分最高者：{student_chinese_max}")
            print(f"语文最低分：{min(chinese_score_list)}")
            print(f"语文得分最低者：{student_chinese_min}")
            print(f"语文平均分：{sum(chinese_score_list) / len(chinese_score_list):.2f}\n")

            print(f"数学最高分：{max(math_score_list)}")
            print(f"数学得分最高者：{student_math_max}")
            print(f"数学最低分：{min(math_score_list)}")
            print(f"数学得分最低者：{student_math_min}")
            print(f"数学平均分：{sum(math_score_list) / len(math_score_list):.2f}\n")

            print(f"英语最高分：{max(english_score_list)}")
            print(f"英语得分最高者：{student_english_max}")
            print(f"英语最低分：{min(english_score_list)}")
            print(f"英语得分最低者：{student_english_min}")
            print(f"英语平均分：{sum(english_score_list) / len(english_score_list):.2f}\n")

        case "7":
            print("bye ～")
            break
        case _:
            print("非法操作，不支持！")



