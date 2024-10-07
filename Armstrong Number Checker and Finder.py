import tkinter as tk
from tkinter import messagebox

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    order = len(str(num))  # Find the number of digits
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10  # Get last digit
        sum += digit ** order  # Add the power of digit to sum
        temp //= 10  # Remove last digit
    return num == sum

# Function to check Armstrong number on button click
def check_armstrong():
    """Check if the entered number is Armstrong."""
    num = int(num_entry.get())  # Get number from entry widget
    if is_armstrong(num):
        messagebox.showinfo("Armstrong Number", f"{num} is an Armstrong number!")
    else:
        messagebox.showerror("Error", f"{num} is not an Armstrong number.")
    messagebox.showinfo("Help", "I will help you to find Armstrong numbers in the given range")
    ask_range()

# Function to open a new window and ask for range
def ask_range():
    """Ask user for range to display Armstrong numbers."""
    range_window = tk.Toplevel(root)
    range_window.title("Enter Range")
    
    name_label = tk.Label(range_window, text="Armstrong Number Generator")
    name_label.grid(row=0, columnspan=2)
    name_label.config(fg="white", bg="black", font=("Helvetica", 15, "bold"))
    
    start_label = tk.Label(range_window, text="Start:")
    start_label.grid(row=1, column=0)
    start_entry = tk.Entry(range_window)
    start_entry.grid(row=1, column=1)
    
    end_label = tk.Label(range_window, text="End:")
    end_label.grid(row=2, column=0)
    end_entry = tk.Entry(range_window)
    end_entry.grid(row=2, column=1)
    
    result_text = tk.Text(range_window, height=10, width=40)
    result_text.grid(row=3, columnspan=2)
    
    # Function to generate Armstrong numbers in the given range
    def generate_armstrong_numbers():
        """Generate Armstrong numbers within the given range."""
        try:
            start = int(start_entry.get())
            end = int(end_entry.get())
            armstrong_numbers = []
            for num in range(start, end + 1):
                if is_armstrong(num):
                    armstrong_numbers.append(num)
                    
            result_text.delete("1.0", tk.END)
            if armstrong_numbers:
                for num in armstrong_numbers:
                    result_text.insert(tk.END, f"{num}\n")
            else:
                result_text.insert(tk.END, "No Armstrong numbers in the given range.")
        except ValueError:
            result_text.insert(tk.END, "Please enter valid start and end values.")
    
    generate_button = tk.Button(range_window, text="Generate Armstrong Numbers", command=generate_armstrong_numbers)
    generate_button.grid(row=4, columnspan=2)

# Create the main window
root = tk.Tk()
root.title("Armstrong Number Checker")

title_label = tk.Label(root, text="Armstrong Number Finder")
title_label.pack()
title_label.config(fg="white", bg="black", font=("Helvetica", 15, "bold"))

num_label = tk.Label(root, text="Enter a number:")
num_label.pack()

num_entry = tk.Entry(root)
num_entry.pack()

check_button = tk.Button(root, text="Check", command=check_armstrong)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
