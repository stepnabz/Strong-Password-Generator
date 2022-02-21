from tkinter import *
from random import randint

root = Tk()
root.title("Strong Password Generator")
root.geometry("500x300")

password = chr(randint(33, 126))

# Generate random strong password
def new_rand():
    # Clear our entry box
    password_entry.delete(0, END)

    # Get Password Length and covert it into an integer
    pw_length = int(my_entry.get())

    # Variable to hold our password
    password = ""

    # Loop through password length
    for x in range(pw_length):
        password += chr(randint(33, 126))

    # Output password to the screen
    password_entry.insert(0, password)


# Copy to clipboard
def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(password_entry.get())

#Label Frame
lf = LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

# Create entry box to designate number of characters
my_entry = Entry(lf, font=("Harrington", 24))
my_entry.pack(pady=20, padx=20)

# Create entry box for our return password
password_entry = Entry(root, text="", font=("Georgia", 24), bd=0, bg="Gold")
password_entry.pack(pady=20)

# Create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()