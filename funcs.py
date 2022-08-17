import string
import random

f = open('PassList.txt', 'a')

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()_')


def generator():

    length = int(input('Enter length of pass: '))

    random.shuffle(characters)

    password = []

    for i in range(length):
        rc = random.choice(characters)
        password.append(rc)

    random.shuffle(password)

    print('\n', 'Ваш пароль: ', ''.join(password))

    cm = input('\nзаписать пароль?\n1 - да\n2 - нет\nвыберете команду: ')
    if cm == '1':
        p = ''.join(password)
        to = input('Пароль для сервиса: ')
        f.write('\n\n' + to + ': ' + p)
    if cm == '2':
        f.close()

