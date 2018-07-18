import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    #PLACING THE BUTTONS AND TEXT
    def create_widgets(self):
        #Frames for operation buttons
        opframe1 = tk.Frame(self, width=100, height=80)
        opframe1.pack()
        opframe2 = tk.Frame(self, width=100, height=80)
        opframe2.pack()

        #Operation Buttons
        self.add_button = tk.Button(opframe1, width=10, text="Add", bg ="grey", command=self.do_add)
        self.add_button.pack(side="left")
        self.subtract_button = tk.Button(opframe1, width=10, text="Subtract", bg="grey", command = self.do_subtract)
        self.subtract_button.pack(side="right")
        self.mult_button = tk.Button(opframe2, width=10, text="Multiply", bg ="grey", command=self.do_mult)
        self.mult_button.pack(side="left")
        self.divide_button = tk.Button(opframe2, width=10, text="Divide", bg="grey", command = self.do_div)
        self.divide_button.pack(side="right")

    #PLACEHOLDER FUNCTIONS TO PERFORM OPERATIONS
    def do_add(self):
        print("DOING ADDITION")
    def do_subtract(self):
        print("DOING SUBTRACT")
    def do_mult(self):
        print("DOING MULTIPLY")
    def do_div(self):
        print("DOING DIVIDE")

root = tk.Tk()
app = Calculator(master = root)
app.mainloop()
