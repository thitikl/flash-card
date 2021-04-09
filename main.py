from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# Setup random French
def random_word_french():
    global french_word
    french_word = random.choice(list(word_dict.keys()))
    canvas.itemconfig(title_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=french_word, fill="black")


# Setup random English
def random_word_eng():
    eng_word = word_dict[french_word]
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=eng_word, fill="white")


# Change canvas color
def flip_card_back():
    canvas.itemconfig(canvas_image, image=back_image)
    random_word_eng()


# Change canvas color
def flip_card_front():
    global wait_flip
    window.after_cancel(wait_flip)
    canvas.itemconfig(canvas_image, image=front_image)
    random_word_french()
    wait_flip = window.after(3000, func=flip_card_back)


# Removing known word from the flash card
def check():
    del word_dict[french_word]
    print(len(word_dict))
    flip_card_front()


# setup word dict
data_file = pandas.read_csv("data/french_words.csv")
word_dict = {row.French: row.English for (index, row) in data_file.iterrows()}

# Window setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

back_image = PhotoImage(file="images/card_back.png")

# setup button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=check)
check_button.grid(column=0, row=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=flip_card_front)
cross_button.grid(column=1, row=1)

# Word label
title_label = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="214", font=("Arial", 60, "bold"))

french_word = random.choice(list(word_dict.keys()))

wait_flip = window.after(3000, func=flip_card_back)
flip_card_front()

window.mainloop()
