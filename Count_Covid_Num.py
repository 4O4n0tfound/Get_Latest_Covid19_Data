# coding=utf-8
from Found_Element import found_element
from Locations import *
from datetime import datetime
import json

"""
用来打印每天新增的数目
"""

def count_covid_num():
    init_date = datetime.today().date()
    today_date = str(init_date).split('-')[-2] + str(init_date).split('-')[-1]
    covid_newadd_shanghai_number = found_element(covid_newadd_shanghai).by_xpath().text  # 国内新增本土数量
    found_element(city_shanghai).by_xpath().click()  # 选择上海
    found_element(one_area, '长宁区').by_xpath().click()  # 选择长宁区
    covid_newadd_changning_number = found_element(covid_newadd_changing).by_xpath().text  # 长宁新增
    with open('Data.json', 'r+') as fp:
        json_file = json.load(fp)
        keys = json_file.keys()
        if today_date in keys:
            json_file[today_date].update({"guonei":covid_newadd_shanghai_number,"changning":covid_newadd_changning_number})
        else:
            json_file.update({today_date:{"guonei":covid_newadd_shanghai_number,"changning":covid_newadd_changning_number}})
        #json_file.update(json_file)
        fp.seek(0,0)
        fp.truncate()
        fp.write(json.dumps(json_file))
    print "今日({}月{}日)上海新增:{}".format(str(init_date).split('-')[-2],str(init_date).split('-')[-1],covid_newadd_shanghai_number)
    print "今日({}月{}日)长宁新增:{}".format(str(init_date).split('-')[-2],str(init_date).split('-')[-1],covid_newadd_changning_number)


#今日(4月24日)上海新增: 1,583