# coding=utf-8
from Found_Element import found_element
from Locations import *
"""
用来打印每天新增的数目
"""

def count_covid_num():
    covid_newadd_shanghai_number = found_element(covid_newadd_shanghai).by_xpath().text  # 国内新增本土数量
    print "今日上海新增: {}".format(covid_newadd_shanghai_number)
    found_element(city_shanghai).by_xpath().click()  # 选择上海
    found_element(one_area, '长宁区').by_xpath().click()  # 选择长宁区
    covid_newadd_changing_number = found_element(covid_newadd_changing).by_xpath().text  # 长宁新增
    print "今日长宁区新增: {}".format(covid_newadd_changing_number)