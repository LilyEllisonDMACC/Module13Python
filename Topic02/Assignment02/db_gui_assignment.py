"""
Program: db_gui_assignment.py
Author: Lily Ellison
Last date modified: 04/17/2023

The purpose of this program is to create databases for the
person and student information with a gui for user interaction.

"""


import sqlite3
from sqlite3 import Error
import create_db
import read_db
import write_db
import update_db
import delete_db
import tkinter
'''
Define functions/methods below here
'''


def create_student_and_person_table():
    create_db.create_tables('gui_db.db')


def insert_person():
    #TODO: how to get user input for first name, last name

    #end TODO

    #Stole below lines from driver of the write_db code
    conn = write_db.create_connection("gui_db.db")
    with conn:
        person = ('Rob', 'Thomas')
        person_id = write_db.create_person(conn, person)
    label.config(text="Person Entered")


def insert_student():
    #TODO: how to get user input for first name, last name

    #end TODO

    #Stole below lines from driver of the write_db code
    conn = write_db.create_connection("gui_db.db")
    with conn:
        person = ('Rob', 'Thomas')
        person_id = write_db.create_person(conn, person)
        student = (person_id, 'Songwriting', '2000-01-01')
        student_id = write_db.create_student(conn, student)
    label.config(text="Student Entered")


def display_person():
    conn = write_db.create_connection("gui_db.db")
    with conn:
        rows = read_db.select_all_persons(conn)
        for row in rows:
            print(row)


def display_student():
    conn = write_db.create_connection("gui_db.db")
    with conn:
        rows = read_db.select_all_students(conn)
        for row in rows:
            print(row)


'''
Define functions/methods above here
'''

#create main window
m = tkinter.Tk()
'''
Insert module code below here
'''
##The Main Window Title that appears in the bar
m.title('Update and Access Person and Student Info') #replace this with whatever you would like

##Insert most of your main button code BELOW/between these --------------------------------------------------

person_fn_label = tkinter.Label(m, text="Enter Person's First Name:")
person_fn_label.grid(row=0, column=0, columnspan=2)

#TODO first name textbox
person_fn_textbox = tkinter.Entry(m, )
person_fn_textbox.grid(row=1, column=1, columnspan=3)

person_ln_label = tkinter.Label(m, text="Enter Person's Last Name:")
person_ln_label.grid(row=2, column=0, columnspan=2)

person_ln_textbox = tkinter.Entry(m, )
person_ln_textbox.grid(row=3, column=1, columnspan=3)

person_enter_button = tkinter.Button(m, text='Enter Person Info', width=30, command=insert_person)
person_enter_button.grid(row=4, columnspan=4)

#TODO create textboxes to hold name, major, and startdate


### Create a text label, put it 2nd from the bottom (since we have 6 rows, row 0 to 5)
label = tkinter.Label(m, text="No Selection Made") #label just displays Text
label.grid(row=10) #placing at 2nd from the bottom Row

##Insert most of your main button code ABOVE/between these --------------------------------------------------

##The Main window Exit/destroy function; Note Feel free to change it's "text='Exit'" to another
##     word like "text='Quit'" or whatever is relevent for you; as well as modify the width
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=11)

'''
Insert module code above here
'''



if __name__ == '__main__':
    create_db.create_tables("gui_db.db")
    m.mainloop()