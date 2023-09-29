# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key,Controller
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Billing(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(10)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Billing).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Bill).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Search Bill Page open successfully' )
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Branch).click()
        Branch=self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Branch.send_keys('HEAD OFFICE')
        Branch.send_keys(Keys.RETURN)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('BRANCH NAME : {a}'.format(a ='HEAD OFFICE'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Date_range).click()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Start_date).clear() 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Start_date).send_keys(data.Logi_Data().From_date)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().End_date).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().End_date).send_keys(data.Logi_Data().To_date)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().apply_date).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Search_bill).click()
        sleep(20) 
        Show_data = Select (self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Show_entries))
        Show_data.select_by_value('50')
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Search_option).send_keys(data.Logi_Data().search_id)
        sleep(5)       
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().edit_option).click()
        sleep(5) 
       
    
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().cheque).click()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().cheque_Date).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().cheque_Date).send_keys(data.Logi_Data().cheque_date)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cheque Date : {a}'.format(a = data.Logi_Data().cheque_date))
        sleep(5)
        bank = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().bank))
        bank.select_by_value('6')
        selected_option = bank.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Bank Name : {a}'.format(a = selected_text))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().cheque_no).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().cheque_no).send_keys(data.Logi_Data().cheque_no)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cheque Number : {a}'.format(a = data.Logi_Data().cheque_no))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().cheque_amount).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().cheque_amount).send_keys(data.Logi_Data().cheque_amt)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cheque Amount : {a}'.format(a = data.Logi_Data().cheque_amt))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().cheque_page_save).click()
        
      
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_bill_edit).click()
        bill = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_bill_edit).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print("clicking Button : {a}".format(a = bill))
        print("save bill edit Option successfully completed")
        
        
        
    