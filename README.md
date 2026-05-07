# Python-Pj-Template

Python プロジェクトのテンプレートです。

## 必要環境

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## インストール

```bash
# 依存パッケージのインストール
uv sync

# Playwright ブラウザのインストール（tasks/ を使う場合）
uv run playwright install chromium
```

## ディレクトリ構成

```
src/      # プロジェクト用ソースコード
tests/    # src/ に対するテスト
tasks/    # タスク用ソースコード(pytest 検出対象)
```

## テスト（tests/）

`tests/` 以下に `test_*.py` というファイルを作成し、`test_` で始まる関数を定義します。

```python
# tests/test_example.py
from src.example import some_func

def test_example() -> None:
    assert some_func() == "expected"
```

## タスク（tasks/）

> [!TIP]
> `tasks/` は `pyproject.toml` の `testpaths` および `.vscode/settings.json` の `pytestArgs` に指定されており、pytest の検出対象になっています。

`tasks/` 以下に `task_*.py` というファイルを作成し、`task_` で始まる関数を定義します。

```python
# tasks/task_example.py
from playwright.sync_api import Page

def task_example(page: Page, url: str) -> None:
    page.goto(url)
```

### タスクへの引数追加

`conftest.py` でカスタム引数を定義し、タスク関数のフィクスチャとして受け取ります。

```python
# conftest.py
import pytest

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--url", action="store", default="https://example.com", help="対象URL")

@pytest.fixture
def url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--url")
```

`--username`、`--password` など任意のオプションを同じ方法で追加できます。

## 環境変数

引数のデフォルト値は `.env` ファイルで管理できます。

```bash
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

## テスト/タスク実行

```bash
# すべてのテスト・タスクを実行
uv run pytest

# テストのみ実行
uv run pytest tests/

# タスクのみ実行
uv run pytest tasks/task_hello.py --headed --url https://google.com
```

## コード品質

[ruff](https://docs.astral.sh/ruff/) によるフォーマットと lint を導入しています。

```bash
uv run ruff check .           # lint チェック
uv run ruff check --fix .     # lint 自動修正
uv run ruff format .          # フォーマット
```
