import pytest

# This fixture should return a ZeroDivision error
@pytest.fixture
def div_zero():
    raise ZeroDivisionError("Zero Division Not Good")
