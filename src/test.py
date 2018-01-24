# -*- coding:utf-8 -*-
import os
import win32process
from Config import config
import re
import sys

Obj = 'C:\Users\Administrator\Desktop'

# if Obj and os.path.exists(Obj):  #文件or 目录存在
#    if os.path.isfile(Obj):
#       try:   # 打开外部可执行程序
#          win32process.CreateProcess(Obj, '',None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())
#       except Exception, e:
#          print(e)
#    else:
#        os.startfile(str(Obj))  # 打开目录
# else:  # 不存在的目录
#    print('不存在的目录')

this_file = os.path.abspath(__file__).replace("\\", "/").rstrip("cd")
print(os.path.abspath(__file__))
file_path = os.path.abspath(__file__)

# if file_path.endswith('wallet\\ui\\src\\test.py'):
#     print(file_path)
#     block_path = file_path.replace('ui\\src\\test.py', 'block')
#     # block_path = re.sub('wallet\\ui\\src\\test.py', "", file_path)
#     os.startfile(block_path)
#     print(block_path)


def actionBackupWallet():
    print('--------actionBackupWallet--------')
    import os
    file_path = os.path.abspath(__file__)
    if file_path.endswith('wallet\\ui\\src\\test.py'):
        print(file_path)
        block_path = file_path.replace('ui\\src\\test.py', 'block')
        os.startfile(block_path)
        print(block_path)

actionBackupWallet()

# if this_file.endswith("/Contents/Resources/core/src/Config.py"):
#     start_dir = re.sub("/[^/]+/Contents/Resources/core/src/Config.py", "", this_file).decode(
#         sys.getfilesystemencoding())
#     config_file = start_dir + "/sbtc.conf"
#     data_dir = start_dir + "/data"
#     log_dir = start_dir + "/log"
#     block_dir = "../block"
# elif this_file.endswith("/core/src/Config.py"):
#     # Running as exe or source is at Application Support directory, put var files to outside of core dir
#     start_dir = this_file.replace("/core/src/Config.py", "").decode(sys.getfilesystemencoding())
#     config_file = start_dir + "/sbtc.conf"
#     data_dir = start_dir + "/data"
#     log_dir = start_dir + "/log"
#     block_dir = "../block"
# else:
#     config_file = "sbtc.conf"
#     data_dir = "data"
#     log_dir = "log"
#     block_dir = "../block"
#
# print(data_dir)
# print(block_dir)
