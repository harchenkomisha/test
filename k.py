turn = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        turn.append(number)
        print('ok')
    elif command == 'pop':
        print(turn.pop(1))
    elif command == 'front':
        print(turn[0])
    elif command == 'size':
        print(len(turn))
    elif command == 'clear':
        turn.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
        break
    else:
        print('error')