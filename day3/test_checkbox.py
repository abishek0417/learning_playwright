import allure
from playwright.sync_api import Page,expect

days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
@allure.title("verify the css id")
def test_checkox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")

    checkboxs=[page.get_by_label(day) for day in days]
    for i in checkboxs:
        i.check()
        expect(i).to_be_checked()

    page.wait_for_timeout(5000)

    for checkbox in checkboxs[-3:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
    page.wait_for_timeout(5000)

    for checkbox in checkboxs:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)



