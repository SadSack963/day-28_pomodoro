import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# Print widget configuration
def print_config(widget, name):
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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_activity = tk.Label(text="Timer")

canvas = tk.Canvas(width=202, height=225)  # Slightly larger than image
image = tk.PhotoImage(file="tomato.png")
# x and y (tuple) specify the center of the image, adjust so that image is not cut off at edges
canvas.create_image((102, 113), image=image)
canvas.create_text((102, 131), text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))  # clock
canvas["bg"] = YELLOW
canvas["highlightthickness"] = 0

button_start = tk.Button(text="Start")

button_reset = tk.Button(text="Reset")

label_tick = tk.Label(text="ü")

# Grid layout
label_activity.grid(row=0, column=1)
canvas.grid(row=1, column=1)


# -------------------
print_config(widget=window, name="window")
print_config(widget=canvas, name="canvas")
print_config(widget=label_activity, name="label_activity")
print_config(widget=button_start, name="button_start")
print_config(widget=button_reset, name="button_reset")
print_config(widget=label_tick, name="label_tick")

# -------------------
window.mainloop()