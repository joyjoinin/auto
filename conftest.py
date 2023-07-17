import pytest
import subprocess
import os

from main import report_summary_folder, html_summary_folder


@pytest.fixture(scope="session")
def reruns(request):
    return request.config.getoption("--reruns 3")


def pytest_sessionfinish():
    result_dir = report_summary_folder
    report_dir = html_summary_folder
    generate_report(result_dir, report_dir)


def generate_report(result_dir,report_dir):
    cmd = ["/usr/local/bin/allure", "generate", result_dir, "-o", report_dir,'--clean']
    subprocess.run(cmd, check=True)
