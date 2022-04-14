from tkinter import *
import pyttsx3
import csv
from threading import Thread
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
import random

from completegame.hangman.titleandman import Titleandman
from completegame.utils.utils import Utils
import completegame.hangman.editprofile as ed
from completegame.hangman.shop import Shop

'================================================LIST OF THINGS======================================================='
lstcolor = ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black', 'Brown', 'Azure', 'Ivory', 'Teal', 'Silver', 'Purple',
            'Gray', 'Orange', 'Maroon', 'Charcoal', 'Aquamarine', 'Coral', 'Fuchsia', 'Wheat', 'Lime', 'Crimson',
            'Khaki', 'Magenta', 'golden', 'Plum', 'Olive', 'Cyan']
lstmusic = ['piano', 'guitar', 'saxophone', 'voilin', 'trumphet', 'cello', 'accordion', 'flute', 'trombone', 'drum',
            'xylophone', 'keyboard', 'harmonica', 'mandolin', 'harp', 'bassoon', 'tuba', 'banjo', 'synthesizer',
            'theremin', 'bagpipe', 'organ', 'bell', 'sitar']
lstcar = ['Maruti', 'Hyundai', 'Mahindra', 'TataMotors', 'Honda', 'Toyota', 'Ford', 'Renault', 'Volkswagen', 'Datsun',
          'Skoda', 'Jeep', 'Nissan', 'Fiat', 'Lamborghini', 'Ferrari', 'AatonMartin', 'Chervolet', 'Mercedes',
          'Porsche', 'Bentley', 'Bugatti']
lstcountry = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria',
              'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
              'Bhutan''Bolivia', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia',
              'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa', 'Croatia',
              'Cuba', 'Cyprus', 'Denmark', 'Djibouti', 'Dominica', 'Dominica', 'Ecuador', 'Egypt', 'Salvador', 'Guinea',
              'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
              'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
              'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
              'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea', 'Kosovo', 'Kuwait', 'Kyrgyzstan''Laos', 'Latvia',
              'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar',
              'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia',
              'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar ', 'Namibia', 'Nauru',
              'Nepal', 'Netherlands', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
              'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Samoa',
              'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'Spain', 'Sudan',
              'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo',
              'Tonga', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'England', 'UnitedStates',
              'Uruguay', 'Uzbekistan', 'Vanuatu', 'VaticanCity', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
lststate = ['AndhraPradesh', 'ArunachalPradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
            'HimachalPradesh', 'JammuKashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'MadhyaPradesh', 'Maharashtra',
            'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'TamilNadu',
            'Telagana', 'Tripura', 'Uttarakhand', 'UttarPradesh', 'WestBengal']

s = ''
s1 = ''
vowels = 'aeiouAEIOU'  # stored vowels, used in line 131
lst1 = []  # contains hidden word(s1) in list format
lstdone = []  # this list contains the words which have already been shown to avoid reoccurance
count = 6  # this is used to count lives
replay = 0  # this ensures only 3 words per category
score = 0  # this is being used for score
countc = 0
show = ''
entered = ''  # this contains letters that have been entered already
chance = 0  # handles termination of the program
entryBox = None
flag = 0
play = 0
list1 = ''
# list_attempted = []
label_valid = 0
label_show_condition = 0

'===================================ROOT DEFINE====================================='
root = None
root1 = None
root2 = None
root3 = None
root4 = None

engine = pyttsx3.init()
engine.setProperty('rate', 125)


class Hangman:
    background = 6

    def __init__(self, list_info):
        self.listdata = list_info
        self.currentname = self.listdata[0][0]
        self.currentusername = self.listdata[0][1]
        self.currentpassword = self.listdata[0][2]
        self.currentage = self.listdata[0][3]
        self.currentcity = self.listdata[0][4]
        # self.money = self.listdata[0][5][0]
        self.money = 1000
        # self.background = self.listdata[0][5][2]
        self.choose()

    def restart(self):
        global copy_of_image, photo, root, countc, count, lst1, s1, replay, show, entered
        root.destroy()
        try:
            root2.destroy()

        except:
            pass

        s = ''  # --------# |
        countc = 0  # |
        count = 6  # |
        lst1 = []  # |
        s1 = ''  # |
        replay = play = flag = 0  # |---------- ALL REQUIRED VALUES ARE RESET
        show = ''  # |
        lst1 = []  # |
        entered = ''  # |
        list_attempted = []  # |
        label_valid = 0  # |
        label_show_condition = 0  # |
        # --------# |

        self.choose()

    @staticmethod
    def graph():
        with open('completegame\loginandregister\currentprofile.csv', 'r', newline='') as cp:
            data9 = csv.reader(cp)
            lst10 = list(data9)
            print(lst10, 'hi')
            x = []
            y = []

            if len(lst10[0]) - 11 >= 6:
                for i in range(len(lst10[0]) - 11, len(lst10[0])):
                    print(lst10[0][i])
                    y.append(int(lst10[0][i]))
                    print(y)
                print(y, 'hello')
            else:
                for i in range(6, len(lst10[0])):
                    print(lst10[0][i])
                    y.append(int(lst10[0][i]))
                    print(y)
                print(y, 'hello')
            for j in range(len(y)):
                x.append(j + 1)
            print(x)

            plt.title('MY PERFORMANCE GRAPH')
            plt.ylabel('SCORE')
            plt.xlabel('NO. OF GAMES PLAYED')
            plt.xticks(x)
            plt.yticks([0, 100, 200, 300, 400, 500, 600])
            plt.plot(x, y)
            plt.show()

    @staticmethod
    def delete():
        ed.delete_profile(root, root1, root2, root3, root4)
        # t1 = Thread(target=Utils.play)
        # t1.start()
        from completegame.Hangman import Main
        root0 = None
        Main(root0)

    def root_profile(self):
        global root4
        root4 = Tk()
        root4.resizable(0, 0)
        root4.title("HANGMAN")
        root4.iconbitmap('hangman.ico')
        root4.geometry('500x600')
        root4.configure(background='RosyBrown1')

        Label(root4, text='PROFILE', bg='turquoise', fg='maroon4', width='300', height='2',
              font=("Comic Sans MS", 30, 'bold')).pack()

        label_name = Label(root4, text='NAME- ', font=('times new roman', 18, 'bold'), background='RosyBrown1',
                           foreground='navy')
        label_name.place(x=10, y=150)

        label_name1 = Label(root4, text=self.currentname, font=('times new roman', 18, 'bold'), background='RosyBrown1',
                            foreground='dark green')
        label_name1.place(x=250, y=150)

        label_username = Label(root4, text='USERNAME- ', font=('times new roman', 18, 'bold'), background='RosyBrown1',
                               foreground='navy')
        label_username.place(x=10, y=210)

        label_show_profile = Label(root4, text=self.currentusername, font=('times new roman', 18, 'bold'),
                                   background='RosyBrown1', foreground='dark green')
        label_show_profile.place(x=250, y=210)

        label_age = Label(root4, text='AGE- ', font=('times new roman', 18, 'bold'), background='RosyBrown1',
                          foreground='navy')
        label_age.place(x=10, y=270)

        label_age1 = Label(root4, text=self.currentage, font=('times new roman', 18, 'bold'), background='RosyBrown1',
                           foreground='dark green')
        label_age1.place(x=250, y=270)

        label_city = Label(root4, text='CITY- ', font=('times new roman', 18, 'bold'), background='RosyBrown1',
                           foreground='navy')
        label_city.place(x=10, y=330)

        label_city1 = Label(root4, text=self.currentcity, font=('times new roman', 18, 'bold'), background='RosyBrown1',
                            foreground='dark green')
        label_city1.place(x=250, y=330)

        label_edit_profile = Label(root4, text='EDIT PROFILE', font=('times new roman', 18, 'bold'),
                                   background='RosyBrown1', foreground='DodgerBlue2')
        label_edit_profile.place(x=150, y=370)

        button_stats = Button(root4, text='EDIT', width=20, bg='dark blue', fg='orange',
                              font=('Calibri', 15), command=ed.edit_profile)
        button_stats.place(x=125, y=400)

        label_delete_profile = Label(root4, text='DELETE ACCOUNT', font=('times new roman', 18, 'bold'),
                                     background='RosyBrown1', foreground='DodgerBlue2')
        label_delete_profile.place(x=130, y=450)

        button_delete = Button(root4, text='DELETE', width=20, bg='dark blue', fg='orange',
                               font=('Calibri', 15), command=Hangman.delete)
        button_delete.place(x=125, y=480)

        button_back = Button(root4, text='BACK', width=20, bg='dark blue', fg='orange',
                             font=('Calibri', 15), command=root4.destroy)
        button_back.place(x=125, y=540)
        root4.mainloop()

    def root_stats(self):
        global root3
        with open('completegame\loginandregister\currentprofile.csv', newline='') as csvfile1:
            data1 = csv.reader(csvfile1)
            listdata = list(data1)
            total_score = 0
            count = 0
            for i in range(6, len(listdata[0])):
                total_score += int(listdata[0][i])
                count += 1
            lastscore = listdata[0][-1]

        root3 = Tk()
        root3.resizable(0, 0)
        root3.title("HANGMAN")
        root3.iconbitmap('hangman.ico')
        root3.geometry('500x600')
        root3.configure(background='grey')

        label1 = Label(root3, text='PERFORMANCE', bg='lime', width='21', height='1', fg='red',
                       font=("Comic Sans MS", 30, 'bold'))
        label2 = Label(root3, text='ANALYSIS', bg='lime', width='21', height='1', fg='red',
                       font=("Comic Sans MS", 30, 'bold'))

        label1.place(x=0, y=0)
        label2.place(x=0, y=50)

        label_total_score = Label(root3, text='TOTAL SCORE- ', font=('times new roman', 18, 'bold'), background='grey',
                                  foreground='red')
        label_total_score.place(x=10, y=150)

        label_total_score1 = Label(root3, text=total_score, font=('times new roman', 18, 'bold'), background='grey',
                                   foreground='blue2')
        label_total_score1.place(x=250, y=150)

        label_show_graph = Label(root3, text='SEE PERFORMANCE GRAPH', font=('times new roman', 18, 'bold', 'underline'),
                                 background='grey', foreground='gold')
        label_show_graph.place(x=70, y=340)

        label_show_profile = Label(root3, text='SEE PROFILE', font=('times new roman', 18, 'bold', 'underline'),
                                   background='grey', foreground='gold')
        label_show_profile.place(x=160, y=420)

        label_accuracy = Label(root3, text='ACCURACY - ', font=('times new roman', 18, 'bold'), background='grey',
                               foreground='red')
        label_accuracy.place(x=10, y=200)

        label_accuracy1 = Label(root3, text=str((total_score * 10) / (count * 600)) + '/10',
                                font=('times new roman', 18, 'bold'), background='grey', foreground='blue2')
        label_accuracy1.place(x=250, y=200)

        label_per = Label(root3, text='PERCENTAGE - ', font=('times new roman', 18, 'bold'), background='grey',
                          foreground='red')
        label_per.place(x=10, y=250)

        label_per1 = Label(root3, text=str(int((total_score * 100) / (count * 600))) + '%',
                           font=('times new roman', 18, 'bold'), background='grey', foreground='blue2')
        label_per1.place(x=250, y=250)

        label_last_score = Label(root3, text='LAST SCORE- ', font=('times new roman', 18, 'bold'), background='grey',
                                 foreground='red')
        label_last_score.place(x=10, y=300)

        label_last_score1 = Label(root3, text=lastscore, font=('times new roman', 18, 'bold'), background='grey',
                                  foreground='blue2')
        label_last_score1.place(x=250, y=300)

        button_stats = Button(root3, text='GRAPH', width=15, bg='orange', fg='dark blue', font=('Calibri', 15),
                              command=Hangman.graph)
        button_stats.place(x=150, y=380)

        button_profile = Button(root3, text='PROFILE', width=15, bg='orange', fg='dark blue', font=('Calibri', 15),
                                command=self.root_profile)
        button_profile.place(x=150, y=460)

        button_back = Button(root3, text='BACK', width=15, bg='orange', fg='dark blue', font=('Calibri', 15),
                             command=root3.destroy)
        button_back.place(x=150, y=520)

        root3.mainloop()

    def win_loss_window(self, condition):
        global root2, count

        root2 = Tk()
        root2.resizable(0, 0)
        root2.title("HANGMAN")
        root2.iconbitmap('hangman.ico')
        root2.geometry('500x340')
        root2.configure(background='orangered')

        label_condition = Label(root2, text=condition, font=("Times new Roman", 30, 'bold'), background='orangered',
                                foreground='gold')  # at last it prints the final hidden word
        label_condition.place(x=150, y=10)

        button1 = Button(root2, text='REPLAY', width=15, bg='violet', font=("Comic Sans MS", 12, 'bold'),
                         command=self.restart)

        button2 = Button(root2, text='STATISTICS', width=15, bg='violet', font=("Comic Sans MS", 12, 'bold'),
                         command=self.root_stats)

        button1.place(x=130, y=70)
        button2.place(x=130, y=120)

        label_right = Label(root2, text='THE CORRECT WORD WAS-', font=('Comic Sans MS', 20), background='orangered',
                            foreground='yellow')
        label_right.place(x=20, y=160)

        label_right_word = Label(root2, text=s, font=('algerian', 28, 'bold'), background='orangered',
                                 foreground='blue')
        label_right_word.place(x=100, y=195)

        label_sc = Label(root2, text='YOUR SCORE WAS -', font=('Comic Sans MS', 20), background='orangered',
                         foreground='yellow')
        label_sc.place(x=20, y=240)

        label_score = Label(root2, text=str(count * 100), font=('algerian', 30, 'bold'), background='orangered',
                            foreground='blue')
        label_score.place(x=200, y=280)

        root2.mainloop()

    def game_execution(self):
        global count, countc, list1, show, score, root, flag, play, chance, entered, lst1, label_word, s2, replay, root2
        global canvas, fullcanvas1, label_wrong_guess, label_valid_consonant, currentusername, play

        list_attempted = []
        while count >= 1 and countc > 0:  # if you have lives more than 0   and   if consonants yet to be found is greater that 0
            flag = 0
            myfile = open('guessed.txt', 'r')
            list1 = myfile.readline()
            try:
                label_wrong_guess.destroy()
            except:
                pass

            try:
                label_already_entered.destroy()
            except:
                pass
            try:
                label_valid_consonant.destroy()
            except:
                pass
            if list1 in list_attempted:
                try:
                    label_valid_consonant.destroy()
                    # if its not the desired consonant else loop is executed and this is printed
                    label_already_entered = Label(text="ALREADY ENTERED", font=('Calibri body', 20), background='black',
                                                  foreground='orange')  # as input is wrong... this is prnted
                    label_already_entered.place(x=120, y=330)
                    break
                except:
                    # if its not the desired consonant else loop is executed and this is printed
                    label_already_entered = Label(text="ALREADY ENTERED", font=('Calibri body', 20), background='black',
                                                  foreground='orange')  # as input is wrong... this is prnted
                    label_already_entered.place(x=120, y=330)
                    break

            list_attempted.extend(list1)
            myfile.close()
            entered = entered + list1 + ','  # adds the letters which have been entered
            label_done = Label(root, text=entered, background='black', font=('Comic Sans MS', 22), foreground='magenta')
            label_done.place(x=270, y=500)

            # if guess is not in the letters already present in the list of elements already contained in the hidden word
            if list1 not in lst1:

                # if guess is not part of vowels, hidden word, digits and special characters, it enters the loop
                if (list1 not in vowels) and (list1 not in s1) and (list1.isdigit() == False) and (
                        list1 not in '!@#$%^&*()_+-=[]{}|\;\':",./<>?~`'):
                    for m in range(len(s)):  # searches the letter in the whole complete word
                        if list1 == s[m]:  # if found
                            lst1[
                                m] = list1  # enter in the letter(guess) in the list which consists of the elements present in the hidden word at the correct index to avoid it getting entered by the player again
                            show = ''  # refreshes it by making in empty constant

                            for p in lst1:
                                show = show + p + ' '  # adds p in the variable 'show' to display the progress to find the hidden word
                            flag += 1  # if consonant is correct 1 is added to the value of flag
                            play += 1  # appends the value of play
                            s2 = show  # puts data of show in s2 and show will be refreshed again

                            countc -= 1  # decreases the consonant count as one consonant is guessed correctly
                            if countc != 0:
                                T2 = Thread(target=Utils.play3)  # create thread
                                T2.start()

                    if flag == 0:  # if flag is 0 i.e. if the player entered the wrong input
                        if play == 0:  # if not even once the player has entered correct input play will be zero
                            label_word = Label(root, text=s1, font=("Comic Sans MS", 35), background='black',
                                               foreground='cyan')
                            label_word.place(x=150, y=210)
                        elif play != 0:  # if play is not 0 i.e. >0 then the s2(changed string) follows(which contains data of 'show')
                            try:
                                label_word.destroy()
                                label_word = Label(root, text=s2, font=("Comic Sans MS", 35), background='black',
                                                   foreground='cyan')  # at last it prints the final hidden word
                                label_word.place(x=150, y=210)
                            except:
                                label_word = Label(root, text=s2, font=("Comic Sans MS", 35), background='black',
                                                   foreground='cyan')  # at last it prints the final hidden word
                                label_word.place(x=150, y=210)
                        count -= 1  # decreases a life as input is a wrong guess
                        Titleandman.hanging_man(fullcanvas1, count)
                        T2 = Thread(target=Utils.play7)  # create thread
                        T2.start()
                        label_wrong_guess = Label(root, text="OHho! Wrong guess     ", font=('Calibri body', 20),
                                                  background='black',
                                                  foreground='red')  # as input is wrong... this is printed
                        label_wrong_guess.place(x=120, y=330)

                    try:
                        label_word.destroy()
                        label_word = Label(root, text=show, font=("Comic Sans MS", 35), background='black',
                                           foreground='cyan')  # at last it prints the final hidden word
                        label_word.place(x=150, y=210)
                    except:
                        label_word = Label(root, text=show, font=("Comic Sans MS", 35), background='black',
                                           foreground='cyan')  # at last it prints the final hidden word
                        label_word.place(x=150, y=210)

                    label_lives_left = Label(root, text=' ' + str(count), font=("Comic Sans MS", 25),
                                             background="black",
                                             foreground='yellow')  # prints the no. of lives remaining
                    label_lives_left.place(x=440, y=570)

                    if countc == 0:  # if no. of constants yet to be found is 0, i.e. all are found
                        replay += 1  # for next word, replay is appended (0<=replay<3)

                        score += count * 100  # score is calculated for all 3 words so lives left multiplied by 100 is added to the existing score

                        with open('completegame/loginandregister/databasecsv.csv', 'r', newline='') as db:
                            data5 = csv.reader(db)
                            data5 = list(data5)
                            for i in range(len(data5)):
                                if data5[i][1] == self.currentusername and data5[i][2] == self.currentpassword:
                                    earlier_money = data5[i][5]
                                    # data5[i][5] = int(earlier_money) + score  # adds money
                                    data5[i][5] = str(data5[i][5])
                                    data5[i].append(str(count * 100))
                                    lst6 = data5[i]
                        with open('completegame\loginandregister\databasecsv.csv', 'w', newline='') as db1:
                            data6 = csv.writer(db1)
                            data6.writerows(data5)

                        with open('completegame\loginandregister\currentprofile.csv', 'w', newline='') as db3:
                            data8 = csv.writer(db3)
                            data8.writerow(lst6)
                        T1 = Thread(target=Utils.play4)  # create thread
                        T1.start()
                        self.win_loss_window('YOU WON!')  # as the given word has been found, this is printed

                    break

                else:
                    # if its not the desired consonant else loop is executed and this is printed
                    label_valid_consonant = Label(root, text="Enter a valid consonant", font=('Calibri body', 20),
                                                  background='black',
                                                  foreground='orange')  # as input is wrong... this is printed
                    label_valid_consonant.place(x=120, y=330)
                    break

        if count == 0:  # if lives left are 0
            replay += 1  # replay is appended for the next word
            T = Thread(target=Utils.play1)  # create thread
            T.start()
            T6 = Thread(target=Utils.play6)  # create thread
            T6.start()
            score1 = 0  # score is displayed

            with open('loginandregister\databasecsv.csv', 'r', newline='') as db:
                data6 = csv.reader(db)
                data6 = list(data6)
                for i in range(len(data6)):
                    if data6[i][1] == self.currentusername and data6[i][2] == self.currentpassword:
                        data6[i].append(str(score1))
                        lst7 = data6[i]

            with open('loginandregister\databasecsv.csv', 'w', newline='') as db1:
                data7 = csv.writer(db1)
                data7.writerows(data6)

            with open('loginandregister\currentprofile.csv', 'w', newline='') as db3:
                data9 = csv.writer(db3)
                data9.writerow(lst7)

            self.win_loss_window('YOU LOST')  # as the player was not able to guess the word this is printed

    def button_utils(self):
        Utils.buttonPushed()
        self.game_execution()

    def hangman(self):
        global count, s1, s, lst1, lstdone, countc, score, vowels, entered, show, guess, play, root, label_word, fullcanvas1

        root = Tk()
        root.title("HANGMAN")
        root.iconbitmap('hangman.ico')
        root.resizable(0, 0)
        root.geometry('1250x680+5+5')

        root.protocol("WM_DELETE_WINDOW", lambda root1=root: Utils.on_closing(root))

        fullcanvas1 = Canvas(root, height='680', width='1250', bd=0, highlightthickness=0, relief='raised', bg='black')
        fullcanvas1.pack()
        try:
            copy_of_image1 = Image.open(r"\hangman\Background\{}.jpg".format(self.background))
            img1 = ImageTk.PhotoImage(copy_of_image1)
            fullcanvas1.create_image(650, 340, image=img1)

        except:
            pass
        Titleandman.LoadTitle(fullcanvas1)

        l_pillar = fullcanvas1.create_rectangle(850, 30, 865, 620, width='2', fill='white')
        r_pillar = fullcanvas1.create_rectangle(1200, 30, 1215, 620, width='2', fill='white')
        l_base = fullcanvas1.create_rectangle(825, 620, 890, 635, width='2', fill='white')
        r_base = fullcanvas1.create_rectangle(1175, 620, 1240, 635, width='2', fill='white')
        u_pillar = fullcanvas1.create_rectangle(830, 30, 1230, 45, width='2', fill='white')
        middle = fullcanvas1.create_rectangle(1023, 45, 1028, 95, width='2', fill='white')

        # T4 = Thread(target=stopwatch())  # create thread
        # T4.start()

        for n in range(len(s)):
            if s[n] not in 'AEIOUaeiou':
                countc += 1
        for k in range(len(s)):
            if s[k] in 'aeiouAEIOU':
                s1 = s1 + s[k] + ' '
            else:
                s1 = s1 + '_ '
        for l in range(0, len(s1), 2):
            lst1.append(s1[l])  # aeroplane-->['a','e','_'

        label_counter = Label(root, text='Counter This Word:', font=("Comic Sans MS", 30), background='black',
                              foreground='pink')
        label_counter.place(x=25, y=125)

        label_word = Label(root, text=s1, font=("Comic Sans MS", 35), background='black', foreground='cyan')
        label_word.place(x=150, y=210)

        label_enter = Label(root, text='Enter Letter:', font=("Comic Sans MS", 30), background='black',
                            foreground='pink')
        label_enter.place(x=25, y=370)

        label_lives = Label(root, text="LIVES REMAINING :", font=("Comic Sans MS", 25), background="black",
                            foreground='yellow')  # prints the no. of lives remaining
        label_lives.place(x=100, y=570)

        label_lives = Label(root, text="6", font=("Comic Sans MS", 25), background="black",
                            foreground='yellow')  # prints the no. of lives remaining
        label_lives.place(x=440, y=570)

        label_entered = Label(root, text="Letters Entered:", font=("Comic Sans MS", 22), background="black",
                              foreground='white')
        label_entered.place(x=25, y=500)

        Utils.createTextBox(root)

        button1 = Button(root, text='Enter', width=15, bg='black', fg='orange', font=('Calibri', 15),
                         command=self.button_utils)
        button1.place(x=300, y=435)

        button_profile = Button(root, text='PROFILE', width=15, bg='black', fg='orange', font=('Calibri', 15),
                                command=self.root_profile)
        button_profile.place(x=600, y=540)

        button_return = Button(root, text='RETURN', width=15, bg='black', fg='orange', font=('Calibri', 15),
                               command=self.restart)
        button_return.place(x=600, y=590)

        T1 = Thread(target=Utils.play2)
        T1.start()

        root.mainloop()

    def button_countries(self):
        global s, lstdone
        root1.destroy()
        index = random.randint(0, 167)  # finds a random index from the asked list
        while index in lstdone:
            # if u (index of word) is in the list which consists of used words, is runs again until a fresh unused
            # word is found and displayed
            index = random.randint(0, 167)
        s = lstcountry[index]
        s = s.lower()  # finds a random index from the asked list
        lstdone.append(index)
        self.hangman()

    def button_carbrand(self):
        global s, lstdone
        root1.destroy()
        index = random.randint(0, 21)  # finds a random index from the asked list
        while index in lstdone:  # if u (index of word) is in the list which consists of used words, is runs again until a fresh unused word is found and displayed
            index = random.randint(0, 21)
        s = lstcar[index]
        s = s.lower()  # finds a random index from the asked list
        lstdone.append(index)
        self.hangman()

    def button_instruments(self):
        global s, lstdone
        root1.destroy()
        index = random.randint(0, 23)  # finds a random index from the asked list
        while index in lstdone:  # if u (index of word) is in the list which consists of used words, is runs again until a fresh unused word is found and displayed
            index = random.randint(0, 23)
        s = lstmusic[index]
        s = s.lower()  # finds a random index from the asked list
        lstdone.append(index)
        self.hangman()

    def button_colours(self):
        global s, lstdone
        root1.destroy()
        index = random.randint(0, 27)  # finds a random index from the asked list
        while index in lstdone:  # if u (index of word) is in the list which consists of used words, is runs again until a fresh unused word is found and displayed
            index = random.randint(0, 27)
        s = lstcolor[index]
        s = s.lower()  # finds a random index from the asked list
        lstdone.append(index)
        self.hangman()

    def button_indian(self):
        global s, lstdone
        root1.destroy()
        index = random.randint(0, 28)  # finds a random index from the asked list
        while index in lstdone:
            # if u (index of word) is in the list which consists of used words, is runs again until
            # a fresh unused word is found and displayed
            index = random.randint(0, 28)
        s = lststate[index]
        s = s.lower()  # finds a random index from the asked list
        lstdone.append(index)
        self.hangman()

    def choose(self):
        global root1
        root1 = Tk()
        root1.title("welcome game")
        root1.iconbitmap('hangman.ico')
        root1.geometry('800x650')
        root1.resizable(0, 0)
        root1.protocol("WM_DELETE_WINDOW", lambda root1=root1: Utils.on_closing(root1))

        frame = Frame(root1, relief='raised', borderwidth=2)
        frame.pack(fill=BOTH, expand=YES)

        copy_of_image = Image.open(r"hangman\Background\im.jpg")
        photo = ImageTk.PhotoImage(copy_of_image)

        button = Button(frame, image=photo)
        button.place(x=0, y=0, relwidth=1, relheight=1)

        # label=Label(frame,image=photo)
        # label.place(x=0, y=0, relwidth=1, relheight=1)

        button1 = Button(root1, text='COUNTRIES', width=15, height=1, font=('arial black', 15, 'bold'), bg='red',
                         fg='black', command=self.button_countries)
        button2 = Button(root1, text='CAR BRANDS', width=15, height=1, font=('arial black', 15, 'bold'), bg='red',
                         fg='black', command=self.button_carbrand)
        button3 = Button(root1, text='INSTRUMENTS', width=15, height=1, font=('arial black', 15, 'bold'), bg='red',
                         fg='black', command=self.button_instruments)
        button4 = Button(root1, text='COLOURS', width=15, height=1, font=('arial black', 15, 'bold'), bg='red',
                         fg='black', command=self.button_colours)
        button5 = Button(root1, text='INDIAN STATES', width=15, height=1, font=('arial black', 15, 'bold'), bg='red',
                         fg='black', command=self.button_indian)

        button1.place(x=100, y=380)
        button2.place(x=455, y=380)
        button3.place(x=275, y=440)
        button4.place(x=100, y=505)
        button5.place(x=455, y=505)

        shop_person = Shop(self.currentusername, self.money)

        button_shop = Button(root1, text='SHOP', width=15, height=1, font=('arial black', 15, 'bold'),
                             bg='DodgerBlue2', fg='white', command=shop_person.shop)
        button_shop.place(x=275, y=575)

        str2 = Label(root1, text='HANGMAN', font=('algerian', 50), background='darkviolet', foreground='cyan')
        str2.place(x=225, y=10)
        str1 = Label(root1, text=('''        1.YOU WILL GET 6 LIVES TO SAVE YOU WHEN YOU INPUT A WRONG ANSWER.
                2.YOU WILL GET 3 WORDS FROM YOUR DESIRED CATEGORY.
                3.CONSONANTS WILL BE REPRESENTED BY '_' AND VOWELS WILL BE VISIBLE ON THERE
                  RESPECTIVE PLACES OF OCCURANCE.
                4.YOU HAVE TO ENTER THE LETTER WHICH YOU GUESS MAY BE PRESENT IN THE WORD.
                5.AS THE MAN COMPLETES ITS SHAPE, YOU LOSE
                6.MOST IMPORTANT RULE-BEST OF LUCK
                '''), font=('Calibri', 13, 'bold'), background='darkviolet', foreground='yellow')

        str1.place(x=80, y=100)

        name_label1 = Label(root1, text='DEVELOPED BY- VAIBHAV BANSAL ', font=('cooper black', 9), background='white')
        name_label2 = Label(root1, text='AARYAN SURYAN', font=('cooper black', 9), background='white')
        name_label1.place(x=550, y=600)
        name_label2.place(x=650, y=620)

        label_1 = Label(root1, text="WELCOME BUDDY! GET READY TO PLAY HANGMAN", font=('algerian', 15, 'bold', 'italic'),
                        background='darkviolet', foreground='white')
        label_2 = Label(root1, text="CHOOSE THE STREAM YOU WANT TO GUESS IN-",
                        font=('cooper black', 12, 'bold', 'italic'), background='darkviolet')

        label_1.place(x=150, y=300)
        label_2.place(x=165, y=350)

        root1.mainloop()
