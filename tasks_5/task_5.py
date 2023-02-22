class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.known_persons = []

    def know(self, person):
        if person not in self.known_persons:
           self.known_persons.append(person)
           print('okay yeah i remembered this buddy.')
        else:
            print("Yeah but i'm already know him.")

    def is_known(self,person):
        if person in self.known_persons:
            print('Yeah i know this dude.')
        else:
            print("Nah, i really don't know who the fuck is it.")

Johny = Person(23, 'Johny')
Oscar = Person(19, 'Oscar')
Johny.know(Oscar)
Johny.is_known(Oscar)
Chris = Person(25, 'Chris')
Johny.know(Chris)
Johny.is_known(Oscar)
Johny.know(Chris)

print('\n\n\n')

class Printer:
    def log(self, *values):
        for i in values:
            for g in i:
                print(g, end=' ')

class FormattedPrinter(Printer):
    def formatted_log(self, *values):
        length = 0
        for i in values:
            if type(i) != str:
                length += len(str(i)) + 1
            else:
                length += len(i) + 1
        print('*' * length)
        self.log(values)
        print('\b')
        print('*' * length)

some_obj = FormattedPrinter()
some_obj.formatted_log('something', 'other',34, 456)

print('\n\n\n')


class Human:
    def is_dangerous(self, animal):
        if animal.animal == 'Predator':
            self.danger = True
            print('Yeah, {} is kinda dangerous!'.format(animal.animal_name))
            return self.danger
        elif animal.animal_poison == 'Poisounus':
            self.danger = True
            print('Yeah, {} is kinda dangerous!'.format(animal.animal_name))
            return self.danger
        else:
            self.danger = False
            print('Nah, {} is not a reason for worries, its safe!'.format(animal.animal_name))
            return self.danger

class Animal:
    def __init__(self, animal_type, poison, name):
        self.animal_name = name
        self.animal = False
        self.animal_poison = False

        if animal_type in ['Predator', 'predator','Зкувфещк', 'зкувфещк']:
            self.animal = 'Predator'
        elif poison in ['Poisounus', 'poisonous', 'Зщшыщгтгы', 'зщшыщгтгы']:
            self.animal_poison = 'Poisounus'


tiger = Animal('Predator', False, 'Tiger')
black_widow = Animal('Predator', 'Poisounus', 'Black Widow')
puffer_fish = Animal(False, 'Poisounus', 'Puffer Fish')
deer = Animal(False, False, 'Deer')
human = Human()
human.is_dangerous(tiger)
human.is_dangerous(black_widow)
human.is_dangerous(puffer_fish)
human.is_dangerous(deer)

def