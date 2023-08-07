import pytest


@pytest.fixture(scope="session")
def reruns(request):
    return request.config.getoption("--reruns 5")




