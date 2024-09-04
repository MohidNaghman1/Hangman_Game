import List_of_Words as Words
import random
import HangMan_Stages as Hanman_stages


random_word= random.choice(Words.Words)
print(random_word)
lives = 6

display = ['_' for _ in random_word]

print(display)

game_over = False
while not game_over:
    user_guess = input("Guess a letter: ")

    for i in range(len(random_word)):
        if random_word[i] == user_guess:
            display[i] = user_guess

    if user_guess not in random_word:
         lives -= 1
         if lives == 0:
             game_over = True
             print("You Lose")
    print(Hanman_stages.hangman_stages[len(Hanman_stages.hangman_stages) - lives-1])
    print(display)
    if '_' not in display:
        game_over = True
        print("You Win")

