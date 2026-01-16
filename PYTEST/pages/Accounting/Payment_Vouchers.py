from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PYTEST.tests.Accounting.login_accounting_test import test_login_to_ims
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from datetime import datetime
import time
import keyboard

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,25)
        self.driver.maximize_window()
        self.actions = ActionChains(driver)

        self.accounting_module = (By.XPATH, "//span[normalize-space(text())='Accounting Module']")
        self.transactions = (By.XPATH, "//span[normalize-space(text())='Transactions']")
        self.voucher_entries = (By.LINK_TEXT, "Voucher Entries")
        self.payment_voucher = (By.LINK_TEXT, "Payment Voucher")
        self.refno = (By.XPATH, "//input[@id='refno']")
        self.remarks = (By.XPATH, "//input[@name='REMARKS']")
        self.payee = (By.XPATH, "//input[@name='BILLTO']")
        self.voucher = (By.XPATH, "//select[@name='TRNMODE']")
        self.cash = (By.XPATH, "//input[@name='TRNAC']")
        self.select_cash = (By.XPATH, "//div[@title='PETTY CASH A/C']")
        self.account = (By.XPATH, "//input[@placeholder='press ENTER to select']")
        self.select_account = (By.XPATH, "//div[@title='windows test']")
        self.amount = (By.XPATH, "//input[@id='DrAmtInput_0']")
        self.narration = (By.XPATH, "//input[@id='narration_0']")
        self.pay_mode = (By.XPATH, "//select[@id='transactionType_0']")
        self.cheque_no = (By.XPATH, "//input[@id='ChequeNo_0']")
        self.cheque_date = (By.ID, "chequeDate_0")
        self.save = (By.XPATH, "//button[contains(text(), 'F6 SAVE')]")
        self.no_popup = (By.ID, "ChequePrintNoBtn")

    def open_accounting_module(self):
        account = self.wait.until(
            EC.element_to_be_clickable( self.accounting_module)
        )
        account.click()
        print("Navigated to Accounting Module.")

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("Switched to Accounting Module tab.")

    def open_payment_voucher(self):
        masters = self.wait.until(
            EC.element_to_be_clickable( self.transactions)
        )
        ActionChains(self.driver).move_to_element(masters).click().perform()
        print("Hovered and clicked on Transactions menu.")

        chart_of_accounts = self.wait.until(
            EC.presence_of_element_located(self.voucher_entries)
        )
        ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
        print("Hovered over Voucher Entries.")

        ledger_group = self.wait.until(
            EC.element_to_be_clickable(self.payment_voucher)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
        time.sleep(2)  
        self.driver.execute_script("arguments[0].click();", ledger_group)
        print("Payment Voucher opened.")

        click = self.wait.until(
            EC.presence_of_element_located(((By.XPATH, "//label[normalize-space()='Refno. :']")
        )))
        click.click()

    def add_voucher_details(self, reference_number: str, enter_remarks: str, payee: str, enter_amount: int, cheque_number: str):
        refno = self.wait.until(
            EC.element_to_be_clickable(self.refno)
        )
        refno.clear()
        refno.send_keys(reference_number)
        print(f"Entered Reference Number: {reference_number}")

        remarks = self.wait.until(
            EC.element_to_be_clickable(self.remarks)
        )
        remarks.clear()
        remarks.send_keys(enter_remarks)
        print(f"Entered Remarks: {enter_remarks}")

        pay_to = self.wait.until(
            EC.element_to_be_clickable(self.payee)
        )
        pay_to.clear()
        pay_to.send_keys(payee)
        print(f"Entered Payee: {payee}")

        voucher_type = self.wait.until(
            EC.element_to_be_clickable(self.voucher)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", voucher_type)

        try:
            voucher_type.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", voucher_type)
            print("Selected Voucher Type: Party Payment")

        cash_bank = self.wait.until(
            EC.element_to_be_clickable(self.cash)
        )
        cash_bank.send_keys(Keys.ENTER)

        select_cash_bank = self.wait.until(
            EC.element_to_be_clickable(self.select_cash)
        )
        select_cash_bank_click = ActionChains(self.driver).double_click(select_cash_bank)
        select_cash_bank_click.perform()
        print("Selected Cash/Bank Account: PETTY CASH A/C")

        account_select = self.wait.until(
            EC.element_to_be_clickable(self.account)
        )
        account_select.send_keys(Keys.ENTER)

        select_account = self.wait.until(
            EC.element_to_be_clickable(self.select_account)
        )
        select_account_click = ActionChains(self.driver).double_click(select_account)
        select_account_click.perform()
        print("Selected Account: Milk Chocolate Vendor")

        ammount = self.wait.until(
            EC.element_to_be_clickable(self.amount)
        )
        ammount.clear()
        ammount.send_keys(enter_amount)
        print(f"Entered Amount: {enter_amount}")

        narration = self.wait.until(
            EC.element_to_be_clickable(self.narration)
        )
        narration.click()
        narration.send_keys("Payment Voucher Automation Test")
        print("Entered Narration.")

        pay_mode = self.wait.until(
            EC.element_to_be_clickable(self.pay_mode)
        )
        pay_mode = Select(pay_mode)
        pay_mode.select_by_visible_text("Cheque")
        print("Selected Payment Mode: Cheque")

        cheque_no = self.wait.until(
            EC.element_to_be_clickable(self.cheque_no)
        )
        cheque_no.send_keys(cheque_number)
        print(f"Entered Cheque Number: {cheque_number}")
        cheque_no.send_keys(Keys.TAB)

        # Type today's date in MMDDYYYY format
        today_date = datetime.today().strftime("%d%m%Y")

                # --- Step: Enter Today's Date ---
        date_field = self.wait.until(
            EC.element_to_be_clickable(self.cheque_date)
        )

        self.driver.execute_script(
        "arguments[0].removeAttribute('readonly')",
        date_field
        )

        date_field.click()
        date_field.clear()
        date_field.send_keys(today_date)
        print(f"Entered Cheque Date: {today_date}") 
        date_field.send_keys(Keys.ENTER)

    def save_voucher(self):
        save_button = self.wait.until(
            EC.element_to_be_clickable(self.save)
        )
        save_button.click()
        print("Clicked on Save button successfully.")

        no_popup = self.wait.until(
            EC.element_to_be_clickable(self.no_popup)
        )
        no_popup.click()
        print("Handled popup.")
