def show_balance(balance, currency):
    print(f'\nYour current balance is: {balance:.2f}{currency}')

def deposit():
    amount = float(input('Enter the amount to deposit: '))
    if amount < 0:
        print('The amount entered is not valid')
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('Enter the amount of money to be withdrawn: '))
    if amount > balance:
        print('Insufficient funds!')
        return 0
    elif amount < 0:
        print('The amount to be withdrawn must be greater than 0.')
        return 0
    else:
        return amount

def main_menu():
    balance = 0
    currency = 'usd'
    carryon = True

    while carryon:
        print('\nBANKING PROGRAM')
        print('''
        1. show balance
        2. Deposit
        3. Withdraw
        4. Leave
        ''')
        option = input('Enter an option 1-4: ')
        match option :
            case '1':
                show_balance(balance, currency)
            case '2':
                balance +=  deposit()
                show_balance(balance, currency)
            case '3':
                balance -= withdraw(balance)
                show_balance(balance, currency)
            case '4': carryon = False
            case _: print('The entered option is not valid!')

if __name__ == '__main__':
    main_menu()

