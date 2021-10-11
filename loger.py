import time 
from datetime import date 
from datetime import time 
from datetime import datetime

def logger(function):
    def new_function(route):
        result=function(route)
        with open(route, 'w') as f:
            function_time = str(datetime.now())
            function_name = function.__name__
            f.write(f'{function_name} — {function_time}. Аргументы: {route}. Возвращаемое значение: {result}')
        return result
    return new_function
    
@logger
def any_function(route):
    print('Здесь может быть любая функция')
    return True
    

any_function('new_file.txt') 



