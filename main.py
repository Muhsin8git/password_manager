from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)

    pas = "".join(password)
    password_entry.insert(string=pas,index=0)
    pyperclip.copy(pas)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_entry.get()
    username = email_user_entry.get()
    password_given = password_entry.get()
    data_dic = {
        web:{
            "username":username,
            "password":password_given,

        }
    }
    if len(web) ==0 or len(password_given) ==0:
        messagebox.showerror(title="Error", message="Please give input")
    else:
        try:
            with open("password_manager.json",mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password_manager.json", mode="w") as file:
                json.dump(data_dic,file, indent=4)
        else:
            data.update(data_dic)
            with open("password_manager.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

                website_entry.delete(0,END)
                password_entry.delete(0,END)
def find_password():
    web = website_entry.get()
    try:
        with open("password_manager.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="No Data Yet Saved")
    else:
        if web not in data:
            messagebox.showerror(message="Not Found")
        else:
            user = data[web]["username"]
            password = data[web]["password"]
            messagebox.showinfo(title=web ,message=f"User:{user}\n password:{password}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website = Label(text="Website:", )
website.grid(row=1,column=0)
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1,column=1)
web_search = Button(text="Search", command=find_password)
web_search.grid(row=1, column=2)
email_user = Label(text="Email/Username:")
email_user.grid(row=2,column=0)
email_user_entry = Entry(width=21)
email_user_entry.insert(0,"muhsin@gmail.com")
email_user_entry.grid(row=2,column=1,)
password = Label(text="Password")
password.grid(row=3,column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)
generate_password_button = Button(text="Generate Password", command=generate)
generate_password_button.grid(row=3,column=2)
add_button =Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)



window,mainloop()