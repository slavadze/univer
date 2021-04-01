# СДЕЛАТЬ КОНСОЛЬНОЕ МЕНЮ ДЛЯ АВТОРИЗАЦИИ В БАЗЕ ДАННЫХ и РЕГИСТРАЦИИ
import pymysql
from pymysql.cursors import DictCursor
import hashlib


class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()
        print('*' * 20)
        print('Программа Univer 1.0')
        print('*' * 20)

    def __del__(self):
        self.connection.close()
        print("Connection closed")

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='6354045',
            db='univer',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self, login, password, type):
        sql = "INSERT INTO users (id, login, password, type) VALUES (%s, %s, %s, %s)"
        temp = ["NULL", login, password, type]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUsers(self):
        sql = "SELECT * FROM users"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        print(data)

    def menu1(self):
        menu = input("Выберите пункт меню: \n 1) Авторизация 2) Регистрация 3) Удаление пользователя\n ")
        while True:
            if menu == "1":
                self.autorization()
            elif menu == "2":
                self.registration()
            elif menu == "3":
                self.delete()
            else:
                print("Такой команды нет!")
            menu = input("Выберете пункт меню: \n 1) Авторизация 2) Регистрация 3) Удаление пользователя\n")
        return

    def registration(self):
        login = input("Login: ")
        password = input("Password: ")
        type = input('Student(S) or Teacher(T): ')
        shifr = password.encode('utf-8')
        hash = hashlib.md5(shifr)  # Пароль при регистрации
        password2 = hash.hexdigest()
        #sql = "SELECT MAX(`id`) FROM `users`"
        #self.cursors.execute(sql)
        #self.connection.commit()
        #data = self.cursors.fetchone()
        #id_max = data.get('MAX(`id`)')
        #id_add = id_max + 1
        if type == "S":
            name = input("Name: ")
            surname = input("Surname: ")
            faculty = input('Faculty: ')
            groupN = input('group №: ')
            sql2 = f"INSERT INTO users (id, login, password, type, name, surname, faculty, groupN) VALUES ('NULL', '{login}', '{password2}', '{type2}', '{name}', '{surname}', '{faculty}', '{groupN}') "
            self.cursors.execute(sql2)
            self.connection.commit()
        if type == "T":
            name = input("Name: ")
            surname = input("Surname: ")
            faculty = input('Faculty: ')
            subject = input('Subject: ')
            sql3 = f"INSERT INTO users (id, login, password, type, name, surname, faculty, subject) VALUES " \
                   f"('NULL', '{login}', '{password2}', '{type2}', '{name}', '{surname}', '{faculty}', '{subject}')"
            self.cursors.execute(sql3)
            self.connection.commit()

    def autorization(self):
        login = input("Login: ")
        sql = f"SELECT password FROM users WHERE login='{login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()  # {'password': '44a34d475e43395047ae67c20a1024f2'}
        password_input = input("Password: ")  # Пароль, введенный пользователем
        hash_password = data.get('password')  # Значение ячейки password
        b = password_input.encode('utf-8')  # b'44a34d475e43395047ae67c20a1024f2'
        hash2 = hashlib.md5(b)  # Пароль, введенный пользователем <md5 _hashlib.HASH object @ 0x0000020942076F90>
        if hash_password == hash2.hexdigest():
            print("Вы авторизованы")
        else:
            print("Пароль неправильный")

    def delete(self):
        number = input("Введите ID ")
        sql = f"DELETE FROM users WHERE id={number}"
        self.cursors.execute(sql)
        self.connection.commit()

    def get_password(self, login):
        sql = "SELECT password FROM users WHERE login=%$"
        self.cursors(sql, [login])
        data = self.cursors.fetchall()
        return data["password"]


#login = input("Login: ")
#password = input("Password: ")
db = DataBase()
#dbPassword = db.get_password(login)
munu1 = db.menu1()
#aaa =db.registration()
