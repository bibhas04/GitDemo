# Any pytest file should start with test_ or end with _test
# Python method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in out put, -v stands for more metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests with @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixture are used to setup and tear down methods for test cases- conftest file to generalize fixture and
# make it available to all test cases
# datadriver and parameterizaion can be done with return statements in tuple format
# when you define fixture to scope only, it will run once before class is initiated and at the end


import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo():
    print("I will execute steps in fixtureDemo method")


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"



