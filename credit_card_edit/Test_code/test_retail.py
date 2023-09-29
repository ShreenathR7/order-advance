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
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Start date : {a}'.format(a =data.Logi_Data().From_date))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().End_date).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().End_date).send_keys(data.Logi_Data().To_date)
        sleep(5)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('End date : {a}'.format(a =data.Logi_Data().To_date))
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
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().cash).send_keys(data.Logi_Data().cash_amount)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Cash amount : {a}'.format(a =data.Logi_Data().cash_amount))     
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().card_payment_option).click()
    
        sleep(10)
        card = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_name))
        card.select_by_value('3')
        selected_option = card.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card Name : {a}'.format(a = selected_text))
        sleep(5)
        card_type = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_type))
        card_type.select_by_value('1')
        selected_option = card_type.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card type : {a}'.format(a = selected_text))
        sleep(5)
        card_device = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Device_name))
        card_device.select_by_value('1')
        selected_option = card_device.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Device Name : {a}'.format(a = selected_text))
        sleep(8)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_No).clear()
        sleep(8)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_No).send_keys(data.Logi_Data().card_no)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card Number : {a}'.format(a = data.Logi_Data().card_no))
        sleep(8)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_amount).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().card_amount).send_keys(data.Logi_Data().card_amount)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Card Amount : {a}'.format(a = data.Logi_Data().card_amount))
        sleep(8)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().approval).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().approval).send_keys(data.Logi_Data().approval_no)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Approval Number : {a}'.format(a = data.Logi_Data().approval_no))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().credit_pagr_save).click()
        
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_bill_edit).click()
        bill = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_bill_edit).text
        assert self.driver.title == 'Logimax Technology | Admin'
        print("clicking Button : {a}".format(a = bill))
       # print("save bill edit Option successfully completed")
        
        
        
    