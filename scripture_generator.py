import tkinter as tk
from tkinter import ttk
from random import choice
from PIL import Image, ImageTk
from pathlib import Path

from scriptures import scriptures

class ScriptureGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scripture Generator")
        self.root.minsize(500, 300)
        self.image_path = Path(__file__).resolve().parent / "scripgenimage.png"
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.root.iconphoto(True, self.photo)
        self.scriptures = scriptures

        self.scrip_values = [key.replace("_scriptures", "").capitalize() for key in self.scriptures]

        self.category_select = ttk.Combobox(self.root, values=self.scrip_values, state="readonly")
        self.category_select.pack(padx=10, pady=10)
        self.category_select.set(self.scrip_values[0])

        self.scrip_frame = tk.Frame(self.root)
        self.scrip_frame.pack(padx=10, pady=10)

        self.verse_labelframe = tk.LabelFrame(self.scrip_frame, text="Verse:")
        self.verse_labelframe.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.verse_label = tk.Label(self.verse_labelframe, anchor="center")
        self.verse_label.pack(fill='x', padx=5, pady=5)

        self.scripture_labelframe = tk.LabelFrame(self.scrip_frame, text="Scripture:")
        self.scripture_labelframe.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.scripture_label = tk.Label(self.scripture_labelframe, justify='left', wraplength=220)
        self.scripture_label.pack(padx=5, pady=5)

        self.meaning_labelframe = tk.LabelFrame(self.scrip_frame, text="Meaning:")
        self.meaning_labelframe.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        self.meaning_label = tk.Label(self.meaning_labelframe, justify='left', wraplength=220)
        self.meaning_label.pack(fill="both", padx=5, pady=5)

        self.generate_scrip_button = tk.Button(
            self.root,
            text="Generate",
            command=self.generate_scripture
            )
        self.generate_scrip_button.pack(padx=10, pady=10)


    def scrip_cat_select(self):
        category = self.category_select.get()
        return self.scriptures[f"{category.lower()}_scriptures"]

    def generate_scripture(self):
        scriptures = self.scrip_cat_select()
        if not scriptures:
            return
        scripture = choice(scriptures)

        self.verse_label.config(text=scripture.location)
        self.scripture_label.config(text=scripture.scripture)
        self.meaning_label.config(text=scripture.meaning)

if __name__ == "__main__":
    app = ScriptureGenerator()
    app.root.mainloop()
