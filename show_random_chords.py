import random
import tkinter as tk
from tkinter import messagebox

# Function to display random chords
def show_random_chords():
    chords = ["A", "Am", "Bm", "C", "D", "Dm", "E", "Em", "F", "G"]
    random_chords = random.sample(chords, 3)
    messagebox.showinfo("Random Chords", f"Your random chords are:\n{', '.join(random_chords)}")

# Create the main window
root = tk.Tk()
root.title("Random Chord Picker")
root.geometry("300x150")

# Create and place a button
pick_button = tk.Button(root, text="Pick Random Chords", command=show_random_chords, font=("Arial", 12))
pick_button.pack(pady=30)

# Run the tkinter event loop
root.mainloop()
