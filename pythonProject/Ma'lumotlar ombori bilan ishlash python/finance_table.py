# SQLite dan foydalanib finance.py nomli command-line application tuzing.
# 3ta:
#    - spend (pul ishlatish)
#    - earn  (pul topish)
#    - balance (balansda qancha pul qolganligini tekshirish)
# imkoniyatlari bo'lsin.
#
# Misol:
# - python finance.py earn 1500  # 1500 daromad qo'shsin
# - python finance.py spend 400  #  400 harajat qo'shsin

'''
import sqlite3
from sqlite3 import connect

with connect("finance.db") as db:
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS finance(
            spend VARCHAR,
            earn VARCHAR,
            balance VARCHAR
        ) 
        """
    )
'''


class ContactsRepo:
    def __init__(self, db):
        self.db = db

    def earn(self, earn, spend, balance):
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT INTO finance(earn, spend, balance)
            VALUES (?, ?, ?)
            ''',
            (earn, spend, balance,)
        )
        db.commit()

    def balance(self):
        cursor = db.cursor()
        cursor.execute(
            '''
            SELECT balance
            FROM finance
            '''
        )
        db.commit()
        return cursor.fetchall()


import sqlite3
import sys

if __name__ == '__main__':
    from prettytable import PrettyTable

    if len(sys.argv) != 2:
        sys.exit('Only 1 argument required')

    available_commands = ('spend', 'earn', 'balance')
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(f'Unknown command: {command}\n available commands')
    with sqlite3.connect('finance.db') as db:
        repo = ContactsRepo(db)
        my_table = PrettyTable(['Balance'])
        if command == 'earn':
            earn = int(input('Balansga pul o`tkazish miqdori: '))
            spend = int(input('Balansdan pul yechish miqdorini kiriting: '))
            balance = earn - spend
            repo.earn(earn, spend, balance)
            print('Amaliyot muvaffaqiyatli bajarildi. Qoldiqni ko`rish uchun balance buyrug`idan foydalaning')
        elif command == 'balance':
            contacts = repo.balance()
            for z in contacts:
                my_table.add_row(z)
                print(my_table)
