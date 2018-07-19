'''
This module sets up the Graphical User Interface of the Tkinter Calculator.

imports:
tkinter framework
addition function from operations module

'''

import tkinter as tk

#CalcLayout class to make GUI
class CalcLayout(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    '''
    create_widgets sets up the widets on the master frame
    Uses grid geometry management

    Creates:
    Entry fields
    Operation Buttons
    '''
    def create_widgets(self):

        self.outputNum = tk.StringVar()
        self.firstNum = tk.StringVar()
        self.secondNum = tk.StringVar()

        #Enter Field
        self.entry1 = tk.Entry(self, textvariable=self.firstNum, width=10, justify="center", bd=4, selectborderwidth=3)
        self.entry1.grid(row=0, column=0)
        self.entry2 = tk.Entry(self, textvariable=self.secondNum, width=10, justify="center", bd=4, selectborderwidth=3)
        self.entry2.grid(row=0, column=1)

        #Operation Buttons
        self.add_button = tk.Button(self, width=10, text="+", bg ="grey", command= lambda: self.set_output(type='+'))
        self.add_button.grid(row=3, column=0)
        self.subtract_button = tk.Button(self, width=10, text="-", bg="grey", command= lambda: self.set_output(type='-'))
        self.subtract_button.grid(row=3,column=1)
        self.mult_button = tk.Button(self, width=10, text="*", bg ="grey", command= lambda: self.set_output(type='*'))
        self.mult_button.grid(row=4, column=0)
        self.divide_button = tk.Button(self, width=10, text="/", bg="grey", command= lambda: self.set_output(type='/'))
        self.divide_button.grid(row=4, column=1)

        self.output = tk.Message(self, width=100, textvariable=self.outputNum)
        self.output.grid(row=2, columnspan=2)
        self.outputNum.set("INITIAL")


    def set_output(self, type):

        if(type=='+'):
            self.outputNum.set(int(self.entry1.get())+int(self.entry2.get()))
            self.master.update_idletasks()
        elif(type=='-'):
            self.outputNum.set(int(self.entry1.get())-int(self.entry2.get()))
            self.master.update_idletasks()
        elif(type=='*'):
            self.outputNum.set(int(self.entry1.get())*int(self.entry2.get()))
            self.master.update_idletasks()
        elif(type=='/'):
            self.outputNum.set(int(self.entry1.get())/int(self.entry2.get()))
            self.master.update_idletasks()
