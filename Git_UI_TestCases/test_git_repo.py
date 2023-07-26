import time


class GitRepo:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://github.com/")

    def login(self):
        self.page.locator("//a[contains(text(), 'Sign in')]").click()
        self.page.locator("//input[@id = 'login_field']").fill('alirana78662@gmail.com')
        self.page.locator("//input[@id = 'password']").click()
        self.page.locator("//input[@id = 'password']").fill('Mcc02151001@')
        self.page.locator("//input[@name = 'commit']").click()
        time.sleep(4)

    def Add_Git_Repo_Ui(self):
        self.page.locator("//span[@class = 'Button-content']").nth(3).click()
        self.page.locator("//input[@id = 'react-aria-2']").fill("GitAutomation")
        self.page.locator("//input[@id='react-aria-6']").click()
        self.page.locator("//input[@id = 'react-aria-8']").click()
        self.page.locator("//span[contains(text(), 'Create repository')]").click()
        time.sleep(5)

    def Del_Git_Repo_Ui(self):
        # self.page.get_by_role("link", name="alirana78662/GitAutomation").click()
        self.page.locator("//a[@id='settings-tab']").click()
        self.page.locator("//span[contains(text(), 'Delete this repository')]").click()
        self.page.locator("//span[contains(text(), 'I want to delete this repository')]").click()
        self.page.locator("//span[contains(text(), 'I have read and understand these effects')]").click()
        self.page.locator("//input[@id = 'verification_field']").fill("alirana78662/GitAutomation")
        # self.page.locator("//span[contains(text(), 'Delete this repository')]").nth(1).click()
        self.page.locator("//span[@class = 'Button-label']").nth(8).click()

        time.sleep(4)
