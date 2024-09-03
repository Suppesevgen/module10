from threading import Thread
from time import sleep
from datetime import datetime

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f'{self.name} на нас напали!')
        day = 1
        self.enemy -= self.power
        while self.enemy > 0:
            print(f'{self.name}, сражается {day} день(дня)..., осталось {self.enemy} воинов')
            day += 1
            self.enemy -= self.power
            sleep(1)
        print(f'{self.name}, сражается {day} день(дня)..., осталось {self.enemy} воинов ')
        print(f'{self.name} одержал победу спустя {day} дней!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')