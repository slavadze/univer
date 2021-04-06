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
        menu1 = input("Выберите пункт меню: \n 1) Авторизация 2) Забыли пароль\n ")
        while True:
            if menu1 == "1":
                self.autorization()
            elif menu1 == "2":
                print("Обратитесь к администратору")
            else:
                print("Такой команды нет!")
            menu1 = input("Выберете пункт меню: \n 1) Авторизация 2) Забыли пароль\n")
        return

    def menu2(self):
        menu2 = input("Выберите пункт меню: \n 1) Инфо о себе 2) Фамилия/имя 3) Средний бал\n "
                      "4) Номер группы 5) Инфо о предметах 6) Главное меню\n ")
        while True:
            if menu2 == "1":
                self.about()
            if menu2 == "2":
                self.surname_name()
            elif menu2 == "3":
                self.score()
            elif menu2 == "4":
                self.group_n()
            elif menu2 == "5":
                self.info_subjects()
            elif menu2 == "6":
                self.menu1()
            else:
                print("Такой команды нет!")
            menu2 = input("Выберите пункт меню: \n 1) Инфо о себе 2) Фамилия/имя 3) Средний бал\n "
                      "4) Номер группы 5) Инфо о предметах 6) Главное меню\n ")
        return

    def menu3(self):
        menu3 = input("Выберите пункт меню: \n 1) Информация о студентах 2) Инфо о студенте 3) Добавить студента\n "
                      "4) Добавить преподавателя 5) Поставить оценку 6) Изменить оценку 7) Главное меню\n ")
        while True:
            if menu3 == "1":
                self.info_students()
            elif menu3 == "2":
                self.student()
            elif menu3 == "3":
                self.add_student()
            elif menu3 == "3":
                self.add_student()
            elif menu3 == "4":
                self.add_teacher()
            elif menu3 == "5":
                self.add_score()
            elif menu3 == "6":
                self.change_score()
            elif menu3 == "7":
                self.menu1()
            else:
                print("Такой команды нет!")
            menu3 = input("Выберите пункт меню: \n 1) Информация о студентах 2) Инфо о студенте 3) Добавить студента\n "
                      "4) Добавить преподавателя 5) Поставить оценку 6) Изменить оценку 7) Главное меню\n ")
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
            sql = f"INSERT INTO users (id, login, password, type, name, surname, faculty, groupN) VALUES " \
                   f"('NULL', '{login}', '{password2}', '{type}', '{name}', '{surname}', '{faculty}', '{groupN}') "
            self.cursors.execute(sql)
            self.connection.commit()
            sql2 = f"SELECT id FROM users WHERE login='{login}'"
            self.cursors.execute(sql2)
            self.connection.commit()
            data = self.cursors.fetchone()
            id = data.get('id')
            sql3 = f"INSERT INTO score (users_id, subject1, subject2, subject3) VALUES ({id}, NULL, NULL, NULL)"
            self.cursors.execute(sql3)
            self.connection.commit()
        if type == "T":
            name = input("Name: ")
            surname = input("Surname: ")
            faculty = input('Faculty: ')
            subject = input('Subject: ')
            sql4 = f"INSERT INTO users (id, login, password, type, name, surname, faculty, subject) VALUES " \
                   f"('NULL', '{login}', '{password2}', '{type}', '{name}', '{surname}', '{faculty}', '{subject}')"
            self.cursors.execute(sql4)
            self.connection.commit()

    def autorization(self):
        self.login = input("Login: ")
        #написать функцию проверки логина
        sql = f"SELECT password, type FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()  # {'password': '44a34d475e43395047ae67c20a1024f2'}
        password_input = input("Password: ")  # Пароль, введенный пользователем
        hash_password = data.get('password')  # Значение ячейки password
        b = password_input.encode('utf-8')  # b'44a34d475e43395047ae67c20a1024f2'
        hash2 = hashlib.md5(b)
        type = data.get('type')
        if hash_password == hash2.hexdigest():
            print("Вы авторизованы")
            if type == "S":
                self.menu2()
            else:
                self.menu3()
        else:
            print("Пароль неправильный")
            self.menu1()

    def get_password(self, login):
        sql = "SELECT password FROM users WHERE login=%$"
        self.cursors(sql, [login])
        data = self.cursors.fetchall()
        return data["password"]


    #Полномочия преподавателя
    def info_students(self):
        sql = f"SELECT name, surname, faculty, groupN FROM users WHERE type='S'"
        self.cursors.execute(sql)
        self.connection.commit()
        while True:
            data = self.cursors.fetchone()
            if data:
                print(data.get('name'), data.get('surname'), data.get('faculty'), data.get('groupN'))
            else:
                break

    def student(self):
        surname = input("Surname: ")
        sql = f"SELECT name, surname, groupN, faculty FROM users WHERE surname='{surname}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        print(data.get('name'), data.get('surname'), data.get('faculty'), data.get('groupN'))

    def add_student(self):
        self.registration()

    def add_teacher(self):
        self.registration()

    def add_score(self):
        surname = input("Surname: ")
        score = int(input("Score: "))
        sql = f"SELECT id FROM users WHERE surname='{surname}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        id = data.get('id')
        sql2 = f"SELECT subject FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql2)
        self.connection.commit()
        data2 = self.cursors.fetchone()
        subject = data2.get('subject')
        sql3 = f"UPDATE `score` SET {subject}={score} WHERE users_id={id}"
        self.cursors.execute(sql3)
        self.connection.commit()

    def change_score(self):
        surname = input("Surname: ")
        newscore = int(input("Score: "))
        sql = f"SELECT id FROM users WHERE surname='{surname}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        id = data.get('id')
        sql2 = f"SELECT subject FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql2)
        self.connection.commit()
        data2 = self.cursors.fetchone()
        subject = data2.get('subject')
        sql3 = f"UPDATE score SET {subject}={newscore} WHERE users_id={id}"
        self.cursors.execute(sql3)
        self.connection.commit()
        print("оценка изменена")

    # Полномочия студента
    def about(self):
        sql = f"SELECT name, surname, groupN, faculty FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        print(data.get('name'), data.get('surname'), data.get('faculty'), data.get('groupN'))

    def surname_name(self):
        sql = f"SELECT name, surname FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        print(data.get('name')+ ' ' + data.get('surname'))

    def score(self):
        sql = f"SELECT id FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        id = data.get('id')
        sql2 = f"SELECT subject1, subject2, subject3 FROM score WHERE users_id='{id}'"
        self.cursors.execute(sql2)
        self.connection.commit()
        data2 = self.cursors.fetchone()
        #list = int(data2.get('subject1')) + int(data2.get('subject2')), int(data2.get('subject3'))
        print(data2)

    def group_n(self):
        sql = f"SELECT groupN FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        info = data.get('groupN')
        print("Группа: №" + str(info))

    def info_subjects(self):
        sql = f"SELECT id FROM users WHERE login='{self.login}'"
        self.cursors.execute(sql)
        self.connection.commit()
        data = self.cursors.fetchone()
        id = data.get('id')
        sql2 = f"SELECT subject1, subject2, subject3 FROM score WHERE users_id='{id}'"
        self.cursors.execute(sql2)
        self.connection.commit()
        data2 = self.cursors.fetchone()
        print(data2)

    def delete(self):
        number = input("Введите users_ID: ")
        sql = f"DELETE FROM score WHERE users_id={number}"
        self.cursors.execute(sql)
        self.connection.commit()

    def delete2(self):
        number = input("Введите ID: ")
        sql = f"DELETE FROM users WHERE id={number}"
        self.cursors.execute(sql)
        self.connection.commit()

#login = input("Login: ")
#password = input("Password: ")
#dbPassword = db.get_password(login)
#aaa =db.registration()
#a = db.autorization()
#l = db.delete2()

db = DataBase()
munu1 = db.menu1()