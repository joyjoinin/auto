import random
import subprocess


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
                 good_password='Joytest159753',
                 username=None,
                 invalid_name='?test',
                 already_took_username='joy001',
                 access_code='test',
                 logo_select=random.randint(1, 12),
                 follow_count=1,
                 level_index=random.randint(1, 3)):
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

test_live_name = 'joy test 28/7'

app_name = 'live.fanatics.FanaticsLive-Development'
# app_name = 'live.fanatics.FanaticsLive-QA'

# test_account = Account('joy0101@fanatics.live', 'Joytest159753?')
test_account = Account('joy0102@fanatics.live', 'Joytest159753?')

level_params = ["I'm a Rookie", "I'm a Collector", "I'm a Seasoned Pro"]

nonexistent_account = Account('test@error.com', 'test123456?')

error_password_account = Account('joy999@fanatics.live', 'Joytest159753')

Logos = ['NFL', 'NBA', 'MLB', 'NHL', 'FIFA', 'MLS', 'WNBA', 'NCAA', 'Formula 1', 'NASCAR', 'WWE', 'UFC']

app_environment = 'Dev'  # QA / Pro

device_type = 'Simulator'  # 'Real'

simulator_device_udid = '93C67BC8-E00B-42DA-B10C-D6C7418E5547'

test_report = {'email': 'this is test email', 'user': 'this is test user', 'add': 'this is test add'}

'''system messages'''
test_message_on_live = 'this is test message'
long_message_on_live = 'This is long test message This is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test messageThis is long test message'
system_message_for_long_message = 'The message you are trying to send is larger than 280 characters'
won_message = 'just bought into the break!'
return_policy_text = "To protect the integrity of the auction process, all bids and sales are final. That said, we're not monsters. If there's a problem with your order, please contact the Seller. If you can't reach a resolution, we'll help set it right with our Buyer Protection Promise."
shipping_taxes_text = "All orders also include a $4.95 domestic shipping fee for your first purchase in a break, with $0.50 assessments on each additional purchase in the same break. Taxes are calculated based on your location. We strive to keep fees as low as we can so we don't get Boston Tea Partied."
random_spot_name = 'Random Spot'
