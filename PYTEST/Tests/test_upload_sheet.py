import pytest
from PYTEST.pages.Login import login
from PYTEST.pages.upload_sheet import UploadSheetPage
import time

def test_upload_sheet(driver):
   login_page = login(driver)
   upload_sheet_page = UploadSheetPage(driver)

   # Perform login
   login_page.perform_login("Testuser", "Test@1234")

   # Navigate to Upload Sheet
   upload_sheet_page.generate_sheet()
   upload_sheet_page.open_upload_sheet()
   time.sleep(20)
   print("Upload sheet process completed successfully!")