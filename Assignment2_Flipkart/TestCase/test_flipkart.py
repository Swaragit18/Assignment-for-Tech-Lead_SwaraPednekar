import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

from PageObject.HomePage import HomePage
from TestData.excelData import ExcelData
from utilities.BaseClass import BaseClass

class TestCase(BaseClass):

    def test_Flipkartecommercewebsite(self):
        homePage = HomePage(self.driver)
        search = ExcelData.getExcelData(self)
        print(search)
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((homePage.loginClose))).click()
        homePage.getsearchText().send_keys(search)
        homePage.getsearchButton().click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((homePage.rangeX)))
        dropdown = Select(homePage.getrangeX())
        dropdown.select_by_visible_text("Min")
        wait.until(expected_conditions.presence_of_element_located((homePage.rangeY)))
        dropdown1 = Select(homePage.getrangeY())
        dropdown1.select_by_visible_text("₹10000")
        time.sleep(5)
        homePage.getram().click()
        time.sleep(5)
        homePage.getprocessorBrand().click()
        homePage.getprocessorBrandCheckbox().click()
        products = homePage.getmultipleProducts()
        dict = {'Mobile Name':[], 'Price(Rs)':[]}
        for product in products:
            productName = product.find_element_by_xpath("div[2]/div[1]/div[1]").text
            price = product.find_element_by_xpath("div[2]/div[2]/div[1]/div[1]/div[1]").text
            dict['Mobile Name'].append(productName)
            dict['Price(Rs)'].append(price[1:])

        df = pd.DataFrame(dict)
        ExcelData.writeExcelData(df)
        self.driver.get_screenshot_as_file("productlist.png")





