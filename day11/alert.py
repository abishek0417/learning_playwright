import allure
import pytest
from playwright.sync_api import Page,expect



@allure.title("handle alert")
@pytest.mark.skip
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")

    def handledialog(dialog):
        dialog.accept()

    page.on("dialog", handledialog)
    page.wait_for_timeout(2000)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_handle_dialogbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")

    #page.on("dialog", lambda dialog:dialog.dismiss())
    page.on("dialog", lambda dialog: dialog.accept())
    page.wait_for_timeout(2000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)
    a=page.locator("#demo").inner_text()
    print(f"action text ==> {a}")
    expect(page.locator("#demo")).to_have_text(a)

def test_promt_dialogbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")

    #page.on("dialog", lambda dialog:dialog.dismiss())
    page.on("dialog", lambda dialog: dialog.accept("abishek"))
    page.wait_for_timeout(2000)
    page.locator("#promptBtn").click()
    page.wait_for_timeout(2000)
    a=page.locator("#demo").inner_text()
    print(f"action text ==> {a}")
    expect(page.locator("#demo")).to_have_text(a)

