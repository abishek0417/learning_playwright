import allure
import pytest
from playwright.sync_api import Page,expect



@allure.title("handle alert")
def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame1=page.frame_locator("//frame[@src='frame_1.html']")
    frame1.locator("input[name='mytext1']").fill("abishek")

    frame2=page.frame(url="https://ui.vision/demo/webtest/frames/frame_2")
    frame2.locator("input[name='mytext2']").fill("narayanan")
    page.wait_for_timeout(2000)
    
    frame3=page.frame_locator("frame[src='frame_3.html']")
    frame3.locator("input[name='mytext3']").fill("frame3")
    page.wait_for_timeout(2000)


    frame31 = frame3.frame_locator("iframe")

    radio=frame31.get_by_label("I am a human")
    radio.click()
    page.wait_for_timeout(2000)

    frame5 = page.frame_locator("frame[src='frame_5.html']")
    frame5.locator("input[name='mytext5']").fill("i am in frame5")
    page.wait_for_timeout(2000)
    frame5.get_by_text("https://a9t9.com").click()
    page.wait_for_timeout(2000)


