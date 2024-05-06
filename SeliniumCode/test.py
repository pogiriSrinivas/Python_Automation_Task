# Kinetic Investment Automation task modules
from selenium.webdriver.common.by import By
from SeliniumCode.SeliniumClassFile import (LoginUser, WebDriverMethodClass,
                                            GDAPI, ChromeOptions, DataHandling, DateGenerator)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import re

url = 'https://a2om.app.match2one.com/#/login'
username = "sambasiva.gangumolu@mediamint.com"
password = "@Shiva@11216@"
download_directory = r'D:\Downloadcsv'
dest_file_name = 'Mysheet_KI'
chromedriver_path = r'D:\Webdriver\chromedriver-win64\chromedriver.exe'
ChromeOptions_instance = ChromeOptions(download_directory, chromedriver_path)
chrome_options = ChromeOptions_instance.chrome_options
driver = webdriver.Chrome(service=Service(executable_path=chromedriver_path),
                          options=chrome_options)
date_range = "last monday to sunday"
required_clients_of_finixio = {
    'CO-KTSW8Z6X' : "Luckyblock℗",
    'CO-KTSW83DS' : "Slothana℗",
    'CO-KTSW83CY' : "Dogecoin20℗",
    'CO-KTSW83CT' : "5thscape℗",
    'CO-KTSW83BJ' : "Green℗",
    'CO-KTSW83B4' : "Scotty℗",
    'CO-KTSW83AM' : "eTukTuk℗",
    'CO-KTSW82XP' : "Bitcoin Minetrix℗",
    'CO-KTSW82XN' : "TG Casino℗",
    'CO-KTSW82QT' : "Megadice℗",
    'CO-KTSW82MR' : "Sponge",
    'CO-KTSW82B5' : "LuckyBlock (FTD)℗"
}
process_completed_for = []

#
second_column_cells = []
final_accounts_data = []


def finixio_sub_projects_data():
    c_ids = []
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)
    cells = driver.find_elements(By.TAG_NAME, "th")
    sleep(2)
    pattern = re.compile('|'.join(map(re.escape, required_clients_of_finixio.keys())))
    for cell in cells:
        print(cell.text)
        c_ids.append(cell.text)
    return c_ids


def matching_sub_accounts_on_the_current_page():

    all_sub_accounts_current_page = finixio_sub_projects_data()
    matching_current_page_accounts = [(key, value) for key, value in required_clients_of_finixio.items() if key in all_sub_accounts_current_page]

    print(matching_current_page_accounts)
    return matching_current_page_accounts


def selenium_finixio_task():

    # Wep Application elements and Xpath values
    username_placeholder = "Email"
    password_placeholder = "Password"
    btn_placeholder = r'/html/body/div[2]/div/div/div/div/form/button'
    companies_xpath = "/html/body/header/nav/div/div/ul/li[2]/ul/li[3]/a"
    input_filed_xpath = "/html/body/div[2]/div/nav/div[1]/div[2]/div/input"
    input_filed_search_key = "Finixio"
    objects_menu = "objects_menu"
    input_filed_btn_xpath = "/html/body/div[2]/div/nav/div[1]/div[2]/div/button"
    finixio_xpath = "/html/body/div[2]/div/div/div/table/tbody/tr/td[1]/a/span"
    balance_option_xpath = "/html/body/div[2]/div/div[2]/nav/a[5]"
    table_xpath = '/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table'
    page_2_xpath = '/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/nav/ul/li[2]/a'
    page_3_xpath = '/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/nav/ul/li[3]/a'
    reports_option_xpath = "/html/body/div[2]/div/div[2]/nav/a[10]"
    geo_stats_xpath = "/html/body/div[2]/div/div[2]/div/div/div[12]/div/div/div/table/tbody/tr[1]/td[1]"
    date_field_one = "/html/body/div[2]/div/div[2]/div/div/div[12]/div/div[1]/div/div/div/div/div[1]/div/div[3]/input"
    date_field_two = "/html/body/div[2]/div/div[2]/div/div/div[12]/div/div[1]/div/div/div/div/div[2]/div/div[3]/input"
    refresh_button = "/html/body/div[2]/div/div[2]/div/div/div[12]/div/nav/div/div[2]/button[1]"
    csv_btn = "/html/body/div[2]/div/div[2]/div/div/div[12]/div/nav/div/div[2]/button[2]"

    # internal variables
    list_options_to_be_clicked = [objects_menu, companies_xpath, input_filed_xpath,
                                  input_filed_search_key, input_filed_btn_xpath, finixio_xpath,
                                  balance_option_xpath, page_2_xpath, reports_option_xpath, geo_stats_xpath,
                                  date_field_one, date_field_two, refresh_button, csv_btn, page_3_xpath]
# Instantiating the classes
    driver.get(url)
    login_user_instance = LoginUser(url, username, password, driver, download_directory, chromedriver_path,
                                    username_placeholder, password_placeholder, btn_placeholder)
    WebDriverMethodClass_instance = WebDriverMethodClass(driver, download_directory, chromedriver_path)
    login_user_instance.login_user()
    print("Login Successful...")

    WebDriverMethodClass_instance.driver_find_element_method_by_id(list_options_to_be_clicked[0]).click()
    sleep(2)
    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[1]).click()
    sleep(2)
    (WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[2])
     .send_keys(list_options_to_be_clicked[3]))
    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[4]).click()
    sleep(2)
    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[5]).click()
    sleep(2)
    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[6]).click()
    sleep(5)
    finixio_sub_projects_data()
    # matching_sub_accounts_on_the_current_page()
    for i in range(6):
        val = i + 1
        sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(5)
        driver.find_element(By.XPATH, f"//*[contains(text(), '{val}')]").click()
        sleep(5)
        finixio_sub_projects_data()


selenium_finixio_task()





