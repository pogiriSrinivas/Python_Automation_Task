from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SeliniumCode.SeliniumClassFile import (LoginUser, WebDriverMethodClass, GDAPI, ChromeOptions, DataHandling, DateGenerator, FileHandler, Extractor)
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import Select


url = 'https://a2om.app.match2one.com/#/login'
username = "sambasiva.gangumolu@mediamint.com"
password = "@Shiva@11216@"
download_directory = r'D:\Downloadcsv'
dest_file_name = 'FinixioDest'
chromedriver_path = r'D:\Webdriver\chromedriver-win64\chromedriver.exe'
ChromeOptions_instance = ChromeOptions(download_directory, chromedriver_path)
chrome_options = ChromeOptions_instance.chrome_options
driver = webdriver.Chrome(service=Service(executable_path=chromedriver_path), options=chrome_options)
company_name = "FinixioCampaigns"
date_range = "last monday to sunday"
# date_range = "last monday to wednesday"
# date_range = "last thursday to sunday"


def finixio_campaigns_sub_projects_data():
    sleep(3)
    rows = Extractor.single_table_row_extractor(driver)
    op_dict = Extractor.rows_to_dict(rows)
    print(op_dict)
    return op_dict


process_completed_for = []
print(process_completed_for)


def selenium_finixio_campaigns_task():
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
    campaigns_option_xpath = "/html/body/div[2]/div/div[2]/nav/a[2]"
    filter_option_xpath = "/html/body/div[2]/div/div[2]/div/div/div[3]/div/nav/div[1]/div[1]/button"
    drop_down_xpath = "/html/body/div[2]/div/div[2]/div/div/div[3]/div/nav/div[2]/select"
    second_input_filed_search_box = "/html/body/div[2]/div/div[2]/div/div/div[3]/div/nav/div/div[2]/div/input"
    second_input_filed_search_box_str_value = 'clickoutaudiences'
    second_input_filed_search_box_btn = '/html/body/div[2]/div/div[2]/div/div/div[3]/div/nav/div[1]/div[2]/div/button'
    page_2_xpath = '/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/nav/ul/li[2]/a'
    page_3_xpath = '/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/nav/ul/li[3]/a'
    reports_option_xpath = "/html/body/div[2]/div/div[2]/nav/a[2]"
    stats_xpath = "/html/body/div[2]/div/div[2]/div/div/div[11]/div/div/div/table/tbody/tr[3]/td[1]"
    advanced_search = "/html/body/div[2]/div/div[2]/div/div/div[11]/div/nav/div/div[1]/button"
    geo_stats_xpath = "/html/body/div[2]/div/div[2]/div/div/div[12]/div/div/div/table/tbody/tr[1]/td[1]"
    date_field_one = "/html/body/div[2]/div/div[2]/div/div/div[11]/div/div[1]/div/div/div/div/div[1]/div/div[3]/input"
    date_field_two = "/html/body/div[2]/div/div[2]/div/div/div[11]/div/div[1]/div/div/div/div/div[2]/div/div[3]/input"
    search_button = "/html/body/div[2]/div/div[2]/div/div/div[11]/div/nav/div/div[2]/div/button"
    csv_btn = "/html/body/div[2]/div/div[2]/div/div/div[11]/div/nav/div/div[2]/button"

    # internal variables
    list_options_to_be_clicked = [objects_menu, companies_xpath, input_filed_xpath,
                                  input_filed_search_key, input_filed_btn_xpath, finixio_xpath,
                                  campaigns_option_xpath, filter_option_xpath, drop_down_xpath,
                                  second_input_filed_search_box, second_input_filed_search_box_str_value,
                                  second_input_filed_search_box_btn, page_2_xpath, reports_option_xpath,
                                  geo_stats_xpath, date_field_one, date_field_two, csv_btn, page_3_xpath]
    # Instantiating the classes
    driver.maximize_window()
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
    sleep(2)
    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[7]).click()
    sleep(2)
    drop_down = WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[8])
    select_value = Select(drop_down)
    sleep(3)
    select_value.select_by_visible_text("Active")
    sleep(2)
    (WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[9])
     .send_keys(list_options_to_be_clicked[10]))
    sleep(2)
    WebDriverMethodClass_instance.webdriver_wait_by_xpath(list_options_to_be_clicked[11]).click()
    sleep(2)
    op_dict = finixio_campaigns_sub_projects_data()

    for key in op_dict.keys():
        print(key)
        sleep(3)
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{key}')]")))
        sleep(4)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(2)
        element.click()
        sleep(4)
        driver.find_element(By.XPATH, reports_option_xpath).click()
        sleep(2)
        driver.find_element(By.XPATH, stats_xpath).click()
        sleep(2)
        WebDriverMethodClass_instance.webdriver_wait_by_xpath(advanced_search).click()
        sleep(2)
        dates = DateGenerator.fetch_date_range(date_range)
        WebDriverMethodClass_instance.webdriver_wait_by_xpath(date_field_one).send_keys(str(dates[0]))
        sleep(1)
        WebDriverMethodClass_instance.webdriver_wait_by_xpath(date_field_two).send_keys(str(dates[1]))
        sleep(1)
        WebDriverMethodClass_instance.webdriver_wait_by_xpath(search_button).click()
        sleep(2)
        WebDriverMethodClass_instance.webdriver_wait_by_xpath(csv_btn).click()
        sleep(4)
        print("Reports file downloaded successfully")

        # data handling start
        drive_api_instance = GDAPI()
        sheet_text = "sheet2"
        data_handling_instance = DataHandling(dest_file_name, sheet_text)
        source_top_csv_file_path = data_handling_instance.get_top_csv_path_from_folder(download_directory)
        _name = op_dict[key].split('\n')[0]
        new_name = _name + '.csv'
        client_name = _name
        source_file_data = data_handling_instance.source_file_data(source_top_csv_file_path)
        destination_file_data = data_handling_instance.dest_file_get_data()
        text_column = "Client Name"
        start_date = str(dates[0])
        date_column_text = "Start Date"
        data_handling_instance.append_to_google_sheets_with_extra_column(source_file_data, destination_file_data, text_column, start_date, date_column_text, client_name)
        # _name = op_dict[key].split('\n')[0]
        # new_name = _name + '.csv'
        destination_folder = r'D:\DownloadCsvHistory'
        FileHandler.complete_data_handler(source_top_csv_file_path, new_name, destination_folder, company_name)
        print(f" File {new_name} moved to history folder successfully..")
        # data handling end

        driver.execute_script("window.history.go(-4)")
        sleep(2)

    for i in range(1, 2):
        val = i+1
        link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, f'{val}')))
        sleep(2)
        driver.execute_script("arguments[0].scrollIntoView();", link)
        sleep(2)
        # Click on the link
        link.click()
        sleep(2)

        op_dict = finixio_campaigns_sub_projects_data()
        for key in op_dict.keys():
            print(key)
            sleep(3)
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{key}')]")))
            sleep(4)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            sleep(2)
            element.click()
            sleep(4)
            driver.find_element(By.XPATH, reports_option_xpath).click()
            sleep(2)
            driver.find_element(By.XPATH, stats_xpath).click()
            sleep(2)
            WebDriverMethodClass_instance.webdriver_wait_by_xpath(advanced_search).click()
            sleep(2)
            dates = DateGenerator.fetch_date_range(date_range)
            WebDriverMethodClass_instance.webdriver_wait_by_xpath(date_field_one).send_keys(str(dates[0]))
            sleep(1)
            WebDriverMethodClass_instance.webdriver_wait_by_xpath(date_field_two).send_keys(str(dates[1]))
            sleep(1)
            WebDriverMethodClass_instance.webdriver_wait_by_xpath(search_button).click()
            sleep(2)
            WebDriverMethodClass_instance.webdriver_wait_by_xpath(csv_btn).click()
            sleep(4)
            print("Reports file downloaded successfully")
            driver.execute_script("window.history.go(-4)")
            sleep(2)


selenium_finixio_campaigns_task()

