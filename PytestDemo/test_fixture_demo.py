import pytest

@pytest.yield_fixture()
def browser_config():
    print('Browser launched.')

    yield
    print('Browser closed.')


def test_login_test001(browser_config):
    print("Login Test case 1 passed.")


def test_login_test002(browser_config):
    print("Login Test case 2 passed.")


def test_login_test003(browser_config):
        print("Login Test case 3 passed.")
