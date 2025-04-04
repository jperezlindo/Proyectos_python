
operators = ['+', '-', '*', '/', '**']

addition = lambda a, b: a + b

subtraction = lambda a,b: a - b

multiplication = lambda a,b: a * b

division = lambda a,b: a / b

power = lambda a,b: a**b

def calculator(operator, a, b):
    if operator == '/' and b == 0:
        raise ValueError('It is not possible to divide by 0')

    if operator not in operators:
        raise ValueError('The operator is invalid')

    core = {
        '+': addition(a,b),
        '-': subtraction(a,b),
        '*': multiplication(a,b),
        '/': division(a,b),
        '**': power(a,b)
    }

    return core[operator]


if __name__ == '__main__':
    print('*** CALCULATOR ***')
    while True:
        try:
            a = float(input('Enter the first value: '))
            operator = input('Entre the operator: ')
            b = float(input('Enter the second value: '))
            result = calculator(operator, a, b)
            print(f'\nResult: {a} {operator} {b} = {round(result, 2)}')
            
            carryon = input('\nDo you want to perform another operation? (Yes / Not): ').upper()
            
            if carryon == 'NOT':
                print('\nTHANKS, SEE YOU SOON.')
                break
        except ValueError as e:
            print(f'\nError: {e}\n')