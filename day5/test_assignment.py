import allure
from playwright.sync_api import Page,expect

days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
@allure.title("verify the dropdown")
def test_dropdown(page:Page):
    page.goto("https://bstackdemo.com/")

    expect(page.locator(".sort")).to_be_visible()
    expect(page.locator(".sort")).to_be_enabled()

    page.locator("select").select_option(value="lowestprice")

    title=page.locator("//div[@class='shelf-item']//p[@class='shelf-item__title']")
    prices=page.locator("//div[@class='shelf-item']//div[@class='shelf-item__price']//div[1]")
    expect(title).to_have_count(25)

    title_list=[text.strip() for text in title.all_inner_texts()]
    price_list=[price.strip() for price in prices.all_inner_texts()]

    for i,j in zip(title_list,price_list):
        print(f"{i} - {j}")

    lis=list(zip(title_list,price_list))
    dic=dict(zip(title_list,price_list))

    print(lis)
    print(dic)


