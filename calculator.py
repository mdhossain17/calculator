import tkinter as tk
import math


# Function to evaluate the expression entered in the entry widget
def evaluate_expression():
    try:
        result = str(eval(entry.get()))  # Use eval to evaluate the entered expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Function to append the pressed button value to the entry widget
def append_to_entry(value):
    entry.insert(tk.END, value)


# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)


# Function to calculate the square root
def calculate_sqrt():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Function to calculate trigonometric functions (sin, cos, tan)
def calculate_trig(func):
    try:
        angle = float(entry.get())
        radians = math.radians(angle)  # Convert degrees to radians
        if func == 'sin':
            result = math.sin(radians)
        elif func == 'cos':
            result = math.cos(radians)
        elif func == 'tan':
            result = math.tan(radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Function to calculate logarithms
def calculate_log():
    try:
        number = float(entry.get())
        result = math.log10(number)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create the main window
root = tk.Tk()
root.title("Smart Scientific Calculator")
root.configure(bg="#333333")

# Define font and colors
font = ('Arial', 14)
bg_color = "#2d2d2d"  # Dark background for the window
button_color = "#4caf50"  # Green color for buttons
button_hover_color = "#45a049"  # Darker green on hover
text_color = "#ffffff"  # White text for readability
entry_bg_color = "#1e1e1e"  # Dark background for entry
entry_fg_color = "#ffffff"  # White text for entry

# Entry widget to display the input and output
entry = tk.Entry(root, width=40, borderwidth=5, font=font, justify='right', bg=entry_bg_color, fg=entry_fg_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function to create buttons and place them in the window
def create_button(text, row, col, command=None, width=10, height=2):
    button = tk.Button(root, text=text, width=width, height=height, font=font,
                       bg=button_color, fg=text_color, relief="raised", bd=2, command=command)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Add hover effect
    button.bind("<Enter>", lambda e: button.config(bg=button_hover_color))
    button.bind("<Leave>", lambda e: button.config(bg=button_color))

    return button


# Button layout for the calculator
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sqrt', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3),
    ('log', 6, 0), ('(', 6, 1), (')', 6, 2), ('Clear', 6, 3)
]

# Create all the buttons and assign their commands
for (text, row, col) in buttons:
    if text == '=':
        create_button(text, row, col, command=evaluate_expression)
    elif text == 'Clear':
        create_button(text, row, col, command=clear_entry)
    elif text == 'sqrt':
        create_button(text, row, col, command=calculate_sqrt)
    elif text in ('sin', 'cos', 'tan'):
        create_button(text, row, col, command=lambda func=text: calculate_trig(func))
    elif text == 'log':
        create_button(text, row, col, command=calculate_log)
    else:
        create_button(text, row, col, command=lambda value=text: append_to_entry(value))

# Make the rows and columns stretchable for resizing
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()
