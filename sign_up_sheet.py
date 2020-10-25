# -*- coding: utf-8 -*-

from tkinter import *
import sqlite3

window = Tk()
window.geometry("500x500+250+250")
window.configure(bg = "purple")

conn = sqlite3.connect("participants.db")
c = conn.cursor()

header = Label(window,text = "Sign Up Sheet",font = ('arial',18),background = 'purple')
header.grid(row = 1, column = 1,sticky = W)
first_name = Label(window, text = "First Name: ")
first_name.grid(row = 2, column = 1, sticky = W, pady = 2)

last_name = Label(window, text = "Last Name: ")
last_name.grid(row = 3, column = 1, sticky = W, pady = 2)

item_name = Label(window, text = "Item you are bringing: ")
item_name.grid(row = 4, column = 1, sticky = W, pady = 3)

enter_first = Entry(window)
enter_first.grid(row = 2, column = 2, sticky = W, pady = 3)

enter_last = Entry(window)
enter_last.grid(row = 3, column = 2, sticky = W, pady = 3)

enter_item = Entry(window)
enter_item.grid(row = 4, column = 2, sticky = W, pady = 3)

def store():
    c.execute("CREATE TABLE IF NOT EXISTS participants (first_name text NOT NULL, last_name text NOT NULL, item text NOT NULL)")
    conn.commit()
    
    c.execute("INSERT INTO participants VALUES(?,?,?)",(enter_first.get(),enter_last.get(),enter_item.get()))
    conn.commit()
        
def clear():
    enter_first.delete(0,END)
    enter_last.delete(0,END)
    enter_item.delete(0,END)

def get_record():
    records = Scrollbar(window)
    participant_list = Listbox(window,yscrollcommand = records.set)
    records.config(command = participant_list.yview)
    records.grid(row = 6, column = 2, sticky = NS, pady = 2)
    
    c.execute("SELECT * FROM participants")
    for row in c.fetchall():
        participant_list.insert(END,row)
    participant_list.grid(row = 6, column = 2, sticky = W, pady = 2)
    records.config(command = participant_list.yview)
    
    
button_1 = Button(window, text = "store", command = store)
button_1.grid(row = 5, column = 1, sticky = W, pady = 2)

button_2 = Button(window, text = 'clear', command = clear)
button_2.grid(row = 6, column = 2, sticky = W, pady = 2)

button_3 = Button(window, text = 'Open to see sheet',command=get_record)
button_3.grid(row = 6, column = 1, sticky = W, pady = 2)


window.mainloop()