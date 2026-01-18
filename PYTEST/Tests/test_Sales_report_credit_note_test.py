import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Credit_Note_Book_Report import CreditNoteBookReportPage


# noinspection PyBroadException
@allure.title("Generate Credit Note Book Report in IMS Application")
@allure.description("Logs in, navigates to Reports → Sales Reports → Credit Note Book Report, selects customer, and generates the report with screenshots on success and failure.")
def test_generate_credit_note_book_report(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        credit_report_page = CreditNoteBookReportPage(driver)
        credit_report_page.generate_credit_note_book_report()
        print("Credit Note Book Report generated successfully.")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="Credit_Note_Book_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful Credit Note Book Report generation.")

    except Exception as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Credit_Note_Book_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Credit Note Book Report test failed due to: {e}")
