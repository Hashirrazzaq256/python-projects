from tkinter import *
import pandas
from  random import  choice
BACKGROUND_COLOR = "#B1DDC6"
french_word = {}
learn_cards = {}

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
         original_data = pandas.read_csv("data/french_words.csv")
         learn_cards = original_data.to_dict(orient = "records")
else:
    learn_cards = df.to_dict(orient="records")
    
    
def next_card():

    global french_word, flip_timer
    window.after_cancel(flip_timer)
    french_word = choice(learn_cards)
    canvas.itemconfig(card_title, text="French",fill= "black")
    canvas.itemconfig(card_word, text= french_word["French"], fill = "black")
    canvas.itemconfig(background_image,image = front_image)
    flip_timer= window.after(3000,func=back_card)


def back_card():
    canvas.itemconfig(card_title, text = "English",fill = "white")
    canvas.itemconfig(card_word, text = french_word["English"],fill = "white")
    canvas.itemconfig(background_image, image=back_image)


def known_card():
    learn_cards.remove(french_word)
    data = pandas.DataFrame(learn_cards)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()




#-----------------UI SETUP-----------------------
window = Tk()
window.title("Flash card app")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=back_card)
canvas = Canvas(height=526, width=800)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400,130 ,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,250,text="", font=("Ariel",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


# buttons
r_image = PhotoImage(file="images/right.png")
known_button = Button(image=r_image, highlightthickness=0, command=known_card)
known_button.grid(row=1,column=0)
w_image = PhotoImage(file="images/wrong.png")
button2 = Button(image=w_image, highlightthickness=0,command=next_card)
button2.grid(row=1,column=1)

next_card()
window.mainloop()
