#The purpose of this program is to practice Python syntax and basic math programming.
#Each step should be shown.
problem_one = '(x^8)/(x^4)'
numerator1 = '(x)' * 8
denominator1 = '(x)' *4
numerator2 = '/x/x/x/x(x)(x)(x)(x)'
denominator2 = '/x' *4
numerator3 = '(x)' *4
numerator4 = 'x^4'

#This is the first step of the problem
print('Problem #1:', problem_one, 'Simplify')
print('Step One: Write out the problem without exponents')
print(problem_one, '=')
print(numerator1)
print('-' * len(numerator1))
print(denominator1)

print()
print()

#This is the second step of the problem.
print('Step Two: Cancel out.')
print(numerator2)
print('-' * len(numerator2))
print(denominator2)

print()
print()

#Solution
print('Solution:')
print(numerator3)
print('=', numerator4)
