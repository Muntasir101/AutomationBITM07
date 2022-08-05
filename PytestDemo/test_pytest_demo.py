import pytest

@pytest.mark.order(1)
def test_login():
    print("Login Test passed")

@pytest.mark.order(3)
def test_home():
    print('Home test passed')

@pytest.mark.order(2)
def test_dashboard():
    print('dashboard test passed')

@pytest.mark.order(4)
def test_logout():
    print("Logout Passed")


    