from datetime import datetime as dt
from time import sleep as s

def data_time_now(func):
    def wrapper():
        print(f'программа была выполнена в {dt.now().hour}:{dt.now().minute}:{dt.now().second}  {dt.now().day}/{dt.now().month}/{dt.now().year}')
        func()
        print(f'программа была завершина в {dt.now().hour}:{dt.now().minute}:{dt.now().second}  {dt.now().day}/{dt.now().month}/{dt.now().year}')
    return wrapper

@data_time_now
def hello():
    print('Привет Игорь. Как у тебя дела?)')
    s(1)

hello()