import sqlite3 as sq
import json
from tkinter import *
from tkinter import messagebox
from difflib import get_close_matches

def connect():
    conn = sq.connect('dictionary.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data(Id INTEGER PRIMARY KEY, word TEXT, meaning TEXT)")
    conn.commit()
    conn.close()

def insert(wd, mean):
    conn = sq.connect('dictionary.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(NULL, ?, ?)",(wd, mean))
    conn.commit()
    conn.close()

def view():
    conn = sq.connect('dictionary.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sq.connect('dictionary.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id =?", (id,))
    conn.commit()
    conn.close()

def search_db(word=''):
    conn = sq.connect('dictionary.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE word=?", (word,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(word=''):

    data = json.load(open("data1.json"))

    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word , data.keys())) > 0:
        gcm = get_close_matches(word, data.keys())[0]
        decide = messagebox.askquestion("Confirm", "Did you mean '%s' instead" %gcm)

        if decide == 'yes':
            return data[gcm]

        elif decide == "no":
            messagebox.showerror("error","You may have entered wrong spelling.\n Please check and try again")


connect()
