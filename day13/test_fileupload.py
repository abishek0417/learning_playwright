import allure
import pytest
from playwright.sync_api import Page,expect



@allure.title("handle alert")
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    page.locator("#singleFileInput").set_input_files("/Users/ezio/PycharmProjects/pw_python/dummyfiles/test1.txt")
    page.get_by_text("Upload Single File").click()
    expect(page.locator("#singleFileStatus")).to_contain_text("test1")
    page.wait_for_timeout(5000)

def test_multiple_fileuplod(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/#")
    files=["dummyfiles/test1.txt","dummyfiles/test2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.get_by_text("Upload Multiple Files").click()
    #expect(page.locator("#singleFileStatus")).to_contain_text("test1")
    page.wait_for_timeout(5000)