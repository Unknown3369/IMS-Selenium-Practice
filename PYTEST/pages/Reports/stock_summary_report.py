from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class StockSummaryReport:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.inventory_report = (By.LINK_TEXT, "Inventory Reports")
      self.stock_summary_report = (By.XPATH, "//span[normalize-space()='Stock Summary Report']")
      self.branch_dropdown = (By.XPATH, "//select[@class='form-control selectText ng-untouched ng-pristine ng-valid']")
      self.select_warehouse = (By.XPATH, "//span[contains(@class,'dropdown-btn') and .//span[contains(text(),'Select Warehouse')]]")
      self.warehouse_option = (By.XPATH, "//div[normalize-space(text())='Main Warehouse']")
      self.run_button = (By.XPATH, "//button[@type='button' and normalize-space(text())='RUN']")

   def open_stock_summary_report(self):
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      inventory_report = self.wait.until(
         EC.presence_of_element_located(self.inventory_report)
      )
      ActionChains(self.driver).move_to_element(inventory_report).perform()
      time.sleep(1)
      inventory_report.click()
      print("Inventory Report clicked successfully!")

      stock_summary_report = self.wait.until(
         EC.presence_of_element_located(self.stock_summary_report)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", stock_summary_report)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", stock_summary_report)
      print("Stock Summary Report clicked successfully!")

   def select_branch(self):
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
      )
      select = Select(branch_dropdown)
      select.select_by_visible_text("ALL")
      print("Branch 'ALL' selected successfully!")

      select_warehouse = self.wait.until(
         EC.presence_of_element_located(self.select_warehouse)
      )
      select_warehouse.click()

      warehouse_option = self.wait.until(
         EC.presence_of_element_located(self.warehouse_option)
      )
      warehouse_option.click()
      print("Warehouse selected successfully!")

   def run_report(self):
      run_button = self.wait.until(
         EC.presence_of_element_located(self.run_button)
      )
      run_button.click()
      print("Run button clicked successfully!")