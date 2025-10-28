from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class login:
   def __init__(self, driver: webdriver):
      self.driver = driver
      self.wait = WebDriverWait(driver, 35)
      self.username = (By.XPATH, "//input[@placeholder='Username']")
      self.password = (By.XPATH, "//input[@placeholder='Password']")
      self.login_button = (By.XPATH, "//button[contains(text(), 'Sign In')]")
      self.logout_button = (By.XPATH, "//button[.//span[text()='Logout']]")
   def perform_login(self, username: str, password: str):
      # Open the login page
      self.driver.get("https://redmiims.webredirect.himshang.com.np/#/login")
      # Enter username
      username_box = self.wait.until(
         EC.presence_of_element_located(self.username)
      )
      username_box.clear()
      username_box.send_keys(username)
      # Enter password
      password_box = self.wait.until(
         EC.presence_of_element_located(self.password)
      )
      password_box.clear()
      password_box.send_keys(password)
      # Click on Sign In button
      login_button = self.wait.until(
         EC.element_to_be_clickable(self.login_button)
      )
      login_button.click()
      print("Login button clicked!")
      # Handle 'already logged in' popup
      try:
         popup_logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.logout_button)
         )
         popup_logout_button.click()
         print("Detected previous session popup and clicked Logout.")
         time.sleep(12)
         # Click on Sign In button
         login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.login_button)
         )
         login_button.click()
         print("Login button re clicked!")
      except:
            print("No previous session popup detected.")
   
   def verify_login(self, driver: webdriver):
      current_url = driver.current_url

      expected_url = "https://redmiims.webredirect.himshang.com.np/#/pages/dashboard"

      if current_url == expected_url:
         print ("Test Sucessfull")
      else:
         print ("Test Failed")