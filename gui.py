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
    def create_widgets(self):s

        self.currentAns = 0
        self.outputNum = tk.StringVar()
        self.firstNum = tk.StringVar()
        self.operation_message = tk.StringVar()
        self.current_op = 0

        self.operation = tk.Message(self, textvariable=self.operation_message, width=80, justify="center")
        self.operation.grid(row=0, columnspan=2)

        #Enter Field
        self.entry1 = tk.Entry(self, textvariable=self.firstNum, width=20, justify="center", bd=4, selectborderwidth=3)
        self.entry1.grid(row=1, columnspan=2)

        #Operation Buttons
        self.add_button = tk.Button(self, width=10, text="+", bg ="grey", command= lambda: self.set_output(type='+'))
        self.add_button.grid(row=3, column=0)
        self.subtract_button = tk.Button(self, width=10, text="-", bg="grey", command= lambda: self.set_output(type='-'))
        self.subtract_button.grid(row=3,column=1)
        self.mult_button = tk.Button(self, width=10, text="*", bg ="grey", command= lambda: self.set_output(type='*'))
        self.mult_button.grid(row=4, column=0)
        self.divide_button = tk.Button(self, width=10, text="/", bg="grey", command= lambda: self.set_output(type='/'))
        self.divide_button.grid(row=4, column=1)
        self.equal_button = tk.Button(self, width=50, text="=", bg="grey", command= self.set_result)
        self.equal_button.grid(row=5, columnspan=2)

        #self.current = tk.Message(self, width=50, textvariable=self.outputNum)
        #self.current.grid(row=0, column=2, sticky="w")
        #self.outputNum.set("INITIAL")


    def set_output(self, type):

        if(type=='+'):
            try:
                self.currentAns = self.currentAns + int(self.entry1.get())
                self.operation_message.set(str(self.currentAns) + " +")
                self.firstNum.set(self.currentAns)
                self.current_op = 0
                self.firstNum.set("")
                self.master.update_idletasks()
            finally:
                self.operation_message.set(str(self.currentAns) + " +")
                self.current_op = 0

        elif(type=='-'):
            try:
                self.currentAns = self.currentAns - int(self.entry1.get())
                self.operation_message.set(str(self.currentAns) + " -")
                self.firstNum.set(self.currentAns)
                self.current_op = 1
                self.firstNum.set("")
                self.master.update_idletasks()
            finally:
                self.operation_message.set(str(self.currentAns) + " -")
                self.current_op = 1

        elif(type=='*'):
            try:
                self.currentAns = self.currentAns * int(self.entry1.get())
                self.operation_message.set(str(self.currentAns) + " *")
                self.firstNum.set(self.currentAns)
                self.current_op = 2
                self.firstNum.set("")
                self.master.update_idletasks()
            finally:
                self.operation_message.set(str(self.currentAns) + " *")
                self.current_op = 2

        elif(type=='/'):
            try:
                self.currentAns = self.currentAns / int(self.entry1.get())
                self.operation_message.set(str(self.currentAns) + " /")
                self.firstNum.set(self.currentAns)
                self.current_op = 3
                self.firstNum.set("")
                self.master.update_idletasks()
            finally:
                self.operation_message.set(str(self.currentAns) + " /")
                self.current_op = 3

    def set_result(self):
        if self.current_op == 0:
            self.operation_message.set(self.currentAns + int(self.entry1.get()))
            self.currentAns = self.currentAns + int(self.entry1.get())
        elif self.current_op == 1:
            self.operation_message.set(self.currentAns - int(self.entry1.get()))
            self.currentAns = self.currentAns - int(self.entry1.get())
        elif self.current_op == 2:
            self.operation_message.set(self.currentAns * int(self.entry1.get()))
            self.currentAns = self.currentAns * int(self.entry1.get())
        elif self.current_op == 3:
            self.operation_message.set(self.currentAns / int(self.entry1.get()))
            self.currentAns = self.currentAns / int(self.entry1.get())
        self.firstNum.set("")
        self.master.update_idletasks()
