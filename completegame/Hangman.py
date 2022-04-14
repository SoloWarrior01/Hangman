import csv
from threading import Thread

from completegame.hangman.hangman import Hangman
from completegame.loginandregister.loginandregister import Loginsignin
from completegame.utils.utils import Utils

root0 = None


class Main:
    def __init__(self, parent):
        self.parent = parent
        self.run()

    def run(self):
        Loginsignin(self.parent)
        with open('loginandregister\\currentprofile.csv', newline='') as csvfile1:
            data1 = csv.reader(csvfile1)
            listdata = list(data1)
        Hangman(listdata)


if __name__ == '__main__':
    t1 = Thread(target=Utils.play)
    t1.start()
    Main(root0)
