# Enhanced Login Page Object (`login.py`)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import time


class login:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 35)
      self.username = (By.XPATH, "//input[@placeholder='Username']")
      self.password = (By.XPATH, "//input[@placeholder='Password']")
      self.login_button = (By.XPATH, "//button[contains(text(), 'Login')]")
      self.logout_button = (By.XPATH,"//button[contains(@class,'mat-flat-button') and .//span[normalize-space()='Sign out']]")
      self.error_message = (By.XPATH,"//p[normalize-space()='Invalid Username or Password']")
      self.ok_button = (By.XPATH,"/html/body/app/alert/div/div/div/div[3]/button")
      self.dashboard_element = (By.XPATH,"//*[contains(text(),'Dashboard') or contains(text(),'Transactions')]")
      self.profile_menu = (By.XPATH, "//*[name()='svg' and @data-icon='caret-down']")
      self.main_logout = (By.XPATH,"//a[@title='log out']")

   # Open Login Page
   def open_login_page(self):
      self.driver.get("http://stc21.webredirect.himshang.com.np")

   # Enter Username
   def enter_username(self, username: str):
      username_box = self.wait.until(
            EC.presence_of_element_located(self.username)
      )
      username_box.clear()
      username_box.send_keys(username)

   # Enter Password
   def enter_password(self, password: str):
      password_box = self.wait.until(
            EC.presence_of_element_located(self.password)
      )
      password_box.clear()
      password_box.send_keys(password)

   # Click Login
   def click_login(self):
      login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
      )
      login_button.click()
      print("Login button clicked!")

   # Complete Login Flow
   def perform_login(self, username: str, password: str):
      self.open_login_page()

      self.enter_username(username)
      self.enter_password(password)
      self.click_login()

      # Handle already logged in popup
      try:
         popup_logout_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.logout_button)
         )
         popup_logout_button.click()
         print("Detected previous session popup and clicked Logout.")
         time.sleep(5)
         login_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.login_button)
         )
         login_button.click()
         print("Login button re-clicked!")

      except TimeoutException:
            print("No previous session popup detected.")

   def invalid_login(self):
      try:
         ok_button = self.wait.until(
            EC.element_to_be_clickable(self.ok_button)
         )
         ok_button.click()
         print("Clicked OK on error popup.")
      except TimeoutException:
         return ""

   # Verify Successful Login
   def verify_login_success(self):
      try:
         self.wait.until(
            EC.visibility_of_element_located(self.dashboard_element)
         )
         return True
      except TimeoutException:
         return False

   # Get Error Message
   def get_error_message(self):
      try:
         error = self.wait.until(
            EC.visibility_of_element_located(self.error_message)
         )
         return error.text
      except TimeoutException:
         return ""
      
   #Account Lockout Detection
   def is_account_locked(self):
      try:
         error = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Exceeded 5 failed attempts. Account locked for 5 mins']"))
         )
         return True
      except TimeoutException:
         return False

   # Check Password Masking
   def get_password_field_type(self):
      password_box = self.wait.until(
         EC.presence_of_element_located(self.password)
      )
      return password_box.get_attribute("type")

# Logout
   def logout(self):
      profile_menu = self.wait.until(
         EC.visibility_of_element_located(self.profile_menu)
      )

      ActionChains(self.driver).move_to_element(profile_menu).perform()
      time.sleep(1)
      
      logout_btn = self.wait.until(
            EC.element_to_be_clickable(self.main_logout)
      )
      logout_btn.click()
      print("Logout successful!")
