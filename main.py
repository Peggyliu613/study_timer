from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
study_or_break = 0
mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global study_or_break
    window.after_cancel(timer)
    study_or_break = 0
    canvas.itemconfig(time, text="00:00")
    check_mark.config(text="")
    title_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    title_label.config(text="Work")
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    global study_or_break
    global mark
    formatted_count = (str(count // 60) if count // 60 >= 10 else "0" + str(count // 60)) + ":" + (str(count % 60) if count % 60 >= 10 else "0" + str(count % 60))
    canvas.itemconfig(time, text=formatted_count)
    if count == 0:
        study_or_break += 1
        if study_or_break > 7:
            title_label.config(text="Timer")
            reset_timer()
        elif study_or_break == 7:
            title_label.config(text="Break", fg=PINK)
            count = LONG_BREAK_MIN * 20
        else:
            if study_or_break % 2 == 0:
                mark += "v"
                check_mark.config(text=mark)
                title_label.config(text="Work", fg=GREEN)
                count = 3
                # count = WORK_MIN * 60
            else:
                title_label.config(text="Break", fg=PINK)
                count = 3
                # count = SHORT_BREAK_MIN * 60
    timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Study Timer")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

check_mark = Label(text="", bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
