from tkinter import Tk, Button, StringVar, Entry

class Calculator:
    def __init__(self, root):
        self.equation = StringVar()
        self.entry_value = ''
        Entry(root, width=17, bg='#ccddff', font=('JetBrains Mono', 28), textvariable=self.equation).place(x=0, y=0)
        # Define buttons
        Button(root, width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(root, width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(root, width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(root, width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0, y=125)
        Button(root, width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90, y=125)
        Button(root, width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180, y=125)
        Button(root, width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0, y=200)
        Button(root, width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90, y=200)
        Button(root, width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180, y=200)
        Button(root, width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0, y=275)
        Button(root, width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=90, y=275)
        Button(root, width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=180, y=275)
        Button(root, width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show('0')).place(x=90, y=350)
        Button(root, width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(root, width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)
        Button(root, width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
        Button(root, width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(root, width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(root, width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(root, width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)

    def show(self, value):
        current_text = self.equation.get()
        new_text = current_text + str(value)
        self.equation.set(new_text)

    def solve(self):
        try:
            result = eval(self.equation.get())
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Error')

    def clear(self):
        self.equation.set('')

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator") 
    root.config(bg = 'gray')
    root.geometry("350x420")
    app = Calculator(root)
    root.mainloop()
