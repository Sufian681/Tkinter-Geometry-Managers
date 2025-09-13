from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="lightgrey")
lbl1 = Label(frame, text = "Full Name", bg="white", fg="black", width=12)
lbl2 = Label(frame, text = "Email Id", bg="white", fg="black", width=12)
lbl3 = Label(frame, text = "Enter Password", bg="white", fg="black", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "Hello " + name
    message = "\nCongratulations! You have successfully logged in."
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="lightgrey", fg="black")
btn = Button(text = "Create Account", command=display, bg="red", fg="white", width=12)

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
lbl2.place(x=20,y=70)
lbl3.place(x=20,y=120)
name_entry.place(x=150,y=20)
email_entry.place(x=150,y=70)
pass_entry.place(x=150,y=120)
btn.place(x=150,y=170)
textbox.place(x=20,y=220)

root.mainloop()