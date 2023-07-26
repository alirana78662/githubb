# import time
#
# from playwright.sync_api import Playwright, sync_playwright
#
#
# def test_login_2(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context(storage_state="state.json")
#     page = context.new_page()
#     page.goto("https://github.com/")
#     time.sleep(5)
#
#
#
#
