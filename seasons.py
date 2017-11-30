#First task

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
     'September', 'October', 'November', 'December']


def seasons(month):
  '''
     Написать функцию, вводишь название месяца, возвращает время года:
     старайтесь пользоваться выражением:
     if month in some_list
  '''
    if month in ['January', 'February', 'December']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Something is wrong'
        
#Second task

def season(month):
    '''
        В переменной month лежит какое-то число из интервала от 1 до 12.
        Определите в какую пору года
        попадает этот месяц
        ((winter) зима, (summer) лето, (spring) весна, (autumn) осень).
    '''
    if month in [1, 2, 12]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'autumn'
    else:
        return 'Something is wrong'


if __name__ == '__main__':
    assert season(1) == 'winter'
    assert season(2) == 'winter'
    assert season(12) == 'winter'

    assert season(3) == 'spring'
    assert season(4) == 'spring'
    assert season(5) == 'spring'

    assert season(6) == 'summer'
    assert season(7) == 'summer'
    assert season(8) == 'summer'

    assert season(9) == 'autumn'
    assert season(10) == 'autumn'
    assert season(11) == 'autumn'
     
     
