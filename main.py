import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import rsa
import os
import time

class Test(tk.Tk):
    def __init__(self, test_type):
        super().__init__()
        self.title(f'Test {test_type}')
        self.geometry('640x480')

        # Frame
        if test_type == 'frame':
            frame = tk.Frame(self,
                             bg='green',
                             bd=50,
                             width=200,
                             height=200,
                             highlightbackground='yellow',
                             highlightcolor='red',
                             highlightthickness=40,
                             relief='raised',
                             cursor='spider')
            frame.pack()
            chechbtn = tk.Checkbutton(frame, name='pushme')
            chechbtn.pack()
            new_frame = tk.Frame(self, bg='red', bd=20, width=100, height=80, cursor='man')
            new_frame.pack()

        # Button
        if test_type == 'btn':
            frame = tk.Button(self,
                              text='pushme',
                              activebackground='green',
                              activeforeground='yellow',
                              bd=7,
                              bg='black',
                              fg='white',
                              font='helvetica 20',
                              height=2,
                              width=100,
                              justify='right',
                              padx=6,
                              pady=8,
                              relief='ridge',
                              state='normal',
                              underline=2,
                              wraplength=0,
                              command=self.test_btn)
            frame.flash() #method
            frame.invoke() # method: Call callback
            frame.pack()
            entry = tk.Entry(self, width=10)
            entry.pack()
            btn_2 = tk.Button(self, text='New button', command= lambda: self.test_btn2(entry.get()))
            btn_2.pack()


        # Entry
        if test_type == 'entry':
            input_scrollbar = tk.Scrollbar(self)
            entry = tk.Entry(self,
                             bg='yellow',
                             bd=10,
                             # command=,
                             cursor='star',
                             font = 'arial 8',
                             # exportselection=0.
                             fg='red',
                             highlightcolor='green',
                             justify=tk.CENTER,
                             relief=tk.RIDGE,
                             selectbackground='blue',
                             selectborderwidth=10,
                             selectforeground='pink',
                             # show='*',
                             state='normal',
                             # textvariable=str_var
                             width=30,
                             xscrollcommand = input_scrollbar.set)
            input_scrollbar.config(command=entry.xview)
            entry.grid(column=0, row=0, sticky="WESN")
            input_scrollbar.grid(column=0, row=1, sticky="WESN")
            entry.insert(0, 'I love my life. I have never heard nothing better than my bro` speech')
            # entry.delete(3)
            # entry.delete(4, tk.END)
            str = entry.get()
            entry.icursor(5)
            entry.index(8)

        # Label
        if test_type == 'label':
            label = tk.Label(self,
                             anchor = 'se',
                             bg='yellow',
                             bd=10,
                             # bitmap=,
                             cursor='star',
                             font='arial 20',
                             fg='red',
                             highlightcolor='green',
                             height=5,
                             # image=,
                             justify=tk.CENTER,
                             padx=4,
                             pady=4,
                             relief=tk.RIDGE,
                             text='test '*5,
                             # textvariable = str_var,
                             underline=0,
                             width=30,
                             wraplength=0)
            label.pack()
            label['text'] = 'aaa'


        # Text
        if test_type == 'text':
            input_scrollbar = tk.Scrollbar(self)
            text = tk.Text(self,
                             bg='yellow',
                             bd=10,
                             # command=,
                             cursor='star',
                             height=5,
                             font='arial 8',
                             # exportselection=0.
                             fg='red',
                             highlightcolor='green',
                             relief=tk.RIDGE,
                             selectbackground='blue',
                             selectborderwidth=10,
                             selectforeground='pink',
                             # show='*',
                             state='normal',
                             # textvariable=str_var
                             width=30,
                           yscrollcommand = input_scrollbar.set)
            input_scrollbar.config(command=text.yview)
            text.grid(column=0, columnspan=3, row=0, sticky="WESN")
            input_scrollbar.grid(column=3, row=0, sticky="WESN")

        # Grid
        if test_type == 'grid':
            tk.Label(text="Имя:").grid(row=0, column=0)
            table_name = tk.Entry(width=30)
            table_name.grid(row=0, column=1, columnspan=3)

            tk.Label(text="Столбцов:").grid(row=1, column=0)
            table_column = tk.Spinbox(width=7, from_=1, to=50)
            table_column.grid(row=1, column=1)
            tk.Label(text="Строк:").grid(row=1, column=2)
            table_row = tk.Spinbox(width=7, from_=1, to=100)
            table_row.grid(row=1, column=3)

            tk.Button(text="Справка").grid(row=2, column=0)
            tk.Button(text="Вставить").grid(row=2, column=2)
            tk.Button(text="Отменить").grid(row=2, column=3)


    def test_btn(self):
        messagebox.showinfo('Test button', 'Is works')

    def test_btn2(self, str):
        messagebox.showinfo('Test button', str)


if __name__ == '__main__':
    types = ['frame', 'btn', 'entry', 'label', 'text', 'grid']
    test = Test(types[-1])
    test.mainloop()
