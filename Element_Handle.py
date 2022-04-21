# coding=utf-8
"""
这个函数是用来处理元素定位的。
因为有些元素定位是唯一的，有些却需要用户的输入，然后组成最终的定位信息。
"""

def element_handle(origin_element, customize_part=None):
    if customize_part != None:
        final_element = origin_element.format(customize_part)
        return final_element
    else:
        return origin_element
