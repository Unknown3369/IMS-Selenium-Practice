from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from login_details import login_to_ims
import time  # Needed for short sleep


class MainPage:
    def __init__(self, driver):
        # Reuse the driver from login_to_ims
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_accounting_module(self):
        # Click Accounting Module
        account = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Accounting Module']"))
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
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Masters']"))
        )
        ActionChains(self.driver).move_to_element(masters).click().perform()
        print("Hovered and clicked on Masters menu.")

        # Hover over Chart Of Accounts to ensure submenu expands
        chart_of_accounts = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Chart Of Accounts"))
        )
        ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
        print("Hovered over Chart Of Accounts.")

        # Wait until Ledger Group Master link appears inside submenu
        ledger_group = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Ledger Group Master"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
        time.sleep(2)  # give some time for the submenu to appear
        driver.execute_script("arguments[0].click();", ledger_group)
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

    def add_new_ledger(self):
        # Click Add New
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='addLedgerDropdown']"))
        )
        add_btn.click()
        print("Clicked Add New button.")

        # Click 'Add New Ledger Group'
        new_ledger = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Add New Ledger']"))
        )
        new_ledger.click()
        print("Add New Ledger clicked.")

        account_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='accountType']"))
        )
        account_type_dropdown.click()

        Select(account_type_dropdown).select_by_visible_text("ASSETS")
        print("Selected Account Type: ASSETS")

        parent_group_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Select Parent Group']"))
        )
        parent_group_dropdown.click()

        parent_group_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[normalize-space(text())='Automation Testing']"))
        )
        ActionChains(self.driver).double_click(parent_group_select).perform()
        print("Selected Parent Group: Automation Testing")

        acc_name_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='accountName']"))
        )
        acc_name_select.send_keys("Automation Ledger")
        print("Entered Account Name: Automation Ledger")

        save_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save']"))
        )
        save_btn.click()
        print("Clicked Save button.")

        time.sleep(5)

if __name__ == "__main__":
    driver = login_to_ims()
    main = MainPage(driver)
    main.open_accounting_module()
    main.open_ledger_group_master()
    main.add_new_ledger()
