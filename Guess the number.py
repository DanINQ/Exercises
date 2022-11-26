import random
from random import randint
def play():
    exact_number = randint(0, 100)
    print("Hello! Here's the game where you should guess the number in range 0 - 100! Let's get started!")
    start_key = input("Press any key to start! ")

    def user_input():
        def control(): #Здесь я сделал через рекурсивную функцию, что вроде не есть хорошо, иначе только создавать бесконечный цикл,
                       # т.к. нужно чтоб после excepta заново шел try,
                       # для этого цикл надо, но если в цикле прописать int(user_number) то ошибка выскакивает до try, поэтому можно бесконечный цикл без этого условия,
                       # а когда инпут совпадет с загаданным числом прописать брейк
            user_number = input("Enter your variant: ")
            try:
                if int(user_number) == exact_number:
                    print("You was good!")
                elif int(user_number) <= exact_number:
                    print("Nope! Bigger!")
                    control()
                elif int(user_number) >= exact_number:
                    print("Nope! Lesser!")
                    control()
            except ValueError as v:
                print('Oops! Numbers only!')
                control()
        control()

    if isinstance(start_key, str):
        user_input()
play()