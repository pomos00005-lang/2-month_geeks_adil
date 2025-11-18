from datetime import datetime as dt


def data_time_now(func):
    def wrapper():
        print(f'программа была выполнена в {dt.now().hour}:{dt.now().minute}:{dt.now().second}  {dt.now().day}/{dt.now().month}/{dt.now().year}')
        func()
    return wrapper()

@data_time_now
def hello():
    print('Привет Игорь. Как у тебя дела?)')