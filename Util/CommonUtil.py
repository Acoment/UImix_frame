# -*- coding: utf-8 -*- 
# @Time : 2022-06-12 14:44 
# @Author : 皓雪
# @File : CommonUtil.py 
# @Software: PyCharm


def generate_method(key_word,location_type,location_express,operate_value):
    """
    构建函数表达式
    :param key_word:
    :param location_type:
    :param location_express:
    :param operate_value:
    :return:
    """
    method_express = ""
    if location_type is None and location_express is None and operate_value:
        # 判断操作值是否是整数类型
        if isinstance(operate_value, int):
            method_express = key_word + "(" + str(operate_value) + ")"
        else:
            method_express = key_word + "('" + str(operate_value) + "')"
    # 只有   key_word  不为空，其他都为空 如 max_window/ close_browser
    if key_word and location_type is None and location_express is None and operate_value is None:
        method_express = key_word + '()'
    # 只有测试数据为空  如 switch_frame / click
    if key_word and location_type and location_express and operate_value is None:
        method_express = key_word + "('" + location_type + "','" + location_express + "')"
    # 都不为为空 如 input_content   input_content('name','email','zhangmingn002')
    if key_word and location_type and location_express and operate_value:
        if isinstance(operate_value, int):
            method_express = key_word + "('" + location_type + "','" + location_express + "'," + str(
                operate_value) + ")"
        else:
            method_express = key_word + "('" + location_type + "','" + location_express + "','" + operate_value + "')"

    return method_express

def case_method(case_word=None,excel='excel',Sheet_name=None,dataSheet=None):
    # print(case_word, excel,Sheet_name,dataSheet)
    """
    构建函数表达式
    :param key_word:
    :param location_type:
    :param location_express:
    :param operate_value:
    :return:
    """
    case_method = ""
    if case_word == 'key_work':
        case_method = case_word + "(" + str(excel) + ",'" + str(Sheet_name) + "')"

    if case_word == 'data_driver':
        case_method = 'add_person'
        # print(case_method)
        case_method = case_method + "(" + str(excel) + ",'" + str(Sheet_name) + "','" + str(dataSheet) + "')"
    # print(case_method,case_word)
    return case_method
