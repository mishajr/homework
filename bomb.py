from tkinter import *

bomb = 100
score = 0
press_return = True
best_score = 0

def save_best_score(score):
    try:
        with open("best_score.txt", "r") as file:
            best_score = int(file.read())
            if score > best_score:
                with open("best_score.txt", "w") as file:
                    file.write(str(score))
    except FileNotFoundError:
        with open("best_score.txt", "w") as file:
            file.write(str(score))

def load_best_score():
    global best_score
    try:
        with open("best_score.txt", "r") as file:
            best_score = int(file.read())
            label_best_score.config(text="Best Score: " + str(best_score), font=("Comic Sans MS", 16))
    except FileNotFoundError:
        label_best_score.config(text="Best Score: 0", font=("Comic Sans MS", 15))

def start(event):
    global press_return, bomb, score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text="")
        uptade_display()
        update_point()
        update_bomb()
        press_return = False

def uptade_display():
    global bomb, score
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb < 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse: " + str(bomb))
    score_label.config(text="Score: " + str(score))
    fuse_label.after(100, uptade_display)

def update_bomb():
    global bomb
    bomb -= 20
    if is_alive():
        fuse_label.after(4000, update_bomb)

def update_point():
    global score
    score += 1
    if is_alive():
        score_label.after(3000, update_point)

def click():
    global bomb
    if is_alive():
        bomb += 1

def is_alive():
    global bomb, press_return
    if bomb <= 0:
        label.config(text="Bang Bang!")
        press_return = True
        save_best_score(score)  
        load_best_score()  
        return False
    else:
        return True

root = Tk()
root.title("bang bang")

root.geometry("500x550")
label = Label(root, text="press Enter to start", font=("Comic Sans MS", 12))
label.pack()

fuse_label = Label(root, text="Fuse: " + str(bomb), font=("Comic Sans MS", 14))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=("Comic Sans MS", 14))
score_label.pack()

label_best_score = Label(root, text="Best Score: " + str(best_score), font=("Comic Sans MS", 14))
label_best_score.pack()

no_photo = PhotoImage(file="homework/image/bomb_no.gif")
normal_photo = PhotoImage(file="homework/image/bomb_normal.gif")
bang_photo = PhotoImage(file="homework/image/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text="Click mek", font=('Conic Sans MS', 14), bg='#000000', fg='#ffffff', command=click, width=15)
click_button.pack()

root.bind("<Return>", start)

root.mainloop()
