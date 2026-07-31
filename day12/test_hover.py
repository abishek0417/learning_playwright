import allure
import pytest
from playwright.sync_api import Page,expect



@allure.title("handle alert")
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    page.get_by_text("Point Me").hover()
    page.wait_for_timeout(2000)
    product=page.locator("div[class='dropdown-content'] a").nth(1)
    #product.click(button="right")#this is right click
    product.click()
    expect(product).to_have_text("Laptops")
    print(product.inner_text())

def test_doubleclick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    page.get_by_text("Copy Text").dblclick()
    page.wait_for_timeout(2000)

def test_drag_and_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    source=page.locator("#draggable")
    target=page.locator("#droppable")
    source.drag_to(target)



