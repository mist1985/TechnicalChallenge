import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from BasePage import BasePage, HomePage, BrowsingPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("http://automationpractice.com/")

signin = HomePage (driver)

signin.click_signin_button()

signin.enter_email_address()

signin.select_gender()

signin.enter_firstname()
signin.enter_lastname()
signin.enter_password()

signin.day_of_birth()
signin.month_of_birth()
signin.year_of_birth()

signin.enter_firstname_address()
signin.enter_lastname_address()
signin.company_address()
signin.company_address_1()
signin.company_address_2()
signin.city()
signin.state()
signin.zip()
signin.country()
signin.additional_info()
signin.phone()
signin.mobile()
signin.alias_address()
signin.register_button()

signin.sign_out_exists()

signin.click_on_home_page()

browsingpage = BrowsingPage (driver)

browsingpage.number_of_popular()
browsingpage.enter_search_word()
browsingpage.click_search_button()

