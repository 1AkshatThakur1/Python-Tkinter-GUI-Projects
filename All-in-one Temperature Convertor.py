import tkinter as tk

def convert_temperature():
    try:
        # Get input value
        value = float(entry_value.get())
        
        # Convert to desired unit
        if var_from.get() == "Fahrenheit":
            if var_to.get() == "Celsius":
                result = (value - 32) * 5/9
            elif var_to.get() == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            else:
                result = value  # Same unit
        
        elif var_from.get() == "Celsius":
            if var_to.get() == "Fahrenheit":
                result = (value * 9/5) + 32
            elif var_to.get() == "Kelvin":
                result = value + 273.15
            else:
                result = value  # Same unit
        
        elif var_from.get() == "Kelvin":
            if var_to.get() == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            elif var_to.get() == "Celsius":
                result = value - 273.15
            else:
                result = value  # Same unit
        
        # Clear any previous result
        entry_result.delete(0, tk.END)
        # Insert new result
        entry_result.insert(tk.END, str(result))
    
    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Invalid input")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Create Label for Title
label_title = tk.Label(root, text="Universal Temperature Unit Converter", fg="white", bg="dark blue")
label_title.grid(row=0, column=1, columnspan=3, pady=10)
label_title.config(font=("Helvetica", 15, "bold"))

# Create input entry
entry_value = tk.Entry(root)
entry_value.grid(row=2, column=1)

# Create "From" unit dropdown
var_from = tk.StringVar(root)
var_from.set("Fahrenheit")
option_from = tk.OptionMenu(root, var_from, "Fahrenheit", "Celsius", "Kelvin")
option_from.grid(row=3, column=1)

# Create "=" label
label_eq = tk.Label(root, text=" =")
label_eq.grid(row=3, column=2)
label_eq.config(font=("Helvetica", 20, "bold"))

# Create result entry
entry_result = tk.Entry(root)
entry_result.grid(row=2, column=3)

# Create "To" unit dropdown
var_to = tk.StringVar(root)
var_to.set("Celsius")
option_to = tk.OptionMenu(root, var_to, "Celsius", "Fahrenheit", "Kelvin")
option_to.grid(row=3, column=3, pady=5)

# Create button to trigger conversion
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(row=6, column=1, columnspan=3)
button_convert.config(width=10)

# Run the GUI
root.mainloop()
