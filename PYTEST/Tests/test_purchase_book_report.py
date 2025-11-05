import pytest
from PYTEST.pages.Purchase_book_report import PurchaseBookReport
from PYTEST.pages.Login import login

def test_purchase_book_report(driver):
   login_page = login(driver)
   purchase_report = PurchaseBookReport(driver)

   login_page.perform_login("Testuser", "Test@1234")
   purchase_report.open_purchase_book_report()  # <-- run actual flow
