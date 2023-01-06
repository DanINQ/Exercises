first_question =  input('Какой язык мы учим?')
right_answers = 0

if first_question in ['Python','python','Питон','питон']:
    print('Nice!')
    right_answers = right_answers + 1
else:
    print('Wrong!')

second_question = input('С помощью какой команды можно привести число к строке?')

if second_question == 'str':
    print("That's right!")
    right_answers = right_answers + 1
elif second_question == 'str()':
    print("That's right!")
    right_answers = right_answers + 1
else:
    print('Nope!')

third_question = input('Какой escape-символ используется для переноса текста на следующую строку?')

if third_question == '\\n':
    print('Great! Mowing next!')
    right_answers = right_answers + 1
else:
    print("Well,it's not...")

fourth_question = input ('Чему равно bool(1)?')

if fourth_question == 'True' or fourth_question == 'true':
    print("Yep! You're going well!")
    right_answers = right_answers + 1
else:
    print('Try next time!')

fifth_question = input('Какая команда показывает длинну строки?')

if fifth_question == 'len':
    print('Perfect!')
    right_answers = right_answers + 1
elif fifth_question == 'len()':
    print('Perfect!')
    right_answers = right_answers + 1
else:
    print('Not exactly...')

sixth_question = input('Атомный номер Плутония?')

if sixth_question == '94':
    print("You're fcking right!")
    right_answers = right_answers + 1
else:
    print('Nah...')

seventh_question = input('В каком году началась Волынская резьня?')

if seventh_question == '1943':
    print('Good!')
    right_answers = right_answers + 1
else:
    print("Well, you're not expected to know that")

eight_question = input('Как называется частица квантовой гравитации?')

if eight_question in ['Гравитон','гравитон']:
    print('Genius!')
    right_answers = right_answers + 1
else:
    print('Well, not exactly...')

ninth_question = input('Как называются нагретые силой трения газо-пылевые скопления вокруг \
массивных компактных космических обьектов по типу активных ядер галактик или черных дыр?')

if ninth_question.lower() == 'аккреационный диск':
    print('How do you know this!')
    right_answers = right_answers + 1
else:
    print("Actually no,it's not")

tenth_question = input('В каком году Гаврило Принцип убил Франца Фердинада?')

if tenth_question == '1914' or tenth_question == '28 июня 1914':
    print('Yes!')
    right_answers = right_answers + 1
else:
    print('Nope!')


if right_answers == 0:
    print("Well, you shoud be better prepared, cuz you gave literally {} answers.".format(right_answers))
elif right_answers <=3:
    if right_answers != 0:
        print('Thanks for you answers! You gave {} correct answers. Well, at least something.'.format(right_answers))
elif right_answers <8:
    if right_answers >3:
        print('Thanks for your answers,you was good! By the way, you gave {} correct answers.'.format(right_answers))
elif right_answers >= 8:
    print("Woah! You're freaking good! You gaved {} correct answers! Nice!".format(right_answers))