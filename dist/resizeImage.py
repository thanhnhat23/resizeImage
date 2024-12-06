from PIL import Image
import tkinter as tk
import os
from tkinter import messagebox, filedialog

def resize(folder, width, height):
    if not os.path.isdir(folder):
        messagebox.showerror("Errol", "Folder does not exist.")
        return
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
            try:
                image = Image.open(file_path)
                image = image.resize((width, height))
                new_filename = f"resize_{filename}"
                new_file_path = os.path.join(folder, new_filename)
                image.save(new_file_path)
                print(f'Resize {filename} to {new_filename}')
            except Exception as e:
                print(f"Can't resize {filename}: {str(e)}")
                continue
    messagebox.showinfo("Completed", "Resize completed!")

def selectFolder():
    folder = filedialog.askdirectory(title="Select image")
    if folder:
        resize(folder, 800, 600)

root = tk.Tk()
root.title("Resize image")
root.geometry("400x200")

title_label = tk.Label(root, text="Resize image to 800x600", font=("Arial", 16))
title_label.pack(pady=20)

select_button = tk.Button(root, text="Select folder", command=selectFolder)
select_button.pack(pady=10)

root.mainloop()
