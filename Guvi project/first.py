import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
class Create_query:
    '''Create the class for login page'''
    def login(self):
        # To provide the username and password for the login form
        driver.get('https://www.zenclass.in')
        time.sleep(4)
        input_username = driver.find_element(by=By.XPATH,
                                             value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input').send_keys('psra7598@gmail.com')
        time.sleep(4)
        input_userpassword = driver.find_element(by=By.XPATH,
                                                 value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input').send_keys('Varshini@4141013')
        time.sleep(4)
        btn_login = driver.find_element(by=By.XPATH,
                                        value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button').click()
     def main_page(self):
        # loading the navigation bar
        time.sleep(3)
        side_bar = driver.find_element(by=By.XPATH,
                                       value='//*[@id="root"]/div[1]/nav/ul/div[1]/li/span/div/div[1]')
        actionchains = ActionChains(driver)
        time.sleep(3)
        actionchains.move_to_element(side_bar).perform()
        time.sleep(3)
        create_Query = driver.find_element(by=By.XPATH,
                                           value='//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]')
        time.sleep(3)
        create_Query.click()
        time.sleep(3)
        away_side_bar = driver.find_element(by=By.XPATH,
                                            value="/html/body/div")
        actionchains.move_to_element(away_side_bar).perform()
    def create_Query_page(self):
        # creating a query
        numbers =0
        while numbers < 4:
            time.sleep(3)
            btn_create_query = driver.find_element(by=By.XPATH,
                                                   value='//*[@id="root"]/div[2]/div/div[1]/div[1]/button').click()
            time.sleep(3)
            btn_create_query_cancel = driver.find_element(by=By.XPATH,
                                                          value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]").click()
            time.sleep(3)
            crete_query_category = driver.find_element(by=By.XPATH,
                                                       value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select')
            crete_query_category.click()
            click_dd = Select(crete_query_category)
            print(click_dd.select_by_index(1))
            click_dd.select_by_index(1)  # zen class creating the query
            time.sleep(3)
            create_query_subcategory = driver.find_element(by=By.XPATH,
                                                           value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select')
            create_query_subcategory.click()
            time.sleep(3)
            click_dd = Select(create_query_subcategory)
            time.sleep(3)
            click_dd.select_by_index(1)  # zen class creating the subcategory

            create_query_lang = driver.find_element(by=By.XPATH,
                                                    value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select')
            create_query_lang.click()
            time.sleep(3)
            click_dd = Select(create_query_lang)
            time.sleep(3)
            click_dd.select_by_index(2)  # zen class creating the subcategory

            time.sleep(3)
            create_query_Title = driver.find_element(by=By.XPATH,
                                                     value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input').send_keys(
                'Guvi Python AT - 1 & W Automation Project')  # zen class for providing the title of the query

            time.sleep(3)
            create_query_description = driver.find_element(by=By.XPATH,
                                                           value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea').send_keys(
                'This is a Project Test Code Running for the Python Automation - 1 & 2 Project Given by a mentor Mr.Suman Gangopadhyay')  # zen class for creating the description
            time.sleep(3)
            btn_submit = driver.find_element(by=By.XPATH,
                                             value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button').click()
            numbers=numbers+1



lurl = Create_query()           #object for the class
lurl.login()
lurl.main_page()
lurl.create_Query_page()
