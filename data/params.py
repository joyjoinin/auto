import random
class TestAccount:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password


class Address:
    def __init__(self, firstname=None, lastname=None, address=None, apartment=None, code=None, city=None, state=None,
                 phone=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.apartment = apartment
        self.code = code
        self.city = city
        self.state = state
        self.phone = phone


class Card:

    def __init__(self, card=None, date=None, cvc=None, country='United States', zip_number=None):
        self.card = card
        self.date = date
        self.cvc = cvc
        self.country = country
        self.zip_number = zip_number


class Account:
    def __init__(self,
                 email=None,
                 password=None,
                 username=None,
                 access_code='test',
                 logo_name='NFL',
                 follow_count=1,
                 level_index=1):

        self.email = email
        self.password = password
        self.username = username
        self.logo_name = logo_name
        self.access_code = access_code
        self.follow_count = follow_count
        self.level_index = level_index

address_info = Address('Joy', 'test', '11061 Wilshire Blvd', '', '90025', 'LA', 'CA')

card_info = Card('4242424242424242', '0130', '111', 'United States','11111')

app_name = 'live.57blocks.fanatics.FanaticsLive-Development'

test_account = TestAccount('joy009@fanatics.live', 'Joytest159753?')

test_creat_account = TestAccount('joy101@fanatics.live', 'Joytest159753?')

level_params = ["I'm a Rookie", "I'm a Collector", "I'm a Seasoned Pro"]

new_account = Account(email='joy' + str(random.randint(200,10000)) + '@fanatics.live',
                      password='Joytest159753?',
                      username='joy' + str(random.randint(200,10000)))
