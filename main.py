# _*_ coding:UTF-8 _*_
# @time：2022/7/3  9:24
# @Author: 皓雪
# @file: main.py
# @Software: PyCharm
import time

from conf.VarConfig import testDataPath
from Util.ExcelUtil import ExcelUtil
from Util.htmlUtil import htmlreturn
from Util.CommonUtil import generate_method
from Scripts.keywork import key_work
from Scripts.add_person import add_person
from Util.CommonUtil import case_method
from Util import ActionUtil
from Util import log
# from Util import ReportUtil
import logging





if __name__ == '__main__':

    logger = log.Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
    driver = None
    filename = testDataPath + '\\test_data.xlsx'
    # print(filename)
    excel = ExcelUtil()
    excel.load_workbook(filename)
    caseSheet_case = excel.get_sheet_by_name('case')


    # stepSheet_add_person = excel.get_sheet_by_name('add_person')
    # dataSheet_person_data = excel.get_sheet_by_name('person_data')
    # loginSheet_login = excel.get_sheet_by_name('login')
    # sendmailSheet_case = excel.get_sheet_by_name('sendmail')
    step_row_nums = excel.get_row_nums(caseSheet_case)

    # ---------------------------------
    # print(step_row_nums)
    ActionUtil.driver = driver
    for iI in range(2, step_row_nums + 1):
        indexI = excel.get_cell_value(iI, 1, caseSheet_case)
        case = excel.get_cell_value(iI, 2, caseSheet_case)
        case_word = excel.get_cell_value(iI, 4, caseSheet_case)
        is_need_run = excel.get_cell_value(iI, 5, caseSheet_case)
        dataSheet = excel.get_cell_value(iI, 6, caseSheet_case)

        case_method2 = case_method(case_word=case_word, Sheet_name=case, dataSheet=dataSheet)
        try:
            if is_need_run != "N":
                logger.logger.debug(f'开始执行模块{case}，调用函数为：{case_method2}')
                # print(f'开始执行模块{case}，调用函数为：{case_method2}')
                if case != None:
                    logger.logger.debug('-----------------------------')
                    logger.logger.debug(case_method2)
                    logger.logger.debug('-----------------------------')
                    eval(case_method2)
                    excel.write_cell(iI, 7, 'Success', filename, caseSheet_case)
                    excel.write_cell(iI, 8, time.strftime('%Y-%m-%d',time.localtime()), filename, caseSheet_case)
        except:
            excel.write_cell(iI, 7, 'Fail', filename, caseSheet_case)
            excel.write_cell(iI, 8, time.strftime('%Y-%m-%d',time.localtime()), filename, caseSheet_case)
    # ---------------------------------

    case_data = excel.get_all_rows_values(step_row_nums, caseSheet_case)
    # print(case_data)
    htmlreturn(step_row_nums,case_data)



    # ---------------------------------
    # test_result = step_row_nums-1
    # test_version = 'V1.0'
    #
    # pass_count = 0
    # fail_count = 0
    # error_count = 0
    # skip_count = 0
    # for i in range(len(case_data)):
    #     if case_data[i]['test_result'] == 'Success':
    #         pass_count += 1
    #     elif case_data[i]['test_result'] == 'Fail':
    #         fail_count += 1
    #     elif case_data[i]['test_result'] == 'Error':
    #         error_count += 1
    #     else:
    #         skip_count += 1
    # percent = pass_count/(pass_count+fail_count+error_count+skip_count)*100
    # report_time = time.strftime('%Y-%m-%d',time.localtime())
    # print(test_result,test_version,pass_count)
    # print(fail_count, error_count, skip_count)
    # print(percent, report_time)
    # for i in range(0,test_result):
    #     ID = case_data[i]['id']
    #     Scene = case_data[i]['case_desc']
    #     Executed = case_data[i]['is_need_run']
    #     Test_Result = case_data[i]['test_result']
    #     Run_time = case_data[i]['test_time']
    #     Test_Log = logger.LogFileName
    #     print(ID,Scene,Executed,Test_Result,Run_time,Test_Log)
    # ---------------------------------