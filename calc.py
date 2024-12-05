# example
print('hello testers')

'''
addition +
substraction -
multiplication *
division /
modulus %
exponent **

greater-than >
less-than <
equal-to ==
not-equal-to !=
greater-than-or-equal-to >=
less-than-or-equal-to <=
'''
while True:

    a = input('enter number for a: ',)
    if a.lower() == 'exit':
        print(f"exit all operations immediately")
        break
        
    b = input('enter number for b :',)
    if b.lower() == 'exit':
        print(f"exit all operations immediately")
        break

    operation = input('Enter operation("+", "-", "*", "/", "%", "**"): ')
    if operation.lower() == 'exit':
        print(f"exit all operations immediately")
        break
    try:
        a = float(a)
        b = float(b)

        # calculation is here    
        if operation == '+':
            result = a + b
            print(f"result of addition {a} + {b}: {result}")
        elif operation == '-':
            result = a - b
            print(f"result of subtraction {a} - {b}: {result}")
        elif operation == '*':
            result = a * b
            print(f"result of multiplication {a} * {b}: {result}")
        elif operation == '/':
            if b == 0:
                print(f"division by zero is zero")
            else:
                result = a / b
                print(f"result of division {a} / {b}:  {result}")
        elif operation == '%':
            if b == 0:
                print(f"modulus by zero is undefined")
            else:
                result = a % b
                print(f"result of modulus {a} % {b}: {result}")
        elif operation == '**':
            result = a ** b
            print(f"result of exponentiation {a} ** {b}: {result}")
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue
    
