import random
import string

from data.params import Account


def save_data(email, password, add_payment=False):
    with open('../../data/created_accounts.txt', 'a') as output_file:
        output_file.write("email: {}, password: {}, add_payment: {} \n".format(email, password, add_payment))
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