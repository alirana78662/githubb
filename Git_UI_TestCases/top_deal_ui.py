import time

from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Top Deals").click()
    page1 = page1_info.value
    page1.get_by_label("Page size:").select_option("10")
    page1.get_by_role("cell", name="Strawberry").click()
    page1.get_by_label("Search:").click()
    page1.get_by_label("Search:").fill("str")
    page1.get_by_role("cell", name="23").click()
    page1.get_by_role("cell", name="15").click()
    page1.get_by_role("cell", name="Strawberry").click()

    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
