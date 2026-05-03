# browser-task-automation

pytest をタスクランナーとして Playwright を動かす自動化プロジェクトです。

## 必要環境

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## インストール

```bash
# 依存パッケージのインストール
uv sync

# Playwright ブラウザのインストール
uv run playwright install chromium
```

## タスクの作成

`src/` 以下に `task_*.py` という名前でファイルを作成し、`task_` で始まる関数を定義します。

```python
# src/task_example.py
from playwright.sync_api import Page

def task_example(page: Page) -> None:
    page.goto("https://example.com")
```

複数セッションが必要な場合（例: ユーザーA・BのチャットなどD）は `Browser` フィクスチャを使います。

```python
# src/task_chat.py
from playwright.sync_api import Browser

def task_chat(browser: Browser) -> None:
    context_a = browser.new_context()
    context_b = browser.new_context()

    page_a = context_a.new_page()
    page_b = context_b.new_page()

    # それぞれ独立したセッションで操作
    ...

    context_a.close()
    context_b.close()
```

## 引数の定義

`src/conftest.py` でカスタム引数を定義し、タスク関数のフィクスチャとして受け取ります。

```python
# src/conftest.py
import pytest

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--url", action="store", default="https://example.com", help="対象URL")

@pytest.fixture
def url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--url")
```

```python
# src/task_example.py
from playwright.sync_api import Page

def task_example(page: Page, url: str) -> None:
    page.goto(url)
```

引数は `--username`、`--password` など任意のオプションを同じ方法で追加できます。

## 環境変数

引数のデフォルト値は `.env` ファイルで管理できます。

```bash
# .env.example をコピーして作成
cp .env.example .env
```

```ini
# .env
URL=https://example.com
```

`.env` は `.gitignore` 済みです。値の優先順位は以下の通りです。

```
コマンドライン引数 > .env の値 > コード内のデフォルト値
```

## 実行

```bash
# すべてのタスクを実行（headless）
uv run pytest

# ブラウザを表示して実行（headed）
uv run pytest --headed

# 特定のタスクファイルのみ実行
uv run pytest src/task_hello.py --headed

# 引数を指定して実行
uv run pytest src/task_hello.py --headed --url https://google.com
```
