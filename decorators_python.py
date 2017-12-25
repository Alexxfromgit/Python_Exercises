# Create file Decorators Python

# Task 1
  """
  1. Есть переменные 
  a = 5
  b = 0
  поменять значения переменных, не используя, новцю переменную
  """
  
  a = 5
  b = 0
  
  a = - a - b
  b = - a - b
  a = - a - b
  
  # Result will be changed values in statements
  
# Task 2
  """
  Запилить кодец, чтоб делал сендвич
  """
  
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def bread(food):
    """Bread decorator"""
    def bread_func():
        print(bcolors.FAIL + "</'''''''\>")
        food()
        print(bcolors.FAIL + "<\_______/>")
    return bread_func


def cotlet(food):
    """Cotlet decorator"""
    def cotlet_func():
        print(bcolors.OKBLUE + "==cotlet==")
        food()
        print(bcolors.OKBLUE + "==cotlet==")
    return cotlet_func


def salad(food):
    """Salad decorator"""
    def salad_func():
        food()
        print(bcolors.OKGREEN + "~~~salad~~~")
    return salad_func


def tomato(food):
    """Tomato decorator"""
    def tomato_func():
        print(bcolors.HEADER + "_tomato_")
        food()
    return tomato_func


def cheese(food):
    """Cheese decorator"""
    def cheese_func():
        print(bcolors.WARNING + "[[[cheese]]]")
        food()
        print(bcolors.WARNING + "[[[cheese]]]")
    return cheese_func


@bread
@cheese
@cotlet
@salad
@tomato
def sandwich():
    print(bcolors.ENDC + "--ham--")
