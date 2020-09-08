import pytest
from selenium import webdriver

# from TestData.excelData import ExcelData
from TestData.excelData import ExcelData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\\Swara\\Selenium-python\\Drivers\\chromedriver.exe")
    elif browser_name == "Firefox":
        driver = webdriver.Chrome(executable_path="E:\\Swara\\Selenium-python\\Drivers\\geckodriver.exe")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()

