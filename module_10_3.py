from threading import Thread, Lock
from random import randint
import time

class Bank:
    def __init__(self, balance=0, lock=Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            deposit = randint(50, 500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            deposit = randint(50, 500)
            print(f'Запрос: {deposit}')
            if self.balance >= deposit:
                self.balance -= deposit
                print(f'Снятие: {deposit}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.0001)


if __name__ == '__main__':
    bk = Bank()
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    time.sleep(1)

print(f'Итоговый баланс: {bk.balance}')