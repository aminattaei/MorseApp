import tkinter as tk
from tkinter import ttk
import pyperclip

class MorseApp:
    Characters = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    MorseCode = [
        ".-", "_...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("400x300")

        # Label for input
        self.label = ttk.Label(root, text="Enter Text or Morse Code:")
        self.label.pack(pady=10)

        # Entry field for input
        self.entry = ttk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Option menu for conversion type
        self.choice_var = tk.IntVar()
        self.choice_var.set(1)  # Default to Text to Morse
        self.option_menu = ttk.OptionMenu(
            root, self.choice_var, 1, 1, 2, command=self.update_label
        )
        self.option_menu.pack(pady=10)

        # Label for conversion type
        self.type_label = ttk.Label(root, text="Text to Morse Code")
        self.type_label.pack(pady=5)

        # Convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

        # Result label
        self.result_label = ttk.Label(root, text="Result will appear here")
        self.result_label.pack(pady=10)

        # Copy button (initially disabled)
        self.copy_button = ttk.Button(root, text="Copy Result", command=self.copy_result, state="disabled")
        self.copy_button.pack(pady=5)

    def update_label(self, value):
        if value == 1:
            self.type_label.config(text="Text to Morse Code")
        elif value == 2:
            self.type_label.config(text="Morse Code to Text")

    def convert(self):
        input_text = self.entry.get().strip().upper()
        choice = self.choice_var.get()
        result = []

        if choice == 1:  # Text to Morse
            for char in input_text:
                if char == " ":
                    result.append(" ")
                elif char in self.Characters:
                    index = self.Characters.index(char)
                    result.append(self.MorseCode[index])
                else:
                    result.append("ERROR")
            output = " ".join(result)

        elif choice == 2:  # Morse to Text
            morse_words = input_text.split("  ")  # Double space for word separation
            for word in morse_words:
                morse_chars = word.split()
                decoded_word = []
                for morse in morse_chars:
                    if morse in self.MorseCode:
                        index = self.MorseCode.index(morse)
                        decoded_word.append(self.Characters[index])
                    else:
                        decoded_word.append("ERROR")
                result.append("".join(decoded_word))
            output = " ".join(result)

        self.result_label.config(text=f"Result: {output}")
        # Enable the copy button after conversion
        self.copy_button.config(state="normal")
        self.last_result = output  # Store the result for copying

    def copy_result(self):
        if hasattr(self, 'last_result'):
            pyperclip.copy(self.last_result)
            self.result_label.config(text=f"Result: {self.last_result} (Copied!)")
            self.root.after(2000, lambda: self.result_label.config(text=f"Result: {self.last_result}"))  # Revert after 2 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()