import tkinter as tk

def on_click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_val = 1
col_val = 0

for btn in buttons:
    action = tk.Button(root, text=btn, font="Arial 18", width=5, height=2)
    action.grid(row=row_val, column=col_val, padx=5, pady=5)
    action.bind("<Button-1>", on_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
