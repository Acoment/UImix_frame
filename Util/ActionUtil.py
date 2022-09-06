# -*- coding: utf-8 -*- 
# @Time : 2022-06-05 16:14 
# @Author : 皓雪
# @File : ActionUtil.py 
# @Software: PyCharm
import time

from selenium import webdriver

# 全局变量
from Util.ElementUtil import find_element, find_elements

driver = None


def open_browser(browser_name, *args):
    """
    打开浏览器
    :param browser_name:
    :param args:
    :return:
    """
    global driver

    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()

def get_url(url, *args):
    """
    输入网址
    :param url:
    :param args:
    :return:
    """
    try:
        driver.get(url)
    except Exception as e:
        raise e


def time_wait(seconds, *args):
    """
    等待
    :param seconds:
    :param args:
    :return:
    """
    try:
        time.sleep(seconds)
    except Exception as e:
        raise e

def max_window(*args):
    """
    浏览器窗口最大化
    :param args:
    :return:
    """
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


def switch_frame(location_type, location_express, *args):
    """
    切换frame
    :param location_type:
    :param location_express:
    :param args:
    :return:
    """
    try:
        i_frame = find_element(driver, location_type, location_express)
        driver.switch_to.frame(i_frame)
    except Exception as e:
        raise e
def default_frame(*args):
    """
    退出frame
    :param location_type:
    :param location_express:
    :param args:
    :return:
    """
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def input_content(location_type, location_express, value, *args):
    '''
    输入文本
    :param location_type:
    :param location_expres:
    :param value:
    :param args:
    :return:
    '''
    try:
        element = find_element(driver, location_type, location_express)
        element.send_keys(value)
    except Exception as e:
        raise e

def input_subject(location_type, location_express, value,*args):
    """
    输入主题
    :param location_type:
    :param location_express:
    :param value:
    :param args:
    :return:
    """
    try:
        location_express , index = location_express.split(',')
        find_elements(driver, location_type, location_express)[int(index)].send_keys(value)
    except Exception as e:
        raise



def click(location_type, location_express, *args):
    """
    单击
    :param location_type:
    :param location_express:
    :param args:
    :return:
    """
    try:
        element = find_element(driver, location_type, location_express)
        element.click()
    except Exception as e:
        raise e





def close_browser(*args):
    """
    关闭浏览器
    :param args:
    :return:
    """
    driver.quit()


if __name__ == '__main__':
    open_browser('chrome')
    get_url("http://mail.163.com")
    max_window()
    time_wait(3)
    switch_frame('tag name','iframe')
    input_content('name','email','zhangmingn002')
    input_content('name','password','cc')



