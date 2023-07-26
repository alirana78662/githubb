import os

from playwright.sync_api import Playwright
from Git_UI_TestCases.test_git_repo import GitRepo


def test_git_repo_ui(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    file_name = "state.json"
    file_path = os.path.abspath(file_name)
    context = browser.new_context(storage_state=file_path)
    page = context.new_page()
    git = GitRepo(page)
    git.navigate()
    git.Add_Git_Repo_Ui()
    git.Del_Git_Repo_Ui()
