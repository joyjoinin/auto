class LocatorInfo:
    def __init__(self, by_type=None, locator=None):
        self.type = by_type
        self.locator = locator


login = LocatorInfo('link text','Sign in')
username = LocatorInfo('id','user_email_or_username')
user_password = LocatorInfo('id','user_password')
sign_in = LocatorInfo('id','submit-button')
schedule_a_show = LocatorInfo('class name', 'fanatics-button--large')
title = LocatorInfo('id','stream-title')
upload = LocatorInfo('class name','image_upload[file]')
date = LocatorInfo('id','startsAtDate')
time = LocatorInfo('id','startsAtTime')
channel = LocatorInfo('id','live_stream-form_channel_id')
creator = LocatorInfo('id','live_stream-form_staffers_0_id')
breaker = LocatorInfo('id','live_stream-form_staffers_1_id')
add_listing = LocatorInfo(locator='//*[@id="live_stream-form"]/button')


'''Listing page'''
save_draft = LocatorInfo(locator='//*[@id="phx-F3kPodRmbxV3l21B"]/div/header/div/a/button')
publish = LocatorInfo(locator='//*[@id="phx-F3kPodRmbxV3l21B"]/div/header/div/button')
listing_title = LocatorInfo('id', 'create-listing-form_title')
select_an_option = LocatorInfo('id','create-listing-form_break_template_id')
random = LocatorInfo(locator='//*[@id="create-listing-form"]/div[1]/div/fieldset[3]/div/label[1]')
pick_your_spot = LocatorInfo(locator='//*[@id="create-listing-form"]/div[1]/div/fieldset[3]/div/label[2]')
set_price = LocatorInfo(locator='//*[@id="create-listing-form"]/div[1]/div/fieldset[4]/div/label[1]')
auction = LocatorInfo(locator='//*[@id="create-listing-form"]/div[1]/div/fieldset[4]/div/label[2]')
assign_price = LocatorInfo('id','open-assign-price-modal')
save_listing = LocatorInfo(locator='//*[@id="create-listing-form"]/div[3]/button')
assign_list = LocatorInfo(locator='//*[@id="item-modal__container"]/div/div/div')
assign_item = LocatorInfo('id')  # f'price_input_{}'
assign_prices = LocatorInfo('id','assign-prices-button')
close_assign_prices = LocatorInfo('id','close-spot-pricing-modal')
