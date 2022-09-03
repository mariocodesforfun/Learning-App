import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("/Users/mariogegprifti/Desktop/learn/python course/capstoneproject/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# /Users/mariogegprifti/Desktop/learn/python course/capstoneproject/data/french_words.csv
data = pandas.read_csv("/Users/mariogegprifti/Desktop/learn/python course/capstoneproject/data/french_words.csv", on_bad_lines='skip')
to_learn = data.to_dict(orient="records")
# print(data_list)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data_file = pandas.DataFrame(to_learn)
    data_file.to_csv("data/to_learn.csv", index=False)
    next_card()


window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)


canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage("/Users/mariogegprifti/Desktop/learn/capstoneproject/images/card_front.png")
card_back_image = tkinter.PhotoImage("/Users/mariogegprifti/Desktop/learn/capstoneproject/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(500, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(500, 263, text="word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


cross_image = tkinter.PhotoImage(file="/Users/mariogegprifti/Desktop/learn/python course/capstoneproject/images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)


check_image = tkinter.PhotoImage(file="/Users/mariogegprifti/Desktop/learn/python course/capstoneproject/images/right.png")
known_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=2)


next_card()


window.mainloop()


