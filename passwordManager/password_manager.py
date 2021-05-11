import secrets
#from secret import get_secret_key
from menu import menu, create, find, find_accounts
import random
from sys import exit
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

def get_secret_key():
    chars = (
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVXYZ'
        '0123456789'
        '#^[]-_*%&=+/'
    )
    keygen = ''.join([random.SystemRandom().choice(chars) for _ in range(50)])
    print(keygen)
    return keygen 


secret = get_secret_key()

passw = input('Provide Master Password for passCodeGen: ')

if passw == secret:
    print('You\'re in')

else:
    print('no luck')
    exit() 

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    if choice == '4':
        choice = menu()   
    else:
        choice = menu()
exit()
