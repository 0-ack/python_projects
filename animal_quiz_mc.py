def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer!')
            score = score + 5 - attempt-1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again.')
            attempt = attempt +1

    if attempt == 3:
        print('The correct answer is ' + answer)

score = 0
print('Guess the Animal!')
guess1 = input('Which bear lives at the North Pole?\n A) Whale Bear\n B) Dolphin Bear\n C) Polar Bear\n D)Yo mama\n Type A, B, C, or D...')
check_guess(guess1, 'C')
guess2 = input('What is the fastest land animal?\n A) A little baby bunny rabbit\n B) Jesus Lizard\n C) Papa Bear\n D) Cheetah\n Type A, B, C, or D...')
check_guess(guess2, 'D')
guess3  = input('What is the largest animal?\n A) Yo mama\n B) Blue Whale\n C) Giant Squid Eye\n D) Baby Elephant\n Type A, B, C, or D...')
check_guess(guess3, 'B')
guess4 = input('Which animal is tearing up my front lawn?\n A) Blue Whale\n B) Yo mama\n C) A guy with a powerwasher and too much time on his hands\n D)Gopher\n Typer A, B, C, or D...')
check_guess(guess4, 'D')
guess5 = input('Which animal is the cockroach of the ocean, but is a delicacy?\n A) Yo mama\n B) Lobster\n C) Manbearpig\n D) Beluga Whale\n Type A, B, C, or D...')
check_guess(guess5, 'B')

print('Your score is ' + str(score))
