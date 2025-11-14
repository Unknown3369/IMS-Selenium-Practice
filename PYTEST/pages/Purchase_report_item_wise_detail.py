from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Purchase_report_item_wise_detail:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(self.driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.purchase_report = (By.LINK_TEXT, "Purchase Reports")
      self.purchase_report_item_wise = (By.XPATH, "//span[normalize-space()='Purchase Report - Item Wise']")
      self.branch_dropdown = (By.XPATH, "//select[@class='form-control input-text ng-untouched ng-pristine ng-valid']")
      self.run_button = (By.XPATH, "//button[@type='button' and text()='RUN']")
   
   def item_wise_detail_report(self):
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

      # Click on "Purchase Report - Item Wise"
      purchase_report_item_wise = self.wait.until(
         EC.presence_of_element_located(self.purchase_report_item_wise)
         )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", purchase_report_item_wise)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", purchase_report_item_wise)
      print("Purchase Report - Item Wise clicked successfully!")

   def open_item_wise_detail_report(self, enter_item_code: str):
      # Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
         )
      select_branch = Select(branch_dropdown)
      select_branch.select_by_visible_text("ALL")
      print("Branch selected successfully!")

      item_select = self.wait.until(
         EC.presence_of_element_located((By.XPATH, "//span[@class='select2-selection__placeholder']"))
         )
      item_select.send_keys(Keys.ENTER)
      select_item_code = self.wait.until(
         EC.presence_of_element_located(self.select_item_code)
         )
      select_item_code.click()
      select_item_code.select_by_visible_text("ITEM CODE")
      print("Item Code selected successfully!")

      search_item = self.wait.until(
         EC.presence_of_element_located(self.search_item)
         )
      search_item.send_keys(enter_item_code)
      search_item.send_keys(Keys.ENTER)
      print(f"Item code {enter_item_code} entered successfully!")

      ok_button = self.wait.until(
         EC.presence_of_element_located(self.ok_button)
         )
      


   def run_item_wise_detail_report(self):
      # Run report
      run_button = self.wait.until(
         EC.presence_of_element_located(self.run_button)
         )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", run_button)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", run_button)
      print("Run button clicked successfully!")