#This imports the necessary built-ins for the code.
import random
import string

#This is the word banks for the adjectives and nouns used in the password.
adjectives = ['sleepy', 'strong', 'gay',
              'smelly', 'tired', 'ripped',
              'compelling', 'just', 'cranky',
              'small', 'smol', 'hairy',
              'stretchy', 'beautiful', 'strange',
              'fun', 'french', 'american',
              'dangerous', 'cantankerous', 'christlike',
              'fat', 'obese', 'devilish', 'strange']

nouns = ['apple', 'car', 'street', 'devil',
         'god', 'pie', 'cake', 'motorcycle',
         'shirt', 'computer', 'hammer', 'dungeoun',
         'tower', 'building', 'book', 'shape']


print('Welcome to Password Picker!\n')

#This is the random selection of each element of the password.
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

#This is defining the parameters of the password.
    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s \n' % password )

    response = input('Would you like another password? y/n: \n')
    if response == 'n':
        break

thank_you = 'Thank you for using the Password Picker!'
print('_' * len(thank_you))
print(thank_you)
print('-' * len(thank_you))
