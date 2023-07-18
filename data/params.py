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
                 weak_password='joytest',
                 fair_password='Joytest1',
                 good_password='Joytest159',
                 username=None,
                 invalid_name='?test',
                 already_took_username='joy001',
                 access_code='test',
                 logo_select= random.randint(1,12),
                 follow_count=1,
                 level_index=random.randint(1,3)):
        self.email = email
        self.password = password
        self.weak_password = weak_password
        self.fair_password = fair_password
        self.good_password = good_password
        self.username = username
        self.invalid_name = invalid_name
        self.already_took_username = already_took_username
        self.logo_select = logo_select
        self.access_code = access_code
        self.follow_count = follow_count
        self.level_index = level_index


address_info = Address('Joy', 'test', '11061 Wilshire Blvd', '', '90025', 'LA', 'CA')

card_info = Card('4242424242424242', '0130', '111', 'United States', '11111')

app_name = 'live.57blocks.fanatics.FanaticsLive-Development'

test_account = TestAccount('joy999@fanatics.live', 'Joytest159753?')

level_params = ["I'm a Rookie", "I'm a Collector", "I'm a Seasoned Pro"]

new_account = Account(email='joy' + str(random.randint(200, 10000)) + '@fanatics.live',
                      password='Joytest159753?',
                      username='joy' + str(random.randint(200, 10000)))

nonexistent_account = TestAccount('test@error.com', 'test123456?')

error_password_account = TestAccount('joy009@fanatics.live', 'Joytest159753')

Logos = ['NFL','NBA','MLB','NHL','FIFA','MLS','WNBA','NCAA','Formula 1','NASCAR','WWE','UFC']

