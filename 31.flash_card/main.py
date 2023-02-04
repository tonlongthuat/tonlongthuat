from tkinter import *
import pandas 
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME="Arial"
current_card={}
# word
try:
    data=pandas.read_csv("./to_learn.csv")
except:
    data=pandas.read_csv("./eng_flash_card.csv")
finally:
    to_learn=data.to_dict(orient="records")
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)  
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_card["english"],fill="black")
    canvas.itemconfig(canvas_img,image=old_img)
    flip_timer=window.after(3000,flip_card)
    
def flip_card():
    canvas.itemconfig(card_title,text="Vietnamese",fill="white")
    canvas.itemconfig(card_word,text=current_card["vietnamese"],fill="white")
    canvas.itemconfig(canvas_img,image=new_img)
def is_known():
    to_learn.remove(current_card)
    to_learn_data=pandas.DataFrame(to_learn)
    to_learn_data.to_csv("./to_learn.csv",index=False)
    next_card()
# UI
window=Tk()
window.title("Flash card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
old_img=PhotoImage(file="./images/card_front.png")
new_img=PhotoImage(file="./images/card_back.png")
canvas_img=canvas.create_image(400,263,image=old_img)
card_title=canvas.create_text(400,150,text="eng",fill="black",font=(FONT_NAME,40,"italic"))
card_word=canvas.create_text(400,263,text="vi",fill="black",font=(FONT_NAME,60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
# flip card

wrong_img=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_img=PhotoImage(file="./images/right.png")
right_button=Button(image=right_img,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()
