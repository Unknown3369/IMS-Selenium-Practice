import pytest
from PYTEST.pages.Login import login
from PYTEST.pages.sheet_generation import SheetGenerationPage
import time

def test_sheet_generation(driver):
   login_page = login(driver)
   sheet_generation_page = SheetGenerationPage(driver)

   # Perform login
   login_page.perform_login("Testuser", "Test@1234")

   # Navigate to Sheet Generation
   sheet_generation_page.generate_sheet()
   sheet_generation_page.open_sheet_generation()
   time.sleep(20)
   print("Sheet generation process completed successfully!")
