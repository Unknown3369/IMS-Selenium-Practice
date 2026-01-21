from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import keyboard
import time

class addCustomer:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 25)
      self.actions = ActionChains(self.driver)

      self.masters = (By.XPATH, "//span[contains(text(),'Masters')]")
      self.custom_info = (By.LINK_TEXT, "Customer & Vendor Info")
      self.customer_master_link = (By.XPATH, "//a[@title='Customer Master']//span[normalize-space()='Customer Master']")
      self.create_customer = (By.XPATH, "//button[@id='create' and normalize-space()='Create Customer']")
      self.customer_name = (By.XPATH, "//input[@id='customerName' and @placeholder='Enter Name']")
      self.address = (By.XPATH, "//input[@id='address' and @placeholder='Enter Address']")
      self.contact = (By.XPATH, "//input[@id='Mobile' and @placeholder='Mobile']")
      self.save_btn = (By.XPATH, "//button[@id='save' and text()='SAVE']")


   def open_add_customer(self):
      # Click on “Masters” menu
      masters = self.wait.until(
         EC.presence_of_element_located(self.masters)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", masters)
      time.sleep(1)
      self.driver.execute_script("arguments[0].click();", masters)
      print("Masters clicked successfully!")

      # Hover over "Inventory Info" before clicking
      custom_info = self.wait.until(
         EC.presence_of_element_located(self.custom_info)
      )
      self.actions.move_to_element(custom_info).perform()
      time.sleep(1)  

      custom_info.click()
      print("Inventory Info hovered and clicked successfully!")

   def add_customer(self, custom_name: str, custom_address: str, custom_contact: int):
      # Click on “Customer Master” link
      customer_master_link = self.wait.until(
         EC.presence_of_element_located(self.customer_master_link)
      )
      time.sleep(2)
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", customer_master_link)
      time.sleep(2)
      self.driver.execute_script("arguments[0].click();", customer_master_link)
      print("Customer Master clicked successfully!")
      time.sleep(5)


      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", customer_master_link)
      time.sleep(2)
      self.driver.execute_script("arguments[0].click();", customer_master_link)
      print("Customer Master clicked successfully!")
      time.sleep(5)

      # Click on "Create Customer" button
      create_customer = self.wait.until(
         EC.element_to_be_clickable(self.create_customer)
      )
      create_customer.click()
      print("Create Customer button clicked successfully!")

      # Add Customer Details
      # add customer name
      customer_name = self.wait.until(
         EC.presence_of_element_located(self.customer_name)
      )
      customer_name.send_keys(custom_name)
      print("Customer Name entered successfully!")

      # add customer address
      address = self.wait.until(
         EC.presence_of_element_located(self.address)
      )
      address.send_keys(custom_address)
      print("Address entered successfully!")

      # add customer contact
      contact = self.wait.until(
         EC.presence_of_element_located(self.contact)
      )
      contact.send_keys(custom_contact)
      print("Contact entered successfully!")

      save_btn = self.wait.until(
         EC.element_to_be_clickable(self.save_btn)
      )
      save_btn.click()
      print("Save button clicked successfully!")

      time.sleep(5)