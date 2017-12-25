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
  
def bread(food):
    """Bread decorator"""
    def bread_func():
        print("</'''''''\>")
        food()
        print("<\_______/>")
    return bread_func


def cotlet(food):
    """Cotlet decorator"""
    def cotlet_func():
        print("==cotlet==")
        food()
        print("==cotlet==")
    return cotlet_func


def salad(food):
    """Salad decorator"""
    def salad_func():
        food()
        print("~~~salad~~~")
    return salad_func


def tomato(food):
    """Tomato decorator"""
    def tomato_func():
        print("_tomato_")
        food()
    return tomato_func


def cheese(food):
    """Cheese decorator"""
    def cheese_func():
        print("[[[cheese]]]")
        food()
        print("[[[cheese]]]")
    return cheese_func


@bread
@cheese
@cotlet
@salad
@tomato
def sandwich():
    print("--ham--")
