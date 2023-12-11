#The goal of this program is to take user input of integers and perform the desired operation on them, returning the result.

#Collect user input and define variables.
print('Please enjoy this program and allow it to do the simple calculations for you!')

#Confirm data input.
while True:
    var1 = int(input('Please input the first number: '))
    var2 = int(input('Please input the second number: '))
    operation = input('What would you like to do with the numbers? \n ADD, SUBTRACT, MULTIPLY, OR DIVIDE? \n')
    print()
    operation = operation.lower()
    if operation not in {'add', 'subtract', 'multiply', 'divide'}:
        print('Please Try Again :)')
        print()
        continue
    if operation == 'add':
        print('You are trying to add', var1, 'to', var2)
        print('The sum of', var1, 'and', var2, 'equals', var1 + var2)
        print()
    elif operation == 'subtract':
        print('You are trying to subtract', var2, 'from', var1)
        print('The difference of', var1, 'and', var2, 'equals', var1 - var2)
        print()
    elif operation == 'multiply':
        print('You are trying to multiply', var1, 'by', var2)
        print('The product of', var1, 'and', var2, 'equals', var1 * var2)
        print()
    elif operation == 'divide':
        print('You are trying to divide', var2, 'out of', var1)
        print('The quotient of', var1, 'and', var2, 'equals', var1 / var2)
        print()
    else:
        break
    break
print('Hope this helps! Bye Felicia!\n')