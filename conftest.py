import pytest

from library_api import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    return app
