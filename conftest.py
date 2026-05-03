import os

import pytest
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--url", action="store", default=os.getenv("URL", "https://example.com"), help="対象URL")


@pytest.fixture
def url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--url")
