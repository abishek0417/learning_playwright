import allure
from playwright.sync_api import Page,expect

@allure.title("verify the css id")
def test_css_id(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    l=page.locator("#name")
    l.fill("abishek")
    expect(l).to_have_value("abishek")
    page.wait_for_timeout(5000)

def test_countofLI(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    l = page.locator("//select[@id='country']/option").all_inner_texts()
    for i in l:
        print(i)

def test_countofinnertext(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    a=page.locator("[name='start']").inner_text()
    print(a)

def test_countofinnervalue(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    name=page.locator("#name")
    name.fill("abishek")
    print(name.input_value())
    expect(name).to_have_value(name.input_value())
