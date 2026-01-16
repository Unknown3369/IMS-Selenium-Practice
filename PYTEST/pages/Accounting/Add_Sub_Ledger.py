from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PYTEST.tests.Accounting.login_accounting_test import test_login_to_ims
import time 

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_accounting_module(self):
        account = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Accounting Module']"))
        )
        account.click()
        print("Navigated to Accounting Module.")

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("Switched to Accounting Module tab.")

    def open_sub_ledger_account_master(self):
        masters = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Masters']"))
        )
        ActionChains(self.driver).move_to_element(masters).click().perform()
        print("Hovered and clicked on Masters menu.")

        chart_of_accounts = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Chart Of Accounts"))
        )
        ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
        print("Hovered over Chart Of Accounts.")

        ledger_group = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Sub Ledger Account Master"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
        time.sleep(2)  
        self.driver.execute_script("arguments[0].click();", ledger_group)
        print("Sub Ledger Account Master opened.")

    def add_new_sub_ledger(self, sub_ledger_name: str, pan_number: str):
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='addLedgerDropdown']"))
        )
        add_btn.click()
        print("Clicked Add New button.")

        add_new_sub_ledger = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Add New Sub Ledger']"))
        )
        add_new_sub_ledger.click()
        print("Selected Add New Sub Ledger option.")

        acc_name_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='SubLedgerName']"))
        )
        acc_name_select.clear()
        acc_name_select.send_keys(sub_ledger_name)
        print(f"Entered Sub Ledger Name: {sub_ledger_name}")

        acc_pan_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='PanNo']"))
        )
        acc_pan_select.clear()
        acc_pan_select.send_keys(pan_number)
        print(f"Entered PAN Number: {pan_number}")

        save_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save']"))
        )
        save_btn.click()
        print("Clicked Save button for Sub Ledger.")
