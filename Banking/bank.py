#Aug 2024
def showBal():
    print('')
    print(f'Your balance is ${bal:.2f}')


def deposit():
    amount = float(input('How much would you like to deposit? '))
    if amount <= 0:
        print('That is not a valid amount')
        return 0
    else:
        rec.append(amount)
        return amount


def withdraw():
    amount = float(input('How much would you like with withdraw? '))
    if amount > bal:
        print('You do not have enough money')
        return 0
    else:
        rec.append((amount*-1))
        return amount


def recCheck():
    for x in range(1, len(rec)):
        print(rec[x])


def changer():
    with open('Personal Project/Banking/record.txt', 'w') as file:
        rec[0] = f'bal: ${bal}'
        file.write(rec[0])
    with open('Personal Project/Banking/record.txt', 'a') as file:
        for x in rectrack.keys():
            file.write(f'\n{x}:${rectrack[x]}')


def reason():
    return (str(input('Where did this transaction come from?'))).lower()


def alter(reason, val):
    if reason in rectrack.keys():
        rectrack[reason] += float(val)
    else:
        rectrack[reason] = float(val)


is_running = True
with open('Personal Project/Banking/record.txt', 'r') as file:
    txt = file.read()
    rec = txt.splitlines()
    rectrack = {}
    for x in range(1, len(rec)):
        type, amount = rec[x].split(':$')
        rectrack[type] = float(amount)
    bal = float(rec[0][6:])


while is_running:
    print('***************')
    print("Banking System")
    print("1. Show Balance ")
    print("2. Deposit money ")
    print("3. Withdraw money ")
    print("4. Check record")
    print("5. exit")
    print('***************')
    decision = input('Enter your choice(1-5): ')
    print('')

    if decision == '1':
        showBal()

    elif decision == '2':
        val = deposit()
        bal += val
        reas = reason()
        alter(reas, val)

    elif decision == '3':
        val = withdraw()
        bal -= val
        reas = reason()
        alter(reas, val)

    elif decision == '4':
        changer()
        recCheck()
        
    elif decision == '5':
        is_running = False
    else:
        print('That is not an option')

print('Goodbye! ')
changer()