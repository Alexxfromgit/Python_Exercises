x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
     'September', 'October', 'November', 'December']


def seasons(month):
  '''
  Написать функцию, вводишь название месяца, возвращает время года:
  старайтесь пользоваться выражением:
  if month in some_list
  '''
    if month in x:
        if x.index(month) == 0 or x.index(month) == 1 or x.index(month) == 11:
            return 'Winter'
        elif x.index(month) == 2 or x.index(month) == 3 or x.index(month) == 4:
            return 'Spring'
        elif x.index(month) == 5 or x.index(month) == 6 or x.index(month) == 7:
            return 'Summer'
        else:
            return 'Autumn'
    else:
        return 'Wrong month'
        
