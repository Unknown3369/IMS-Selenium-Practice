import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from PYTEST.pages.Login import login
from PYTEST.pages.Reports.Membership_Point_Report import MembershipPointReportPage


# noinspection PyBroadException
@allure.title("Generate Membership Point Report in IMS Application")
@allure.description(
    "Logs in, navigates to Reports → Loyalty & Promotion Report → Membership Point Report, "
    "selects Member, selects Detail Report option, clicks RUN, and verifies the table."
)
def test_generate_membership_point_report(driver):
    login_page = login(driver)

    try:
        login_page.perform_login("Testuser", "Test@1234")
        print("Logged into IMS")

        # --- Step 2: Generate Membership Point Report ---
        mem_point_page = MembershipPointReportPage(driver)
        mem_point_page.generate_membership_point_report()

        print("Membership Point Report generated successfully.")

        # Screenshot on success
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Membership_Point_Report_Success",
            attachment_type=allure.attachment_type.PNG
        )
        print("Screenshot captured after successful report generation.")

    except Exception as e:
        # Screenshot on failure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Membership_Point_Report_Error",
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            str(e),
            name="Error_Details",
            attachment_type=allure.attachment_type.TEXT
        )
        pytest.fail(f"Membership Point Report test failed due to: {e}")
