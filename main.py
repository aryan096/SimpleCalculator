'''
This is the main file of the calculator.
Starts the main loop.
'''


import gui
import tkinter as tk

root = tk.Tk()
app = gui.CalcLayout(master = root)
app.mainloop()
