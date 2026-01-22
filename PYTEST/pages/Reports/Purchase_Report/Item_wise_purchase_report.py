from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time
import pytest

class PurchaseReport_ItemWise:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.purchase_report = (By.LINK_TEXT, "Purchase Reports")
      self.purchase_report_item_wise = (By.XPATH, "//span[normalize-space()='Purchase Report - Item Wise']")
      self.branch_dropdown = (By.XPATH, "//select[option[@disabled and normalize-space()='Select Branch']]")
      self.run_button = (By.XPATH, "//button[@class='btn btn-info confirm-btn' and text()='RUN']")

   def open_purchase_report_item_wise(self):
      driver = self.driver
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
         )
      driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      # Hover over "Purchase Report- Item Wise"
      purchase_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_report)
         )
      ActionChains(driver).move_to_element(purchase_report).perform()
      time.sleep(1)
      purchase_report.click()
      print("Purchase Report clicked successfully!")
      # Click on “Purchase Book Report”
      purchase_report_item_wise = self.wait.until(
         EC.presence_of_element_located(self.purchase_report_item_wise)
         )
      driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_report_item_wise)
      time.sleep(1)
      driver.execute_script("arguments[0].click();", purchase_report_item_wise)
      print("Purchase Report - Item Wise clicked successfully!")
   
   def run_item_wise_purchase_report(self):
      # Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
         )
      select_branch = Select(branch_dropdown)
      time.sleep(1)
      select_branch.select_by_visible_text("ALL")
      print("Branch selected successfully!")
      # Run report
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
         )
      run_button.click()
      print("Run button clicked successfully!")
