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
        
