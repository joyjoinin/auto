import pytest


@pytest.fixture(scope="session")
def reruns(request):
    return request.config.getoption("--reruns 3")


def pytest_addoption(parser):
    parser.addoption("--num-parallel", action="store", default=10, help="Number of parallel test processes")


@pytest.fixture(scope="session")
def num_parallel(request):
    return int(request.config.getoption("--num-parallel"))
