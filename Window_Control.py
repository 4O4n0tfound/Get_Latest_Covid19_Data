# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
class window_control():

    """
    所有对窗口的操作，将保存在这个文件中(例如打开/关闭窗口，窗口最大化）
    """
    def __init__(self, url):
        self.url = url

    def open_window(self):
        driver.get(self.url)

    def close_window(self):
        driver.quit()

    def maximize_window(self):
        driver.maximize_window()

    def minimize_window(self):
        driver.minimize_window()






