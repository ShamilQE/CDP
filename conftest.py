import pytest


@pytest.fixture
def copart(py):
    py.visit('https://copart.com')
    return py


