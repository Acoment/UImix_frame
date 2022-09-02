# _*_ coding:UTF-8 _*_
# @time：2022/6/18  12:31
# @Author: 皓雪
# @file: log.py.py   
# @Software: PyCharm

import logging
import time,os

# 项目根目录
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# log文件存放路径
logPath = projectPath + '\\log\\'

class Logger(object):
    """封装的日志模块"""

    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        try:
            self.logger = logging.getLogger(logger)
            self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
            # 日志输出格式
            fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
            # 日志文件名称
            # self.LogFileName = os.path.join(conf.log_path, "{0}.log.txt".format(time.strftime("%Y-%m-%d")))# %H_%M_%S
            curr_time = time.strftime("%Y-%m-%d %H_%M_%S")
            self.LogFileName = logPath + curr_time + '.txt'
            # 设置控制台输出
            # 设置文件输出
            fh = logging.FileHandler(self.LogFileName)
            fh.setFormatter(fmt)
            fh.setLevel(FileLevel)  # 日志级别
            self.logger.addHandler(fh)
        except Exception as e:
            raise e


if __name__ == '__main__':
    logger = Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
    logger.logger.debug("debug")
    # curr_time = time.strftime("%Y-%m-%d %H_%M_%S")
    # print(curr_time)