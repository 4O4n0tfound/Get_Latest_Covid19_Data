# coding=utf-8

from Window_Control import driver,window_control
from Locations import *
from Found_Element import found_element
import time
from Count_Covid_Num import count_covid_num
url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'


if __name__ == '__main__':
    driver.implicitly_wait(10)
    # 打开浏览器指定url
    WC = window_control(url)
    WC.open_window()
    #WC.maximize_window(
    count_covid_num()
    WC.close_window()





