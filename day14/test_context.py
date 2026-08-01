import allure
import pytest
from playwright.sync_api import Playwright,expect

@pytest.mark.skip
@allure.title("handle alert")
def test_context(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parent=context.new_page()
    parent.goto("https://testautomationpractice.blogspot.com/#")
    parent.on("popup",lambda popup:popup.wait_for_load_state())
    parent.get_by_text("New Tab").click()
    parent.wait_for_timeout(3000)

    allpages=context.pages
    title=allpages[1].title()

    print(title)

@pytest.mark.skip
def test_tab(playwright:Playwright):  #handle multiple tabs
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parent=context.new_page()
    parent.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    parent.on("page",lambda page:page.wait_for_load_state())
    parent.get_by_text("OrangeHRM, Inc").click()

    allcontext=context.pages
    print(len(allcontext))
    allcontext[0].get_by_placeholder("Username").fill("Admin")
    allcontext[0].get_by_placeholder("Password").fill("admin123")
    #allcontext[0].get_by_text(" Login ").click()

    allcontext[0].wait_for_timeout(5000)

    title=allcontext[1].title()

    print(title)
    allcontext[1].wait_for_timeout(5000)


def test_multiplecontext(playwright:Playwright):  #handle context
    browser=playwright.chromium.launch(headless=False)
    admin=browser.new_context()
    employee = browser.new_context()

    page1=admin.new_page()
    page2=employee.new_page()

    page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page1.get_by_placeholder("Username").fill("Admin")
    page1.get_by_placeholder("Password").fill("admin123")
    page1.wait_for_timeout(3000)
    page2.goto("https://testautomationpractice.blogspot.com/#")
    page2.locator("#name").fill("abishek")
    page2.locator("#email").fill("sheka")
    page2.wait_for_timeout(3000)