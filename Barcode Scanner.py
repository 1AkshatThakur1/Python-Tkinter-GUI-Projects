import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pyzbar.pyzbar import decode

def browse_file():
    # Open file dialog box to select image
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    # Check if an image file is selected
    if filepath:
        try:
            # Attempt to open image file and decode barcode
            barcode_data = decode(Image.open(filepath))
            
            # Check if barcode data is decoded successfully
            if barcode_data:
                # Display the extracted barcode data
                result_label.config(text="Barcode: " + barcode_data[0].data.decode('utf-8'))
            else:
                result_label.config(text="No barcode found in the image.")
        except Exception as e:
            # Display error message if image file fails to open
            messagebox.showerror("Error", "Failed to open image file: " + str(e))

# Create Tkinter window
root = tk.Tk()
root.title("Barcode Scanner")

# Create and configure title label
title_label = tk.Label(root, text="Barcode Scanner")
title_label.pack(pady=10)
title_label.config(fg="white", bg="Dark Red", font=("Helvetica", 15, "bold"))

# Create and pack the label for instructions
label = tk.Label(root, text="Select Barcode Image:")
label.pack()

# Create and pack the Browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Create and pack the label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
