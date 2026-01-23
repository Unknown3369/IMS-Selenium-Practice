from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SalesBookReportPage:
   def __init__(self, driver):
      self.driver = driver
      self.wait = WebDriverWait(self.driver, 15)
      self.action = ActionChains(self.driver)

      self.reports = (By.XPATH, "//span[contains(text(),'Reports')]")
      self.sales_report = (By.LINK_TEXT, "Sales Report")
      self.sales_book_report = (By.XPATH, "//span[normalize-space()='Sales Book Report']")
      self.branch_dropdown = (By.XPATH, "//select[contains(@class, 'form-control') and contains(@class, 'selectText')]")
      self.user_dropdown = (By.XPATH, "//input[@type='checkbox' and @value='0']")
      self.select_customer = (By.XPATH, "//input[@type='text' and @placeholder='Press Enter or Tab for Account List']")
      self.search_customer = (By.XPATH, "//input[@placeholder='Enter keyword to search']")
      self.select_customer_list = (By.XPATH, "//div[normalize-space(text())='Cash Customer']")
      self.run_button = (By.XPATH, "//button[normalize-space(text())='RUN']")

   def open_sales_book_report(self):
      # Click on “Reports” menu
      reports = self.wait.until(
         EC.presence_of_element_located(self.reports)
      )
      self.driver.execute_script("arguments[0].scrollIntoView(true);", reports)
      self.driver.execute_script("arguments[0].click();", reports)
      print("Reports clicked successfully!")

      # Hover over "Sales Report" before clicking
      sales_report = self.wait.until(
         EC.presence_of_element_located(self.sales_report)
      )
      ActionChains(self.driver).move_to_element(sales_report).perform()

      # Click after hovering
      sales_report.click()
      print("Sales Report hovered and clicked successfully!")

      # Click on “Sales Book Report” link
      sales_book_report = self.wait.until(
         EC.presence_of_element_located(self.sales_book_report)
      )
      self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sales_book_report)
      self.driver.execute_script("arguments[0].click();", sales_book_report)
      print("Sales Book Report clicked successfully!")

   def run_sales_book_report(self):
      #Branch Selection
      branch_dropdown = self.wait.until(
         EC.presence_of_element_located(self.branch_dropdown)
      )
      branch_dropdown.click()
      select_branch = Select(branch_dropdown)
      select_branch.select_by_visible_text("ALL")
      print("Branch selected successfully!")

      #Select All user
      user_dropdown = self.wait.until(
         EC.presence_of_element_located(self.user_dropdown)
      )
      user_dropdown.click()
      print("All users selected successfully!")

      #Customer Selection
      select_customer = self.wait.until(
         EC.presence_of_element_located(self.select_customer)
      )
      select_customer.send_keys(Keys.ENTER)

      search_customer = self.wait.until(
         EC.presence_of_element_located(self.search_customer)
      )
      search_customer.send_keys("cash")
      print("'Cash Customer' searched successfully!")

      select_customer_list = self.wait.until(
         EC.presence_of_element_located(self.select_customer_list)
      )
      select_customer_click = ActionChains(self.driver)
      select_customer_click.double_click(select_customer_list).perform()
      print("Customer selected successfully!")

      # Click on the "Run" button
      run_button = self.wait.until(
         EC.element_to_be_clickable(self.run_button)
      )
      run_button.click()
      print("Run button clicked successfully!") 