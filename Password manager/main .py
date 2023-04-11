from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json


# --------------generating password-------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_number + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

def save():
        website = website_entry.get()
        email = email_entry.get()
        password_input = password_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password_input
            }
        }
        if len(website) == 0 or len(password_input) == 0:
            messagebox.showerror(title="error", message="Don't leave any fields empty")
        else:
            try:
                with open("data.json", "r") as data:
                    data_file = json.load(data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                data_file.update(new_data)
                with open("data.json", "w") as data:
                    json.dump(data_file, data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

def search_credentials():

    search_website=  website_entry.get()
    found = ""

    try:
        with open("data.json") as data_file:
            credentials = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="Sorry the file not found")
    else:
        if search_website in credentials:
            found = credentials[search_website]["password"]
            messagebox.showinfo(title=search_website, message=f" your website is {search_website}\n password is {found}")
        else:
                messagebox.showinfo(title=search_website,message="Sorry Wesbite details not found")








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo (2).png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "hashirrazzaq256@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search_credentials)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password )
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36,command= save )
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()


