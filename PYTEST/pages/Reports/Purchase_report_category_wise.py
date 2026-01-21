from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Purchase_report_category_wise:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(self.driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.purchase_report = (By.LINK_TEXT, "Purchase Reports")
      self.report_category_wise = (By.XPATH, "//span[normalize-space()='Purchase Report - Category Wise']")
      self.branch_dropdown = (By.XPATH, "//select[@class='form-control input-text ng-untouched ng-pristine ng-valid']")
      self.run_button = (By.XPATH, "//button[@type='button' and text()='RUN']")

   def category_wise_report(self):
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
         )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      # Hover over "Purchase Report- Category Wise"
      purchase_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_report)
         )
      self.actions.move_to_element(purchase_report).perform()
      time.sleep(1)
      purchase_report.click()
      print("Purchase Report clicked successfully!")

      # Click on "Sales Report - Customer Wise"
      report_category_wise = self.wait.until(
         EC.presence_of_element_located(self.report_category_wise)
         )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", report_category_wise)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", report_category_wise)
      print("Purchase Report - Category Wise clicked successfully!")

   def open_category_wise_report(self):
      # Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
         )
      select_branch = Select(branch_dropdown)
      select_branch.select_by_visible_text("ALL")
      print("Branch selected successfully!")

      # Run report
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
         )
      run_button.click()
      print("Run button clicked successfully!")