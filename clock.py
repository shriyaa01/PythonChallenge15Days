import tkinter as tk
from time import strftime
# Create a function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time) 
# Update time every 1000ms (1 second)
# Create the main window
window = tk.Tk()
window.title("Digital Clock")
# Create a label widget to display the time
label = tk.Label(window, font=('roboto', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')
time()
# Call the time function to display the initial time
# Run the main loop
window.mainloop()
