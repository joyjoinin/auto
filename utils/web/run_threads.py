import threading
import pytest


def create_pa():
    pytest.main(['./testcase/web/create_pick_auction.py', '--capture=sys', '-q'])


def create_ps():
    pytest.main(['./testcase/web/create_pick_set_price.py', '--capture=sys', '-q'])


def create_ra():
    pytest.main(['./testcase/web/create_random_auction.py', '--capture=sys', '-q'])


def create_rs():
    pytest.main(['./testcase/web/create_random_set_price.py', '--capture=sys', '-q'])


def threads_flow():
    threads = [
        threading.Thread(target=create_pa),
        threading.Thread(target=create_ps),
        threading.Thread(target=create_ra),
        threading.Thread(target=create_rs)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def run_threads_flow():
    thread = threading.Thread(target=threads_flow)
    thread.start()
