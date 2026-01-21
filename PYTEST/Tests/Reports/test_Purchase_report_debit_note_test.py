import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Debit_Note_Book_Report import DebitNoteBookReportPage


# noinspection PyBroadException
@allure.title("Generate Debit Note Book Report in IMS Application")
@allure.description("Logs in, navigates to Reports → Purchase Reports → Debit Note Book Report, and generates the report with screenshots on success and failure.")
def test_generate_debit_note_book_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        debit_report_page = DebitNoteBookReportPage(driver)
        debit_report_page.generate_debit_note_book_report()
        print(" Debit Note Book Report generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Debit_Note_Book_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print(" Screenshot captured after successful Debit Note Book Report generation.")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Debit_Note_Book_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f" Debit Note Book Report test failed due to: {e}")
