import pyttsx3
from tkinter import *
import playsound
import sys
from tkinter import messagebox
engine = pyttsx3.init()
engine.setProperty('rate',125)

class Utils:

    @staticmethod
    def play():
        while True:
            playsound.playsound('hangman\\audios\\Game-Menu.mp3')

    @staticmethod
    def play1():
        playsound.playsound('hangman\\audios\\completeloss.mp3')

    @staticmethod
    def play2():
        engine.say("let's begin. Good luck")
        engine.runAndWait()

    @staticmethod
    def play3():
        playsound.playsound('hangman\\audios\\SUCCESS.mp3')

    @staticmethod
    def play7():
        playsound.playsound('hangman\\audios\\wrongletter.mp3')

    @staticmethod
    def play4():
        playsound.playsound('hangman\\audios\\completesuccess.mpeg')

    @staticmethod
    def play5():
        engine.say(' Congratulations .. you guessed it right ')
        engine.runAndWait()

    @staticmethod
    def play6():
        engine.say(' you guessed it wrong.. better luck next time ')
        engine.runAndWait()

    @staticmethod
    def cleartext():
        global entryBox
        entryBox.delete(0, END)

    @staticmethod
    def buttonPushed():
        global entryBox, myValue
        guess = entryBox.get()
        myfile = open('guessed.txt', 'w')
        myfile.write(guess)
        myfile.close()
        Utils.cleartext()

    @staticmethod
    def createTextBox(parent):
        global entryBox
        entryBox = Entry(parent, width='30', background='white', foreground='black')
        entryBox.place(x=100, y=445)

    @staticmethod
    def ok(parent):
        parent.withdraw()

    @staticmethod
    def on_closing(parent):
        root = Tk()
        root.withdraw()
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            parent.destroy()
            sys.exit()
