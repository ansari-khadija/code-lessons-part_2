
from tkinter import *
import random

root = Tk()
root.geometry("450x520")
root.title("Hogwarts House Selector")
root.configure(bg="#100D0B")
root.resizable(False, False)

# Hogwarts colors
black = "#100D0B"
brown = "#2B1D16"
white = "#F5EBDD"

# Heading
Label(
    root,
    text="⚡ HOGWARTS ⚡",
    font=("Georgia", 26, "bold"),
    bg=black,
    fg="#D9B56D"
).pack(pady=(25, 5))

Label(
    root,
    text="THE SORTING HAT",
    font=("Georgia", 12, "italic"),
    bg=black,
    fg=white
).pack(pady=5)

Label(
    root,
    text="Enter your name, young wizard",
    font=("Arial", 12),
    bg="#000000",
    fg=white
).pack(pady=(25, 10))

# Name entry
name_entry = Entry(
    root,
    font=("Arial", 14),
    bg="#8A7454",
    fg=white,
    insertbackground=white,
    relief="flat",
    justify="center"
)
name_entry.pack(padx=50, fill="x", ipady=10)

# House name, background color, description
houses = [
    ("GRYFFINDOR 🦁", "#C62828",
     "Bravery, courage and determination!"),

    ("SLYTHERIN 🐍", "#21804A",
     "Ambition, cunning and resourcefulness!"),

    ("RAVENCLAW 🦅", "#2875C7",
     "Wisdom, creativity and intelligence!"),

    ("HUFFLEPUFF 🦡", "#D9AC20",
     "Patience, loyalty and hard work!")
]



# Result frame
result_frame = Frame(
    root,
    bg=brown,
    padx=15,
    pady=25
)
result_frame.pack(padx=35, fill="x", pady=30)

result_label = Label(
    result_frame,
    text="YOUR HOUSE AWAITS...",
    font=("Georgia", 16, "bold"),
    bg=brown,
    fg=white,
    wraplength=340
)
result_label.pack()

message_label = Label(
    result_frame,
    text="The Sorting Hat will decide your fate.",
    font=("Arial", 10),
    bg=brown,
    fg=white,
    wraplength=340
)
message_label.pack(pady=(12, 0))


# Sorting button
Button(
    root,
    text="✦  SORT ME  ✦",
    font=("Georgia", 13, "bold"),
    bg="#D9B56D",
    fg="#100D0B",
    activebackground="#F0D28E",
    relief="flat",
    cursor="hand2",
    command=lambda: (
        result_label.config(
            text=(house := random.choice(houses))[0],
            bg=house[1],
            fg="white"
        ),
        message_label.config(
            text=house[2],
            bg=house[1],
            fg="white"
        ),
        result_frame.config(bg=house[1])
    )
).pack(pady=5)


root.mainloop()
