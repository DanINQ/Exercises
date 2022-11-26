import random

def hangman():
    word_plane = ['Аварийщик', 'Ограничение', 'Комедия']
    word = random.choice(word_plane)
    hidden_word = []
    lifes = [10, ]
    word_listed = []
    for i in word:
        word_listed += i
    for i in word_listed:
        hidden_word += '*'
    print(hidden_word)
    def control():
        user_variant = input("Guess the letter: ")
        matches = 0
        for i in range(len(word_listed)):
            if user_variant.lower() == hidden_word[i].lower():
                print("You're already guessed this letter! Try another one.")
                matches += 1
                break
            elif word_listed[i].lower() == user_variant.lower():
                hidden_word[i] = word_listed[i]
                matches += 1
        if matches == 0:
            lifes.append(lifes[0] - 1)   #здесь я меняю число в переменной с помощью мутации ее получается,
                                         # т.к. функция не может чужие переменные перезаписвать, хз насколько правильно
            del lifes[0]
            print('Nope! Lifes left: ', lifes[0])
        else:
            print('Lifes left: ', lifes[0])
        print(hidden_word)
    while hidden_word != word_listed and lifes[0] != 0:
        control()
    if lifes[0] == 0:
        print('Oops! No lifes left! Game over!')
    elif hidden_word == word_listed:
        print("That's it! You guessed the word!")

hangman()