from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SheetGenerationPage:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 20)
      self.actions = ActionChains(driver)

      self.utilities = (By.XPATH, "//span[contains(text(),'Utilities')]")
      self.migration = (By.LINK_TEXT, "Migration")
      self.master_migration = (By.XPATH, "//a[span[normalize-space()='Master Migration']]")
      self.select_master = (By.XPATH, "//select[@name='selectedMaster']")
      # self.select_file = (By.XPATH, "//option[@value='Opening Stocks']")
      # self.select_file = (By.XPATH, "//option[@value='Product Master']")
      # self.select_file = (By.XPATH, "//option[@value='Product Update']")
      # self.select_file = (By.XPATH, "//option[@value='Customer Master']")
      self.select_file = (By.XPATH, "//option[@value='Vendor Master']")
      self.download_btn = (By.XPATH, "//button[normalize-space()='Download Sample Excel']")

   def generate_sheet(self):
      #Click on Utilities -> Migration -> Sheet Generation
      utilities = self.wait.until(
         EC.element_to_be_clickable(self.utilities)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", utilities)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", utilities)
      print("Utilities clicked successfully!")

      #Hover over Migration
      migration = self.wait.until(
         EC.presence_of_element_located(self.migration)
      )
      self.actions.move_to_element(migration).perform()
      time.sleep(1)
      migration.click()
      print("Migration hovered and clicked successfully!")

      #Click on Sheet Generation
      master_migration = self.wait.until(
         EC.presence_of_element_located(self.master_migration)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", master_migration)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", master_migration)
      print("Master Migration clicked successfully!")

   def open_sheet_generation(self):
      select_master = self.wait.until(
         EC.element_to_be_clickable(self.select_master)
      )
      select_master.click()
      time.sleep(2)
      print("Select master dropdown clicked successfully!")

      select_file = self.wait.until(
         EC.element_to_be_clickable(self.select_file)
      )
      select_file.click()
      print(f"File {select_file} selected successfully!")

      download_btn = self.wait.until(
         EC.element_to_be_clickable(self.download_btn)
      )
      download_btn.click()
      print("Download button clicked successfully!")
