import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Vat_Report.Materialized_View import MaterializedViewReportPage


# noinspection PyBroadException
@allure.title("Generate Materialized View Report in IMS Application")
@allure.description("Logs in, navigates to Materialized View Report, clicks RUN, and verifies the table.")
def test_materialized_view_report(driver):
    wait = WebDriverWait(driver, 30)
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Materialized View Report ---
        materialized_view_report = MaterializedViewReportPage(driver)
        materialized_view_report.generate_materialized_view_report()

        print("Materialized View Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Materialized_View_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as e:

        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Materialized_View_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )

        # Attach exception details
        allure.attach(
            str(e),
            name="Error Details",
            attachment_type=allure.attachment_type.TEXT
        )

        pytest.fail(f"Test failed due to: {e}")
