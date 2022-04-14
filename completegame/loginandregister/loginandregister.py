from tkinter import *
import csv
from tkinter import messagebox

from completegame.utils.utils import Utils


class Loginsignin:
    def __init__(self, parent):
        self.parent = parent
        self.entryscreen()

    def login(self):
        global usrnm, psd, f1, f2, flag
        flag = 0
        if (usrnm.get() is not None) and (psd.get() is not None) and flag == 0:
            username_entered = usrnm.get()
            password_entered = psd.get()

            with open('loginandregister\databasecsv.csv', newline='') as csvfile:
                data = csv.reader(csvfile)
                for row in data:

                    try:
                        if row[1] == username_entered and row[2] == password_entered:

                            with open('loginandregister\currentprofile.csv', 'w') as f:
                                data1 = csv.writer(f)
                                data1.writerow(row)
                            flag = 1
                            screenlogin.destroy()
                            self.parent.destroy()
                            break

                        else:
                            pass

                    except:
                        pass

                if flag == 0:
                    messagebox.showinfo("ERROR", "Username and Password Do Not Match")
                    screenlogin.destroy()
        else:
            pass

    def signin(self):
        global usrnm, confpsd, psd, f1, f2, screensignin, name, city, age_slider, screenlogin
        if usrnm.get() != '' and psd.get() != '' and name.get() != '' and city.get() != '' and age_slider.get() != '':
            username_entered = usrnm.get()
            password_entered = psd.get()
            name_entered = name.get()
            age_entered = age_slider.get()
            city_entered = city.get()
            yes = 'y'

            while yes == 'y':
                if password_entered != confpsd.get():
                    label = Label(screensignin, text="Passwords Do Not Match", bg='black', foreground='red',
                                  font='Comic')
                    label.place(x=140, y=245)
                    yes = 'n'
                else:
                    yes = 'n'

                    lst_details = [name_entered, username_entered, password_entered, age_entered,
                                   city_entered]  # first is total score then individual score
                    with open('loginandregister\databasecsv.csv', 'a', newline='') as f:
                        data = csv.writer(f)
                        data.writerow(lst_details)
                    screensignin.destroy()
                    self.login_screen()

        else:
            label_required = Label(screensignin, text="All Fields Required", bg='black', foreground='red',
                                   font='Comic')
            label_required.place(x=150, y=520)

    def signin_screen(self):
        global usrnm, psd, screensignin, confpsd, name, city, age_slider

        screensignin = Tk()
        screensignin.iconbitmap('hangman.ico')
        self.parent.destroy()
        screensignin.geometry('480x600')
        screensignin.title("SIGN-UP WINDOW")
        screensignin.configure(bg='black')
        screensignin.protocol("WM_DELETE_WINDOW", lambda root1=screensignin: Utils.on_closing(screensignin))

        Label(screensignin, text='SIGN UP WINDOW', bg='orange', width='300', height='2',
              font=("Comic Sans MS", 13, 'bold')).pack()

        label2 = Label(screensignin, text="Username *", bg='black', foreground='white', font='Comic')
        label2.place(x=50, y=70)

        usrnm = Entry(screensignin, width='40')
        usrnm.place(x=125, y=106)

        label3 = Label(screensignin, text="Password *", bg='black', foreground='white', font='Comic')
        label3.place(x=50, y=130)

        psd = Entry(screensignin, width='40', show='*')
        psd.place(x=125, y=166)

        label4 = Label(screensignin, text="Confirm Password *", bg='black', foreground='white',
                       font='Comic')
        label4.place(x=50, y=190)

        confirm_psd = Entry(screensignin, width='40', show='*')
        confirm_psd.place(x=125, y=226)

        label5 = Label(screensignin, text="Name *", bg='black', foreground='white', font='Comic')
        label5.place(x=50, y=250)

        name = Entry(screensignin, width='40')
        name.place(x=125, y=286)

        label6 = Label(screensignin, text="Age *", bg='black', foreground='white', font='Comic')
        label6.place(x=50, y=310)

        age_slider = Scale(screensignin, from_=5, to=85, orient=HORIZONTAL, background='black', foreground='white',
                           length='239', tickinterval=15)
        age_slider.place(x=125, y=326)

        label7 = Label(screensignin, text="City *", bg='black', foreground='white',
                       font='Comic')
        label7.place(x=50, y=385)

        city = Entry(screensignin, width='40')
        city.place(x=125, y=421)

        button_submit = Button(screensignin, text='SIGN UP', width='20', height=2, bg='orange', fg='black',
                               command=self.signin)
        button_submit.place(x=150, y=470)

        screensignin.mainloop()

    def login_screen(self):
        global usrnm, psd, screenlogin

        screenlogin = Tk()
        screenlogin.iconbitmap('hangman.ico')
        screenlogin.geometry('450x350')
        screenlogin.title("LOGIN WINDOW")
        screenlogin.configure(bg='black')

        Label(screenlogin, text='LOGIN WINDOW', bg='orange', width='300', height='2',
              font=("Comic Sans MS", 13, 'bold')).pack()

        label2 = Label(screenlogin, text="Username *", bg='black', foreground='white', font='Comic')
        label2.place(x=25, y=100)

        usrnm = Entry(screenlogin, width='40')
        usrnm.place(x=140, y=106)

        label3 = Label(screenlogin, text="Password *", bg='black', foreground='white', font='Comic')
        label3.place(x=25, y=180)

        psd = Entry(screenlogin, width='40', show='*')
        psd.place(x=140, y=186)

        button_submit = Button(screenlogin, text='LOGIN', width='20', height=2, bg='orange', fg='black',
                               command=self.login)
        button_submit.place(x=150, y=250)

        screenlogin.mainloop()

    def entryscreen(self):
        global screen
        self.parent = Tk()
        self.parent.iconbitmap('hangman.ico')
        self.parent.protocol("WM_DELETE_WINDOW", lambda root1=self.parent: Utils.on_closing(self.parent))
        self.parent.geometry('450x325')
        self.parent.title("LOGIN OR SIGN IN WINDOW")
        self.parent.configure(bg='yellowgreen')

        label2 = Label(self.parent, text='HANGMAN', bg='yellow', width="300", height='2',
                       font=("Comic Sans MS", 15, 'bold'))
        label2.pack()

        label1 = Label(self.parent, text='LOGIN OR SIGN IN', bg='yellow', width="300", height='1',
                       font=("Comic Sans MS", 13))
        label1.pack()

        Label(self.parent, text='', bg='yellowgreen').pack()
        Label(self.parent, text='', bg='yellowgreen').pack()

        button_login = Button(self.parent, text='LOGIN', width='30', height=2, command=self.login_screen)
        button_login.configure(bg='pink', foreground='red')
        button_login.pack()

        Label(self.parent, text='', bg='yellowgreen').pack()
        Label(self.parent, text='OR', bg='yellowgreen').pack()
        Label(self.parent, text='', bg='yellowgreen').pack()

        button_signin = Button(self.parent, text='SIGN IN', width='30', height=2, command=self.signin_screen)
        button_signin.configure(bg='pink', foreground='red')
        button_signin.pack()

        self.parent.mainloop()


if __name__ == "__main__":
    root = None
    Loginsignin(root)
