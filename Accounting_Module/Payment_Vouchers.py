from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from login_details import login_to_ims
from selenium.webdriver.support.ui import Select
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

    def open_payment_voucher(self):
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
                (By.LINK_TEXT, "Payment Voucher"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
        time.sleep(2)  
        self.driver.execute_script("arguments[0].click();", ledger_group)
        print("Payment Voucher opened.")
        time.sleep(5)

    def add_voucher_details(self, reference_number: str, enter_remarks: str, payee: str, enter_amount: int, cheque_number: str, cheque_date: str):
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

        pay_to = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='BILLTO']"))
        )
        pay_to.clear()
        pay_to.send_keys(payee)
        print(f"Entered Payee: {payee}")

        voucher_type = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='TRNMODE']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", voucher_type)

        try:
            voucher_type.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", voucher_type)
            print("Selected Voucher Type: Party Payment")

        cash_bank = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='TRNAC']"))
        )
        cash_bank.send_keys(Keys.ENTER)

        select_cash_bank = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='PETTY CASH A/C']"))
        )
        select_cash_bank_click = ActionChains(self.driver).double_click(select_cash_bank)
        select_cash_bank_click.perform()
        print("Selected Cash/Bank Account: PETTY CASH A/C")

        account_select = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='press ENTER to select']"))
        )
        account_select.send_keys(Keys.ENTER)

        select_account = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title='Milk Chocolate Vendor']"))
        )
        select_account_click = ActionChains(self.driver).double_click(select_account)
        select_account_click.perform()
        print("Selected Account: Milk Chocolate Vendor")

        ammount = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='DrAmtInput_0']"))
        )
        ammount.clear()
        ammount.send_keys(enter_amount)
        print(f"Entered Amount: {enter_amount}")

        narration = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='narration_0']"))
        )
        narration.click()
        narration.send_keys("Payment Voucher Automation Test")
        print("Entered Narration.")

        pay_mode = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='transactionType_0']"))
        )
        pay_mode = Select(pay_mode)
        pay_mode.select_by_visible_text("Cheque")
        print("Selected Payment Mode: Cheque")

        cheque_no = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='ChequeNo_0']"))
        )
        cheque_no.send_keys(cheque_number)
        print(f"Entered Cheque Number: {cheque_number}")

        date_field = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='ChequeDate_0']"))
        )
        date_field.send_keys(cheque_date)
        print(f"Entered Cheque Date: {cheque_date}")

        try: 
            error_handler = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[@aria-hidden='true' and text()='×']]"))
            )
            error_handler.click()
            print("Handled unexpected popup.")
        except Exception:
            print("No unexpected popup appeared.")

        action_shift = ActionChains(self.driver)
        action_shift.key_down(Keys.SHIFT).pause(0.5).key_up(Keys.SHIFT).perform()

        save_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'F6 SAVE')]"))
        )
        save_button.click()
        print("Clicked on SAVE button.")

        no_popup = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='nobtn' and normalize-space(text())='No']"))
        )
        no_popup.click()
        print("Handled popup.")



if __name__ == "__main__":
    driver = login_to_ims()
    payment_voucher = MainPage(driver)
    payment_voucher.open_accounting_module()
    payment_voucher.open_payment_voucher()
    time.sleep(5)
    driver.quit()