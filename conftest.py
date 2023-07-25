import pytest
import subprocess
from main import report_summary_folder, html_summary_folder
from utils.help_function import get_file_direction


@pytest.fixture(scope="session")
def reruns(request):
    return request.config.getoption("--reruns 3")


def pytest_sessionfinish():
    result_dir = report_summary_folder
    report_dir = html_summary_folder
    generate_report(result_dir, report_dir)


def generate_report(result_dir, report_dir):
    file_direction = get_file_direction('allure')
    cmd = [file_direction, "generate", result_dir, "-o", report_dir, '--clean']
    subprocess.run(cmd, check=True)


