import pandas
from tkinter import *
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    words_to_learn_path = os.path.join(SCRIPT_DIR, "words_to_learn.csv")
    data = pandas.read_csv(words_to_learn_path)
except FileNotFoundError:
    try:
        csv_path = os.path.join(SCRIPT_DIR, "data", "spanish_words.csv")
        print(f"Attempting to read CSV from: {csv_path}")
        data = pandas.read_csv(csv_path)
    except Exception as e:
        print(f"Error reading CSV: {str(e)}")
        raise

dictionary_list = data.to_dict(orient='records')
rand_dict = random.choice(dictionary_list)


# BUTTON FUNCTIONS
def right_fun():
    global rand_dict
    dictionary_list.remove(rand_dict)
    rand_dict = random.choice(dictionary_list)
    reset_window()
    window.after(2100, flip)


def wrong_fun():
    global rand_dict
    rand_dict = random.choice(dictionary_list)
    reset_window()
    window.after(2100, flip)


# FLIP CARD
def flip():
    """Flip the card to the English side"""
    canvas.itemconfig(front_image, image=back_card)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(card_text, text=f"{rand_dict['English']}", fill="white")


# RESET WINDOW
def reset_window():
    """Set the window screen to the default"""
    canvas.itemconfig(front_image, image=front_card)
    canvas.itemconfig(lang_text, text="Spanish", fill="black")
    canvas.itemconfig(card_text, text=f"{rand_dict['Spanish']}", fill="black")


# UI INTERFACE
window = Tk()
window.title("Persis' FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "card_front.png"))
back_card = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "card_back.png"))

front_image = canvas.create_image(400, 265, image=front_card)
lang_text = canvas.create_text(400, 170, text="Spanish", font=("Arial", 30, "italic"))
card_text = canvas.create_text(400, 280, font=("Arial", 40, "bold"), text=f"{rand_dict['Spanish']}")
canvas.grid(row=0, column=0, columnspan=2)


# Canvas Text
my_right_image = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "right.png"))
right = Button(image=my_right_image, highlightthickness=0, command=right_fun, bd=-1)
right.grid(row=1, column=1)
my_wrong_image = PhotoImage(file=os.path.join(SCRIPT_DIR, "images", "wrong.png"))
wrong = Button(image=my_wrong_image, highlightthickness=0, bd=-1, command=wrong_fun)
wrong.grid(row=1, column=0)


# Start the first flip
window.after(2100, flip)


window.mainloop()

word_to_learn_list = pandas.DataFrame(dictionary_list)
word_to_learn_list.to_csv(os.path.join(SCRIPT_DIR, "words_to_learn.csv"), columns=["Spanish", "English"])