import tkinter as t
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def Password():
    PasswordEntry.delete(0, len(PasswordEntry.get()))
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    Symbol = [random.choice(symbols) for j in range(nr_symbols)]
    Number = [random.choice(numbers) for k in range(nr_numbers)]
    password_list.extend(Symbol)
    password_list.extend(Number)
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    PasswordEntry.insert(index=0, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    Data = {WebsiteEntry.get() : {"Username": UsernameEntry.get(), "password" : PasswordEntry.get()}}
    if WebsiteEntry.get() == "" or UsernameEntry.get() =="" or PasswordEntry.get() == "":
        messagebox.showinfo(title = "Error", message="Please fill all the required data.")
    else:
        Check = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered\n Website : {WebsiteEntry.get()}\nEmail : {UsernameEntry.get()}\nPassowrd : {PasswordEntry.get()}\nDo you want to save?")
        if Check:
            with open("data.json", "w") as F:
                json.dump(Data, F, indent = 4)
            # with open("data.txt", "a") as F:
            #    F.write(f"{WebsiteEntry.get()} | {UsernameEntry.get()} | {PasswordEntry.get()}\n")

            WebsiteEntry.delete(0, len(WebsiteEntry.get()))
            PasswordEntry.delete(0, len(PasswordEntry.get()))



# ---------------------------- UI SETUP ------------------------------- #
Windows = t.Tk()
Windows.title("Password Manager")
Windows.config(padx=20, pady=20)
Can = t.Canvas(width=200, height=200,highlightthickness=0)
Can.grid(row=0, column=1)
Lock = t.PhotoImage(file="logo.png")
CanImage = Can.create_image(100,100,image = Lock)
# Label placement
WebsiteLabel = t.Label(text = "Website: ")
WebsiteLabel.grid(row=1, column=0)
UsernameLabel = t.Label(text = "E-mail/Username:")
UsernameLabel.grid(row=2, column=0)
PasswordLabel = t.Label(text="Password: ")
PasswordLabel.grid(row=3, column=0)
# Entry Placement
WebsiteEntry = t.Entry(width=35)
WebsiteEntry.grid(row=1, column=1, columnspan=2)
WebsiteEntry.focus()
UsernameEntry = t.Entry(width=35)
UsernameEntry.grid(row=2, column=1, columnspan=2)
UsernameEntry.insert(index=0,string="kaustuvpradhan8@gmail.com")
PasswordEntry = t.Entry(width=25)
PasswordEntry.grid(row=3, column=1, columnspan=1)
# Button Placement
GenerateButton = t.Button(text="Generate Password", width=20, command=Password)
GenerateButton.grid(row=3,column=2,columnspan=1)
AddButton = t.Button(text="Add", width=35, command=save_data)
AddButton.grid(row=4, column=1,columnspan=2)
Windows.mainloop()