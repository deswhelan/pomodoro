import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1500)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if count >= 0:
        minutes = math.floor(count/60)
        seconds = count % 60

        if seconds < 10:
            seconds = "0" + str(seconds)

        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        window.after(100, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(height=475, width=300)
window.config(background=YELLOW, padx=50, pady=50)

canvas = Canvas(width=205, height=224, background=YELLOW, highlightthickness=0)
TOMATO_IMAGE = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=TOMATO_IMAGE)
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill=YELLOW)
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", command=start_timer, background=PINK, foreground=YELLOW)
start_button.grid(column=1, row=3)

def reset_timer():
    print("Timer reset!")
start_button = Button(text="Reset", command=reset_timer, background=PINK, foreground=YELLOW)
start_button.grid(column=3, row=3)

pomodoros_completed_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
pomodoros_completed_label.grid(column=2, row=4)

window.mainloop()