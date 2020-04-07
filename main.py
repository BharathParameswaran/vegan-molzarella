from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time

class InstagramBot():
	def __init__(self, email, password):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--incognito")
		self.browser = webdriver.Chrome(executable_path=os.path.abspath("./chromedriver"), chrome_options=chrome_options)
		self.email = email
		self.password = password
    
	def signIn(self):
	    self.browser.get('https://www.instagram.com/accounts/login/')
	    time.sleep(2)
	    emailInput = self.browser.find_element_by_name('username')
	    passwordInput = self.browser.find_element_by_name('password')

	    emailInput.send_keys(self.email)
	    passwordInput.send_keys(self.password)
	    passwordInput.send_keys(Keys.ENTER)
	    time.sleep(3)
	    buttons = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
	    for btn in buttons:
    		btn.click()

    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()

bot = InstagramBot('shakahaar1', 'LaLaLand@1993X')
bot.signIn()