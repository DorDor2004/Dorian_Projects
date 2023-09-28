import random
import json

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = '0123456789'
symbol = '!@#$%^&*()-_[]{};:,.></?'

upper, lower, num, sym = True, True, True, True

selections = ''

if upper:
    selections += uppercase
if lower:
    selections += lowercase
if num:
    selections += numbers
if sym:
    selections += symbol

storage_file = 'passwords.json'

try:
    with open(storage_file, 'r') as file:
        storage = json.load(file)
except FileNotFoundError:
    storage = {}


def generation():
    nickname = input("Password Nickname?")
    length = int(input('Password Length?'))
    password = ''.join(random.sample(selections, length))
    storage[nickname] = password
    print(f'Password for {nickname}: {password}')


def get_password():
    nickname = input("Enter the Password Nickname to get the password: ")
    password = storage.get(nickname)
    if password:
        print(f'Password for {nickname}: {password}')
    else:
        print(f'Password with nickname "{nickname}" not found in storage.')


def save_storage():
    with open(storage_file, 'w') as file:
        json.dump(storage, file)

while True:
    choice = input('What do you want to do?\n1. Generate a new password\n2. Get a password\n3. Save and Exit\nEnter your choice: ')
    if choice == '1':
        generation()
    elif choice == '2':
        get_password()
    elif choice == '3':
        save_storage()
        break
    else:
        print('Invalid input. Please select a valid option.')

print('Exiting...')
