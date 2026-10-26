
from tkinter import *

root = Tk()
root.geometry("500x650")
root.title("About Me")
root.configure(bg="#E4FAE2")
root.resizable(False, False)

# Main heading
label = Label(
    root,
    text="✦ ABOUT ME ✦",
    font=("Arial", 25, "bold"),
    bg="#E4FAE2",
    fg="#426144"
)
label.pack(pady=(20, 5))

# Subtitle
subtitle = Label(
    root,
    text="Tell us something about yourself",
    font=("Arial", 11),
    bg="#E4FAE2",
    fg="#426144"
)
subtitle.pack(pady=(0, 20))

# Form frame
frame = Frame(
    root,
    bg="#D2F0CE",
    padx=25,
    pady=20
)
frame.pack(padx=25, fill="x")

# Name
Label(
    frame,
    text="👤  Your Name",
    font=("Arial", 12, "bold"),
    bg="#D2F0CE",
    fg="#426144"
).pack(anchor="w")

name_entry = Entry(
    frame,
    font=("Arial", 14),
    bg="#F7FFF5",
    fg="#426144",
    insertbackground="#426144",
    relief="flat"
)
name_entry.pack(fill="x", ipady=8, pady=(5, 15))

# Favorite color
Label(
    frame,
    text="🎨  Favorite Color",
    font=("Arial", 12, "bold"),
    bg="#D2F0CE",
    fg="#426144"
).pack(anchor="w")

color_entry = Entry(
    frame,
    font=("Arial", 14),
    bg="#F7FFF5",
    fg="#426144",
    insertbackground="#426144",
    relief="flat"
)
color_entry.pack(fill="x", ipady=8, pady=(5, 15))

# Favorite place
Label(
    frame,
    text="📍  Favorite Place",
    font=("Arial", 12, "bold"),
    bg="#D2F0CE",
    fg="#426144"
).pack(anchor="w")

place_entry = Entry(
    frame,
    font=("Arial", 14),
    bg="#F7FFF5",
    fg="#426144",
    insertbackground="#426144",
    relief="flat"
)
place_entry.pack(fill="x", ipady=8, pady=(5, 15))

# Favorite animal
Label(
    frame,
    text="🐼  Favorite Animal",
    font=("Arial", 12, "bold"),
    bg="#D2F0CE",
    fg="#426144"
).pack(anchor="w")

animal_entry = Entry(
    frame,
    font=("Arial", 14),
    bg="#F7FFF5",
    fg="#426144",
    insertbackground="#426144",
    relief="flat"
)
animal_entry.pack(fill="x", ipady=8, pady=(5, 5))

# Submit button
button = Button(
    root,
    text="✦   SUBMIT   ✦",
    width=22,
    font=("Arial", 14, "bold"),
    bg="#B7E4B0",
    fg="#28452B",
    activebackground="#8CCF91",
    activeforeground="#28452B",
    relief="flat",
    cursor="hand2"
)
button.pack(pady=22, ipady=8)

# Footer
footer = Label(
    root,
    text="✧  Made with Python & Tkinter  ✧",
    font=("Arial", 10, "italic"),
    bg="#E4FAE2",
    fg="#426144"
)
footer.pack(pady=5)

root.mainloop()
