from selenium import webdriver
from time import sleep

username = 'azhaarm94@gmail.com'
password = 'azhaar354'

class QL_Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://qatarliving.com')

        sleep(2)
        lg_btn =  self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/header/div[2]/div/div[1]/div/a[2]')
        lg_btn.click()

        sleep(4)
        email_in = self.driver.find_element_by_xpath('//*[@id="edit-name"]')
        email_in.send_keys(username)

        sleep(2)
        pw_in = self.driver.find_element_by_xpath('//*[@id="edit-pass"]')
        pw_in.send_keys(password)

        sleep(1)
        login_bt = self.driver.find_element_by_xpath('//*[@id="edit-submit"]')
        login_bt.click()

        sleep(1)
        js_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/a')
        js_btn.click()

        sleep(1)
        js1_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/main/div/div[2]/div/div/a/div[2]')
        js1_btn.click()

        sleep(1)
        rfs_btn = self.driver.find_element_by_xpath('//*[@id="classifieds"]/main/div[1]/a')
        rfs_btn.click()

        sleep(1)
        mnu_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/header/div[2]/div/div[1]/div/a[1]/span')
        mnu_btn.click()

        sleep(1)
        lg_out = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/a[2]')
        lg_out.click()




bot = QL_Bot()
bot.login()
