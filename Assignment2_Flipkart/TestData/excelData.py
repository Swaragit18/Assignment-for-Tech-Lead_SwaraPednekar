# # import openpyxl
# import pandas as pd
import csv
class ExcelData:

    def getExcelData(self):
        path = r'E:\Swara\Selenium-python\Pycharm Projects\Assignment2_Flipkart\InputDataFile.csv'
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return(row['Product to search'])
                # print(row)

    def writeExcelData(df):
        filename = r'E:\Swara\Selenium-python\Pycharm Projects\Assignment2_Flipkart\OutputFile.csv'
        df.to_csv(filename, index=False)


