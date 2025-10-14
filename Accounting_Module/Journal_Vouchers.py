from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from login_details import login_to_ims
from selenium.webdriver.common.keys import Keys
import time
import keyboard

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
    
    def open_journal_voucher(self):
        masters = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Transactions']"))
        )
        ActionChains(self.driver).move_to_element(masters).click().perform()
        print("Hovered and clicked on Transactions menu.")

        chart_of_accounts = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Voucher Entries"))
        )
        ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
        print("Hovered over Voucher Entries.")

        ledger_group = self.wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Journal Voucher"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
        time.sleep(2)  
        self.driver.execute_script("arguments[0].click();", ledger_group)
        print("Journal Voucher opened.")
        time.sleep(5)

    def add_voucher(self, reference_number: str, enter_remarks: str, debit_amount: int, credit_amount: int):
        refno = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='refno']"))
        )
        refno.clear()
        refno.send_keys(reference_number)
        print(f"Entered Reference Number: {reference_number}")

        remarks = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='REMARKS']"))
        )
        remarks.clear()
        remarks.send_keys(enter_remarks)
        print(f"Entered Remarks: {enter_remarks}")

        select_account = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='ACCODEInput_0']"))
        )
        select_account.send_keys(Keys.ENTER)

        selected_account = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='TheTestCustom']"))
        )
        selected_account_click = ActionChains(self.driver).double_click(selected_account)
        selected_account_click.perform()

        dr_amount = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='DrAmtInput_0']"))
        )
        dr_amount.clear()
        dr_amount.send_keys(debit_amount)
        print(f"Entered Debit Amount: {debit_amount}")

        narration = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='narration_0']"))
        )
        narration.send_keys(Keys.ENTER)
        print("Entered Next Line")

        select_account_n = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='ACCODEInput_1']"))
        )
        select_account_n.send_keys(Keys.ENTER)

        # Always locate the element right before performing the action
        ActionChains(self.driver).double_click(
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='TheTestCustom']")))
        ).perform()


        cr_amount = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='CrAmtInput_1']"))
        )
        cr_amount.clear()
        cr_amount.send_keys(credit_amount)
        print(f"Entered Debit Amount: {credit_amount}")

        save_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'F6 SAVE')]"))
        )
        save_button.click()
        print("Clicked on Save button.")

        no_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='nobtn' and contains(@class, 'btn-warning') and normalize-space(text())='No']"))
        )
        no_btn.click()
        print("Clicked 'No' on the confirmation dialog.")


if __name__ == "__main__":
    driver = login_to_ims()
    journal_voucher = MainPage(driver)
    journal_voucher.open_accounting_module()
    journal_voucher.open_journal_voucher()
    time.sleep(15)
    driver.quit()