from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PYTEST.tests.Accounting.login_accounting_test import test_login_to_ims
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class ContraVouchersPage:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver,12)

      self.accounting_module =(By.XPATH, "//span[normalize-space(text())='Accounting Module']")
      self.transactions = (By.XPATH, "//span[normalize-space(text())='Transactions']")
      self.chart_of_accounts = (By.LINK_TEXT, "Voucher Entries")
      self.contra_voucher = (By.LINK_TEXT, "Contra Voucher")
      self.ok_button = (By.XPATH, "//button[@title='Save' and normalize-space()='OK']")
      self.refno = (By.XPATH, "//input[@id='refno']")
      self.remarks = (By.XPATH, "//input[@name='REMARKS']")
      self.select_account = (By.XPATH, "//input[@id='ACCODEInput_0']")
      self.selected_account = (By.XPATH, "//div[@title='testing 11']")
      self.amount_dr = (By.XPATH, "//input[@id='DrAmtInput_0']")
      self.cost_center = (By.XPATH, "//input[@id='CostCenterInput_0']")
      self.select_cost_center = (By.XPATH, "//td/div[normalize-space()='12 JANUARY']")
      self.narration = (By.XPATH, "//input[@id='narration_0']")
      self.tran = (By.XPATH, "//*[@id='transactionType_0']")
      self.select_account_n = (By.XPATH, "//input[@id='ACCODEInput_1']")
      self.selected_account_n = (By.XPATH, "//div[@title='testing 11']")
      self.cr_amount = (By.XPATH, "//input[@id='CrAmtInput_1']")
      self.cost_center_n = (By.XPATH, "//input[@id='CostCenterInput_1']")
      self.narration = (By.XPATH, "//input[@id='narration_1']")
      self.save_button = (By.XPATH,"//button[normalize-space()='F6 SAVE']")
      self.no_button = (By.XPATH, "//button[contains(text(),'No')]")
      
   def open_accounting_module(self): 
      account = self.wait.until(
            EC.element_to_be_clickable(self.accounting_module)
      )
      account.click()
      print("Navigated to Accounting Module.")

      WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
      self.driver.switch_to.window(self.driver.window_handles[-1])
      print("Switched to Accounting Module tab.")
   
   def open_contra_voucher(self):
      transactions = self.wait.until(
         EC.element_to_be_clickable(self.transactions)
      )
      ActionChains(self.driver).move_to_element(transactions).click().perform()
      print("Hovered and clicked on Transactions menu.")
      chart_of_accounts = self.wait.until(
         EC.presence_of_element_located(self.chart_of_accounts)
      )
      ActionChains(self.driver).move_to_element(chart_of_accounts).perform()
      print("Hovered over Voucher Entries.")
      contra = self.wait.until(
         EC.element_to_be_clickable(self.contra_voucher)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contra)
      time.sleep(2)  
      self.driver.execute_script("arguments[0].click();", contra)
      print("Contra Voucher opened.")
      time.sleep(5)

   def add_contra_voucher(self, reference_number: str, enter_remarks: str, debit_amount: int, credit_amount: int):
      try:
            ok_button = self.wait.until(
            EC.element_to_be_clickable(self.ok_button)
            )
            ok_button.click()
            print("Clicked OK button to proceed.")
      except TimeoutException:
            print("OK button not found or not clickable.")

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

      select_account = self.wait.until(
            EC.element_to_be_clickable(self.select_account)
      )
      select_account.send_keys(Keys.ENTER)

      ActionChains(self.driver).double_click(
            self.wait.until(
                  EC.element_to_be_clickable(self.selected_account)
            )
      ).perform()

      amount_dr = self.wait.until(
            EC.element_to_be_clickable(self.amount_dr)
      )
      amount_dr.clear()
      amount_dr.send_keys(debit_amount)
      print(f"Entered Debit Amount: {debit_amount}")

      cost_center = self.wait.until(
            EC.element_to_be_clickable(self.cost_center)
      )
      cost_center.click()
      cost_center.send_keys(Keys.ENTER)
      print("Opened Cost Center.")

      select_cost_center = self.wait.until(
         EC.element_to_be_clickable(self.select_cost_center)
         )
      ActionChains(self.driver).double_click(select_cost_center).perform()
      print("Selected Cost Center.")

      # narration = self.wait.until(
      #       EC.presence_of_element_located(self.narration)
      # )
      # self.driver.execute_script("""arguments[0].scrollIntoView({block:'center'});arguments[0].focus();""", narration)
      # narration.clear()
      # narration.send_keys(enter_remarks)
      # print("Narration added.")
      
      check = self.wait.until(
            EC.element_to_be_clickable(self.tran)
      )
      check.click()
      check.send_keys(Keys.ENTER)
      print("Jumped to next line.")

      select_account_n = self.wait.until(
            EC.element_to_be_clickable(self.select_account_n)
      )
      select_account_n.send_keys(Keys.ENTER)

      ActionChains(self.driver).double_click(
            self.wait.until(
                  EC.element_to_be_clickable(self.selected_account_n)
            )
      ).perform()

      cr_amount = self.wait.until(
            EC.element_to_be_clickable(self.cr_amount)
      )
      cr_amount.clear()
      cr_amount.send_keys(credit_amount)
      print(f"Entered Credit Amount: {credit_amount}")

      cost_center_n = self.wait.until(
            EC.element_to_be_clickable(self.cost_center_n)
      )
      cost_center_n.click()
      cost_center_n.send_keys(Keys.ENTER)

      select_cost_center = self.wait.until(
            EC.element_to_be_clickable(self.select_cost_center)
      )
      select_cost_center.click = ActionChains(self.driver).move_to_element(select_cost_center).double_click().perform()

      try:
      # Try to find and click the Save button
         save_button = self.wait.until(
            EC.element_to_be_clickable(self.save_button)
         )
         save_button.click()
         print("Clicked on Save button.")
      except (TimeoutException, ElementClickInterceptedException):
         print("Save button not found or not clickable. Pressing SHIFT and retrying...")
         # Press and release SHIFT key
         ActionChains(self.driver).key_down(Keys.SHIFT).pause(0.5).key_up(Keys.SHIFT).perform()
            # Try again to find and click the button
         save_button = self.wait.until(
            EC.element_to_be_clickable(self.save_button)
         )
         save_button.click()
         print("Clicked on Save button after pressing SHIFT.")

      no_btn = self.wait.until(
            EC.element_to_be_clickable(self.no_button)
      )
      no_btn.click()
      print("Clicked 'No' on the confirmation dialog.")

if __name__ == "__main__":
   driver = webdriver.Chrome()
   test_login_to_ims(driver)
   contra_voucher_page = ContraVouchersPage(driver)
   contra_voucher_page.open_accounting_module()
   contra_voucher_page.open_contra_voucher()
   driver.quit()