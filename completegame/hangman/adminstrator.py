from tkinter import *
import csv
from PIL import ImageTk, Image
import random

#from completegame.utils.utils import Utils

class Example:
    def __init__(self, parent):

        self.parent = parent
        self.canvas = Canvas(self.parent, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(self.parent, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((6,6), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        print(self.collect_data)

    @property
    def collect_data(self):
        with open('loginandregister\databasecsv.csv',newline='') as csvfile1:
            data1 = csv.reader(csvfile1)
            data = list(data1)
        return data
##        for row in range(50):
##            Label(self.frame, text=row).grid(row=row, column=1)

    #def show_data(self):
        

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    data=None
    root = Tk()
    root.geometry('500x500')
    Example(root)
    root.mainloop()
