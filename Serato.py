import tkinter as tk

def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == 'X':
        entry.delete(len(entry.get()) - 1)
    elif symbol == '%':
        entry.insert(tk.END, "/100")
    else:
        entry.insert(tk.END, symbol)

# Create the main application window
app = tk.Tk()
app.title("                        SIMPLE CALCULATOR")
app.configure(bg='grey')  # Set background color

# Create an entry widget to display input and results
entry = tk.Entry(app, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Create buttons for digits and operators with colors
buttons = [
    'C', '/', '*', 'X',
    '7', '8', '9', '-',
    '4', '5', '6', '+',
    '1', '2', '3', '=',
    '0', '.', '%',
]


button_colors = [
    ('Black', 'Red'), ('Black', 'Yellow'), ('Black', 'Yellow'), ('Black', 'Red'),
    ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'Yellow'),
    ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'Yellow'),
    ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'White'),
    ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'LightBlue'), ('Black', 'LightBlue'),
]

for i in range(len(buttons)):
    row = i // 4+1
    col = i % 4
    if buttons[i] == '=':
        button = tk.Button(app, text=buttons[i], width=4, height=4, bg=button_colors[i][0], fg=button_colors[i][1], command=lambda symbol=buttons[i]: button_click(symbol))
        button.grid(row=row, column=col, rowspan=2, pady=5)
    else:
        button = tk.Button(app, text=buttons[i], width=4, height=2, bg=button_colors[i][0], fg=button_colors[i][1], command=lambda symbol=buttons[i]: button_click(symbol))
        button.grid(row=row, column=col)

# Run the application
app.mainloop()
