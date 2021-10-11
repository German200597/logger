import time 
from datetime import date 
from datetime import time 
from datetime import datetime



def logger(function):
    def new_function(*args, **kwargs):
        result=function(*args, **kwargs)
        with open('new_file.txt', 'w') as f:
            function_time = str(datetime.now())
            function_name = function.__name__
            f.write(f'{function_name} — {function_time}. Аргументы: {args}, {kwargs}. Возвращаемое значение: {result}')
        return result
    return new_function
    
@logger
def any_function(*args, **kwargs):
    print('Здесь может быть любая функция')
    return True
    

any_function() 



