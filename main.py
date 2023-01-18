from tkinter import *
import pandas
import pandas as pd
import random

BACK_GROUND = "#FFFAF0"
current_word = {}
to_learn = {}

# ------------------------    Reading the data from CSV file and creating new CSV to learn new words-------------------
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Data_sheet.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#-------------------------------------------Randomising words-----------------------------------------------------------
def flash_words():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(title, text="Português", fill="black")
    canvas.itemconfig(word, text=current_word["Portugues"], fill="black")
    canvas.itemconfig(image_config, image=card_front)
    flip_timer = window.after(6000, func=flash_words)

# ----------------------------------------Showing the English Words-----------------------------------------------------
def flip_card():
    canvas.itemconfig(title, text="English Translation", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(image_config, image=back_img)

def right_words():
    to_learn.remove(current_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    flash_words()

#---------------------------------------------------Creating UI--------------------------------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACK_GROUND)
flip_timer = window.after(3000, func=flash_words)

canvas = Canvas(width=800, height=526, )
card_front = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
right_button = PhotoImage(file="right.png")
wrong_button = PhotoImage(file="wrong.png")

image_config = canvas.create_image(400, 260, image=card_front)
img_settings = canvas.config(bg=BACK_GROUND, highlightthickness=0)
title = canvas.create_text(400, 90, text="", font=("Arial", 30, "italic"))
word = canvas.create_text(400, 250, text="", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=1)

#--------------------------------------------Creating Buttons----------------------------------------------------------
button_green = Button(image=right_button, bg=BACK_GROUND, highlightthickness=0, borderwidth=0, command=right_words)
button_green.grid(row=3, column=2, )

button_red = Button(image=wrong_button, bg=BACK_GROUND, highlightthickness=0, borderwidth=0, command=flip_card)
button_red.grid(row=3, column=0)


flash_words()

window.mainloop()
