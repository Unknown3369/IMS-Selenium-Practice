import pytest
import allure
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
   """
   Hook to automatically attach screenshots on test failure.
   Runs after each test phase.
   """
   outcome = yield
   report = outcome.get_result()
   print(f"Running hook for: {item.name}, status: {report.outcome}")
   if report.when == "call" and report.failed:
      driver = item.funcargs.get("driver")  # Access the fixture
      if driver:
         try:
            # Attach screenshot to Allure report
            allure.attach(
               driver.get_screenshot_as_png(),
               name=f"Screenshot_{item.name}",
               attachment_type=allure.attachment_type.PNG
            )
         except Exception as e:
            print(f"[Allure Screenshot Error] Could not attach screenshot: {e}")
