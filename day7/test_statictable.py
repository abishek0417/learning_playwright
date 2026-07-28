import allure
from playwright.sync_api import Page,expect

days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
@allure.title("verify the dropdown")
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    page.locator("#male").check()
    a=["Sunday","Monday"]
    for j in a:
        page.get_by_text(j)
    print("helo hi suma")
