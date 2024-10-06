import pandas
from tkinter import *
import random
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/spanish_words.csv")

dictionary_list = data.to_dict(orient='records')
rand_dict = random.choice(dictionary_list)


# BUTTON FUNCTIONS
def right_fun():
    global rand_dict
    dictionary_list.remove(rand_dict)
    rand_dict = random.choice(dictionary_list)
    reset_window()
    wait()


def wrong_fun():
    global rand_dict
    rand_dict = random.choice(dictionary_list)
    reset_window()
    wait()


# FLIP CARD
def flip():
    """Flip the card to the English side"""
    canvas.itemconfig(front_image, image=back_card)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(card_text, text=f"{rand_dict['English']}", fill="white")
    window.update()


# RESET WINDOW
def reset_window():
    """Set the window screen to the default"""
    canvas.itemconfig(front_image, image=front_card)
    canvas.itemconfig(lang_text, text="Spanish", fill="black")
    canvas.itemconfig(card_text, text=f"{rand_dict['Spanish']}", fill="black")
    window.update()


# WAIT TIME
def wait():
    """Replace the after Tk() method"""
    window.update()
    sleep(2.1)
    flip()


# UI INTERFACE
window = Tk()
window.title("Persis' FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_front.png")

front_image = canvas.create_image(400, 265, image=front_card)
lang_text = canvas.create_text(400, 170, text="Spanish", font=("Arial", 30, "italic"))
card_text = canvas.create_text(400, 280, font=("Arial", 40, "bold"), text=f"{rand_dict['Spanish']}")
canvas.grid(row=0, column=0, columnspan=2)


# Canvas Text
my_right_image = PhotoImage(file="./images/right.png")
right = Button(image=my_right_image, highlightthickness=0, command=right_fun, bd=-1)
right.grid(row=1, column=1)
my_wrong_image = PhotoImage(file="./images/right.png")
wrong = Button(image=my_wrong_image, highlightthickness=0, bd=-1, command=wrong_fun)
wrong.grid(row=1, column=0)


# manage sleep for first loop
count = 0
if count == 0:
    wait()


window.mainloop()

word_to_learn_list = pandas.DataFrame(dictionary_list)
word_to_learn_list.to_csv("words_to_learn.csv", columns=["Spanish", "English"])