#Create a user registration form with Tkinter! Students will learn to 
# build a login interface with text input fields, password masking, button functionality, 
# and message display. Perfect for understanding form creation 
# and user interaction in GUI applications.
import tkinter as tk
window=tk.Tk()
window.title("GUI APP")
window.geometry("200x200")
l=tk.Label(window,text="Please, enter your name.")
l.pack(padx=30)
e=tk.Entry(window)
e.pack(pady=5)
a=tk.Label(window,text="Please, enter your password.")
a.pack(padx=30)
y=tk.Entry(window)
y.pack(pady=5)
x=tk.Button(window,text="Register!",bg="blue")
x.pack(pady=15)
window.mainloop()
