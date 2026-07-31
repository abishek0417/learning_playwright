import allure
import pytest
from playwright.sync_api import Page,expect



@allure.title("handle alert")
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")

    input1=page.locator("#input1")
    input1.focus()
    page.keyboard.insert_text("welcome")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.wait_for_timeout(5000)
