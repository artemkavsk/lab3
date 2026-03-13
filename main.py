import tkinter as tk
import random
import string

# keygen func
def generate_key():
    blocks = []

    for i in range(3):
        letters = random.sample(string.ascii_uppercase, 3)
        digits = random.sample(string.digits, 2)
        chars = letters + digits
        random.shuffle(chars)
        blocks.append("".join(chars))

    key = "-".join(blocks)
    key_label.config(text=key)


# wndw
root = tk.Tk()
root.title("keygen")
root.geometry("333x151")

# png bg
bg_photo = tk.PhotoImage(file="window.png")
canvas = tk.Canvas(root, width=333, height=151)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# generate button
button = tk.Button(root, text="generate key", command=generate_key)
canvas.create_window(333/2, 151/2, window=button)

# output
key_label = tk.Label(root, text="", font=("Arial", 16), bg="white")
canvas.create_window(333/2, 151/2+50, window=key_label)

root.mainloop()