"""
Program: gui_number_game.py
Author: Lily Ellison
Last date modified: 04/17/2023

The purpose of this program is to create a gui with a number guessing game.

"""
import tkinter
import random


class NumberGuesser:

    def __init__(self, g_list=[]):
        self.guessed_list = g_list
        #print(self.guessed_list)
        #print(len(self.guessed_list))

    def add_guess(self, g: int):
        self.guessed_list.append(g)
        #print(self.guessed_list) <- added for testing


game_win = tkinter.Tk()


def create_number():
    reactive()
    global num_guesser
    num_guesser = NumberGuesser()
    global rand_num
    rand_num = random.randint(1, 10)
    #print(rand_num) <- added for testing
    return rand_num


def guess(g: int):
    num_guesser.add_guess(g)
    if g == rand_num:
        display_winner()
    else:
        deactivate(g)


def guess_1():
    guess(1)


def guess_2():
    guess(2)


def guess_3():
    guess(3)


def guess_4():
    guess(4)


def guess_5():
    guess(5)


def guess_6():
    guess(6)


def guess_7():
    guess(7)


def guess_8():
    guess(8)


def guess_9():
    guess(9)


def guess_10():
    guess(10)


def reset_game():
    num_guesser.guessed_list.clear()
    create_number()
    reactive()


def display_winner():
    winner_win = tkinter.Tk()
    winner_win.title('WINNER!')

    w_label01 = tkinter.Label(winner_win, text="Yes! You guessed the number!")
    w_label01.grid(row=0, rowspan=2, columnspan=3)

    w_label02 = tkinter.Label(winner_win, text="Would you like to play again or exit?")
    w_label02.grid(row=2, rowspan=2, columnspan=3)

    play_button = tkinter.Button(winner_win, text='Play Again', width=30, pady=5, command=lambda: [reset_game(), winner_win.destroy()])
    play_button.grid(row=4, columnspan=3)

    close_button = tkinter.Button(winner_win, text='Exit', width=30, pady=5, command=lambda: [game_win.destroy(), winner_win.destroy()])
    close_button.grid(row=5, columnspan=3)


def deactivate(d: int):
    button_array[d-1]['state'] = tkinter.DISABLED


def reactive():
    for item in button_array:
        item['state'] = tkinter.NORMAL


"""make button inactive"""


game_win.title('Pick A Number')

label01 = tkinter.Label(game_win, text="Click 'Start' to start.")
label01.grid(row=0, columnspan=3)

start_button = tkinter.Button(game_win, text='Start', width=30, pady=5, command=create_number)
start_button.grid(row=1, columnspan=3)

label02 = tkinter.Label(game_win, text="Guess a number: ")
label02.grid(row=2, columnspan=3)


button_array = []

button_1 = tkinter.Button(game_win, text='1', width=9, command=guess_1)
button_1.grid(row=3, column=0)
button_array.append(button_1)

button_2 = tkinter.Button(game_win, text='2', width=9, command=guess_2)
button_2.grid(row=3, column=1)
button_array.append(button_2)

button_3 = tkinter.Button(game_win, text='3', width=9, command=guess_3)
button_3.grid(row=3, column=2)
button_array.append(button_3)


button_4 = tkinter.Button(game_win, text='4', width=9, command=guess_4)
button_4.grid(row=4, column=0)
button_array.append(button_4)

button_5 = tkinter.Button(game_win, text='5', width=9, command=guess_5)
button_5.grid(row=4, column=1)
button_array.append(button_5)

button_6 = tkinter.Button(game_win, text='6', width=9, command=guess_6)
button_6.grid(row=4, column=2)
button_array.append(button_6)


button_7 = tkinter.Button(game_win, text='7', width=9, command=guess_7)
button_7.grid(row=5, column=0)
button_array.append(button_7)

button_8 = tkinter.Button(game_win, text='8', width=9, command=guess_8)
button_8.grid(row=5, column=1)
button_array.append(button_8)

button_9 = tkinter.Button(game_win, text='9', width=9, command=guess_9)
button_9.grid(row=5, column=2)
button_array.append(button_9)


button_10 = tkinter.Button(game_win, text='10', width=9, command=guess_10)
button_10.grid(row=6, column=1)
button_array.append(button_10)

reset_button = tkinter.Button(game_win, text='Reset', width=30, pady=5, command=reset_game)
reset_button.grid(row=7, columnspan=3)

exit_button = tkinter.Button(game_win, text='Exit', width=30, pady=5, command=game_win.destroy)
exit_button.grid(row=8, columnspan=3)

for nums in range(0, 11):
    deactivate(nums)

game_win.mainloop()
