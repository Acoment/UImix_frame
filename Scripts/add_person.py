# _*_ coding:UTF-8 _*_
# @time：2022/6/19  10:15
# @Author: 皓雪
# @file: add_person.py   
# @Software: PyCharm

from conf.VarConfig import testDataPath
from Util.ExcelUtil import ExcelUtil
from Util.CommonUtil import generate_method
from Util import ActionUtil
from Util import log
import logging

logger = log.Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
def add_person(excel,stepSheet,dataSheet):
    """
    添加联系人
    :return:
    """
    stepSheet = excel.get_sheet_by_name(stepSheet)
    dataSheet = excel.get_sheet_by_name(dataSheet)
    try:
        #数据源数据行数
        data_row_nums = excel.get_row_nums(dataSheet)
        #得到步骤页
        step_row_nums = excel.get_row_nums(stepSheet)
        for j in range(2,data_row_nums+1):
            if excel.get_cell_value(j,6,dataSheet).lower() == 'y':
                name = excel.get_cell_value(j,1,dataSheet)
                mail = excel.get_cell_value(j,2,dataSheet)
                phone = excel.get_cell_value(j,3,dataSheet)
                is_star = excel.get_cell_value(j,4,dataSheet)
                renarks = excel.get_cell_value(j,5,dataSheet)
                # print(name,mail,phone,is_star,renarks)
            for i in range(2,step_row_nums+1):
                index =excel.get_cell_value(i,1,stepSheet)
                step_desc = excel.get_cell_value(i,2,stepSheet)
                location_type = excel.get_cell_value(i,3,stepSheet)
                location_express = excel.get_cell_value(i, 4, stepSheet)
                key_word = excel.get_cell_value(i,5, stepSheet)
                operate_value = excel.get_cell_value(i,6, stepSheet)
                # 当 operate_value 是以变量的形式的存在，要进行替换掉
                if isinstance(operate_value,str) and "$" in operate_value and '{' in operate_value and '}' in operate_value:
                    # name = 'zgabf'
                    # a = '${name}'
                    # operate_value = eval(a[2:-1])
                    # print(operate_value)
                    operate_value = eval(operate_value[2:-1])

                method_express = generate_method(key_word,location_type,location_express,operate_value)
                if operate_value !="N":
                    logger.logger.debug(f'开始执行{step_desc}，调用函数为：{method_express}')
                    print(f'开始执行{step_desc}，调用函数为：{method_express}')
                    if step_desc != None:
                        run = 'ActionUtil.' + method_express
                        eval(run)
                        print(run)
    except Exception as e:
        logger.logger.error(e)
        # raise e
        ActionUtil.driver.refresh()




if __name__ == '__main__':
    logger = log.Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
    driver = None
    filename = testDataPath + '\\test_data.xlsx'
    print(filename)
    excel = ExcelUtil()
    excel.load_workbook(filename)
    caseSheet_case = excel.get_sheet_by_name('case')

    # stepSheet_add_person = excel.get_sheet_by_name('add_person')
    # dataSheet_person_data = excel.get_sheet_by_name('person_data')
    # loginSheet_login = excel.get_sheet_by_name('login')
    # sendmailSheet_case = excel.get_sheet_by_name('sendmail')

    step_row_nums = excel.get_row_nums(caseSheet_case)
    # print(step_row_nums)
    ActionUtil.driver = driver
    for iI in range(2, step_row_nums+1):
        indexI = excel.get_cell_value(iI, 1, caseSheet_case)
        case = excel.get_cell_value(iI, 2, caseSheet_case)
        case_word = excel.get_cell_value(iI, 4, caseSheet_case)
        is_need_run = excel.get_cell_value(iI, 5, caseSheet_case)
        dataSheet = excel.get_cell_value(iI, 6, caseSheet_case)

        case_method2 = case_method(case_word=case_word, Sheet_name=case, dataSheet=dataSheet)

        if is_need_run != "N":
            logger.logger.debug(f'开始执行模块{case}，调用函数为：{case_method2}')
            # print(f'开始执行模块{case}，调用函数为：{case_method2}')
            if case != None:
                logger.logger.debug('-----------------------------')
                logger.logger.debug(case_method2)
                logger.logger.debug('-----------------------------')
                eval(case_method2)



    # driver.get('https://mail.163.com')
    # driver.maximize_window()
    # iframe = driver.find_element(by='tag name',value='iframe')
    # driver.switch_to.frame(iframe)
    # driver.find_element(by='name',value='email').send_keys('Li14959398')
    # driver.find_element(by='name', value='password').send_keys('lidehuang2')
    # driver.find_element(by='id',value='dologin').click()
    # time.sleep(2)

    # ActionUtil.driver = driver
    # key_work(excel,loginSheet_login)
    # add_person(excel,stepSheet_add_person,dataSheet_person_data)
    # key_work(excel,sendmailSheet_case)
