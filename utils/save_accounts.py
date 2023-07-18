def save_data(email,password,add_payment=False):
    with open('data/created_accounts.txt', 'w') as output_file:
        output_file.write("email: {}, password: {}, add_payment: {}".format(email,password,add_payment))

    output_file.close()