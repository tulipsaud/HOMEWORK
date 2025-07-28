import tkinter as tk

window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

label = tk.Label(window, text="Enter length in meters:", font=("Arial", 12))
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)

def convert():
    try:
        meters = float(entry.get())
        centimeters = meters * 100
        result_label.config(text=f"{centimeters} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
convert_button = tk.Button(window, text="Convert to cm", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)
window.mainloop()
