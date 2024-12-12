import tkinter as tk

# Create a root window
root = tk.Tk()
root.title("Tkinter Test")

# Add a label to the window
label = tk.Label(root, text="Tkinter is working!")
label.pack(pady=20)

# Start the main event loop
root.mainloop()
