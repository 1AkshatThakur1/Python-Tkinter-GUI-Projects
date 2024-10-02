import tkinter as tk

# Calculate function
def calculate():
    shape = shape_var.get()
    # Get the relevant entry widgets based on the selected shape
    relevant_entry_widgets = entry_widgets[shape]
    # Extract values from the entry widgets
    values = []
    for i in range(1, len(relevant_entry_widgets), 2):  # We skip the label and iterate over entry widgets only
        entry_widget = relevant_entry_widgets[i]
        value = float(entry_widget.get())
        values.append(value)

    # Check formulas for all shapes
    if shape == "Square":  # if selected shape is square
        side_length = values[0]
        area = side_length ** 2
        perimeter = 4 * side_length
    elif shape == "Rectangle":  # if selected shape is rectangle
        length, width = values
        area = length * width
        perimeter = 2 * (length + width)
    elif shape == "Triangle":  # if selected shape is triangle
        base, height = values
        area = 0.5 * base * height
        # Assuming it's an equilateral triangle for simplicity
        perimeter = 3 * base
    else:
        area = perimeter = 0  # Default values for unknown shape

    result_label.config(text=f"Area: {area:.2f}\nPerimeter: {perimeter:.2f}")

# Show variable function
def show_variables(*args):
    shape = shape_var.get()
    # Hide all entry widgets and labels initially
    for widget_list in entry_widgets.values():
        for widget in widget_list:
            widget.grid_remove()  # Remove all entry and label widgets from grid layout

    # Display entry widgets and labels based on the selected shape
    for widget in entry_widgets[shape]:
        widget.grid()  # Display selected shape on grid layout

# Create the main window
root = tk.Tk()
root.title("Shape Calculator")
root.config(bg="white")

# Create Label for Project title
font_bold = ("Helvetica", 18, "bold")
label_title = tk.Label(root, text="Area and Perimeter Calculator for Shapes")
label_title.config(fg="white", bg="Navy Blue", font=font_bold)
label_title.grid(row=0, columnspan=2, padx=5, pady=5)

# Create and place widgets
label_shape = tk.Label(root, text="Select a Shape:")
label_shape.config(font=("helvetica", 15), bg="white", fg="Navy blue")
label_shape.grid(row=1, column=0, pady=5)

shapes = ["Square", "Rectangle", "Triangle"]
shape_var = tk.StringVar(value=shapes[0])
shape_menu = tk.OptionMenu(root, shape_var, *shapes, command=show_variables)
shape_menu.config(width=25, font=("TkDefaultFont", 10, "bold"), fg="Navy Blue", bg="white")
shape_menu.grid(row=1, column=1, pady=5)

# Create entry widgets and labels for each shape dynamically
entry_widgets = {
    "Square": [tk.Label(root, text="Side Length:"), tk.Entry(root)],
    "Rectangle": [tk.Label(root, text="Length:"), tk.Entry(root), tk.Label(root, text="Width:"), tk.Entry(root)],
    "Triangle": [tk.Label(root, text="Base:"), tk.Entry(root), tk.Label(root, text="Height:"), tk.Entry(root)]
}

# Place entry widgets and labels on the form and initially hide them
row_count = 2
for shape in shapes:
    for widget in entry_widgets[shape]:
        widget.grid(row=row_count, columnspan=2, pady=5)
        row_count += 1
        widget.grid_remove()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate, width=10, height=2)
calculate_button.config(font=("Arial", 12, "bold"), bg="Navy Blue", fg="white")
calculate_button.grid(row=row_count, column=0, columnspan=2, pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.config(font=("Arial", 12, "bold"), bg="white", fg="Navy Blue")
result_label.grid(row=row_count + 1, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
