import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()_')


def generator():

    length = int(input('Enter length of pass: '))

    random.shuffle(characters)

    passwd = []

    for i in range(length):
        c = random.choice(characters)
        passwd.append(c)

    random.shuffle(passwd)

    print(''.join(passwd))
