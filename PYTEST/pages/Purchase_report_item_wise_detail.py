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
      self.purchase_report_item_wise = (By.XPATH, "//span[normalize-space()='Purchase Report - Item Wise Detail']")
      self.branch_dropdown = (By.XPATH, "//select[option[@disabled and normalize-space()='Select Branch']]")
      self.item_name = (By.XPATH, "//input[@placeholder='Press Enter to select Items']")
      self.item_select = (By.XPATH, "//select[option[text()='Select Filter Option']]")
      self.select_item_code = (By.XPATH, "//select[option[text()='ITEM CODE'] and option[text()='DESCRIPTION']]")
      self.search_item = (By.XPATH, "//input[@placeholder='Enter keyword to search']")
      self.select_search_item = (By.XPATH,"//input[@type='checkbox']")
      self.ok_button = (By.XPATH, "//button[normalize-space()='OK']")
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
      time.sleep(3)

   def open_item_wise_detail_report(self):
      # Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
         )
      time.sleep(2)
      select_branch = Select(branch_dropdown)
      select_branch.select_by_visible_text("ALL")
      print("Branch selected successfully!")

      item_name = self.wait.until(
         EC.presence_of_element_located(self.item_name)
         )
      item_name.click()
      item_name.send_keys(Keys.ENTER)
      time.sleep(2)
      print("Item Name selected successfully!")

      item_select = self.wait.until(
         EC.presence_of_element_located(self.item_select)
         )
      self.driver.execute_script("arguments[0].click();", item_select)
      select_item_code = self.wait.until(
         EC.presence_of_element_located(self.select_item_code)
         )
      select_item_code_dropdown = Select(select_item_code)
      time.sleep(2)
      select_item_code_dropdown.select_by_visible_text("ITEM CODE")
      print("Item Code selected successfully!")

   def fill_item_wise_detail_report(self, enter_item_code: str):
      search_item = self.wait.until(
         EC.presence_of_element_located(self.search_item)
         )
      search_item.click()
      search_item.send_keys(enter_item_code)
      select_search_item = self.wait.until(
         EC.presence_of_element_located(self.select_search_item)
         )
      select_search_item.click()
      print(f"Item code {enter_item_code} entered successfully!")
      
   def run_item_wise_detail_report(self):
      ok_button = self.wait.until(
         EC.presence_of_element_located(self.ok_button)
         )
      ok_button.click()
      print("OK button clicked successfully!")
      # Run report
      run_button = self.wait.until(
         EC.presence_of_element_located(self.run_button)
         )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", run_button)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", run_button)
      print("Run button clicked successfully!")
      