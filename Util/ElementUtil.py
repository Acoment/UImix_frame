# -*- coding: utf-8 -*- 
# @Time : 2022-06-12 10:59 
# @Author : kunp
# @File : ElementUtil.py 
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver,find_type, exrpession):
    """
    根据 find_type, exrpession 找控件，并返回控件
    :param driver:
    :param find_type:
    :param exrpession:
    :return:

    """
    # WebDriverWait(driver,sec).until(mesthod,message="") 表示每隔0.5秒就调用method方法，直到这个method不返回fasle为止
# 一旦超过了sec，就抛出异常，信息为 message
    try:
        element = WebDriverWait(driver,10).until(lambda driver: driver.find_element(by=find_type, value=exrpession))
        return element
    except:
        print("没找到控件")



def find_elements(driver,find_type, exrpession):
    """
    根据 find_type, exrpession 找控件列表，并返回控件列表
    :param driver:
    :param find_type:
    :param exrpession:
    :return:

    """
    # WebDriverWait(driver,sec).until(mesthod,message="") 表示每隔0.5秒就调用method方法，直到这个method不返回fasle为止
# 一旦超过了sec，就抛出异常，信息为 message
    try:
        elements = WebDriverWait(driver,10).until(lambda driver: driver.find_elements(by=find_type, value=exrpession))
        return elements
    except:
        print("没找到控件")