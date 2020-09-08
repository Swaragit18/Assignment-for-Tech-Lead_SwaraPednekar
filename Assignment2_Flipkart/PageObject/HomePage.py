from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # By.XPATH, "//div[@class='_3Njdz7']/button")
    loginClose = (By.XPATH, "//div[@class='_3Njdz7']/button")

    #self.driver.find_element_by_css_selector("input[type='text']").send_keys(search)
    searchText = (By.CSS_SELECTOR, "input[type='text']")

    #self.driver.find_element_by_xpath("//button[@class='vh79eN']").click()
    searchButton = (By.XPATH, "//button[@class='vh79eN']")

    #self.driver.find_element_by_xpath("//div[@class='_1qKb_B']//select[@class='fPjUPw']")
    rangeX = (By.XPATH, "//div[@class='_1qKb_B']//select[@class='fPjUPw']")

    #self.driver.find_element_by_xpath("//div[@class='_1YoBfV']//select[@class='fPjUPw']")
    rangeY = (By.XPATH, "//div[@class='_1YoBfV']//select[@class='fPjUPw']")

    #self.driver.find_element_by_xpath("//section[4]//div[2]//div[1]//div[3]//div[1]//div[1]//label[1]//div[1]").click()
    ram = (By.XPATH, "//section[4]//div[2]//div[1]//div[3]//div[1]//div[1]//label[1]//div[1]")

    #self.driver.find_element_by_xpath("//div[contains(text(),'Processor Brand')]").click()
    processorBrand = (By.XPATH, "//div[contains(text(),'Processor Brand')]")

    #self.driver.find_element_by_xpath("//section[16]//div[2]//div[1]//div[3]//div[1]//div[1]//label[1]//div[1]").click(
    processorBrandCheckbox = (By.XPATH, "//section[16]//div[2]//div[1]//div[3]//div[1]//div[1]//label[1]//div[1]")

    #self.driver.find_elements_by_xpath("//a[@class='_31qSD5']")
    multipleProducts = (By.XPATH, "//a[@class='_31qSD5']")

    def getsearchText(self):
        return self.driver.find_element(*HomePage.searchText)

    def getsearchButton(self):
        return self.driver.find_element(*HomePage.searchButton)

    def getrangeX(self):
        return self.driver.find_element(*HomePage.rangeX)

    def getrangeY(self):
        return self.driver.find_element(*HomePage.rangeY)

    def getram(self):
        return self.driver.find_element(*HomePage.ram)

    def getprocessorBrand(self):
        return self.driver.find_element(*HomePage.processorBrand)

    def getprocessorBrandCheckbox(self):
        return self.driver.find_element(*HomePage.processorBrandCheckbox)

    def getmultipleProducts(self):
        return self.driver.find_elements(*HomePage.multipleProducts)
