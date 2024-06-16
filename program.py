from tkinter import *
# ---------- PASSWORD GENERATOR ---------- #

# ------------ SAVE PASSWORD ----------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("senhas.txt", "a") as s:
        s.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)


# ---------------- UI ---------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
