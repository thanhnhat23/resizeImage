from PIL import Image
import tkinter as tk
import os
from tkinter import messagebox, filedialog

def resize(files, width, height):
    for file_path in files:
        if file_path.lower().endswith(('.jpeg', '.jpg', '.png')):
            try:
                image = Image.open(file_path)
                image = image.resize((width, height))
                new_filename = f"resize_{os.path.basename(file_path)}"
                new_file_path = os.path.join(os.path.dirname(file_path), new_filename)
                image.save(new_file_path)
                print(f'Resized {os.path.basename(file_path)} to {new_filename}')
            except Exception as e:
                print(f"Can't resize {os.path.basename(file_path)}: {str(e)}")
                continue
    messagebox.showinfo("Completed", "Resize completed!")

def selectFiles():
    files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if files:
        resize(files, 800, 600)

def resizeCustom():
    width = entry_width.get()
    height = entry_height.get()
    if not width.isdigit() or not height.isdigit() or int(width) <= 0 or int(height) <= 0:
        messagebox.showerror("Invalid input", "Please enter valid width and height.")
        return
    files = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if files:
        resize(files, int(width), int(height))

root = tk.Tk()
root.title("Resize Image")
root.geometry("400x250")

title_label = tk.Label(root, text="Resize images", font=("Arial", 16))
title_label.pack(pady=10)

default_button = tk.Button(root, text="Resize for Instagram", command=selectFiles)
default_button.pack(pady=10)

frame_custom = tk.Frame(root)
frame_custom.pack(pady=10)

label_width = tk.Label(frame_custom, text="Width:")
label_width.pack(side=tk.LEFT)

entry_width = tk.Entry(frame_custom)
entry_width.pack(side=tk.LEFT)

label_height = tk.Label(frame_custom, text="Height:")
label_height.pack(side=tk.LEFT)

entry_height = tk.Entry(frame_custom)
entry_height.pack(side=tk.LEFT)

custom_button = tk.Button(root, text="Resize to Custom Size", command=resizeCustom)
custom_button.pack(pady=10)

root.mainloop()
