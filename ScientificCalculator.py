import math
import tkinter as tk

class ScientificCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.geometry("400x500")

        self.entry = tk.Entry(self.root, width=30, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.buttons = {
            "7": (1, 0), "8": (1, 1), "9": (1, 2), "/": (1, 3), "C": (1, 4),
            "4": (2, 0), "5": (2, 1), "6": (2, 2), "*": (2, 3), "CE": (2, 4),
            "1": (3, 0), "2": (3, 1), "3": (3, 2), "-": (3, 3), "=": (3, 4),
            "0": (4, 0), ".": (4, 1), "+": (4, 2), "sin": (4, 3), "cos": (4, 4),
            "tan": (5, 0), "log": (5, 1), "sqrt": (5, 2), "**": (5, 3), "pi": (5, 4),
            "e": (6, 0), "ln": (6, 1), "x^2": (6, 2), "x^3": (6, 3), "fact": (6, 4)
        }

        for key, (row, col) in self.buttons.items():
            button = tk.Button(self.root, text=key, font=("Arial", 12), command=lambda key=key: self.button_click(key))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.root.mainloop()

    def button_click(self, key):
        if key == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except SyntaxError:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif key == "C":
            self.entry.delete(0, tk.END)
        elif key == "CE":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        elif key == "pi":
            self.entry.insert(tk.END, math.pi)
        elif key == "e":
            self.entry.insert(tk.END, math.e)
        elif key == "fact":
            try:
                value = int(self.entry.get())
                result = math.factorial(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except ValueError:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    calculator = ScientificCalculator()