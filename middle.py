
from tkinter import *

root = Tk()
root.title("Color Picker")
root.geometry("400x400")

def show_color(color_name, hex_code, color_name_entry, hex_code_entry):
    color_name_entry.delete(0, END)
    color_name_entry.insert(0, color_name)
    hex_code_entry.delete(0, END)
    hex_code_entry.insert(0, hex_code)

favorite_colors = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Purple": "#800080",
    "Orange": "#FFA500",
    "Cyan": "#00FFFF",
    "Pink": "#FFC0CB",
    "Brown": "#A52A2A",
    "Gray": "#808080"
}

for color_name, hex_code in favorite_colors.items():
    color_frame = Frame(root)
    color_frame.pack(side=TOP, padx=5, pady=5, fill=X)

    hex_code_entry = Entry(color_frame, width=10)
    hex_code_entry.pack(side=RIGHT)

    color_name_entry = Entry(color_frame, width=20)
    color_name_entry.pack(side=LEFT)


 
    color_button = Button(color_frame, text=color_name, bg=hex_code, width=20,command=lambda c=color_name, h=hex_code, c_entry=color_name_entry, h_entry=hex_code_entry: show_color(c, h, c_entry, h_entry))
    color_button.pack(side=LEFT)

root.mainloop()
