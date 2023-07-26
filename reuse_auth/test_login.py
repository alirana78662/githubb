# import time
#
# from playwright.sync_api import Playwright, sync_playwright
#
#
# def test_login(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://github.com/")
#     page.locator("//a[contains(text(), 'Sign in')]").click()
#     page.locator("//input[@id = 'login_field']").fill('alirana78662@gmail.com')
#     page.locator("//input[@id = 'password']").click()
#     page.locator("//input[@id = 'password']").fill('Mcc02151001@')
#     page.locator("//input[@name = 'commit']").click()
#     time.sleep(4)
#
#     # Save storage state into the file.
#     context.storage_state(path="state.json")
#
#
