import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from modules.webdriver_setup import create_driver
from modules.account_generator import (
    generate_random_username, 
    generate_random_password, 
    generate_random_first_name, 
    generate_random_last_name, 
    generate_random_birth_date
)
from modules.discord_notifier import send_discord_message
from capsolver import capsolver
from config import CAPSOLVER_API_KEY, WEBHOOK_URL

if CAPSOLVER_API_KEY:
    capsolver.api_key = CAPSOLVER_API_KEY

def solve_captcha(driver):
    if not CAPSOLVER_API_KEY:
        print("CAPSolver API key not provided. Manual CAPTCHA solving required.")
        return False

    try:
        captcha_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'g-recaptcha'))
        )
        site_key = captcha_element.get_attribute('data-sitekey')
        solution = capsolver.solve({
            "type": "ReCaptchaV2TaskProxyLess",
            "websiteURL": driver.current_url,
            "websiteKey": site_key
        })
        driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{solution['solution']['gRecaptchaResponse']}';")
        driver.execute_script('document.querySelector("[data-sitekey]").parentElement.submit();')
        return True
    except Exception as e:
        print(f"CAPSolver failed: {e}")
        return False

def create_outlook_account(driver, username, password, first_name, last_name, birth_date):
    try:
        driver.get('https://signup.live.com/')
        time.sleep(2)
        
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'MemberName'))
        )
        email_field.send_keys(username + "@outlook.com")
        email_field.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'Password'))
        )
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        first_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'FirstName'))
        )
        first_name_field.send_keys(first_name)
        
        time.sleep(1)
        
        last_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'LastName'))
        )
        last_name_field.send_keys(last_name)
        last_name_field.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        birth_month, birth_day, birth_year = birth_date.split('/')
        birth_month = str(int(birth_month))
        birth_day = str(int(birth_day))
        birth_month_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'BirthMonth'))
        )
        Select(birth_month_field).select_by_value(birth_month)
        time.sleep(1)
        birth_day_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'BirthDay'))
        )
        Select(birth_day_field).select_by_value(birth_day)
        time.sleep(1)
        birth_year_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'BirthYear'))
        )
        birth_year_field.send_keys(birth_year)
        birth_year_field.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        captcha_solved = solve_captcha(driver)
        if not captcha_solved:
            print("Manual CAPTCHA solving required. Please solve the CAPTCHA in your browser and then press Enter to continue...")
            input("Press Enter to continue after solving the CAPTCHA...")
        
        submit_button = WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((By.ID, 'id__0'))
        )
        submit_button.click()
        
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error during account creation: {e}")
        driver.save_screenshot('account_creation_error.png')
        return False

if __name__ == "__main__":
    try:
        num_accounts = int(input("How many accounts would you like to create? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)
    
    accounts = []
    
    for i in range(num_accounts):
        print(f"Creating account {i + 1} of {num_accounts}...")
        driver = create_driver()
        
        try:
            username = generate_random_username()
            password = generate_random_password()
            first_name = generate_random_first_name()
            last_name = generate_random_last_name()
            birth_date = generate_random_birth_date()
            
            account_created = create_outlook_account(driver, username, password, first_name, last_name, birth_date)
            if account_created:
                account_details = {
                    "name": f"{first_name} {last_name}",
                    "birth": birth_date,
                    "email": f"{username}@outlook.com",
                    "password": password
                }
                accounts.append(account_details)
                send_discord_message(
                    f"name:\n {account_details['name']}\n"
                    f"birth:\n {account_details['birth']}\n"
                    f"email:\n {account_details['email']}\n"
                    f"password:\n {account_details['password']}\n\n"
                )
                print(f"Account created: {username}@outlook.com with password: {password}")
            else:
                print("Account creation failed. Please close the script and try again.")
                break
        finally:
            driver.quit()
    
    if accounts:
        current_directory = os.getcwd()
        folder_path = os.path.join(current_directory, 'Outlook-Gen-Captcha')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        txt_file_path = os.path.join(folder_path, 'created_accounts.txt')
        with open(txt_file_path, mode='a', newline='') as file:
            for account in accounts:
                file.write(f"name:\n {account['name']}\n")
                file.write(f"birth:\n {account['birth']}\n")
                file.write(f"email:\n {account['email']}\n")
                file.write(f"password:\n {account['password']}\n\n")
