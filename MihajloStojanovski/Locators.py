from selenium.webdriver.common.by import By
from selenium import webdriver
class Locators ():

    # -- Home Page Locators --
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a.login")

    # -- Create an account Email --
    CREATE_EMAIL = (By.ID, "email_create")

    # -- Create an Account Button --
    CREATE_BUTTON = (By.XPATH, "//button[@id='SubmitCreate']/span")

    # -- Select Gender --
    FORM_GENDER = (By.ID, "id_gender1")

    # -- First Name Form --
    FIRST_NAME = (By.ID, "customer_firstname")

    # -- Last Name Form --
    LAST_NAME = (By.ID, "customer_lastname")

    # -- Email form --
    EMAIL_FORM = (By.ID, "email")

    # -- Password Form --
    PASSWORD_FORM = (By.ID, "passwd")

    # -- Date of Birth - Day --
    DOB_DAY = (By.ID, "days")

    # -- Date of Birth - Month --
    DOB_MONTH = (By.ID, "months")

    # -- Date of Birth - Year --
    DOB_YEAR = (By.ID, "years")

    # -- Address First name --
    FIRSTNAME_ADDRESS = (By.ID, "firstname")

    # -- Address Last name --
    LASTNAME_ADDRESS = (By.ID, "lastname")

    # -- Address Company --
    COMPANY_ADDRESS = (By.ID, "company")

    # -- Address Street 1 --
    ADDRESS_1 = (By.ID, "address1")

    # -- Address Street 2 --
    ADDRESS_2 = (By.ID,"address2")

    # -- Adress City --
    ADDRESS_CITY = (By.ID, "city")

    # -- Address State --

    # ADDRESS_STATE = (By.ID, "id_state")
    ADDRESS_STATE = (By.XPATH, "//*[@id='id_state']")

    # -- Address ZIP ==
    ADDRESS_ZIP = (By.ID, "postcode")

    # -- Address Country --
    ADDRESS_COUNTRY = (By.ID, "id_country")

    # -- Address Additional information --
    ADDRESS_ADDITIONAL = (By.ID, "other")

    # -- Address Phone --
    ADDRESS_PHONE = (By.ID, "phone")

    # -- Address Mobile --
    ADDRESS_MOBILE = (By.ID,"phone_mobile")

    # -- Address Alias --
    ADDRESS_ALIAS = (By.ID, "alias")

    # -- Register Button --
    ADDRESS_REGISTER = (By.XPATH, "//button[@id='submitAccount']/span")

    # -- Sign Out Button --
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, "a.logout")

    # -- Click on Home page --
    HOME_PAGE_CLICK = (By.XPATH, "//div[@id='columns']/div/a/i")

    # -- Number of products --
    NUMBER_OF_POPULAR = (By.XPATH, "//div[@class = 'ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line first-item-of-tablet-line first-item-of-mobile-line'")
    BEST_SELLERS = (By.CLASS_NAME,"product_list grid row homefeatured tab-pane"
                                  "")
    # -- Enter Search word --
    SEARCH_WORD = (By.ID, "search_query_top")

    # -- Search button -
    CLICK_SEARCH_BUTTON = (By.XPATH, "//form[@id='searchbox']/button")


