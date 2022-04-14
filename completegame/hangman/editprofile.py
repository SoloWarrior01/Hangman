from tkinter import *
import csv
from tkinter import messagebox


def edit_profile():
    with open('loginandregister\currentprofile.csv', newline='') as csvfile1:
        data1 = csv.reader(csvfile1)
        listdata = list(data1)
        currentname = listdata[0][0]
        currentusername = listdata[0][1]
        currentpassword = listdata[0][2]
        currentage = listdata[0][3]
        currentcity = listdata[0][4]

    def updateprofile():
        global usrnm, psd, confpsd, name, age_slider, city, screensignin

        if usrnm.get() != '' and psd.get() != '' and name.get() != '' and city.get() != '' and age_slider.get() != None:
            username_entered = usrnm.get()
            password_entered = psd.get()
            name_entered = name.get()
            age_entered = age_slider.get()
            city_entered = city.get()

            yes = 'y'
            while yes == 'y':
                if password_entered != confpsd.get():
                    label = Label(screensignin, text="Passwords Do Not Match", bg='black', foreground='red',
                                  font=('Comic', 15, 'bold'))
                    label.place(x=120, y=450)
                    yes = 'n'
                else:
                    yes = 'n'
                    with open('completegame\loginandregister\databasecsv.csv', 'r', newline='') as f:
                        data = csv.reader(f)
                        lst = list(data)
                    with open('completegame\loginandregister\databasecsv.csv', 'w', newline='') as f:
                        for i in lst:
                            if i[1] == listdata[0][1] and i[2] == listdata[0][2]:
                                i[1] = username_entered
                                i[0] = name_entered
                                i[2] = password_entered
                                i[3] = age_entered
                                i[4] = city_entered
                        data1 = csv.writer(f)
                        data1.writerows(lst)
                    with open('completegame\loginandregister\currentprofile.csv', 'w', newline='') as csvfile1:
                        listdata[0][1] = username_entered
                        listdata[0][0] = name_entered
                        listdata[0][2] = password_entered
                        listdata[0][3] = age_entered
                        listdata[0][4] = city_entered
                        data1 = csv.writer(csvfile1)
                        data1.writerows(listdata)
            screensignin.destroy()

        else:
            label = Label(screensignin, text="*ALL FIELDS REQUIRED! ", bg='black', foreground='red',
                          font=('Comic', 15, 'bold'))
            label.place(x=120, y=450)

    def edit():
        global usrnm, psd, confpsd, name, age_slider, city, screensignin
        screensignin = Tk()
        screensignin.geometry('480x600')
        screensignin.title("EDIT PROFILE")
        screensignin.configure(bg='black')

        Label(screensignin, text='EDIT MY PROFILE', bg='orange', width='300', height='2',
              font=("Comic Sans MS", 13, 'bold')).pack()

        label2 = Label(screensignin, text="Username *", bg='black', foreground='white', font='Comic')
        label2.place(x=50, y=70)

        usrnm = Entry(screensignin, width='40')
        usrnm.place(x=125, y=106)

        label3 = Label(screensignin, text="Password *", bg='black', foreground='white', font='Comic')
        label3.place(x=50, y=130)

        psd = Entry(screensignin, width='40', show='*')
        psd.place(x=125, y=166)

        label4 = Label(screensignin, text="Confirm Password *", bg='black', foreground='white',font='Comic')
        label4.place(x=50, y=190)

        confirm_psd = Entry(screensignin, width='40', show='*')
        confirm_psd.place(x=125, y=226)

        label5 = Label(screensignin, text="Name *", bg='black', foreground='white', font='Comic')
        label5.place(x=50, y=250)

        name = Entry(screensignin, width='40')
        name.place(x=125, y=286)

        label6 = Label(screensignin, text="Age *", bg='black', foreground='white', font='Comic')
        label6.place(x=50, y=310)

        age_slider = Scale(screensignin, from_=5, to=85, orient=HORIZONTAL, background='black',
                           foreground='white', length='239', tickinterval=15)
        age_slider.place(x=125, y=326)

        label7 = Label(screensignin, text="City *", bg='black', foreground='white', font='Comic')
        label7.place(x=50, y=385)

        city = Entry(screensignin, width='40')
        city.place(x=125, y=421)

        button_submit = Button(screensignin, text='UPDATE', width='20', height=2, bg='orange', fg='black',
                               command=updateprofile)
        button_submit.place(x=150, y=500)

        screensignin.mainloop()

    edit()


def delete_profile(screen_1, screen_2, screen_3, screen_4, screen_5):
    with open('loginandregister\currentprofile.csv', newline='') as csvfile1:
        data1 = csv.reader(csvfile1)
        listdata = list(data1)

    i = messagebox.askyesnocancel(title='delete account', message='DO YOU WANT TO DELETE YOUR ACCOUNT?!')
    if i:
        # account delete
        try:
            screen_1.destroy()
        except:
            pass
        try:
            screen_2.destroy()
        except:
            pass

        try:
            screen_3.destroy()
        except:
            pass

        try:
            screen_4.destroy()
        except:
            pass

        try:
            screen_5.destroy()
        except:
            pass

        with open('loginandregister\databasecsv.csv', 'r', newline='') as f:
            data = csv.reader(f)
            lst = list(data)
        with open('loginandregister\databasecsv.csv', 'w', newline='') as f:
            for i in lst:
                if i[1] == listdata[0][1] and i[2] == listdata[0][2]:
                    lst.remove(i)
            data1 = csv.writer(f)
            data1.writerows(lst)
