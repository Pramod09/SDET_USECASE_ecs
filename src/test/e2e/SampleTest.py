from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ECSDigitalChal :

    def __init__(self, browserName) :

        self.URL = "http://localhost:3000/"
        self.BrowserPath = "./chromedriver"
        self.BrowserName = "Chrome"
        self.UserName = "Pramod Dalavi"
        
        self.btnRender = "//*[@id='home']/div/div/button"
        self.xpathOfRow1 = "//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[1]"
        self.xpathOfRow2 = "//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[2]"
        self.xpathOfRow3 = "//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[3]"
        
        self.txtSubChale1 = "/html/body/div[1]/div/section[2]/div/div/div[2]/div/div[1]/div[1]/input"
        self.txtSubChale2 = "/html/body/div[1]/div/section[2]/div/div/div[2]/div/div[1]/div[2]/input"
        self.txtSubChale3 = "/html/body/div[1]/div/section[2]/div/div/div[2]/div/div[1]/div[3]/input"
        self.txtName = "/html/body/div[1]/div/section[2]/div/div/div[2]/div/div[1]/div[4]/input"
        self.btnSumbit = "//*[@id='challenge']/div/div/div[2]/div/div[2]/button"
        self.driver = webdriver

        if self.BrowserName in browserName :
            self.driver = webdriver.Chrome(self.BrowserPath)
            self.driver.get(self.URL)
            self.driver.maximize_window()
            
    def getSumOfList(arr) :
        sumL = 0
        for index in range(len(arr)) :
            sumL += arr[index]
        return sumL

    def getAvgIndex(arr) :
        index = 0
        for index in range(len(arr)) :
            if ECSDigitalChal.getSumOfList(arr[:index]) == ECSDigitalChal.getSumOfList(arr[index+1:]) :
                    break
        if index == len(arr) :
            index = None
        return index

    def continueTest(self) :
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btnRender).click()
        return True
    
    def getIndexOfSum(self, tableTrXpath) : 
        row = []
        for ele in range(1, 10) :
            value =  self.driver.find_element_by_xpath(tableTrXpath+"/td["+str(ele)+"]").text
            row.append(int(value))
        return ECSDigitalChal.getAvgIndex(row)

    def submitChaResult(self, *result) :
        
        self.driver.find_element_by_xpath(self.txtSubChale1).send_keys(result[0])
        self.driver.find_element_by_xpath(self.txtSubChale2).send_keys(result[1])
        self.driver.find_element_by_xpath(self.txtSubChale3).send_keys(result[2])
        self.driver.find_element_by_xpath(self.txtName).send_keys(self.UserName)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btnSumbit).click()

    def __del__(self) :
        time.sleep(3)
        self.driver.close()
        
if __name__ == "__main__" :
    escInst = ECSDigitalChal("Chrome")

    if escInst.continueTest() :
        indexOfFirstRow1 = escInst.getIndexOfSum(escInst.xpathOfRow1)
        indexOfFirstRow2 = escInst.getIndexOfSum(escInst.xpathOfRow2)
        indexOfFirstRow3 = escInst.getIndexOfSum(escInst.xpathOfRow3)
        escInst.submitChaResult(indexOfFirstRow1, indexOfFirstRow2, indexOfFirstRow3)