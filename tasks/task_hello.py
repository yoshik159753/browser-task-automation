from playwright.sync_api import Page


def task_hello(page: Page, url: str) -> None:
    page.goto(url)
    print(f"タイトル: {page.title()}")
