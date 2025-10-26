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
      self.load_btn = (By.XPATH, "//button[contains(@class, 'btn-info') and normalize-space(text())='Load']")

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

   def party_balance_(self):
      print("party_balance_ function called")
      select_from_date = self.wait.until(
         EC.presence_of_element_located(self.select_from_date)
      )
      select_from_date.clear()
      select_from_date.send_keys("09262025")
      print("Entered From Date: 09262025")

      select_to_date = self.wait.until(
         EC.presence_of_element_located(self.select_to_date)
      )
      select_to_date.clear()
      select_to_date.send_keys("10262025")
      print("Entered To Date: 10262025")

      party_account_select = self.wait.until(
         EC.element_to_be_clickable(self.account_select)
      )
      party_account_select.send_keys(Keys.ENTER)
      select_party_account = self.wait.until(
         EC.element_to_be_clickable(self.select_account)
      )
      select_party_account_click = ActionChains(self.driver).double_click(select_party_account)
      select_party_account_click.perform()
      print("Selected Party Account: IMSTestCustom")
      time.sleep(2)

      # save_button = self.wait.until(
      #    EC.element_to_be_clickable(self.load_btn)
      # )
      # self.actions.double_click(save_button).perform()
      # print("Load button clicked successfully!")

      try:
         load_button = self.wait.until(
         EC.element_to_be_clickable(self.load_btn)
         )
         self.driver.execute_script("arguments[0].scrollIntoView(true);", load_button)
         load_button.click()
         print("Clicked Load button successfully.")
      except:
         print("Could not find or click the Load button within time.")


if __name__ == "__main__":
   driver = login_to_ims()
   main_page = MainPage(driver)
   main_page.open_accounting_module()
   main_page.open_party_bl_conformation()
   main_page.party_balance_()
   time.sleep(25)
   driver.quit()