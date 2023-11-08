import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('scores.db')
        cur = self.connection.cursor()
        self.cursor = cur
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS score(
            username VARCHAR(30),
            wins INTEGER
        );
        ''')

    def add(self, user, win):
        xd = self.query(user)
        if not xd:
            self.cursor.execute("INSERT INTO score(username, wins) VALUES(?, ?)", (user, win))
        else:
            self.cursor.execute('UPDATE SCORE SET wins = ? WHERE username = ?', (win, user))
        self.connection.commit()
        return True

    def query(self, user):
        self.cursor.execute("SELECT wins FROM score WHERE username = ?", (user,))
        return self.cursor.fetchone()

    def lead(self):
        self.cursor.execute("SELECT * FROM score ORDER BY wins DESC")
        return self.cursor.fetchall()

    def reset(self):
        self.cursor.execute("DROP TABLE score")

    def exit(self):
        self.connection.close()

