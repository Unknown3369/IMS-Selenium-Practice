from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Tests.login_test import login_to_ims

class MainPage:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 15)

      self.accounting_module = (By.XPATH, "//span[normalize-space(text())='Accounting Module']")
      self.transactions = (By.XPATH, "//span[normalize-space(text())='Transactions']")
      self.opening_entries = (By.LINK_TEXT, "Opening Entries")
      self.party_opening_bl = (By.LINK_TEXT, "Party Opening B/L")
      self.refno = (By.XPATH, "//input[@id='refno']")
      self.select_account = (By.XPATH, "//input[@id='ACCODEInput_0']")
      self.account_select = (By.XPATH, "//div[@title='Milk Chocolate Vendor']")
      self.amount_dr = (By.XPATH, "//input[contains(@id, 'DrAmtInput')]")
      self.narration = (By.ID, "narration_0")
      self.save_button = (By.XPATH, "//button[normalize-space(text())='F6 SAVE']")
      self.no_button = (By.ID, "nobtn")
      
   def open_accounting_module(self):
      account = self.wait.until(
            EC.element_to_be_clickable(self.accounting_module)
      )
      account.click()
      print("Navigated to Accounting Module.")

      WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
      self.driver.switch_to.window(self.driver.window_handles[-1])
      print("Switched to Accounting Module tab.")

   def open_party_opening_bl(self):
      transactions = self.wait.until(
         EC.element_to_be_clickable(self.transactions)
      )
      ActionChains(self.driver).move_to_element(transactions).click().perform()
      print("Hovered and Clicked on Transactions menu.")
      opening_entries = self.wait.until(
         EC.presence_of_element_located(self.opening_entries)
      )
      opening_entries.click()
      print("Clicked on opening entries.")
      ledger_opening_bl = self.wait.until(
         EC.presence_of_element_located(self.party_opening_bl)
      )
      ledger_opening_bl.click()
      print("Clicked on Party Opening B/L.")

   def add_party_opening_details(self, reference_number: str, debit_amount: float, enter_narration: str):
      refno = self.wait.until(
         EC.element_to_be_clickable(self.refno)
      )
      refno.clear()
      refno.send_keys(reference_number)
      print(f"Entered Reference Number: {reference_number}")

      select_acc = self.wait.until(
         EC.element_to_be_clickable(self.select_account)
      )
      select_acc.send_keys(Keys.ENTER)

      account_select = self.wait.until(
         EC.element_to_be_clickable(self.account_select)
      )
      actions_select = ActionChains(self.driver).double_click(account_select).perform()
      print("Selected Account")

      amount_dr = self.wait.until(
         EC.element_to_be_clickable(self.amount_dr)
      )
      amount_dr.clear()
      amount_dr.send_keys(debit_amount)
      print(f"Entered Debit Amount: {debit_amount}")

      narration = self.wait.until(
         EC.element_to_be_clickable(self.narration)
      )
      narration.clear()
      narration.send_keys(enter_narration)
      print(f"Entered Narration: {enter_narration}")

      save_button = self.wait.until(
         EC.element_to_be_clickable(self.save_button)
      )
      save_button.click()
      print("Clicked on Save button.")

      no_button = self.wait.until(
         EC.element_to_be_clickable(self.no_button)
      )
      no_button.click()
      print("Clicked on No button in confirmation dialog.")

if __name__ == "__main__":
   driver = login_to_ims()
   main_page = MainPage(driver)
   main_page.open_accounting_module()
   main_page.open_party_opening_bl()
   # Add further interactions as needed
   driver.quit()