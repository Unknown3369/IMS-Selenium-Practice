from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Sales_report_customer_wise:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.action = ActionChains(driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.sales_report = (By.LINK_TEXT, "Sales Report")
      self.sales_report_customer_wise = (By.XPATH, "//span[normalize-space()='Sales Report - Customer Wise']")
      self.branch = (By.XPATH, "//select//option[normalize-space()='ALL']")
      self.run_button = (By.XPATH, "//button[@type='button' and text()='RUN']")
   
   def sale_report_customer_wise(self):
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
         )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      # Hover over "Sales Report"
      sales_report = self.wait.until(
         EC.presence_of_element_located(self.sales_report)
         )
      self.action.move_to_element(sales_report).perform()
      time.sleep(1)
      sales_report.click()
      print("Sales Report clicked successfully!")

      # Click on "Sales Report - Customer Wise"
      sales_report_customer_wise = self.wait.until(
         EC.presence_of_element_located(self.sales_report_customer_wise)
         )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sales_report_customer_wise)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", sales_report_customer_wise)
      print("Sales Report - Customer Wise clicked successfully!")

   def test_sales_report_customer_wise(self):
      # Branch Selection
      branch = self.wait.until(
         EC.presence_of_element_located(self.branch)
         )
      branch.click()
      print("Branch selected successfully!")

      # Run report
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
         )
      run_button.click()
      print("Run button clicked successfully!")