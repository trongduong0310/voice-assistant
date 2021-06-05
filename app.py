from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import main
import sys


class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass
    
root = Tk()
root.title('Virtual Assistant')
root.geometry('520x320')

panel = Label(root) 
panel.pack(side='right', fill='both', expand='no')
compText = StringVar()
userText = StringVar()
userText.set('Your Virtual Assistant')
top = Message(textvariable=userText, bg='black',fg='white')
top.config(font=("Century Gothic", 15, 'bold'))
top.pack(side='top', fill='both', expand='yes')
btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white',command=main.MainFucntion).pack(fill='x', expand='no')
btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
t = tk.Text()
t.pack()
pl = PrintLogger(t)
sys.stdout = pl
root.mainloop()