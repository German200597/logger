import time 
from datetime import date 
from datetime import time 
from datetime import datetime

def any_function():
    print('Здесь может быть любая функция')

def logger(function):
    with open('new_file.txt', 'w') as f:
        x = str(datetime.now())
        f.write(x)
    
   
    def new_function():
        result=function()
        return result
    return new_function
    

any_function = logger(any_function)

any_function() 



