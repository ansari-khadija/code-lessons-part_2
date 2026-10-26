
from tkinter import *

root = Tk()
root.geometry("500x700")
root.title("My Profile")
root.configure(bg="#E2E8FA")
root.resizable(False, False)

# Menu bar
menubar = Menu(root)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Heading
Label(
    root, text="✦ MY PROFILE ✦",
    font=("Arial", 24, "bold"),
    bg="#E2E2FA", fg="#424261"
).pack(pady=15)

# Form frame
frame = Frame(root, bg="#CED1F0", padx=20, pady=15)
frame.pack(padx=25, fill="x")

# Name
Label(frame, text="Your Name",
      bg="#D0CEF0", fg="#424261",
      font=("Arial", 11, "bold")).pack(anchor="w")

name_entry = Entry(frame, font=("Arial", 12),
                   bg="#F5F5FF", fg="#424461")
name_entry.pack(fill="x", pady=5)

# Checkbox
python_var = IntVar()

Checkbutton(
    frame, text="I like Python programming",
    variable=python_var,
    bg="#D1CEF0", fg="#424261",
    activebackground="#CECEF0",
    selectcolor="#B0B8E4"
).pack(anchor="w", pady=5)

# Radio buttons
Label(frame, text="Your status:",
      bg="#CECEF0", fg="#424461").pack(anchor="w")

status = StringVar(value="Student")

Radiobutton(
    frame, text="Student", variable=status,
    value="Student", bg="#CECEF0",
    fg="#424261", activebackground="#CED0F0"
).pack(anchor="w")

Radiobutton(
    frame, text="Working", variable=status,
    value="Working", bg="#D1CEF0",
    fg="#424461", activebackground="#CECEF0"
).pack(anchor="w")

# Scrollable listbox
Label(frame, text="Choose your hobbies:",
      bg="#CED1F0", fg="#424261",
      font=("Arial", 11, "bold")).pack(anchor="w", pady=(8, 3))

list_frame = Frame(frame, bg="#CED0F0")
list_frame.pack(fill="x")

hobbies = Listbox(
    list_frame, height=4,
    selectmode=MULTIPLE,
    font=("Arial", 11),
    bg="#F6F5FF", fg="#444261",
    selectbackground="#8D8CCF"
)

scrollbar = Scrollbar(
    list_frame, orient=VERTICAL,
    command=hobbies.yview
)

hobbies.config(yscrollcommand=scrollbar.set)

hobbies.pack(side=LEFT, fill="both", expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

hobbies.insert(END, "Cricket")
hobbies.insert(END, "Reading")
hobbies.insert(END, "Gaming")
hobbies.insert(END, "Music")
hobbies.insert(END, "Drawing")
hobbies.insert(END, "Travel")
hobbies.insert(END, "Coding")
hobbies.insert(END, "Photography")

# Submit button (visual only for now)
Button(
    root, text="SAVE PROFILE",
    font=("Arial", 13, "bold"),
    bg="#B1B0E4", fg="#292845",
    relief="flat", cursor="hand2",
    width=20
).pack(pady=18)

Label(
    root, text="Made with Python & Tkinter",
    font=("Arial", 10, "italic"),
    bg="#E2E4FA", fg="#424761"
).pack()

root.mainloop()
