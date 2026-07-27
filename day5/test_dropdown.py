import allure
from playwright.sync_api import Page,expect

days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
@allure.title("verify the dropdown")
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    a=page.locator("#country")
    a.select_option("India")
    print(a.input_value())

    b=page.locator("#country")
    b.select_option("germany")
    print(b.input_value())

    c=page.locator("#country")
    c.select_option(index=5)
    print(c.input_value())


    d=page.locator("#country>option")
    expect(d).to_have_count(10)

    countrys=[text.strip() for text in d.all_inner_texts()]
    for i in countrys:
        print(i)