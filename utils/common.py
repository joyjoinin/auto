import random
import string
import subprocess
from data.params import Account
class LocatorInfo:
    def __init__(self, by_type=None, locator=None):
        self.type = by_type
        self.locator = locator


def save_data(email, password, add_payment=False):
    with open('../../data/created_accounts.txt', 'a') as output_file:
        output_file.write("\n email: {}, password: {}, add_payment: {} \n".format(email, password, add_payment))
    output_file.close()


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


def get_random_username():
    random_string = ''
    for i in range(15):
        random_string = generate_random_string(15)
    return random_string


def generate_random_text(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choices(characters + " ", k=length))
    return random_string


def get_random_text():
    random_string = ''
    for i in range(50):
        random_string = generate_random_text(50)
    return random_string


def get_expected_interests(a, b):
    new_list = a
    for item in b:
        if item not in new_list:
            new_list.append(item)
        else:
            new_list.remove(item)

    return new_list


def get_new_account():
    new_account = Account(email=generate_random_string(12) + '@fanatics.live',
                          password='Joytest159753?',
                          username=get_random_username())
    return new_account


def get_file_direction(name):
    result = subprocess.run(['which', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return result.stdout.decode('utf-8').strip()
    else:
        return f"can't find {name}"


def kill_appium():
    output = subprocess.check_output(['ps', 'ax']).decode('utf-8')
    for line in output.splitlines():
        if 'appium' in line:
            pid = line.split()[0]
            name = line.split()[-1]
            print(f'find process：PID={pid}，name={name}')
            subprocess.call(['kill', pid])
            print(f'process {name} is killed')

    if 'appium' not in output:
        print('no running Appium process')


def get_image_path():
    import os
    script_dir = os.path.dirname(os.path.realpath(__file__))
    new_path = script_dir.replace('utils', 'img.png')
    print(new_path)
    return new_path
