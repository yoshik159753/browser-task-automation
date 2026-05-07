from playwright.sync_api import Browser


def task_chat_sample(browser: Browser) -> None:
    context_a = browser.new_context()
    context_b = browser.new_context()

    page_a = context_a.new_page()
    page_b = context_b.new_page()

    # ユーザーA・Bそれぞれで同じページを開く
    page_a.goto("https://example.com")
    page_b.goto("https://example.com")

    title_a = page_a.title()
    title_b = page_b.title()

    print(f"ユーザーA: {title_a}")
    print(f"ユーザーB: {title_b}")

    assert title_a == title_b == "Example Domain"

    context_a.close()
    context_b.close()
