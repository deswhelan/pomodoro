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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(height=475, width=300)
window.config(background=YELLOW, pady=50)

canvas = Canvas(width=205, height=224, background=YELLOW, highlightthickness=0)
TOMATO_IMAGE = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=TOMATO_IMAGE)
canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill=YELLOW)
canvas.pack()

window.mainloop()