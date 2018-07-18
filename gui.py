'''
This module sets up the Graphical User Interface of the Tkinter Calculator.

imports:
tkinter framework
addition function from operations module

'''

import tkinter as tk
from operations import addition

#CalcLayout class to make GUI
class CalcLayout(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    '''
    create_widgets sets up the widets on the master frame
    Uses grid geometry management

    Creates:
    Entry fields
    Operation Buttons
    '''
    def create_widgets(self):

        #Enter Field
        self.firstNum = tk.StringVar()
        self.secondNum = tk.StringVar()
        self.entry1 = tk.Entry(self, textvariable=self.firstNum, width=10, justify="center", bd=4, selectborderwidth=3)
        self.entry1.grid(row=0, column=0)
        self.entry2 = tk.Entry(self, textvariable=self.secondNum, width=10, justify="center", bd=4, selectborderwidth=3)
        self.entry2.grid(row=0, column=1)


        #Operation Buttons
        self.add_button = tk.Button(self, width=10, text="+", bg ="grey", command=self.set_output())
        self.add_button.grid(row=3, column=0)
        self.subtract_button = tk.Button(self, width=10, text="-", bg="grey", command = self.set_output())
        self.subtract_button.grid(row=3,column=1)
        self.mult_button = tk.Button(self, width=10, text="*", bg ="grey", command=self.set_output())
        self.mult_button.grid(row=4, column=0)
        self.divide_button = tk.Button(self, width=10, text="/", bg="grey", command = self.set_output())
        self.divide_button.grid(row=4, column=1)

    '''
    setOutput places the output message after calculating it using functions in operations module

    '''
    def set_output(self):
        outputNum = op.addition(num1=self.entry1.get(), num2=self.entry2.get())
        self.output = tk.Message(self, width=100, text=outputNum)
        self.output.grid(row=2, columnspan=2)
        print(self.entry1.get())
