# coding=utf-8
from  Window_Control import driver
from Locations import *
from Element_Handle import element_handle
class found_element():

    """
    重新封装 find_element_by 方法
    """
    def __init__(self, origin_element, customize_element=None):
        self.origin_element = origin_element
        self.customize_element = customize_element

    def by_xpath(self):
        final_element = element_handle(self.origin_element,self.customize_element)
        xpath = driver.find_element_by_xpath(final_element)
        return xpath

