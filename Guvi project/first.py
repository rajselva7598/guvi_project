import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Login:
    '''Create the class for login page'''
    service = Service('C:\Program Files (x86)\chromedriver.exe')
    driver = webdriver.Chrome(service= service)
    def provide_input(self,url):
         #To provide the username and password for the login form
        self.driver.get(url)
        input_value = self.driver.find_element(
        by=By.XPATH ,
        value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input')
        input_value.send_keys('psra7598@gmail.com')
        time.sleep(4)
        input_value = self.driver.find_element(
        by=By.XPATH , 
        value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input')
        input_value.send_keys('Varshini@4141013')
        submit=self.driver.find_element(
        by=By.XPATH , 
        value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button')
        submit.click()
    def load_side_bar(self):
        #loading the navigation bar
        time.sleep(3)
        action = ActionChains(self.driver)
        time.sleep(3)
        action_main= self.driver.find_element(
        by=By.XPATH , 
        value='/html/body/div/div[1]/nav/ul/div[6]/li/span/div/div[2]')
        time.sleep(3)
        action.move_to_element(action_main).click().perform()
    def create_query(self ,url1):
         #creating a query
        time.sleep(3)
        self.driver.get(url1)
        time.sleep(3)
        category =self.driver.find_element(
        by=By.XPATH , 
        value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select')
        time.sleep(3)
        communication =self.driver.find_element(
        by=By.XPATH , 
        value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select')
        time.sleep(3)
        query_title =self.driver.find_element(
        by=By.XPATH , 
        value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input')
        time.sleep(3)
        query_description =self.driver.find_element(
        by=By.XPATH ,
        value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea')
        time.sleep(3)
        btn_create_quries =self.driver.find_element(
        by=By.XPATH , 
        value='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button')
        time.sleep(3)
        category.send_keys("Placement Related")
        time.sleep(3)
        communication.send_keys('Tamil')
        time.sleep(3)
        query_title.send_keys('Guvi Python AT - 1 & W Automation Project')
        time.sleep(3)
        query_description.send_keys('This is a Project Test Code Running for the Python Automation - 1 & 2 Project Given by a mentor Mr.Suman Gangopadhyay')
        time.sleep(3)
        btn_create_quries.click()
        self.driver.close()
lurl = Login()
#initial page
URL='https://www.zenclass.in'
#login credentials
lurl.provide_input(URL)
#navigation
lurl.load_side_bar()
#create queries
URL1 ='https://www.zenclass.in/queries/create'
lurl.create_query(URL1)

