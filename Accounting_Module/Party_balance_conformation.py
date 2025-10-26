from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from login_details import login_to_ims
from datetime import date
import time


class MainPage:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 15)
      self.actions = ActionChains(driver)

      self.accounting_module = (By.XPATH, "//span[normalize-space(text())='Accounting Module']")
      self.utilities = (By.XPATH, "//span[normalize-space(text())='Utilities']")
      self.reconciliation = (By.LINK_TEXT, "Reconciliation")
      self.party_balance_confirmation = (By.LINK_TEXT, "Party Balance Confirmation")
      self.select_from_date = (By.XPATH, "//input[@type='date' and @placeholder='Year Start Date' and contains(@style, 'width: 128px; height: 25px;') and not(contains(@style, 'margin-left'))]")
      self.select_to_date = (By.XPATH, "//input[@type='date' and @placeholder='Year Start Date' and contains(@style, 'margin-left: 13px')]")
      self.account_select = (By.XPATH, "//input[@name='customerName' and @placeholder='Press Enter to select']")
      self.select_account = (By.XPATH, "//div[@title='IMSTestCustom']")

   def open_accounting_module(self):
      account = self.wait.until(
            EC.element_to_be_clickable(self.accounting_module)
      )
      account.click()
      print("Navigated to Accounting Module.")

      WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
      self.driver.switch_to.window(self.driver.window_handles[-1])
      print("Switched to Accounting Module tab.")

   def open_party_bl_conformation(self):
      utilities = self.wait.until(
         EC.element_to_be_clickable(self.utilities)
      )
      ActionChains(self.driver).move_to_element(utilities).click().perform()
      print("Hovered and Clicked on Utilities.")
      reconciliation = self.wait.until(
         EC.presence_of_element_located(self.reconciliation)
      )
      reconciliation.click()
      print("Clicked on opening entries.")
      party_bl_conformation = self.wait.until(
         EC.presence_of_element_located(self.party_balance_confirmation)
      )
      party_bl_conformation.click()
      print("Clicked on Party Balance Conformation.")




      # # Type today's date in MMDDYYYY format
      # today_date = date.today().strftime("%m%d%Y")
      # # Use the initialized ActionChains instance
      # self.actions.send_keys(today_date).perform()
      # try:
      #    alert_ok = WebDriverWait(self.driver, 5).until(
      #       EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='OK']"))
      #    )
      #    alert_ok.click()
      #    print("Closed 'Invalid Transaction Date' popup")
      # except Exception:
      #    pass

      select_to_date = self.wait.until(
         EC.presence_of_element_located(self.select_to_date)
      )
      select_to_date.clear()



if __name__ == "__main__":
   driver = login_to_ims()
   main_page = MainPage(driver)
   main_page.open_accounting_module()
   main_page.open_party_bl_conformation()
   time.sleep(25)
   driver.quit()