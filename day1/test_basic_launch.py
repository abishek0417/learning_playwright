import allure
from playwright.sync_api import Page,expect

@allure.title("Verify Home Page URL")
def test_verify_url(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    expect(page).to_have_url("https://testautomationpractice.blogspot.com/#" )

@allure.title("Verify title of the page")
def test_verify_title(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    expect(page).to_have_title("Automation Testing Practice")
