from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class addVendor:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(self.driver)

      self.masters = (By.XPATH, "//span[contains(text(),'Masters')]")
      self.custom_info = (By.LINK_TEXT, "Customer & Vendor Info")
      self.vendor_master_link = (By.XPATH, "//a[@title='Vendor Master']//span[normalize-space()='Vendor Master']")
      self.create_vendor = (By.XPATH, "//button[@id='create' and normalize-space()='Create Vendor']")
      self.vendor_name = (By.XPATH, "//input[@id='vendorName']")
      self.address = (By.XPATH, "//input[@id='address']")
      self.vat_no = (By.XPATH, "//input[@id='vatNo']")
      self.email = (By.XPATH, "//input[@id='email']")
      self.mobile = (By.XPATH, "//input[@id='Mobile']")
      self.save_btn = (By.XPATH, "//button[@id='save' and text()='SAVE']")

   def open_add_vendor(self):
      # Click on “Masters” menu
      masters = self.wait.until(
         EC.presence_of_element_located(self.masters)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", masters)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", masters)
      print("Masters clicked successfully!")

      # Hover over "Customer & Vendor Info" before clicking
      custom_info = self.wait.until(
         EC.presence_of_element_located(self.custom_info)
      )
      self.actions.move_to_element(custom_info).perform()
      time.sleep(1)  

      custom_info.click()
      print("Info hovered and clicked successfully!")

   def add_vendor(self, vendor_name: str, vendor_address: str, vendor_vat_no: str, vendor_email: str, vendor_mobile: int):
      # Click on “Vendor Master” link
      vendor_master_link = self.wait.until(
         EC.presence_of_element_located(self.vendor_master_link)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vendor_master_link)
      time.sleep(2)
      self.driver.execute_script("arguments[0].click();", vendor_master_link)
      print("Vendor Master clicked successfully!")
      time.sleep(5)

      # Click on "Create Vendor" button
      create_vendor = self.wait.until(
         EC.element_to_be_clickable(self.create_vendor)
      )
      create_vendor.click()
      print("Create Vendor button clicked successfully!")

      # Fill Vendor Details
      self.wait.until(EC.presence_of_element_located(self.vendor_name)).send_keys(vendor_name)
      print("Vendor name entered successfully!")
      self.driver.find_element(*self.address).send_keys(vendor_address)
      print("Vendor address entered successfully!")
      self.driver.find_element(*self.vat_no).send_keys(vendor_vat_no)
      print("Vendor VAT No entered successfully!")
      self.driver.find_element(*self.email).send_keys(vendor_email)
      print("Vendor email entered successfully!")
      self.driver.find_element(*self.mobile).send_keys(vendor_mobile)
      print("Vendor mobile entered successfully!")

      # Click Save
      save_btn = self.wait.until(
         EC.element_to_be_clickable(self.save_btn)
      )
      save_btn.click()
      print("Save button clicked successfully!")