from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PYTEST.tests.Accounting.login_accounting_test import test_login_to_ims
import time  # Needed for short sleep

class MainPage:
    def __init__(self, driver):
        # Reuse the driver from login_to_ims
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

        self.accounting_module = (By.XPATH, "//span[normalize-space(text())='Accounting Module']") 
        self.masters = (By.XPATH, "//span[normalize-space(text())='Masters']")
        self.chart_accounts = (By.LINK_TEXT, "Chart Of Accounts")
        self.group_ledger = (By.LINK_TEXT, "Ledger Group Master")
        self.add_btn = (By.XPATH, "//button[@id='addLedgerDropdown']")
        self.new_ledger = (By.XPATH, "//label[normalize-space(text())='Add New Ledger']")
        self.account_dropdown = (By.XPATH, "//select[@id='accountType']")
        self.parent_dropdown = (By.XPATH, "//button[normalize-space(text())='Select Parent Group']")
        self.parent_select = (By.XPATH, "//li[normalize-space(text())='FIXED ASSETS']")
        self.account_select = (By.XPATH, "//input[@id='accountName']")
        self.sub_ledger = (By.XPATH, "//input[@type='checkbox' and @formcontrolname='HasSubLedger']")
        self.save_btn = (By.XPATH, "//button[@id='save']")

    def open_accounting_module(self):
        # Click Accounting Module
        account = self.wait.until(
            EC.element_to_be_clickable(self.accounting_module)
        )
        account.click()
        print("Navigated to Accounting Module.")

        # Handle new tab
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("Switched to Accounting Module tab.")

    def open_ledger_group_master(self):
        # Hover over or click Masters menu to render submenu
        masters = self.wait.until(
            EC.element_to_be_clickable(self.masters)
        )
        ActionChains(self.driver).move_to_element(masters).click().perform()
        print("Hovered and clicked on Masters menu.")

        # Hover over Chart Of Accounts to ensure submenu expands
        chart_of_accounts = self.wait.until(
            EC.presence_of_element_located(self.chart_accounts)
        )
        ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
        print("Hovered over Chart Of Accounts.")

        # Wait until Ledger Group Master link appears inside submenu
        ledger_group = self.wait.until(
            EC.element_to_be_clickable(self.group_ledger)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
        time.sleep(2)  # give some time for the submenu to appear
        self.driver.execute_script("arguments[0].click();", ledger_group)
        print("Ledger Group Master opened.")

        # Close sidebar if existsgit 
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='sidebar-close']"))
            )
            close_btn.click()
            print("Sidebar closed.")
        except:
            print("Sidebar close button not found.")
        click_whitespace = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//th[contains(@class,'mat-column-action') and @role='columnheader']"))
        )
        click_whitespace.click()

    def add_new_ledger(self, account_name: str):
        # Click Add New
        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.add_btn)
        )
        add_btn.click()
        print("Clicked Add New button.")

        # Click 'Add New Ledger Group'
        new_ledger = self.wait.until(
            EC.element_to_be_clickable(self.new_ledger)
        )
        new_ledger.click()
        print("Add New Ledger clicked.")

        account_type_dropdown = self.wait.until(
            EC.element_to_be_clickable(self.account_dropdown)
        )
        account_type_dropdown.click()

        account_type_dropdown.click()
        option = self.wait.until( 
            EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='ASSETS']"))
            )
        option.click()

        parent_group_dropdown = self.wait.until(
            EC.element_to_be_clickable(self.parent_dropdown)
        )
        parent_group_dropdown.click()

        parent_group_select = self.wait.until(
            EC.element_to_be_clickable(self.parent_select)
        )
        ActionChains(self.driver).double_click(parent_group_select).perform()
        print("Selected Parent Group: Automation Testing")

        acc_name_select = self.wait.until(
            EC.element_to_be_clickable(self.account_select)
        )
        acc_name_select.clear()
        acc_name_select.send_keys(account_name)
        print(f"Entered Account Name: {account_name}")

        # sub_ledger_checkbox = self.wait.until(
        #     EC.element_to_be_clickable(self.sub_ledger)
        # )
        # sub_ledger_checkbox.click()
        # print("Checked Sub Ledger checkbox.")

        save_btn = self.wait.until(
            EC.element_to_be_clickable(self.save_btn)
        )
        save_btn.click()
        print("Clicked Save button.")
