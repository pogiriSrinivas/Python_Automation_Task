from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
from datetime import datetime, timedelta


class ChromeOptions:
    driver = None

    def __init__(self, download_directory, chromedriver_path):
        self.webdriver = webdriver
        self.chrome_options = webdriver.ChromeOptions()
        self.download_directory = download_directory
        self.chromedriver_path = chromedriver_path
        self.chrome_options.add_experimental_option("prefs", {
                "download.default_directory": self.download_directory,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
         })

    # driver = webdriver.Chrome(service=Service(executable_path=self.chromedriver_path),options=self.chrome_options)


class WebDriverMethodClass:

    def __init__(self, driver, download_directory, chromedriver_path):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        self.download_directory = download_directory
        self.chromedriver_path = chromedriver_path
        self.ChromeOptions_instance = ChromeOptions(self.download_directory, self.chromedriver_path)

    def web_driver_method_css_selector(self, placeholder_value):
        css_selector = f"input[placeholder='{placeholder_value}']"
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def driver_find_element_method_css_selector(self, placeholder_value):
        css_selector = f"input[placeholder='{placeholder_value}']"
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def driver_find_element_method_by_class_name(self, placeholder_value):
        css_selector = f"input[placeholder='{placeholder_value}']"
        return self.driver.find_element(By.CLASS_NAME, css_selector)

    def driver_find_element_method_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def driver_find_element_method_by_id(self, placeholder_value):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, placeholder_value)))

    def webdriver_wait_by_xpath(self, placeholder_value):
        return WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, placeholder_value)))

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_element_by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def find_elements_by_tag_name(self, tag_name):
        return self.driver.find_elements_by_tag_name(tag_name)


class LoginUser(WebDriverMethodClass):

    def __init__(self, url, username, password, driver, download_directory, chromedriver_path,
                 username_placeholder, password_placeholder, btn_placeholder):
        super().__init__(driver, download_directory, chromedriver_path)
        self.url = url
        self.webdriver = webdriver
        self.username = username
        self.password = password
        self.driver = driver
        self.username_placeholder = username_placeholder
        self.password_placeholder = password_placeholder
        self.btn_placeholder = btn_placeholder

    def login_user(self):
        username_filed = self.web_driver_method_css_selector(self.username_placeholder)
        password_field = self.driver_find_element_method_css_selector(self.password_placeholder)
        username_filed.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button = self.driver_find_element_method_by_xpath(self.btn_placeholder)
        login_button.click()


class GDAPI:
    def __init__(self):
        # use creds to create a client to interact with the Google Drive API
        self.scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.readonly']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('Credentials_Final.json', self.scope)
        self.client = gspread.authorize(self.creds)


class DataHandling(GDAPI):

    def __init__(self, dest_sheet_name):
        super().__init__()  # Initialize the parent class to set up the client
        self.dest_sheet_name = dest_sheet_name
        self.sheet = self.client.open(self.dest_sheet_name).sheet1  # Access the Google Sheets client from the parent class

    def dest_file_get_data(self):
        # Here you can use self.sheet to interact with the Google Sheets API
        # For example, read data from the sheet:
        data = self.sheet.get_all_records()
        return data

    def get_top_csv_path_from_folder(self, folder_path):
        # Get the top CSV file path from the specified folder
        all_files = os.listdir(folder_path)
        csv_files = [file for file in all_files if file.endswith('.csv')]
        sorted_csv_files = sorted(csv_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
        if sorted_csv_files:
            top_csv_file_path = os.path.join(folder_path, sorted_csv_files[0])
            return top_csv_file_path
        else:
            return None

    def source_file_data(self, source_csv_file_path):
        # Read data from the CSV file and return it as a list of lists
        source_file_data = []
        with open(source_csv_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                source_file_data.append(row)
        return source_file_data

    def write_data_to_dest_file(self, destination_file_data, source_file_data):
        combined_data = None

        # Check if destination_file_data is not empty
        if destination_file_data and len(destination_file_data) > 0:
            # If existing data is not empty and contains headers, remove the first row
            if all(cell == '' for cell in destination_file_data[0]):
                combined_data = source_file_data
            elif all(cell != '' for cell in destination_file_data[0]):
                if len(source_file_data) > 0:
                    source_file_data.pop(0)
                    combined_data = source_file_data

                else:
                    print("can not add the empty file to destination folder")

        else:
            # If destination_file_data is empty, use source_file_data directly
            combined_data = source_file_data

        if len(source_file_data) > 0:
            # Append the combined data to the Google Sheets document
            self.sheet.append_rows(combined_data)

        else:
            print("Source file is empty")


class DateGenerator:
    @staticmethod
    def fetch_date_range(date_range):
        # Get today's date
        today = datetime.today()

        if date_range == "last monday to sunday":
            # Find the previous week's Monday
            previous_monday = today - timedelta(days=today.weekday() + 7)

            # Find the previous week's Sunday
            previous_sunday = previous_monday + timedelta(days=6)

            # Get only the date part without the timestamp
            previous_monday = previous_monday.date()
            previous_sunday = previous_sunday.date()

            return [previous_monday, previous_sunday]
        else:
            raise ValueError("Invalid date range. Supported options: 'last monday to sunday'")












