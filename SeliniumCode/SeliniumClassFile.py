import logging

from gspread import client
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
from datetime import datetime, timedelta
import shutil
from Country_Names import county_names

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
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, placeholder_value)))

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

    def __init__(self, dest_sheet_name, sheet_text):
        super().__init__()  # Initialize the parent class to set up the client
        self.dest_sheet_name = dest_sheet_name
        self.sheet_text = sheet_text
        self.sheet = self.client.open(self.dest_sheet_name).worksheet(self.sheet_text)  # Access the Google Sheets client from the parent class

    def dest_file_get_data(self):
        # Here you can use self.sheet to interact with the Google Sheets API
        # For example, read data from the sheet:
        data = self.sheet.get_all_records()
        return data

    @staticmethod
    def get_top_csv_path_from_folder(folder_path):
        # Get the top CSV file path from the specified folder
        all_files = os.listdir(folder_path)
        print(f"All files {all_files}")
        csv_files = [file for file in all_files if file.endswith('.csv')]
        print(f" csv file{csv_files}")
        sorted_csv_files = sorted(csv_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
        print(f"sorted csv file{sorted_csv_files}")
        if sorted_csv_files:
            top_csv_file_path = os.path.join(folder_path, sorted_csv_files[0])
            return top_csv_file_path
        else:
            return None

    def source_file_data(self, source_csv_file_path):
        # Check if source_csv_file_path is None
        if source_csv_file_path is None:
            return None  # Return None or handle the case appropriately

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
                if source_file_data and len(source_file_data) > 0:
                    source_file_data.pop(0)
                    combined_data = source_file_data

                else:
                    print("can not add the empty file to destination folder")

        else:
            # If destination_file_data is empty, use source_file_data directly
            combined_data = source_file_data
            print(f"Combined data : {combined_data} ")

        if source_file_data and len(source_file_data) > 0:
            # Append the combined data to the Google Sheets document
            self.sheet.append_rows(combined_data)

        else:
            print("Source file is empty")

        print(combined_data)

    def append_to_google_sheets_with_extra_column(self, source_file_data, destination_file_data,
                                                  text_column, start_date, date_column_text, client_name):
        combined_data = None
        # Check if destination_file_data is not empty
        if destination_file_data and len(destination_file_data) > 0:
            # If existing data is not empty and contains headers, remove the first row
            if all(cell == '' for cell in destination_file_data[0]):
                combined_data = source_file_data
                if combined_data:
                    print("Special 1")
                    print(combined_data)
                    for row in combined_data:
                        row.append(client_name)

            elif all(cell != '' for cell in destination_file_data[0]):
                if len(source_file_data) > 0:
                    source_file_data.pop(0)
                    combined_data = source_file_data
                    if combined_data:
                        print("Special 2")
                        for row in combined_data:
                            row.append(client_name)
                            row.append(start_date)

                    print(f"Combined data : {combined_data} ")

                else:
                    print("can not add the empty file to destination folder")

        else:
            # If destination_file_data is empty, use source_file_data directly
            combined_data = source_file_data
            if combined_data:
                print("Special 3")
                for i in range(len(combined_data)):
                    if i == 0:
                        combined_data[i].append(text_column)
                        combined_data[i].append(date_column_text)

                    if i > 0:
                        combined_data[i].append(client_name)
                        combined_data[i].append(start_date)

            print(f"Combined data : {combined_data} ")

        if len(source_file_data) > 0:
            # Append the combined data to the Google Sheets document
            self.sheet.append_rows(combined_data)

        else:
            print("Source file is empty")

        print(combined_data)

    def append_to_google_sheets_with_extra_column_ki(self, destination_file_data, source_file_data):
        combined_data = None
        extra_column_list = ["Week No", "Downloaded Report Name", "Presales", "Country Name"]
        # Check if destination_file_data is not empty
        if destination_file_data and len(destination_file_data) > 0:
            # If existing data is not empty and contains headers, remove the first row
            if all(cell == '' for cell in destination_file_data[0]):
                combined_data = source_file_data
                if combined_data:
                    print("Special 1")
                    print(combined_data)

            elif all(cell != '' for cell in destination_file_data[0]):
                if len(source_file_data) > 0:
                    source_file_data.pop(0)
                    combined_data = source_file_data
                    if combined_data:
                        print("Special 2")
                        for i in range(len(combined_data)):
                            formatted_week = None
                            Extract_Download_report_name = None
                            presale_value = None
                            country_name = None
                            non_csvfile_column_values = [formatted_week, Extract_Download_report_name, presale_value, country_name]

                            # week number:
                            date_obj = datetime.strptime(combined_data[i][0], "%Y-%m-%d")
                            week_number = date_obj.strftime("%W")
                            non_csvfile_column_values[0] = f"Week {int(week_number) + 1}"
                            # Extract Download report name:
                            last_underscore_index = combined_data[i][1].rfind('_')
                            non_csvfile_column_values[1] = combined_data[i][1][last_underscore_index + 1:]
                            # Extract Presales value:
                            first_underscore_index = combined_data[i][1].find('_')
                            non_csvfile_column_values[2] = combined_data[i][1][:first_underscore_index]
                            # Extract Country name:
                            if combined_data[i][2] in county_names:
                                non_csvfile_column_values[3] = county_names[combined_data[i][2]]
                            print(non_csvfile_column_values)
                            for j in range(len(non_csvfile_column_values)):
                                combined_data[i].insert(j, non_csvfile_column_values[j])

                    print(f"Combined data : {combined_data} ")

                else:
                    print("can not add the empty file to destination folder")

        else:
            # If destination_file_data is empty, use source_file_data directly
            combined_data = source_file_data
            if combined_data:
                print("Special 3")
                for i in range(len(combined_data)):
                    if i == 0:
                        for j in range(len(extra_column_list)):
                            combined_data[i].insert(j, extra_column_list[j])

                    if i > 0:
                        formatted_week = None
                        Extract_Download_report_name = None
                        presale_value = None
                        country_name = None
                        non_csvfile_column_values = [formatted_week, Extract_Download_report_name, presale_value,
                                                     country_name]
                        # week number:
                        date_obj = datetime.strptime(combined_data[i][0], "%Y-%m-%d")
                        week_number = date_obj.strftime("%W")
                        non_csvfile_column_values[0] = f"Week {int(week_number) + 1}"
                        # Extract Download report name:
                        last_underscore_index = combined_data[i][1].rfind('_')
                        non_csvfile_column_values[1] = combined_data[i][1][last_underscore_index + 1:]
                        # Extract Presales value:
                        first_underscore_index = combined_data[i][1].find('_')
                        non_csvfile_column_values[2] = combined_data[i][1][:first_underscore_index]
                        # Extract Country name:
                        if combined_data[i][2] in county_names:
                            non_csvfile_column_values[3] = county_names[combined_data[i][2]]
                        print(non_csvfile_column_values)
                        for j in range(len(non_csvfile_column_values)):
                            k = j
                            combined_data[i].insert(k, non_csvfile_column_values[j])
            print(f"Combined data : {combined_data} ")

        if len(source_file_data) > 0:
            # Append the combined data to the Google Sheets document
            self.sheet.append_rows(combined_data)

        else:
            print("Source file is empty")

        print(combined_data)

    def append_to_google_sheets_with_extra_column_finixio(self, destination_file_data, source_file_data):
        combined_data = None
        extra_column_list = ['Week No',	'Account Name', 'Country Name']
        # Check if destination_file_data is not empty
        if destination_file_data and len(destination_file_data) > 0:
            # If existing data is not empty and contains headers, remove the first row
            if all(cell == '' for cell in destination_file_data[0]):
                combined_data = source_file_data
                if combined_data:
                    print("Special 1")
                    print(combined_data)

            elif all(cell != '' for cell in destination_file_data[0]):
                if len(source_file_data) > 0:
                    source_file_data.pop(0)
                    combined_data = source_file_data
                    if combined_data:
                        print("Special 2")
                        for i in range(len(combined_data)):
                            formatted_week = None
                            Account_Name = None
                            country_name = None
                            non_csvfile_column_values = [formatted_week, Account_Name, country_name]

                            # week number:
                            date_obj = datetime.strptime(combined_data[i][0], "%Y-%m-%d")
                            week_number = date_obj.strftime("%W")
                            non_csvfile_column_values[0] = f"Week {int(week_number) + 1}"
                            # Extract Download report name:
                            last_underscore_index = combined_data[i][1].rfind('_')
                            non_csvfile_column_values[1] = combined_data[i][1][last_underscore_index + 1:]
                            # Extract Country name:
                            if combined_data[i][2] in county_names:
                                non_csvfile_column_values[2] = county_names[combined_data[i][2]]
                            print(non_csvfile_column_values)
                            for j in range(len(non_csvfile_column_values)):
                                combined_data[i].insert(j, non_csvfile_column_values[j])

                    print(f"Combined data : {combined_data} ")

                else:
                    print("can not add the empty file to destination folder")

        else:
            # If destination_file_data is empty, use source_file_data directly
            combined_data = source_file_data
            if combined_data:
                print("Special 3")
                for i in range(len(combined_data)):
                    if i == 0:
                        for j in range(len(extra_column_list)):
                            combined_data[i].insert(j, extra_column_list[j])

                    if i > 0:
                        formatted_week = None
                        Account_Name = None
                        country_name = None
                        non_csvfile_column_values = [formatted_week, Account_Name, country_name]
                        # week number:
                        date_obj = datetime.strptime(combined_data[i][0], "%Y-%m-%d")
                        week_number = date_obj.strftime("%W")
                        non_csvfile_column_values[0] = f"Week {int(week_number) + 1}"
                        # Account Name:
                        first_underscore_index = combined_data[i][1].find('_')
                        substring_after_first_underscore = combined_data[i][1][first_underscore_index + 1:]
                        next_underscore_index = substring_after_first_underscore.find('_')
                        non_csvfile_column_values[1] = substring_after_first_underscore[:next_underscore_index]
                        # Extract Country name:
                        if combined_data[i][2] in county_names:
                            non_csvfile_column_values[2] = county_names[combined_data[i][2]]
                        print(non_csvfile_column_values)
                        for j in range(len(non_csvfile_column_values)):
                            k = j
                            combined_data[i].insert(k, non_csvfile_column_values[j])
            print(f"Combined data : {combined_data} ")

        if len(source_file_data) > 0:
            # Append the combined data to the Google Sheets document
            self.sheet.append_rows(combined_data)

        else:
            print("Source file is empty")

        print(combined_data)

class DateGenerator:
    # def fetch_date_range(date_range):
    #     # Get today's date
    #     today = datetime.today()
    #
    #     if date_range == "last monday to sunday":
    #         # Find the previous week's Monday
    #         previous_monday = today - timedelta(days=today.weekday() + 7)
    #
    #         # Find the previous week's Sunday
    #         previous_sunday = previous_monday + timedelta(days=6)
    #
    #         # Get only the date part without the timestamp
    #         previous_monday = previous_monday.date()
    #         previous_sunday = previous_sunday.date()
    #
    #         return [previous_monday, previous_sunday]
    #     else:
    #         raise ValueError("Invalid date range. Supported options: 'last monday to sunday'")

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

        elif date_range == "last thursday to sunday":
            # Find the previous week's Thursday
            previous_thursday = today - timedelta(days=(today.weekday() + 3 + 7) % 7)

            # Find the previous week's Sunday
            previous_sunday = previous_thursday + timedelta(days=(6 - (previous_thursday.weekday() + 7) % 7))

            # Get only the date part without the timestamp
            previous_thursday = previous_thursday.date()
            previous_sunday = previous_sunday.date()

            return [previous_thursday, previous_sunday]

        elif date_range == "last monday to wednesday":
            # Find the previous week's Monday
            previous_monday = today - timedelta(days=today.weekday() + 7)

            # Find the previous week's Wednesday
            previous_wednesday = previous_monday + timedelta(days=2)

            # Get only the date part without the timestamp
            previous_monday = previous_monday.date()
            previous_wednesday = previous_wednesday.date()

            return [previous_monday, previous_wednesday]

        else:
            raise ValueError(
                "Invalid date range. Supported options: 'last monday to sunday', 'last thursday to sunday', 'last monday to wednesday'")


class FileRenamer:
    def __init__(self, file_path):
        self.file_path = file_path

    def rename(self, new_name):
        # Get the directory path and current file name
        dir_path, file_name = os.path.split(self.file_path)

        # Construct the new file path with the new name
        new_file_path = os.path.join(dir_path, new_name)

        # Rename the file
        os.rename(self.file_path, new_file_path)

        return new_file_path


class FileManager:
    def __init__(self, destination_folder):
        self.destination_folder = destination_folder

    def move_file(self, source_file_path):
        # Get the filename from the full file path
        file_name = os.path.basename(source_file_path)

        # Move the file to the destination folder
        destination_file_path = os.path.join(self.destination_folder, file_name)
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)  # Create destination folder if it doesn't exist

        shutil.move(source_file_path, destination_file_path)
        print(f"{file_name} moved successfully to {self.destination_folder}")

    @staticmethod
    def create_folder_with_today_date(folder_path):
        # Get today's date
        today_date = datetime.today().strftime('%Y-%m-%d')

        # Create folder with today's date
        folder_path_with_date = os.path.join(folder_path, today_date)
        if not os.path.exists(folder_path_with_date):
            os.makedirs(folder_path_with_date)
            print(f"Folder '{today_date}' created successfully at '{folder_path_with_date}'")
        else:
            print(f"Folder '{today_date}' already exists at '{folder_path_with_date}'")

    @staticmethod
    def create_folder_with_date_and_string(self, client_name):
        # Get today's date
        today_date = datetime.today().strftime('%Y-%m-%d')

        # Create folder with today's date and client name
        folder_name = f"{today_date}_{client_name}"
        folder_path = os.path.join(self.history_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created successfully at '{folder_path}'")
        else:
            print(f"Folder '{folder_name}' already exists at '{folder_path}'")

        return folder_path


class FileHandler:
    @staticmethod
    def complete_data_handler(file_path, new_name, destination_folder, company_name):
        # Check if the destination folder exists, create it if not
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Construct the new file path with the new name
        new_file_path = os.path.join(destination_folder, new_name)
        # Rename the file
        os.rename(file_path, new_file_path)

        # Get the filename from the full file path
        file_name = os.path.basename(new_file_path)

        # Construct the folder name with current date and string name
        today_date = datetime.now().strftime("%Y-%m-%d")
        folder_name = f"{company_name}_{today_date}"

        # Check if the folder exists, create it if not
        folder_path = os.path.join(destination_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file to the folder
        destination_file_path = os.path.join(folder_path, file_name)
        shutil.move(new_file_path, destination_file_path)


class Extractor:
    @staticmethod
    def extract_specific_values_from_list(string_value, list_value):
        output = []
        for i in range(len(list_value)):
            _val = list_value.starswith(string_value)
            output.append(_val)

        return output

    @staticmethod
    def single_table_row_extractor(driver):
        tables = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))
        rows = None
        # Iterate over each table
        for table in tables:
            # Find all rows within the table
            rows = table.find_elements(By.TAG_NAME, "tr")

        return rows

    @staticmethod
    def rows_to_dict(rows):
        _rows = []

        c_ids = []
        c_names = []
        op_dict = {}
        for row in rows:
            _row = row.text.split(" ")
            _rows.append(_row)
        _rows.pop(0)
        for r in _rows:
            if len(r) >= 2:  # Check if the row has at least 2 elements
                c_ids.append(r[0])
                c_names.append(r[1])

        op_dict = dict(zip(c_ids, c_names))
        return op_dict

    @staticmethod
    def add_client_column(csv_file, client_name):
        rows = []
        with open(csv_file, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            try:
                header = next(csvreader)  # Read the header row
            except StopIteration:
                header = []  # If there's no header row, create an empty header
            header.append('Client')  # Add 'Client' to the header
            rows.append(header)  # Append the modified header to rows
            for row in csvreader:
                row.append(client_name)  # Add client name to each row
                rows.append(row)  # Append the modified row to rows
        return rows

