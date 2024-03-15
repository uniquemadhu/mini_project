import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd
import random

# Load the dataset containing paths to real and fake logos
real_logos_df = pd.read_csv('logo_dataset/real_logo.csv')
fake_logos_df = pd.read_csv('logo_dataset/fake_logo.csv')

def display_random_logos(brand_name):
    real_logo = real_logos_df[real_logos_df['Brandname'] == brand_name]
    fake_logo = fake_logos_df[fake_logos_df['Brand Name'] == brand_name]

    if real_logo.empty and fake_logo.empty:
        messagebox.showinfo("Info", "No logos found for the entered brand.")
        return

    root = tk.Toplevel()
    root.title(f"Real and Fake Logos for {brand_name}")

    # Randomly select one real logo and one fake logo
    real_path = real_logo.sample(n=1)['Filename'].iloc[0]
    fake_path = fake_logo.sample(n=1)['Filename'].iloc[0]

    # Display real logo with label
    real_image = Image.open(real_path)
    real_image.thumbnail((200, 200))
    real_photo = ImageTk.PhotoImage(real_image)
    real_label = tk.Label(root, text="Real", image=real_photo, compound=tk.TOP)
    real_label.grid(row=0, column=0, padx=5, pady=5)
    real_label.image = real_photo

    # Display fake logo with label
    fake_image = Image.open(fake_path)
    fake_image.thumbnail((200, 200))
    fake_photo = ImageTk.PhotoImage(fake_image)
    fake_label = tk.Label(root, text="Fake", image=fake_photo, compound=tk.TOP)
    fake_label.grid(row=0, column=1, padx=5, pady=5)
    fake_label.image = fake_photo

def on_search():
    brand_name = brand_entry.get()
    if brand_name:
        display_random_logos(brand_name)
    else:
        messagebox.showinfo("Info", "Please enter a brand name.")

# Create main window
root = tk.Tk()
root.title("Logo Viewer")

# Create entry for brand name
brand_label = ttk.Label(root, text="Enter brand name:")
brand_label.grid(row=0, column=0, padx=5, pady=5)
brand_entry = ttk.Entry(root)
brand_entry.grid(row=0, column=1, padx=5, pady=5)

# Create search button
search_button = ttk.Button(root, text="Search", command=on_search)
search_button.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
