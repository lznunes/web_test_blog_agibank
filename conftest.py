import pytest
from utils.webdriver import get_driver

@pytest.fixture(scope="function")
def driver(request):
    driver_instance = get_driver()

    def teardown():
        driver_instance.quit()

    request.addfinalizer(teardown)
    return driver_instance
