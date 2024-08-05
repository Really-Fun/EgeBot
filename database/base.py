import sqlite3


class Database:

    def __init__(self, path: str) -> None:
        """_summary_

        Args:
            path (str): path_to_SQLbase

        Создается класс с путем к базе данных
        """
        self.path = path

    def write_to_database(self, id: str):
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            cur.execute(
                f'INSERT INTO levels(id, total, wins, zadanie, vip) VALUES({id}, 0, 0, 0, 0)')

    def write_zadanie(self, id: int, zadanie: int) -> None:
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            cur.execute(
                f'UPDATE levels SET zadanie = {zadanie} WHERE id = {id}')

    def get_zadanie(self, id: int):
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            return cur.execute(f'SELECT zadanie FROM levels WHERE id == {id}').fetchone()[0]

    def get_in_database(self, id: int):
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            a = cur.execute(f'SELECT * FROM levels id WHERE id == {id}')
            return a.fetchall()

    def get_in_task(self, id: int) -> int:
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            return cur.execute(f'SELECT in_level FROM levels WHERE id == {id}').fetchone()[0]

    def in_task(self, id: str, in_level: int, level: int):
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            cur.execute(
                f'UPDATE levels SET in_level = {in_level}, level_1 = {level} WHERE id = {id}')

    def get_id_user_task(self, id: int) -> int:
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            return cur.execute(f'SELECT level_1 FROM levels WHERE id == {id}').fetchone()

    def add_total(self, id: int):
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            total = cur.execute(
                f'SELECT total FROM levels WHERE id == {id}').fetchone()[0]
            cur.execute(
                f'UPDATE levels SET total = {total + 1} WHERE id = {id}')

    def add_win(self, id: int):
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            wins = cur.execute(
                f'SELECT wins FROM levels WHERE id == {id}').fetchone()[0]
            cur.execute(
                f'UPDATE levels SET wins = {wins + 1} WHERE id = {id}')

    def get_total_and_wins(self, id: int) -> int:
        with sqlite3.connect(self.path) as base:
            cur = base.cursor()
            return cur.execute(f'SELECT total, wins FROM levels WHERE id == {id}').fetchone()


baza = Database('first_database.db')