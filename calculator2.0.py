import tkinter as tk

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
    print("Result:", result)  # Print result to terminal

def clear():
    entry.delete(0, tk.END)
    memory.clear()

def memory_add():
    memory.append(float(entry.get()))
    entry.delete(0, tk.END)

def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(0, str(memory[-1]))

def memory_clear():
    memory.clear()

memory = []

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", "/"],
]

for i in range(4):
    for j in range(4):
        button = tk.Button(root, text=buttons[i][j], width=5, height=2,
                           command=lambda x=buttons[i][j]: handle_button(x))
        button.grid(row=i+1, column=j)

memory_button = tk.Button(root, text="M+", width=5, height=2, command=memory_add)
memory_button.grid(row=5, column=0)

memory_recall_button = tk.Button(root, text="MR", width=5, height=2, command=memory_recall)
memory_recall_button.grid(row=5, column=1)

memory_clear_button = tk.Button(root, text="MC", width=5, height=2, command=memory_clear)
memory_clear_button.grid(row=5, column=2)

clear_button = tk.Button(root, text="C", width=5, height=2, command=clear)
clear_button.grid(row=5, column=3)

def handle_button(value):
    if value == "=":
        calculate()
    elif value == "C":
        clear()
    else:
        entry.insert(tk.END, value)

root.mainloop()