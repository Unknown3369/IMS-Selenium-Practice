from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from ..tests.login_test import test_login_to_ims
import keyboard
import time

class TestPurchaseBookReport:
   def test_purchase_book_report(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.purchase_report = (By.LINK_TEXT, "Purchase Reports")
      self.purchase_book_report = (By.XPATH, "//span[normalize-space()='Purchase Book Report']")
      self.warehouse_alert_handle = (By.XPATH, "//button[contains(text(), 'OK')]")
      self.branch_dropdown = (By.XPATH, "//select[contains(@class, 'form-control') and contains(@class, 'selectText')]")
      self.user_name = (By.XPATH, "//input[@placeholder='Press Enter for User List']")
      self.select_user = (By.XPATH, "//div[@title='Admin' and normalize-space()='Admin']")
      self.warehouse = (By.XPATH, "//select[@class='form-control input-text ng-untouched ng-pristine ng-valid']")
      self.select_supplier = (By.XPATH, "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']")
      self.select_supplier_list = (By.XPATH, "//div[normalize-space(text())='ABC Camp 2']")
      self.run_button = (By.XPATH, "//button[normalize-space(text())='RUN']")
      self.load_button = (By.XPATH, "//div[@class='option-card' and .//span[normalize-space()='Load Report']]")


   def purchase_book_report_test(self, driver: webdriver):
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")
      time.sleep(5)

      # Hover over "Purchase Report" before clicking
      purchase_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_report)
      )
      ActionChains(driver).move_to_element(purchase_report).perform()
      time.sleep(2)  # give some time for the submenu to appear

      # Click after hovering
      purchase_report.click()
      print("Purchase Report hovered and clicked successfully!")

      # Click on “Sales Invoice” link
      purchase_book_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_book_report)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_book_report)
      time.sleep(2)
      self.driver.execute_script("arguments[0].click();", purchase_book_report)
      print("Purchase Book Report clicked successfully!")
      time.sleep(5)

      #exception handling for alert
      try:
         warehouse_alert = self.wait.until(
            EC.presence_of_element_located(self.warehouse_alert_handle)
         )
         warehouse_alert.click()
         print("Warehouse alert handled successfully.")
      except:
         print("No warehouse alert present.")

      time.sleep(4)

      #Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
      )
      branch_dropdown.click()
      time.sleep(5)
      select_branch = Select(branch_dropdown)
      time.sleep(1)
      select_branch.select_by_visible_text("GRN")
      select_branch_click = ActionChains(driver)
      select_branch_click.double_click(branch_dropdown).perform()
      print("Branch selected successfully!")

      #select user
      user_name = self.wait.until(
         EC.presence_of_element_located(self.user_name)
      )
      user_name.send_keys(Keys.ENTER)

      select_user = self.wait.until(
         EC.presence_of_element_located(self.select_user)
      )
      select_user_click = ActionChains(driver)
      select_user_click.double_click(select_user).perform()
      print("User selected successfully!")

      #select warehouse
      warehouse = self.wait.until(
         EC.presence_of_element_located(self.warehouse)
      )
      warehouse.click()
      select_warehouse = Select(warehouse)
      select_warehouse.select_by_visible_text("ALL")
      print("Warehouse selected successfully!")

      #Supplier Selection
      select_supplier = self.wait.until(
         EC.presence_of_element_located(self.select_supplier)
      )
      select_supplier.send_keys(Keys.ENTER)
      time.sleep(0.5)

      select_supplier_list = self.wait.until(
         EC.presence_of_element_located(self.select_supplier_list)
      )
      select_supplier_click = ActionChains(driver)
      select_supplier_click.double_click(select_supplier_list).perform()
      print("Supplier selected successfully!")

      # Click on the "Run" button
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
      )
      run_button.click()
      print("Run button clicked successfully!")

      #load Report
      load_button = self.wait.until(
         EC.element_to_be_clickable(self.load_button)
      )
      load_button.click()
      print("Load Report clicked successfully!")

      # self.wait for user input before closing the browser
      print("Press 'Enter' to close the browser.")
      keyboard.self.wait('enter')
      driver.quit()
