"""
Program: db_gui_assignment.py
Author: Lily Ellison
Last date modified: 04/18/2023

The purpose of this program is to create databases for the
person and student information with a gui for user interaction.

"""


import create_db
import read_db
import write_db
import tkinter


def create_student_and_person_table():
    # Create the database:
    create_db.create_tables('gui_db.db')


#global variables
fname = ""
lname = ""
major = ""
sdate = ""


def name_is_valid(name: str) -> bool:
    """
    Checks if names for first name, last name, and major are valid
    :param name: the string being tested (first/last name or major)
    :return: true if valid, false if not
    """
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
    return name_characters.issuperset(name) and name != ""


def invalid_alert(category: str):
    """
    Opens a new window with an alert
    :param category: where the invalid entry occurred (last/first name, major, or date fields)
    :return: none, opens a gui window
    """
    i = tkinter.Tk()
    i.geometry("300x100")
    i.title('INVALID ENTRY!')

    invalid_info = category + " ENTRY INVALID. PLEASE TRY AGAIN."
    person_info_label = tkinter.Label(i, text=invalid_info)
    person_info_label.pack()

    close_button = tkinter.Button(i, text="Close", command=lambda: [i.destroy(), reset_form()])
    close_button.pack(side='bottom', pady="10")


def insert_person():
    """
    Makes an entry for a person on the person table
    :return: None, creates db entry or notifies user of invalid entry
    """

    #Stole below lines from driver of the write_db code and modified them
    conn = write_db.create_connection("gui_db.db")
    with conn:
        first = fn_contents.get()
        last = ln_contents.get()
        if name_is_valid(first):
            if name_is_valid(last):
                person = (first, last)
                person_id = write_db.create_person(conn, person)
                label.config(text="Person Entered")
                activate_student_option()
            else:
                invalid_alert("LAST NAME")
                label.config(text="Invalid Last Name. Please Try Again.")
        else:
            invalid_alert("FIRST NAME")
            label.config(text="Invalid First Name. Please Try Again.")


def find_person(conn, last, first):
    """
    Searches person database for the first instance of the person with the first and last name of the student being
    entered to match student to person id
    :param conn: db connection
    :param last: last name of person
    :param first: first name of person
    :return: the person's id as a string
    """
    cur = conn.cursor()
    cur.execute("SELECT id FROM person WHERE lastname = '" + last + "' AND firstname = '" + first + "'")
    info_list = cur.fetchall()
    person_id_list = info_list[0]
    person_id = person_id_list[0]
    print(person_id)
    return str(person_id)
'''
This was very tricky to get the syntax and types correct for searching the database and bringing back the one piece
of information. I know it's not the best way, but it seems to work. I hope I did it right.
'''


def date_is_valid(sd: str) -> bool:
    """
    Checks that date is in YYYY/MM/DD format. Probably should have used a date object, but time is ticking
    :param sd: Start date, as entered by the user
    :return: true if valid, false otherwise
    """
    length = 10
    valid_chars = set("0123456789/")
    dash = "/"
    first_dash = 4
    second_dash = 7
    return len(sd) == length and valid_chars.issuperset(sd) and sd != "" and sd.find(dash) == first_dash and \
        sd.rfind(dash) == second_dash and sd.count(dash) == 2
    #if all of the above conditions are true, the date is in a valid format.


def insert_student():
    """
    Adds a new student object to the student table using the information the user provides after validation
    :return: none. Either adds the student information or gives an invalid entry alert
    """
    #Stole below lines from driver of the write_db code
    conn = write_db.create_connection("gui_db.db")
    with conn:
        major = m_contents.get()
        start_date = sd_contents.get()
        if name_is_valid(major):
            if date_is_valid(start_date):
                person_id = find_person(conn, ln_contents.get(), fn_contents.get())
                student = (person_id, major, start_date)
                student_id = write_db.create_student(conn, student)
                label.config(text="Student Entered")
            else:
                invalid_alert("START DATE")
                label.config(text="Invalid Start Date. Please Try Again.")
        else:
            invalid_alert("MAJOR")
            label.config(text="Invalid Major. Please Try Again.")


def display_person():
    """
    Gets info from the person table to be displayed
    :return: Person table information as strings, each person on a new line.
    """
    conn = write_db.create_connection("gui_db.db")
    row_string = ""
    with conn:
        rows = read_db.select_all_persons(conn)
        for row in rows:
            for item in row:
                row_string += str(item) + " "
            row_string += "\n"
        return row_string


def create_person_display():
    """
    Creates a new window to display the information from the person table on the gui
    :return: None. Opens a new window with information.
    """
    p = tkinter.Tk()
    p.geometry("400x200")
    p.title('Person Table Information:')

    p_info = display_person()

    person_info_label = tkinter.Label(p, text=p_info)
    person_info_label.pack()

    close_button = tkinter.Button(p, text="Close", command=p.destroy)
    close_button.pack(side='bottom', pady="10")


def display_student():
    """
    Gets student info to be displayed
    :return: student info from table as strings, each student on a new line
    """
    conn = write_db.create_connection("gui_db.db")
    row_string = ""
    with conn:
        s_rows = read_db.select_all_students(conn)
        for row in s_rows:
            for item in row:
                row_string += str(item) + " "
            row_string += "\n"
        return row_string


def create_student_display():
    """
    Creates a new window to display student info
    :return: None. Creates a window
    """
    p = tkinter.Tk()
    p.geometry("400x200")
    p.title('Student Table Information:')

    s_info = display_student()

    student_info_label = tkinter.Label(p, text=s_info)
    student_info_label.pack()

    close_button = tkinter.Button(p, text="Close", command=p.destroy)
    close_button.pack(side='bottom', pady="10")


def activate_student_option():
    """
    Activates the student information fields.
    :return: Active fields
    """
    student_m_label['state'] = tkinter.NORMAL
    student_m_textbox['state'] = tkinter.NORMAL
    student_sd_label['state'] = tkinter.NORMAL
    student_sd_textbox['state'] = tkinter.NORMAL


def reset_form():
    """
    Clears the entry textboxes and disables the student information fields, prepares for a new entry.
    :return: Cleared entry textboxes and disabled fields
    """
    person_fn_textbox.delete(0, 'end')
    person_ln_textbox.delete(0, 'end')
    student_m_textbox.delete(0, 'end')
    student_sd_textbox.delete(0, 'end')
    student_m_label['state'] = tkinter.DISABLED
    student_m_textbox['state'] = tkinter.DISABLED
    student_sd_label['state'] = tkinter.DISABLED
    student_sd_textbox['state'] = tkinter.DISABLED


#create main window
m = tkinter.Tk()

##The Main Window Title that appears in the bar
m.title('Update and Access Person and Student Info')
m.geometry("300x450")

#Person info: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
person_fn_label = tkinter.Label(m, text="Enter Person's First Name:")
person_fn_label.grid(row=0, column=0, pady=10)


person_fn_textbox = tkinter.Entry(m, )
person_fn_textbox.grid(row=0, column=1, columnspan=2, pady=10)
fn_contents = tkinter.StringVar()
fn_contents.set("")
person_fn_textbox["textvariable"] = fn_contents

person_ln_label = tkinter.Label(m, text="Enter Person's Last Name:")
person_ln_label.grid(row=1, column=0, pady=10)

person_ln_textbox = tkinter.Entry(m, )
person_ln_textbox.grid(row=1, column=1, columnspan=2, pady=10)
ln_contents = tkinter.StringVar()
ln_contents.set("")
person_ln_textbox["textvariable"] = ln_contents

person_enter_button = tkinter.Button(m, text='Enter Person Info', width=30, command=insert_person)
person_enter_button.grid(row=2, column=0, columnspan=3, pady=10)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Student Info ---------------------------------------------------------------
student_m_label = tkinter.Label(m, text="Student's Major: ", state=tkinter.DISABLED)
student_m_label.grid(row=3, column=0, pady=10)

student_m_textbox = tkinter.Entry(m, state=tkinter.DISABLED)
student_m_textbox.grid(row=3, column=1, columnspan=2, pady=10)
m_contents = tkinter.StringVar()
m_contents.set("")
student_m_textbox["textvariable"] = m_contents

student_sd_label = tkinter.Label(m, text="Student's Start Date: ", state=tkinter.DISABLED)
student_sd_label.grid(row=4, column=0, pady=(10, 0))

student_sdf_label = tkinter.Label(m, text="Format: YYYY/MM/DD", state=tkinter.DISABLED)
student_sdf_label.grid(row=5, column=0, pady=(0, 10))
#This label stays "disabled" as I liked the way it looked, it's just a reminder

student_sd_textbox = tkinter.Entry(m, state=tkinter.DISABLED)
student_sd_textbox.grid(row=4, column=1, columnspan=2, pady=10)
sd_contents = tkinter.StringVar()
sd_contents.set("")
student_sd_textbox["textvariable"] = sd_contents

student_enter_button = tkinter.Button(m, text='Enter Student Info', width=30, command=insert_student)
student_enter_button.grid(row=6, columnspan=3)
#-------------------------------------------------------------------------------

#Other buttons and info display ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
reset_button = tkinter.Button(m, text='Reset', width=30, command=reset_form)
reset_button.grid(row=7, columnspan=3, pady=10)

display_person_button = tkinter.Button(m, text='Display Person Table', command=create_person_display)
display_person_button.grid(row=8, column=0, pady=10)

display_student_button = tkinter.Button(m, text='Display Student Table', command=create_student_display)
display_student_button.grid(row=8, column=2, pady=10)

label = tkinter.Label(m, text="No Entry Made")
label.grid(row=9, columnspan=3, pady=10)

exit_button = tkinter.Button(m, text='Exit', command=m.destroy, width=30)
exit_button.grid(row=10, columnspan=3)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Driver
if __name__ == '__main__':
    create_db.create_tables("gui_db.db")
    m.mainloop()