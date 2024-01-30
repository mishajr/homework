from tkinter import *




from tkinter import *

cookie = 100
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
    global press_return, cookie, score
    if not press_return:
        pass
    else:
        cookie = 100
        score = 0
        label.config(text="")
        uptade_display()
        update_point()
        update_bomb()
        press_return = False

def uptade_display():
    global cookie, score
    if cookie > 50:
       cookie_button.config(image=normal_photo)
    elif 0 < cookie < 50:
        cookie_button.config(image=no_photo)
    else:
        cookie_button.config(image=bang_photo)
    fuse_label.config(text="Fuse: " + str(cookie))
    score_label.config(text="Score: " + str(score))
    fuse_label.after(100, uptade_display)

def update_bomb():
    global cookie
    cookie -= 20
    if is_alive():
        fuse_label.after(4000, update_bomb)

def update_point():
    global score
    score += 1
    if is_alive():
        score_label.after(3000, update_point)

def click():
    global cookie
    if is_alive():
        cookie += 1

def is_alive():
    global cookie, press_return
    if cookie <= 0:
        label.config(text="Cookie is dead!")
        press_return = True
        save_best_score(score)  
        load_best_score()  
        return False
    else:
        return True

root = Tk()
root.title("Cookie Clicker")

root.geometry("500x550")
label = Label(root, text="press Enter to start", font=("Comic Sans MS", 12))
label.pack()

fuse_label = Label(root, text="Fuse: " + str(cookie), font=("Comic Sans MS", 14))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=("Comic Sans MS", 14))
score_label.pack()

label_best_score = Label(root, text="Best Score: " + str(best_score), font=("Comic Sans MS", 14))
label_best_score.pack()

normal_photo = PhotoImage(file="homework/image_cookie/380ad8e64053f28077ef9e309d76c765_w200.gif")
no_photo = PhotoImage(file="homework/image_cookie/3580617sz0ygexqpz.gif")
bang_photo = PhotoImage(file="homework/image_cookie/giphy.gif")

cookie_button = Button(root, image=normal_photo, command=click)
cookie_button.pack(pady=10)



root.bind("<Return>", start)

root.mainloop()
