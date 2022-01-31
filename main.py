from typing import Optional, Any
THEME_COLOR = "#375362"
FONT=("Arial",15,"italic")
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
selected={}
score=0
generate_word={}
try:
    generate_word=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    generate_word=pd.read_csv("data/french_words.csv")
else:
    generate_word=generate_word.to_dict(orient="records")
def randomwords():
    # with open("data/french_words.csv","r") as generate_word:
    #     random_flines=generate_word.read().splitlines()
    #     return list(random.choice(random_flines).split(","))
    global selected,flip_timer
    window.after_cancel(flip_timer)

    selected=random.choice(generate_word)

    canvas.itemconfig(text_word,text=selected["French"],fill="black")
    canvas.itemconfig(text_lang,text="French",fill="black")
    canvas.itemconfig(photo,image=cardfront)
    flip_timer=window.after(3000,change_image)

def change_image():
    canvas.itemconfig(photo, image=card_open)
    canvas.itemconfig(text_lang,text="English",fill="white")
    canvas.itemconfig(text_word, text=selected['English'],fill="white")

def is_known():
    generate_word.remove(selected)
    print(len(generate_word))
    global score
    score+=1
    label.config(text=f"Score: {score}")
    data=pd.DataFrame(generate_word)
    data.to_csv("data/words_to_learn.csv",index=False);
    randomwords()

window = Tk()
window.title("FlashCard App")
window.config(bg=BACKGROUND_COLOR,padx=40,pady=40)
flip_timer=window.after(3000, change_image)
#delay




label=Label(text=f"Score: {score}")
label.grid(row=0,column=0)
canvas =Canvas(width="800",height="526",highlightthickness=0,bg=BACKGROUND_COLOR)
card_open=PhotoImage(file="images/card_back.png")
cardfront=PhotoImage(file="images/card_front.png")
photo=canvas.create_image(400,263,image=cardfront)
text_lang=canvas.create_text(400, 150, text='French',font="Arial 40 italic")
text_word=canvas.create_text(400,263,text="",font="Arial 60 bold")
canvas.grid(row=1,column=0,columnspan=2)

#Buttons
tick_image = PhotoImage(file="images/right.png")
correct = Button(image=tick_image, highlightthickness=0,command=is_known)
correct.grid(column=0,row=2)
cross_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=cross_image, highlightthickness=0,command=randomwords)
wrong.grid(row=2,column=1)
randomwords()


window.mainloop()
