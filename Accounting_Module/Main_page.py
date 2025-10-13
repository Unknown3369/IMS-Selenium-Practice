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
        self.wait = WebDriverWait(self.driver, 25)

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

        # Close sidebar if exists
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='sidebar-close']"))
            )
            close_btn.click()
            print("Sidebar closed.")
        except:
            print("Sidebar close button not found.")

    def add_new_ledger_group(self):
        # Click Add New
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='addLedgerDropdown']"))
        )
        add_btn.click()
        print("Clicked Add New button.")

        # Click 'Add New Ledger Group'
        new_group = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Add New Ledger Group']"))
        )
        new_group.click()
        print("Add New Ledger Group clicked.")

        # Select Account Type
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='accountType']"))
        )
        select = Select(dropdown)
        select.select_by_value("AT")  # ASSETS
        print("Selected 'ASSETS' from Account Type dropdown.")


if __name__ == "__main__":
    driver = login_to_ims()
    main = MainPage(driver)
    main.open_accounting_module()
    main.open_ledger_group_master()
    main.add_new_ledger_group()
