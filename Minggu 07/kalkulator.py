from functools import partial
import tkinter as tk

class calculatorApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kalkulator Tkinter")
        self.createButton()
        self.decider = False
    
    def createButton(self):
        self.screen = tk.Entry(self, width=25)
        self.screen.grid(row=0, column=0, columnspan=5)

        btn_list = [
            '1','2','3',
            '4','5','6',
            '7','8','9',
            '0','+','-',
            'C','/','*',
            '='
        ]

        row = 1
        column = 0

        for container in btn_list:
            command = partial(self.count, container)
            if container == '=':
                tk.Button(self, text='=', width=22, command=command).grid(row=row, column=column, columnspan=5)
            else: 
                tk.Button(self, text=container, width=5, command=command).grid(row=row, column=column)
            column += 1
            if column > 2:
                column = 0
                row += 1
    
    def count(self, key):
        if key == '=':
            self.decider = True
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, str(result))
            except:
                self.screen.insert(tk.END, "->Error!")
        elif key == 'C':
            self.screen.delete(0, tk.END)
        else:
            if self.decider:
                self.screen.delete(0, tk.END)
                self.decider = False
            self.screen.insert(tk.END, key)

call = calculatorApplication()
call.mainloop()