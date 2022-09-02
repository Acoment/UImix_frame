# _*_ coding:UTF-8 _*_
# @time：2022/7/3  9:24
# @Author: 皓雪
# @file: keywork.py   
# @Software: PyCharm

import logging
from Util.CommonUtil import generate_method
from Util import log
from Util import ActionUtil

logger = log.Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
def key_work(excel,stepSheet):
    stepSheet = excel.get_sheet_by_name(stepSheet)
    step_row_nums = excel.get_row_nums(stepSheet)
    try:
        for i in range(2, step_row_nums + 1):
            index = excel.get_cell_value(i, 1, stepSheet)
            step_desc = excel.get_cell_value(i, 2, stepSheet)
            location_type = excel.get_cell_value(i, 3, stepSheet)
            location_express = excel.get_cell_value(i, 4, stepSheet)
            key_word = excel.get_cell_value(i, 5, stepSheet)
            operate_value = excel.get_cell_value(i, 6, stepSheet)
            method_express = generate_method(key_word, location_type, location_express, operate_value)
            if operate_value != "N":
                logger.logger.debug(f'开始执行{step_desc}，调用函数为：{method_express}')
                # print(f'开始执行{step_desc}，调用函数为：{method_express}')
                if step_desc != None:
                    run = 'ActionUtil.' + method_express
                    eval(run)
                    print(run)
    except Exception as e:
        print(e)
        logger.logger.error(e)





# if __name__ == '__main__':
#     logger = log.Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)