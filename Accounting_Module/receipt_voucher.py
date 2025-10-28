from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from login_details import login_to_ims
from datetime import date
import time  # Needed for short sleep


class MainPage:
   def __init__(self, driver):
      self.driver = driver
      self.actions = ActionChains(driver)
      self.wait = WebDriverWait(self.driver, 15)
      self.accounting_module = (By.XPATH, "//span[normalize-space(text())='Accounting Module']")
      self.transactions = (By.XPATH, "//span[normalize-space(text())='Transactions']")
      self.chart_of_accounts = (By.LINK_TEXT, "Voucher Entries")
      self.receipt_voucher = (By.LINK_TEXT, "Receipt Voucher")
      self.refno = (By.XPATH, "//input[@id='refno' and @placeholder='press Enter to Select SO']")
      self.select_refno = (By.XPATH, "//div[@title='SO3-KAT-82/83' and normalize-space(text())='SO3-KAT-82/83']")
      self.remarks = (By.XPATH, "//input[@name='REMARKS']")
      self.received_from = (By.XPATH, "//input[@name='BILLTO']")
      self.voucher_type = (By.XPATH, "//select[@name='TRNMODE']")
      self.cash_bank = (By.XPATH, "//input[@name='TRNAC']")
      self.select_cash = (By.XPATH, "//div[normalize-space(text())='PETTY CASH A/C']")
      self.select_account = (By.XPATH, "//input[@id='ACCODEInput_0']")
      self.account_select= (By.XPATH, "//div[@title='Test' and normalize-space()='Test']")
      self.amount_cr = (By.XPATH, "//input[@id='CrAmtInput_0']")
      self.narration= (By.XPATH, "//input[@id='narration_0']")
      self.receipt_mode = (By.XPATH, "//select[@id='transactionType_0']")
      self.receipt_number = (By.ID, "ChequeNo_0")
      self.date = (By.XPATH, "//input[@id='ChequeDate_0']")
      self.cross = (By.XPATH, "//span[@aria-hidden='true' and text()='×']")
      self.save = (By.XPATH, "//button[contains(text(), 'F6 SAVE')]")



   def open_accounting_module(self):
      account = self.wait.until(
         EC.element_to_be_clickable(self.accounting_module)
      )
      account.click()
      print("Navigated to Accounting Module.") 
      WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
      self.driver.switch_to.window(self.driver.window_handles[-1])
      print("Switched to Accounting Module tab.")

   def open_receipt_voucher(self):
      transactions = self.wait.until(
         EC.element_to_be_clickable(self.transactions)
      )
      ActionChains(self.driver).move_to_element(transactions).click().perform()
      print("Hovered and clicked on Transactions menu.")
      chart_of_accounts = self.wait.until(
         EC.presence_of_element_located(self.chart_of_accounts)
      )
      ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
      print("Hovered over Voucher Entries." )
      ledger_group = self.wait.until(
         EC.element_to_be_clickable(self.receipt_voucher)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ledger_group)
      time.sleep(2)  
      self.driver.execute_script("arguments[0].click();", ledger_group)
      print("Receipt Voucher opened.")
      time.sleep(5)

   def add_voucher(self, enter_remarks: str, received_text: str):

      ref_no_field = self.wait.until(
         EC.element_to_be_clickable(self.refno)
      )
      ref_no_field.send_keys(Keys.ENTER)
      select_ref_no = self.wait.until(
         EC.element_to_be_clickable(self.select_refno)
      )
      select_ref_number = ActionChains(self.driver).double_click(select_ref_no)
      select_ref_number.perform()

      remarks = self.wait.until(
         EC.element_to_be_clickable(self.remarks)
      )
      remarks.clear()
      remarks.send_keys(enter_remarks)
      print(f"Entered Remarks: {enter_remarks}")

      received_from = self.wait.until(
         EC.element_to_be_clickable(self.received_from)
      )
      received_from.clear()
      received_from.send_keys(received_text)
      print(f"Entered Received From: {received_text}")

      voucher_type_element = self.wait.until(
         EC.element_to_be_clickable(self.voucher_type)
      )
      voucher_type = Select(voucher_type_element)
      voucher_type.select_by_visible_text("Income Voucher")
      print("Selected Voucher Type: Income Voucher")

      cash_bank = self.wait.until(
         EC.element_to_be_clickable(self.cash_bank)
      )
      cash_bank.send_keys(Keys.ENTER)
      select_cash_bank = self.wait.until(
         EC.element_to_be_clickable(self.select_cash)
      )
      select_acc = ActionChains(self.driver).double_click(select_cash_bank)
      select_acc.perform()
      print("Selected Cash/Bank Account: PETTY CASH A/C")

   def voucher_details(self, cr_amount: int, enter_narration: str, number_receipt: str):
      select_account = self.wait.until(
         EC.element_to_be_clickable(self.select_account)
      )
      select_account.send_keys(Keys.ENTER)
      account_select = self.wait.until(
         EC.element_to_be_clickable(self.account_select)
      )
      account_select_click = ActionChains(self.driver).double_click(account_select)
      account_select_click.perform()
      print("Selected Account: IMSTestCustom")

      amount = self.wait.until(
         EC.element_to_be_clickable(self.amount_cr)
      )
      amount.clear()
      amount.send_keys(cr_amount)
      print(f"Entered Credit Amount: {cr_amount}")

      narration = self.wait.until(
         EC.element_to_be_clickable(self.narration)
      )
      narration.send_keys(enter_narration)
      print(f"Entered Narration: {enter_narration}")

      receipt_mode = self.wait.until(
         EC.element_to_be_clickable(self.receipt_mode)
      )
      receipt_mode.click()
      Select(receipt_mode).select_by_visible_text("E-Transfer")
      print("Selected Receipt Mode: Cheque")

      receipt_number = self.wait.until(
         EC.element_to_be_clickable(self.receipt_number)
      )
      receipt_number.send_keys(number_receipt)
      print(f"Entered Receipt Number: {number_receipt}")
      time.sleep(15)

      # --- Step: Enter Today's Date ---
      date_field = self.wait.until(
            EC.element_to_be_clickable(self.date)
         )
      date_field.click()

      # Type today's date in MMDDYYYY format
      today_date = date.today().strftime("%m%d%Y")

      # Use the initialized ActionChains instance
      self.actions.send_keys(today_date).perform()

      time.sleep(5)   

      try:
         alert_ok = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='OK']"))
         )
         alert_ok.click()
         print("Closed 'Invalid Transaction Date' popup")
      except Exception:
         pass

      time.sleep(10)
      

      # try:
      # Try clicking directly
      save_button = self.wait.until(EC.element_to_be_clickable(self.save))
      save_button.click()
      print("Save button clicked successfully.")
      # except:
      #    print("Save button not clickable....trying Shift key workaround...")
      #    # Send Ctrl keypress (you can change this to TAB, ENTER, etc.)
      #    actions = ActionChains(self.driver)
      #    actions.key_down(Keys.SHIFT).pause(0.1).key_up(Keys.SHIFT).perform()
      #    # Try again
      #    save_button = self.wait.until(EC.element_to_be_clickable(self.save))
      #    save_button.click()
      #    print("Save button clicked after Shift key workaround.")




if __name__ == "__main__":
   driver = login_to_ims()
   receipt_voucher = MainPage(driver)
   receipt_voucher.open_accounting_module()
   receipt_voucher.open_journal_voucher()
   time.sleep(2)
   driver.quit()

