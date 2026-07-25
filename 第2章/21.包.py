# 1. 导入模块
# import utils.my_fun

# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()

# from utils import my_fun

# my_fun.log_separator1()
# my_fun.log_separator2()
# my_fun.log_separator3()

# # 注意：如果要通过 from utils import * 导入包下的所有功能，需要在包下的 __init__.py 文件中定义 __all__  = []列表，列表中包含要导出的功能名
# from utils import *
#
# my_fun.log_separator1()
# my_fun.log_separator3()
# my_fun.log_separator2()
#
# print(my_var.PI)
# print(my_var.NAME)

# 2.导入模块中的功能
# 相对路径： 从当前文件所在目录开始查找
from utils.my_fun import log_separator1, log_separator3

# 绝对路径： 从项目的根目录开始查找
from 第2章.utils.my_fun import log_separator1, log_separator3

log_separator1()
log_separator3()
