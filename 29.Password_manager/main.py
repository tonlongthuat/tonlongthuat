from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(8)]
    password_symbols = [random.choice(numbers) for _ in range(2)]
    password_number = [random.choice(symbols) for _ in range(5)]
    password_list=password_letter + password_symbols + password_number
    random.shuffle(password_list)
    password="".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(input_password.get())

# save password
def save_password():
    website=input_website.get()
    email=input_email.get()
    password=input_password.get()
    new_data={
        website:{
        "email": email,
        "password": password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops! Something went wrong",message="make sure you haven't left any fields empty")
    else:
        try:
            with open("./data.json","r") as f_data:
                # reading old data
                data=json.load(f_data)
        except:
            with open("./data.json","w") as f_data:
                # saving new data
                json.dump(new_data,f_data,indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            # saving updated data
            with open("./data.json","w") as f_data:
                json.dump(data,f_data,indent=4)
        finally:
            input_website.delete(0,END)
            input_password.delete(0,END)

# find password
def find_password():
    website=input_website.get()
    try:
        with open("./data.json") as pw_data:
            data=json.load(pw_data)
    except FileNotFoundError:
        messagebox.showerror(title="Oops! Something went wrong",message="No data file found please enter your password first")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="here is your infomation:",message=f"website:  {website}\nemail:  {email}\npassword:  {password}\nI have copied password to your clipboard")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Oops! Something went wrong",message="Website not found please enter again")



window=Tk()
window.title("password manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
password_img=PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=password_img)
canvas.grid(row=0,column=1)

website_lable=Label(text="Website:")
website_lable.grid(row=1,column=0)
input_website=Entry(width=22)
input_website.grid(row=1,column=1)
input_website.focus()
search_button=Button(text="Search",width=14,command=find_password)
search_button.grid(row=1,column=2)

email_lable=Label(text="Email:")
email_lable.grid(row=2,column=0)
input_email=Entry(width=40)
input_email.grid(row=2,column=1,columnspan=2)
input_email.insert(0,"@gmail.com")

password_lable=Label(text="Password:")
password_lable.grid(row=3,column=0)
input_password=Entry(width=22)
input_password.grid(row=3,column=1)

generate_button=Button(text="Generate Password",width=14,command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

 





window.mainloop()