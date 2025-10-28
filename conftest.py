import pytest
from selenium import webdriver

@pytest.fixture
def driver():
   # Setup
   driver = webdriver.Edge()
   driver.maximize_window()
   driver.implicitly_wait(10)
   yield driver
   # Teardown
   driver.quit()
