import os

import pytest
import subprocess
from main import report_summary_folder, html_summary_folder
from utils.help_function import get_file_direction


@pytest.fixture(scope="session")
def reruns(request):
    return request.config.getoption("--reruns 3")




