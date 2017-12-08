#Task1
    '''
    создать класс: Animal() у которого есть атрибуты:
    tail = 1
    paw = 4
    wool = True
    
    создать класс Dog(), который наследует класс Animal()
    и у него появляется метод
    say_something() он отвечает Woof - woof
    
    создать класс Cat(), который наследует класс Animal()
    и у него появляется метод
    say_something() он отвечает Meow - meow
    
    создать класс SphynxCat(), который наследует класс Cat()
    шерсти нет, и на say_something() он отвечает murr-murr
    
    создать класс Rooster(), который наследует класс Animal()
    у него 2 лапы, а не 4, и шерсти у него нет (woof=False)
    и у него появляется метод
    say_something() он отвечает Cocorico
    '''

class Animal:

    tail = 1
    paw = 4
    wool = True


class Dog(Animal):

    @staticmethod
    def say_something():
        return "Woof - woof"


class Cat(Animal):

    @staticmethod
    def say_something():
        return "Meow - meow"


class SphynxCat(Cat):

    wool = False

    @staticmethod
    def say_something():
        return "Murr - murr"


class Rooster(Animal):

    paw = 2
    wool = False

    @staticmethod
    def say_something():
        return "Cocorico"


some_animal = Animal()
doggy = Dog()
kitty = Cat()
gib = SphynxCat()
petya = Rooster()
