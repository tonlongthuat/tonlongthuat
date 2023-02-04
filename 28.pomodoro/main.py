from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_lable.config(text="TIMER",fg=GREEN)
    check_mark_label.config(text="")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_time=WORK_MIN*60
    short_break_time=SHORT_BREAK_MIN*60
    long_break_time=LONG_BREAK_MIN*60
    if reps ==8:
        reps==0
        count_down(long_break_time)
        title_lable.config(text="LONG REST",fg=RED)
    elif reps %2==0:
        count_down(short_break_time)
        title_lable.config(text="REST",fg=RED)
    else:
        count_down(work_time)
        title_lable.config(text="WORK",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    if count_min<10:
        count_min = f"0{count_min}" 
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        check_mark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=((FONT_NAME),35,"bold"))
canvas.grid(column=1,row=1)

title_lable=Label(text="TIMER",fg=GREEN,font=((FONT_NAME),30,"bold"),bg=YELLOW)
title_lable.grid(column=1,row=0)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark_label=Label(text="",bg=YELLOW,fg=GREEN)
check_mark_label.grid(column=1,row=4)


window.mainloop()