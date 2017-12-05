#Created a file

#Task1

class Boxer:
    '''
    1. All atributes are fully works with it    
    vasily.age, vasily.weight, vasily.height
    
    2. All methods are fully works with it
    vasily.kick(), vasily.pull_ups()    
    '''
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    @staticmethod
    def kick():
        return "I'll kill you!!!"

    @staticmethod
    def pull_ups():
        return "I can make 50 pull-ups!!!"

vasiliy = Boxer(22, 100, 150)

#Task2

class Person:
    '''
    1. All of [body.age, body.first_name, body.second_name, body.birthday_month, 
    body.full_name(), body.email(), body.birth_season()] works correct.
    '''
    def __init__(self, age, first_name, second_name, birthday_month):
        self.age = age
        self.first_name = first_name
        self.second_name = second_name
        self.birthday_month = birthday_month

    def full_name(self):
        return self.first_name + " " + self.second_name

    def email(self):
        return self.first_name + "." + self.second_name + "@email.com"

    def birth_season(self):
        if self.birthday_month in ['January', 'February', 'December']:
            return 'Winter'
        if self.birthday_month in ['March', 'April', 'May']:
            return 'Winter'
        if self.birthday_month in ['June', 'July', 'August']:
            return 'Winter'
        if self.birthday_month in ['September', 'October', 'November']:
            return 'Winter'


body = Person(age='18', first_name='Pedro', second_name='Villalobos', birthday_month='March')

