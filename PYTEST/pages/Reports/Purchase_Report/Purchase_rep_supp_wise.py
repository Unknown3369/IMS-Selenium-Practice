from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Purchase_rep_supp_wise:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 25)
      self.actions = ActionChains(driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.purchase_report = (By.LINK_TEXT, "Purchase Reports")
      self.purchase_report_item_wise = (By.XPATH, "//span[normalize-space()='Purchase Report - Supplier Wise']")
      self.supplier = (By.XPATH, "//input[@placeholder='Press Enter or Tab for Account List' and @type='text']")
      self.select_supplier = (By.XPATH, "//div[contains(@title, '11 QA Vendor') and contains(text(), '11 QA Vendor')]")
      self.run_button = (By.XPATH, "//button[@type='button' and contains(@class, 'confirm-btn') and normalize-space(text())='RUN']")

   def purchase_report_supp(self):
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
         )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      # Hover over "Purchase Report- Item Wise"
      purchase_report = self.wait.until(
         EC.presence_of_element_located(self.purchase_report)
         )
      self.actions.move_to_element(purchase_report).perform()
      time.sleep(1)
      purchase_report.click()
      print("Purchase Report clicked successfully!")
      # Click on “Purchase Book Report”
      purchase_report_supp_wise = self.wait.until(
         EC.presence_of_element_located(self.purchase_report_item_wise)
         )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_report_supp_wise)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", purchase_report_supp_wise)
      print("Purchase Report - Supplier Wise clicked successfully!")

   def run_purchase_report_supp(self):

      # Supplier Select
      supplier = self.wait.until(
         EC.presence_of_element_located(self.supplier)
      )
      supplier.click()
      supplier.send_keys(Keys.ENTER)
      select_supplier = self.wait.until(
         EC.presence_of_element_located(self.select_supplier)
      )
      self.actions.double_click(select_supplier).perform()
      print("Supplier selected successfully!")

      # Run report
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
         )
      run_button.click()
      print("Run button clicked successfully!")