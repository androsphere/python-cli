import sqlite3

CONN = sqlite3.connect('characters.db')
CURSOR = CONN.cursor()
