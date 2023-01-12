# Darsda yaratilgan "Contacts Command-line Application"ni list va search qilganda, "prettytable" dan foydalanib,
# natijalarni jadval ko'rinishida chiqaring

import sqlite3


class ContactsRepo:
    def __init__(self, db):
        self.db = db

    def add(self, first_name, last_name, phone_number):
        cursor = db.cursor()
        cursor.execute(
            f'''
            INSERT INTO contacts(first_name, last_name, phone_number)
            VALUES (?, ?, ?)
            ''',
            (first_name, last_name, phone_number)
        )
        db.commit()

    def list(self):
        cursor = db.cursor()
        cursor.execute(
            '''
            SELECT*
            FROM contacts
            '''
        )
        return cursor.fetchall()

    def search(self, first_name):
        cursor = db.cursor()
        cursor.execute(
            '''
            SELECT*
            FROM contacts
            WHERE first_name=?
            ''',
            (first_name,)
        )

        return cursor.fetchall()


import sys

if __name__ == '__main__':
    from prettytable import PrettyTable

    if len(sys.argv) != 2:
        sys.exit('Only 1 argument required')

    available_commands = ('add', 'list', 'search',)
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(f'Unknown command: {command}\n available commands')

    with sqlite3.connect('contacts.db') as db:
        repo = ContactsRepo(db)
        my_table = PrettyTable(['First name', 'Last name', 'Phone number'])
        if command == 'add':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            phone_number = input('Phone number: ')
            repo.add(first_name, last_name, phone_number)
            print("Successfully")
        elif command == 'list':
            contacts = repo.list()
            for z in contacts:
                my_table.add_row(z)
            y = my_table
            print(y)
        elif command == 'search':
            first_name = input('First name: ')
            contacts = repo.search(first_name)
            my_table.add_row(*contacts)
            x = my_table
            print(x)
