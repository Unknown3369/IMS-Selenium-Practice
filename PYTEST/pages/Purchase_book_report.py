from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time
import pytest

class PurchaseBookReport:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)
      # Define all locators once
      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.purchase_report = (By.LINK_TEXT, "Purchase Reports")
      self.purchase_book_report = (By.XPATH, "//span[normalize-space()='Purchase Book Report']")
      self.warehouse_alert_handle = (By.XPATH, "//button[contains(text(), 'OK')]")
      self.branch_dropdown = (By.XPATH, "//select[contains(@class, 'form-control') and contains(@class, 'selectText')]")
      self.user_name = (By.XPATH, "//input[@placeholder='Press Enter for User List']")
      self.select_user = (By.XPATH, "//div[@title='Admin' and normalize-space()='Admin']")
      self.warehouse = (By.XPATH, "//select[@class='form-control input-text ng-untouched ng-pristine ng-valid']")
      self.select_supplier = (By.XPATH, "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']")
      self.select_supplier_list = (By.XPATH, "//div[normalize-space(text())='Dark Chocolate Vendor']")
      self.run_button = (By.XPATH, "//button[normalize-space(text())='RUN']")
      self.load_button = (By.XPATH, "//div[@class='option-card' and .//span[normalize-space()='Load Report']]")
      self.button = (By.XPATH, "//button[normalize-space()='OK']")
   def open_purchase_book_report(self):
      """Actually runs the Purchase Book Report test flow."""
      driver = self.driver
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
         )
      driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      # Hover over "Purchase Report"
      purchase_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_report)
         )
      ActionChains(driver).move_to_element(purchase_report).perform()
      time.sleep(1)
      purchase_report.click()
      print("Purchase Report clicked successfully!")
      # Click on “Purchase Book Report”
      purchase_book_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_book_report)
         )
      driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_book_report)
      time.sleep(1)
      driver.execute_script("arguments[0].click();", purchase_book_report)
      print("Purchase Book Report clicked successfully!")
      # Handle alert if exists
      try:
         warehouse_alert = self.wait.until(
            EC.presence_of_element_located(self.warehouse_alert_handle)
            )
         warehouse_alert.click()
         print("Warehouse alert handled successfully!")
      except:
         print("No warehouse alert present.")
      # Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
         )
      select_branch = Select(branch_dropdown)
      select_branch.select_by_visible_text("ALL")
      print("Branch selected successfully!")
      # Warehouse selection
      warehouse = self.wait.until(
         EC.presence_of_element_located(self.warehouse)
         )
      select_warehouse = Select(warehouse)
      select_warehouse.select_by_visible_text("ALL")
      print("Warehouse selected successfully!")
      # Supplier selection
      select_supplier = self.wait.until(
         EC.presence_of_element_located(self.select_supplier)
         )
      select_supplier.send_keys(Keys.ENTER)
      select_supplier_item = self.wait.until(
         EC.presence_of_element_located(self.select_supplier_list)
         )
      ActionChains(driver).double_click(select_supplier_item).perform()
      print("Supplier selected successfully!")
      # Run report
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
         )
      run_button.click()
      print("Run button clicked successfully!")
      # Load report
      load_button = self.wait.until(
         EC.element_to_be_clickable(self.load_button)
         )
      load_button.click()
      print("Load Report clicked successfully!")

      try:
         alert_text = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Data Not found with given filters')]"))
         )
         if alert_text:
            ok_button = driver.find_element(self.button)
            ok_button.click()
            pytest.fail("Test failed: 'Data Not found with given filters' alert appeared.")
      except:
         print("No popup detected.")
