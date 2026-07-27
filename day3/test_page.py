import allure
from playwright.sync_api import Page,expect

@allure.title("verify the css id")
def test_go_back(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    l=page.get_by_text("Udemy Courses")
    l.click()
    page.wait_for_timeout(5000)
    page.go_back()
    page.wait_for_timeout(2000)
    print(page.title())
