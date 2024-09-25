import tkinter as tk

def show_input():
    user_input = entry.get()
    result_label.config(text="User input: " + user_input)
    
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x200")

label = tk.Label(root, text="Enter something:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
