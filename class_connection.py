import sqlite3

class Connection:
    def open_connection(self):
        self.connection = sqlite3.connect("peluqueria")
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()