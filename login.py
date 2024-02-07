
from tkinter import *
from tkinter import messagebox
import pickle


def registration():
    label_error = None
    frame = Frame(root,bd=18)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")
    label = Label(frame, text="Sign up",font='16')
    label.place(relwidth=1, relheight=0.1)
    label_login = Label(frame, text="Login :")
    label_login.place(rely=0.2,relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)
    
    label_password1 = Label(frame, text="Password :")
    label_password1.place(rely=0.4,relwidth=0.35, relheight=0.1)
    password1 = Entry(frame, show="*")
    password1.place(rely=0.4,relwidth=0.55, relheight=0.1, relx=0.4)

    label_password2 = Label(frame, text="Password :")
    label_password2.place(rely=0.6,relwidth=0.35, relheight=0.1)
    password2 = Entry(frame, show="*")
    password2.place(rely=0.6,relwidth=0.55, relheight=0.1, relx=0.4)

    button = Button(frame, text="Sign up" , command= lambda: sign_up())
    button.place(rely=0.8, relwidth=0.5, relheight=0.15, relx=0.3)
    def sign_up():
        nonlocal label_error
        error = ""
        if label_error:
            label_error.destroy()
        if len(login_register.get()) == 0:
            error = "*Login error"
        elif len(password1.get()) < 5:
            error = "*your password is too short. it must be at least 5 characters"
        elif not password1.get() == password2.get():
            error = "*passwords error"
        else:
            save()
        label_error = Label(frame, text=error, fg="red")
        label_error.place(rely=0.7)
    def save():
        data = dict()
        data[login_register.get()] = password1.get()
        with open("login.txt", "wb") as f:
            pickle.dump(data, f)
        login_form()


def login_form():
    frame = Frame(root,bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")
    label = Label(frame, text="Sign in",font='16')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text="Login :")
    label_login.place(rely=0.2,relwidth=0.35, relheight=0.1)

    enter_login = Entry(frame)
    enter_login.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)
    
    label_password = Label(frame, text="Password :")
    label_password.place(rely=0.4,relwidth=0.35, relheight=0.1)

    enter_password = Entry(frame, show="*")
    enter_password.place(rely=0.4,relwidth=0.55, relheight=0.1, relx=0.4)

    button = Button(frame, text="Sign in", command=lambda: login_pass())
    button.place(rely=0.8, relwidth=0.5, relheight=0.15, relx=0.3)
    def login_pass():
        with open("login.txt", "rb") as f:
            a = pickle.load(f)
        
        if enter_login.get() in a and enter_password.get() == a[enter_login.get()]:
            messagebox.showinfo("Welcome", "You are logged in")
        else:
            messagebox.showerror("Error", "Login or password is incorrect")




root = Tk()
root.title("login form")
root.geometry("500x550")
root.resizable(False, False)
root.option_add("*Font", "SegoeUI 12")
root.option_add("*Background", "gray")

img = PhotoImage(file="image_login/bg2.gif")
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text="Sign up", bg="gray", command=registration)
button_signup.place(relx=0.2, rely=0.1,relwidth=0.3)

button_signin = Button(root, text="Sign in", bg="gray", command=login_form)
button_signin.place(relx=0.5, rely=0.1,relwidth=0.3)


root.mainloop()




