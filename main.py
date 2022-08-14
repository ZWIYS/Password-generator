import funcs

while True:

    print('1. Generate new password\n2. exit')

    command = input('choice number of command: ')

    if command == '1':
        funcs.generator()

    elif command == '2':
        print('program is off')
        break

    else:
        print('this command doesnt exist!')
