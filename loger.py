import time 
from datetime import date 
from datetime import time 
from datetime import datetime



def logger(function):
    with open('new_file.txt', 'w') as f:
        function_time = str(datetime.now())
        function_name = function.__name__
        f.write(f'{function_name} — {function_time}')

    def new_function():
        result=function()
        return result
    return new_function
    
@logger
def any_function():
    print('Здесь может быть любая функция')
    return True

any_function() 



