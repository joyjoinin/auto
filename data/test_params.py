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


address_info = Address('Joy', 'test', '11061 Wilshire Blvd', '', '90025', 'LA', 'CA')

card_info = Card('4242424242424242', '0130', '111', 'United States','11111')

app_name = 'live.57blocks.fanatics.FanaticsLive-Development'

test_account = TestAccount('joy009@fanatics.live', 'Joytest159753?')
