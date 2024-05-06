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
# required_clients_of_finixio = [
#     "Luckyblock℗",
#     "Slothana℗",
#     "Dogecoin20℗",
#     "5thscape℗",
#     "Green Bitcoin ℗",
#     "Scotty The AI℗",
#     "eTukTuk℗",
#     "Bitcoin Minetrix℗",
#     "TG Casino℗",
#     "Megadice℗",
#     "Sponge V2℗",
#     "LuckyBlock (FTD)℗"
# ]

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
    'CO-KTSW82MR' : "Sponge V2℗",
    'CO-KTSW82B5' : "LuckyBlock (FTD)℗"
}
process_completed_for = []
print(process_completed_for)


# def finixio_sub_projects_data():
#
#     accounts_data = []
#     rows = driver.find_elements(By.TAG_NAME, "tr")
#
#     # Iterate through each row, extract the value at index 1, and store it in accounts_data
#     for row in rows:
#         row_values = row.text.split()
#         # print(row_values)
#         if len(row_values) > 0 and row_values[0].startswith('C'):
#             accounts_data.append(row_values)
#
#     print("Accounts Data:", accounts_data)
#
#     final_accounts_data = accounts_data[:]
#
#     i = 0
#     while len(accounts_data) > i:
#         ele = accounts_data[i]
#         j = 0
#         if len(ele) > j + 3 and ele[j + 1][0].isalpha() and ele[j + 2][0].isalpha() and ele[j + 3][0].isdigit():
#             concat_val = accounts_data[i][j + 1] + " " + accounts_data[i][j + 2]
#             final_accounts_data[i].insert(1, concat_val)
#             final_accounts_data[i].pop(2)
#             final_accounts_data[i].pop(2)
#         i = i + 1
#
#     print(final_accounts_data)
#
#     return final_accounts_data



# def finixio_sub_projects_data():
#     second_column_cells = []
#     final_accounts_data = []
#     sleep(3)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     sleep(3)
#     cells = driver.find_elements(By.TAG_NAME, "td")
#     sleep(2)
#     pattern = r'^[a-zA-Z0-9]+\s?[a-zA-Z]*[^\w\s]?\s?$'
#
#     for row in cells:
#         second_column_cells.append(row.text)
#
#     for cell in second_column_cells:
#         # Apply your regex pattern to check if the cell text matches the desired format
#         if re.search(pattern, cell):
#             final_accounts_data.append(cell)
#     print(final_accounts_data)
#     return final_accounts_data


# def matching_sub_accounts_on_the_current_page():
#     matching_current_page_accounts = []
#     all_sub_accounts_current_page = finixio_sub_projects_data()
#     i = 0
#     while len(all_sub_accounts_current_page) > i:
#         j = 0
#         if all_sub_accounts_current_page[i][j+1] in required_clients_of_finixio:
#             matching_current_page_accounts.append(all_sub_accounts_current_page[i][j+1])
#         i = i+1
#     print(matching_current_page_accounts)
#     return matching_current_page_accounts

# def matching_sub_accounts_on_the_current_page():
#
#     all_sub_accounts_current_page = finixio_sub_projects_data()
#     matching_current_page_accounts = [value for value in all_sub_accounts_current_page if value
#                                       in required_clients_of_finixio]
#     print(matching_current_page_accounts)
#     return matching_current_page_accounts

def finixio_sub_projects_data():
    c_ids = []
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)
    cells = driver.find_elements(By.TAG_NAME, "th")
    sleep(2)
    pattern = re.compile('|'.join(map(re.escape, required_clients_of_finixio.keys())))
    for cell in cells:
        c_ids.append(cell.text)
    return c_ids


def matching_sub_accounts_on_the_current_page():

    all_sub_accounts_current_page = finixio_sub_projects_data()
    matching_current_page_accounts = [key for key in required_clients_of_finixio.keys() if
                                      key in all_sub_accounts_current_page]

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
    matching_sub_accounts_current_page = matching_sub_accounts_on_the_current_page()
    list_length = len(matching_sub_accounts_current_page)
    if len(process_completed_for) < 12:
        print('Pending with sub accounts......')
        if list_length == 0:
            print("Not even a single client is matched continue the process to the next page....")
            sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(5)
            WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[7]).click()
            sleep(5)
            print("Next page......")
            finixio_sub_projects_data()
            matching_sub_accounts_current_page = matching_sub_accounts_on_the_current_page()
            print(f"Matching accounts: {matching_sub_accounts_current_page} now we need to perform the next steps")

            for j in range(1, 6):
                list_length_current = len(matching_sub_accounts_current_page)
                k = j + 1
                for i in range(list_length_current):

                    print(f"i {i} value")
                    val = matching_sub_accounts_current_page[i]
                    print(val)
                    sleep(5)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    sleep(5)
                    # driver.find_element(By.XPATH, f"//*[contains(text(), '{val}')]").click()
                    driver.find_element(By.XPATH, f"//a[contains(text(), '{val}')]").click()
                    sleep(5)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[8]).click()
                    sleep(2)
                    dates = DateGenerator.fetch_date_range(date_range)
                    sleep(5)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[9]).click()
                    sleep(2)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[10]).clear()
                    sleep(2)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[11]).clear()
                    sleep(2)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[10]).send_keys(
                        str(dates[0]))
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[11]).send_keys(
                        str(dates[1]))
                    sleep(2)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[12]).click()
                    sleep(2)
                    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[13]).click()
                    sleep(10)
                    print("Reports file downloaded successfully......")
                    sleep(3)
                    driver.execute_script("window.history.go(-4)")
                    sleep(3)
                    process_completed_for.append(matching_sub_accounts_current_page[i])

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                sleep(3)
                WebDriverMethodClass_instance.webdriver_wait_by_xpath(
                    f'/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/nav/ul/li[{k + 1}]/a').click()
                sleep(3)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                sleep(3)
                finixio_sub_projects_data()
                matching_sub_accounts_current_page = matching_sub_accounts_on_the_current_page()


selenium_finixio_task()
print(process_completed_for)
