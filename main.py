from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
CHECKS = []
MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- #
def restart():
    global reps, timer, CHECKS, label
    windows.after_cancel(timer)
    canvas.itemconfig(text, text=f"00:00")
    label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    reps = 0
    CHECKS = []
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        cdown(LONG_BREAK_MIN*60)
        label.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        cdown(SHORT_BREAK_MIN*60)
        label.config(fg=PINK, text="Break")
    else:
        cdown(WORK_MIN*60)
        label.config(fg=GREEN, text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def cdown(count):
    global reps, timer
    if count >= 0:
        if count >= 60:
            if count // 60 < 10 and count % 60 >= 10:
                canvas.itemconfig(text, text=f"0{math.floor(count / 60)}:{count % 60}")
            elif count // 60 < 10 and count % 60 < 10:
                canvas.itemconfig(text, text=f"0{math.floor(count / 60)}:0{count % 60}")
            elif count // 60 >= 10 and count % 60 < 10:
                canvas.itemconfig(text, text=f"{math.floor(count / 60)}:0{count % 60}")
            elif count // 60 >= 10 and count % 60 >= 10:
                canvas.itemconfig(text, text=f"{math.floor(count / 60)}:{count % 60}")

        else:
            if count % 60 >= 10:
                canvas.itemconfig(text, text=f"00:{count}")
            else:
                canvas.itemconfig(text, text=f"00:0{count}")
        timer = windows.after(1000, cdown, count - 1)
    else:
        if reps % 2 != 0:
            CHECKS.append(MARK)
            label2.config(text=f"{''.join(CHECKS)}")
        else:
            label2.config(text=f"{''.join(CHECKS)}")
        start()



# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Productivity Tomatty!")
windows.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pic)
text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button1 = Button(text="Start", command=start, highlightthickness=0)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=restart, highlightthickness=0)
button2.grid(column=2, row=2)

label2 = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

windows.mainloop()
