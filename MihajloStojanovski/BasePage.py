import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from Locators import Locators

class BasePage():
    """Parent class for all of the pages, elements and functionalities."""

    # This function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver

    # This function performs a click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()


    # This function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # This function checks if the web element is visible or not
    # Returns true or false depending upon its visibility. Hence bool.

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


class HomePage (BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_signin_button(self):
        self.is_visible(Locators.SIGN_IN_BUTTON)
        self.click(Locators.SIGN_IN_BUTTON)

    def enter_email_address(self):
        self.driver.find_element(*Locators.CREATE_EMAIL).clear()
        self.enter_text(Locators.CREATE_EMAIL, "mihajlo.stojanovski143@yopmail.com")
        self.click(Locators.CREATE_BUTTON)

    def select_gender(self):
        self.click(Locators.FORM_GENDER)

    def enter_firstname(self):
        self.enter_text(Locators.FIRST_NAME,"Mihajlo")

    def enter_lastname(self):
        self.enter_text(Locators.LAST_NAME,"Stojanovski")

    def enter_email(self):
        self.enter_text(Locators.EMAIL_FORM,"mihajlo.stojanovski103@yopmail.com")

    def enter_password(self):
        self.enter_text(Locators.PASSWORD_FORM,"Password!")

    def day_of_birth(self):
        self.click(Locators.DOB_DAY)

        "Tried to normalize the space for the extra space characters in the date, month and year by I could not make it work"
        # dob_select = self.driver.find_element(*Locators.DOB_DAY)
        # dob_select.click()
        # dob_option = dob_select.find_element_by_xpath(".//option[normalize-space()='31']")
        # dob_option.click()

        Select(self.driver.find_element(*Locators.DOB_DAY)).select_by_visible_text("31  ")

    def month_of_birth(self):
        self.click(Locators.DOB_MONTH)
        #dob_select = self.driver.find_element(*Locators.DOB_MONTH)
        # dob_select.click()
        # dob_option = dob_select.find_element_by_xpath(".//option[normalize-space()='October']")
        Select(self.driver.find_element(*Locators.DOB_MONTH)).select_by_visible_text("May ")


    def year_of_birth(self):
        self.click(Locators.DOB_YEAR)
        # dob_select = self.driver.find_element(*Locators.YEAR)
        # dob_select.click()
        # dob_option = dob_select.find_element_by_xpath(".//option[normalize-space()='1985']")
        Select(self.driver.find_element(*Locators.DOB_YEAR)).select_by_visible_text("1985  ")

    def enter_firstname_address(self):
        self.driver.find_element(*Locators.FIRSTNAME_ADDRESS).clear()
        self.enter_text(Locators.FIRSTNAME_ADDRESS, "Mihajlo")

    def enter_lastname_address(self):
        self.driver.find_element(*Locators.LASTNAME_ADDRESS).clear()
        self.enter_text(Locators.LASTNAME_ADDRESS, "Stojanovski")

    def company_address(self):
        self.enter_text(Locators.COMPANY_ADDRESS,"Fake Street 22")

    def company_address_1(self):
        self.enter_text(Locators.ADDRESS_1,"Fake Street Address 1")

    def company_address_2(self):
        self.enter_text(Locators.ADDRESS_2,"Fake Street Address 2")

    def city(self):
        self.enter_text(Locators.ADDRESS_CITY,"New York")

    def state(self):
        self.click(Locators.ADDRESS_STATE)
        Select(self.driver.find_element(*Locators.ADDRESS_STATE)).select_by_visible_text("Alabama")

    def zip(self):
        self.enter_text(Locators.ADDRESS_ZIP, "97000")

    def country(self):
        self.click(Locators.ADDRESS_COUNTRY)
        Select(self.driver.find_element(*Locators.ADDRESS_COUNTRY)).select_by_visible_text("United States")

    def additional_info(self):
        self.enter_text(Locators.ADDRESS_ADDITIONAL,"Additional Info")

    def phone(self):
        self.enter_text(Locators.ADDRESS_PHONE, "+38970777019")

    def mobile(self):
        self.enter_text(Locators.ADDRESS_MOBILE, "+38970777019")

    def alias_address(self):
        self.driver.find_element(*Locators.ADDRESS_ALIAS).clear()
        self.enter_text(Locators.ADDRESS_ALIAS, "Alias Address 22")

    def register_button(self):
        self.click(Locators.ADDRESS_REGISTER)

    def sign_out_exists(self):
        self.is_visible(Locators.SIGN_OUT_BUTTON)

    def click_on_home_page(self):
        self.click(Locators.HOME_PAGE_CLICK)

class BrowsingPage(BasePage):

    def number_of_popular(self):
       count_pop = len(Locators.NUMBER_OF_POPULAR)
       count_best =len(Locators.BEST_SELLERS)
       print ("The number is ", count_pop)
       print ("The number is ", count_best)

    def enter_search_word(self):
       self.driver.find_element(*Locators.SEARCH_WORD).clear()
       self.enter_text(Locators.SEARCH_WORD, "Printed dresses")

    def click_search_button(self):
        self.click(Locators.CLICK_SEARCH_BUTTON)
