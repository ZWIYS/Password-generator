import funcs

while True:

    print('1. Generate new password\n2. exit')

    command = input('choice number of command: ')

    if command == '1':
        funcs.generator()

    elif command == '2':
        funcs.f.close()
        print('finishing...')
        break

    else:
        print('this command doesnt exist!')
