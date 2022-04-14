from tkinter import *
from PIL import ImageTk, Image

from completegame.utils.utils import Utils

root10 = None


class Shop:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # def check_money(self):

    # def buy(self):

    def shop(self):
        root10 = Toplevel()

        root10.resizable(0, 0)
        root10.title("HANGMAN MARKET")
        root10.geometry('1200x680')
        fullcanvas2 = Canvas(root10, height='680', width='1300', bd=0, highlightthickness=0, relief='raised',
                             bg='black')
        fullcanvas2.pack()
        label_username = Label(root10, text='Welcome Back {} ! '.format(self.name.upper()),
                               font=('Comic Sans MS', 15, 'bold'), fg='red', bg='black')
        label_username.place(x=20, y=10)

        img0 = Image.open(r'hangman\Background\icon.jpg')
        img0 = img0.resize((70, 70), Image.ANTIALIAS)
        img0 = ImageTk.PhotoImage(image=img0)
        fullcanvas2.create_image(500, 35, image=img0)

        img1 = Image.open(r'hangman\Background\1.jpg')
        img1 = img1.resize((400, 256), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(image=img1)
        fullcanvas2.create_image(200, 198, image=img1)

        img2 = Image.open(r'hangman\Background\2.jpg')
        img2 = img2.resize((400, 256), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(image=img2)
        fullcanvas2.create_image(600, 198, image=img2)

        img3 = Image.open(r'hangman\Background\3.jpg')
        img3 = img3.resize((400, 256), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(image=img3)
        fullcanvas2.create_image(1000, 198, image=img3)

        img4 = Image.open(r'hangman\Background\4.jpg')
        img4 = img4.resize((400, 256), Image.ANTIALIAS)
        img4 = ImageTk.PhotoImage(image=img4)
        fullcanvas2.create_image(200, 491, image=img4)

        img5 = Image.open(r'hangman\Background\5.jpg')
        img5 = img5.resize((400, 256), Image.ANTIALIAS)
        img5 = ImageTk.PhotoImage(image=img5)
        fullcanvas2.create_image(600, 491, image=img5)

        img6 = Image.open(r'hangman\Background\6.jpg')
        img6 = img6.resize((400, 256), Image.ANTIALIAS)
        img6 = ImageTk.PhotoImage(image=img6)
        fullcanvas2.create_image(1000, 491, image=img6)

        button2 = Button(root10, text='BLOCK LAMPS : 5000', width=44, font=('Comic Sans MS', 11, 'bold'),
                         bg='DodgerBlue2',
                         fg='white')
        button2.place(x=400, y=326)

        button4 = Button(root10, text='NEON BALLS: 10000', width=44, font=('Comic Sans MS', 11, 'bold'),
                         bg='DodgerBlue2',
                         fg='white')
        button4.place(x=0, y=619)

        button5 = Button(root10, text='ELECTRO-EAGLE : 12000', width=44, font=('Comic Sans MS', 11, 'bold'),
                         bg='DodgerBlue2',
                         fg='white')
        button5.place(x=400, y=619)
        button1 = Button(root10, text='RING OF LIGHT : 3000', width=44, font=('Comic Sans MS', 11, 'bold'),
                         bg='DodgerBlue2', fg='white')
        button1.place(x=0, y=326)

        button3 = Button(root10, text='CITY LIGHTS : 7000', width=44, font=('Comic Sans MS', 11, 'bold'),
                         bg='DodgerBlue2',
                         fg='white')
        button3.place(x=800, y=326)

        button6 = Button(root10, text='HONEYCOMB : 15000', width=44, font=('Comic Sans MS', 11, 'bold'),
                         bg='DodgerBlue2',
                         fg='white')
        button6.place(x=800, y=619)

        label_money = Label(root10, text=': {}'.format(self.money), font=('Comic Sans MS', 25, 'bold'),
                            bg='black', fg='white')
        label_money.place(x=530, y=10)

        def button_exit():
            Utils.ok(root10)

        button_back = Button(root10, text=' Back ', width=15, font=('Comic Sans MS', 15, 'bold'),
                             bg='red', fg='white', command=button_exit)
        button_back.place(x=800, y=10)
        root10.mainloop()
