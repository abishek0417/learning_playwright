import allure
import pytest
from playwright.sync_api import Page,expect
import os



@allure.title("handle alert")
def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.on("download",lambda download:download.save_as("download/testfile.txt"))
    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()
    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(5000)
    if os.path.exists("download/testfile.txt"):
        print("file exist")
    else:
        print("not exist")

