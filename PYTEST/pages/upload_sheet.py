import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

class UploadSheetPage:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 20)
      self.actions = ActionChains(driver)

      self.utilities = (By.XPATH, "//span[contains(text(),'Utilities')]")
      self.migration = (By.LINK_TEXT, "Migration")
      self.master_migration = (By.XPATH, "//a[span[normalize-space()='Master Migration']]")
      self.upload_sheet = (By.XPATH, "//a[@href='#upload-sheet' and normalize-space()='Upload Sheet']")
      self.select_master = (By.XPATH, "//select[@name='selectedMaster' and contains(@class,'form-control')]")
      self.choose_file = (By.XPATH, "//input[@type='file' and contains(@accept,'.xlsx')]")
      self.upload_btn = (By.XPATH, "//button[normalize-space()='Upload File']")

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
      time.sleep(2)

      rand_click = self.wait.until(
         EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'col-md-12') and contains(@style,'overflow-y: auto')]"))
      )
      rand_click.click()

      upload_sheet = self.wait.until(
         EC.presence_of_element_located(self.upload_sheet)
      )
      upload_sheet.click()
      print("Upload Sheet clicked successfully!")
      time.sleep(2)

   def open_upload_sheet(self):
      self.wait.until(
         EC.presence_of_element_located((By.TAG_NAME, "body"))
      )

      self.driver.execute_script("""
         const select = document.querySelector("select[name='selectedMaster']");
         if (!select) {
            throw new Error("Upload Sheet dropdown not found");
         }

         const option = Array.from(select.options)
         .find(o => o.text.trim() === "Vendor Master");

         if (!option) {
            throw new Error("Vendor Master option not found");
         }

         option.selected = true;

         select.dispatchEvent(new Event('input', { bubbles: true }));
         select.dispatchEvent(new Event('change', { bubbles: true }));
      """)

      print("Upload Sheet dropdown selected successfully")


      choose_path = self.wait.until(
         EC.presence_of_element_located(self.choose_file)
      )
      time.sleep(1)
      
      excel_path = r"C:\Users\tamra\OneDrive\Documents\GitHub\IMS-Selenium-Practice\Product Master Sample.xlsx"
      # excel_path = r"C:\Users\tamra\OneDrive\Documents\GitHub\IMS-Selenium-Practice\Vendor Master Sample.xlsx"
      
      choose_path.send_keys(excel_path)
      print("File path chosen successfully!")

      upload_btn = self.wait.until(
         EC.element_to_be_clickable(self.upload_btn)
      )
      upload_btn.click()
      print("Upload button clicked successfully!")