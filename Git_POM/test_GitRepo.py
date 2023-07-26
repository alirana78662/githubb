from playwright.sync_api import Playwright
from Git_UI_TestCases.test_git_repo import GitRepo


def test_git_repo_ui(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    git = GitRepo(page)
    git.navigate()
    git.Add_Git_Repo_Ui()
    git.Del_Git_Repo_Ui()
