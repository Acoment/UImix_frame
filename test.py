# _*_ coding:UTF-8 _*_
# @time：2022/7/4  20:02
# @Author: 皓雪
# @file: htmlUtil.py
# @Software: PyCharm

import re,time
from Util import log
import logging
from conf.VarConfig import BASE_DIR





def htmlreturn(step_row_nums=3):
    template = BASE_DIR + '\\conf' + '\\template.html'
    Reports = BASE_DIR + '\\Reports' + '\\Reports.html'

    test_date = 'test_date'
    test_result = step_row_nums-1
    test_version = 'V1.0'
    pass_count = 3
    fail_count = 3
    error_count = 4
    skip_count = 2

    percent = pass_count/(pass_count+fail_count+error_count+skip_count)*100
    report_time = time.strftime('%Y-%m-%d',time.localtime())


    with open(template,'r',encoding='utf-8') as f :
        for line in f:
            line = line.replace('$test_date', str(eval('test_date')))
            line = line.replace('$pass_count',str(eval('pass_count')))
            line = line.replace('$test_version', str(eval('test_version')))
            line = line.replace('$fail_count', str(eval('fail_count')))
            line = line.replace('$error_count', str(eval('error_count')))
            line = line.replace('$skip_count', str(eval('skip_count')))
            line = line.replace('$percent', str(eval('percent')))
            line = line.replace('$report_time', str(eval('report_time')))
            line = line.replace('$skip_count', str(eval('skip_count')))
            with open(Reports,'a',encoding='utf-8') as f :
                f.write(line)


if __name__ == '__main__':
    htmlreturn()