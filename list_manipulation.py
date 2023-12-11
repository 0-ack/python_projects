#The goal of this program is to create a list and manipulate it based on certain parameters provided by the user.

#Define the functions.
def createList():
    choice_one = input('Please enter the first item for your list: ')
    choice_two = input('Please enter the second item for your list: ')
    choice_three = input('Please enter the third item for your list: ')
    choice_four = input('Please enter the fourth item for your list: ')
    choice_five = input('Please enter the final item for your list: ')
    choice_one, choice_two, choice_three, choice_four, choice_five = choice_one.lower(), choice_two.lower(), choice_three.lower(), choice_four.lower(), choice_five.lower()
    global created_list
    created_list = [choice_one, choice_two, choice_three, choice_four, choice_five]
    print()
    print('Here is the list you have created!', created_list)

def sortByLength(list_choice):
    print('Here is your original list.', list_choice)
    print()
    sort_by_length_list = list_choice.sort(key = len)
    print('Here is your list sorted by length!')
    print()
    return sort_by_length_list

def reverseOrder(list_choice):
    print('Here is your original list', list_choice)
    print()
    reverse_order_list = list_choice.reverse()
    print('Here is your list in reverse order:')
    print()
    return reverse_order_list

def removeCharacter(list_choice, character_choice):
    print('Here is your original list', list_choice)
    print('You have decided to remove', "'", character_choice, "'", 'from this list.')
    print('Here is your list with that character removed: ')
    print()
    print([s.replace(character_choice, '') for s in list_choice])



#Greet user.
print()
print('Hello! Welcome to the list manipulator!\n')
print('Let us start by creating our list!\n')

#Create our list from user input.
choose_list = input('What would you like to create a list of? ANIMALS, NUMBERS, or CITIES? ')
choose_list = choose_list.lower()
print()

if choose_list == 'animals':
    print('Great let\'s get started!')
    createList()
    list_animals = created_list
    print()

    manipulate_animal = input('''How would you like to manipulate this list of animals?\n
          SORT BY LENGTH?\n
          REVERSE THE ORDER\n
          or, REMOVE A CHARACTER: ''')
    manipulate_animal = manipulate_animal.lower()
    print()
    if manipulate_animal == 'sort by length':
        sortByLength(list_animals)
        print(list_animals)
    elif manipulate_animal == 'reverse the order':
        reverseOrder(list_animals)
        print(list_animals)
    elif manipulate_animal == 'remove a character':
        character = input('Which character would you like to remove? ')
        removeCharacter(list_animals, character)
        print()
    elif manipulate_animal != 'remove a character' or 'reverse the order' or 'sort by length':
        print('Request not supported, please begin again.')

elif choose_list == 'numbers':
    print('Great! Let\'s get started.')
    createList()
    list_numbers = created_list
    print()
    manipulate_numbers = input('''How would you like to manipulate this list of numbers?\n
          SORT BY LENGTH?\n
          REVERSE THE ORDER\n
          or, REMOVE A CHARACTER: ''')
    if manipulate_numbers == 'sort by length':
        sortByLength(list_numbers)
        print(list_numbers)
    elif manipulate_numbers == 'reverse the order':
        reverseOrder(list_numbers)
        print(list_numbers)
    elif manipulate_numbers == 'remove a character':
        character = input('Which character would you like to remove? ')
        removeCharacter(list_numbers, character)
    elif manipulate_numbers != 'remove a character' or 'reverse the order' or 'sort by length':
        print('Request not supported, please begin again.')

elif choose_list == 'cities':
    print('Great! Let\'s get started.')
    createList()
    list_cities = created_list
    print()
    manipulate_cities = input('''How would you like to manipulate this list of cities?\n
          SORT BY LENGTH?\n
          REVERSE THE ORDER\n
          or, REMOVE A CHARACTER: ''')
    if manipulate_cities == 'sort by length':
        sortByLength(list_cities)
        print(list_cities)
    elif manipulate_cities == 'reverse the order':
        reverseOrder(list_cities)
        print(list_cities)
    elif manipulate_cities == 'remove a character':
        character = input('Which character would you like to remove? ')
        removeCharacter(list_cities, character)
    elif manipulate_cities != 'remove a character' or 'reverse the order' or 'sort by length':
        print('Request not supported, please begin again.')
print()
print('Thank you for using the List Manipulator.')
print('''NOTE: This was a program created to practice creating functions and working with lists.
Feedback is always welcome on how to improve this program''')