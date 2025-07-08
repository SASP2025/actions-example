import random
import pytest
import sys
import example_source

# These need to be flushed out more but are a decent start

def test_nothin():
    assert example_source.does_nothing()

# Test expected failure
@pytest.mark.xfail
def test_xpass():
    assert 0.0 > random.random()


# Test parameterized tests runs
@pytest.mark.parametrize(
    "name, expected",
    [
        ("Rudolph the reindeer", "Hello Rudolph the reindeer!"),
        ("Bozo", "Hello Bozo!"),
    ],
)
def test_passed(name, expected):
    assert f"Hello {name}!" == expected


# Test that fixures return error
@pytest.mark.xfail(reason="This test is expected to fail due to an error")
def test_div_zero(div_zero):
    with pytest.raises(ZeroDivisionError, match="Zero Division Not Good"):
        pass
        


def test_expected_error():
    """Test that a failed test yields the expected tag in allure
    and raises an expected failure 
                            
    you can use the following to show no raise:
    from contextlib import nullcontext as does_not_raise
    does_not_raise()        
    """                 
    with pytest.raises(ZeroDivisionError):
        _ = 1/0    


# Test skip mark
@pytest.mark.skip(reason="this test should be skipped")
def test_skipped():
    assert true


@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls:
    def test_function(self):
        "will not be setup or run under 'win32' platform"


@pytest.mark.skipif("sys.version_info >= (3, 11)")
def test_only_on_311minus():
    """ only run this test if the python version is below 3.11

    Something like this can be used to create tests that run 
    only for specific versions of the installed package
    which we can create different testing environments for as needed
    """
    x = 3
    assert f"{x = }" == "x = 3"

