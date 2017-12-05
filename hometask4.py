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

