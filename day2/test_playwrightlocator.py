import allure
from playwright.sync_api import Page,expect

@allure.title("verify the logo is visible")
def test_getbyalt(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logo=page.get_by_alt_text("company-branding")
    expect(logo).to_be_visible()

@allure.title("verify the text is visible")
def test_getbytext(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    expect(page.get_by_text("Data Entry Form")).to_be_visible()

@allure.title("verify the placeholder is visible")
def test_getbyplaceholder(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    expect(page.get_by_placeholder("Select an item")).to_be_visible()

@allure.title("verify the get by lable")
def test_getbylabel(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    l=page.get_by_label("Female")
    l.check()
    expect(l).to_be_checked()