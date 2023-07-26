from playwright.sync_api import Playwright
from Git_UI_TestCases.test_git_repo import GitRepo


def test_git_repo_ui(page: Playwright) -> None:
    browser = page.chromium.launch()
    page = browser.new_page()
    git = GitRepo(page)
    git.navigate()
    git.login()
    # git.Add_Git_Repo_Ui()
    # git.Del_Git_Repo_Ui()
