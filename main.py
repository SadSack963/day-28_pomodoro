import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
stop = True


# Print widget configuration
def print_config(widget, name):
    # Print to console
    # print(name + " Config:")
    # widget_config = widget.config()
    # for item in widget_config:
    #     print(item, widget_config[item])
    # print("\n")

    # (create a config directory in the project tree)
    # Write to text file
    widget_config = widget.config()
    filename = "./config/config_" + name + ".txt"
    with open(filename, mode="w") as file:
        for item in widget_config:
            file.write(f"{item}, {widget_config[item]}\n")


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, stop
    stop = True
    reps = 0
    label_activity["text"] = "Timer"
    label_activity["fg"] = GREEN
    label_tick["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    button_start["state"] = "active"


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer(work=WORK_MIN, short=SHORT_BREAK_MIN, long=LONG_BREAK_MIN):
    global reps, stop
    stop = False
    button_start["state"] = "disabled"
    if reps == 7:
        time = long * 60
        label_activity["text"] = "Long Break"
        label_activity["fg"] = RED
    elif reps % 2 == 0:
        time = work * 60
        label_activity["text"] = "Work"
        label_activity["fg"] = GREEN
    else:
        time = short * 60
        label_activity["text"] = "Short Break"
        label_activity["fg"] = PINK
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, stop
    if not stop:
        minutes = count // 60  # Floor operator
        seconds = count % 60  # Modulus operator
        # global canvas
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02}")
        # Subtract 1 from count every 1000ms
        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            if reps % 2 == 0:
                label_tick["text"] = label_tick["text"] + "✓"
            reps += 1
            if reps > 7:
                reps = 0
                label_tick["text"] = ""
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label_activity = tk.Label(text="Timer", width=11, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))

canvas = tk.Canvas(width=202, height=225, bg=YELLOW, highlightthickness=0)  # Slightly larger than image
image = tk.PhotoImage(file="tomato.png")
# x and y (tuple) specify the center of the image,
# manually adjust so that image is not cut off at edges
canvas.create_image(102, 113, image=image)
# Again, manually adjust for best appearance
timer_text = canvas.create_text((102, 131), text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))  # clock

button_start = tk.Button(text="Start", padx=5, pady=5, font=(FONT_NAME, 12, "bold"), command=start_timer)

button_reset = tk.Button(text="Reset", padx=5, pady=5, font=(FONT_NAME, 12, "bold"), command=reset_timer)

label_tick = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
# label_tick = tk.Label(text=u'\u2713')
# label_tick = tk.Label(text=u'\N{check mark}')

# Grid layout
label_activity.grid(row=0, column=1)
canvas.grid(row=1, column=1)
button_start.grid(row=2, column=0)
button_reset.grid(row=2, column=2)
label_tick.grid(row=3, column=1)


# -------------------
# print_config(widget=window, name="window")
# print_config(widget=canvas, name="canvas")
# print_config(widget=label_activity, name="label_activity")
# print_config(widget=button_start, name="button_start")
# print_config(widget=button_reset, name="button_reset")
# print_config(widget=label_tick, name="label_tick")  # Can't write unicode "check mark" to file?

# -------------------
window.mainloop()
