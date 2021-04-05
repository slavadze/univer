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
        sql3 = f"INSERT INTO `score`(`users_id`, `{subject}`) VALUES ('{id}', '{score}')"
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