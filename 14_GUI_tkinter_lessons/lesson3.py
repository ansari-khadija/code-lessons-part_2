
from tkinter import *

root = Tk()
root.geometry("450x650")
root.title("10th Grade Marks Calculator")
root.configure(bg="#FAE2F7")
root.resizable(False, False)

# Heading
Label(
    root,
    text="🎓 Student Marks",
    font=("Arial", 23, "bold"),
    bg="#FAE2F7",
    fg="#61425F"
).pack(pady=15)

Label(
    root,
    text="10th Grade Result Calculator",
    font=("Arial", 12),
    bg="#FAE2F7",
    fg="#61425F"
).pack(pady=5)

# Student name
Label(
    root, text="Student Name",
    font=("Arial", 12, "bold"),
    bg="#FAE2F7", fg="#61425F"
).pack(anchor="w", padx=60, pady=(10, 0))

name_entry = Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

# Subject marks
Label(
    root, text="English Marks (out of 100)",
    bg="#FAE2F7", fg="#61425F"
).pack()

english_entry = Entry(root, font=("Arial", 12))
english_entry.pack(pady=5)

Label(
    root, text="Mathematics Marks (out of 100)",
    bg="#FAE2F7", fg="#61425F"
).pack()

math_entry = Entry(root, font=("Arial", 12))
math_entry.pack(pady=5)

Label(
    root, text="Science Marks (out of 100)",
    bg="#FAE2F7", fg="#61425F"
).pack()

science_entry = Entry(root, font=("Arial", 12))
science_entry.pack(pady=5)

Label(
    root, text="Social Science Marks (out of 100)",
    bg="#FAE2F7", fg="#61425F"
).pack()

social_entry = Entry(root, font=("Arial", 12))
social_entry.pack(pady=5)

Label(
    root, text="Marathi Marks (out of 100)",
    bg="#FAE2F7", fg="#61425F"
).pack()

marathi_entry = Entry(root, font=("Arial", 12))
marathi_entry.pack(pady=5)

# Calculate button
Button(
    root,
    text="Calculate Result",
    font=("Arial", 13, "bold"),
    bg="#E4B0DB",
    fg="#452844",
    relief="flat",
    cursor="hand2",
    command=lambda: print(
        "\n====== STUDENT RESULT ======",
        "\nStudent:", name_entry.get(),
        "\nEnglish:", english_entry.get(),
        "\nMathematics:", math_entry.get(),
        "\nScience:", science_entry.get(),
        "\nSocial Science:", social_entry.get(),
        "\nMarathi:", marathi_entry.get(),
        "\nTotal:",
        sum(int(e.get()) for e in [
            english_entry, math_entry, science_entry,
            social_entry, marathi_entry
        ]),
        "/ 500",
        "\nPercentage:",
        round(sum(int(e.get()) for e in [
            english_entry, math_entry, science_entry,
            social_entry, marathi_entry
        ]) / 5, 2),
        "%",
        "\n============================"
    )
).pack(pady=20)

root.mainloop()
