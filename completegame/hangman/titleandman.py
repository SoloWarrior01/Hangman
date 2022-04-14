from tkinter import *


class Titleandman:
    def __init__(self, parent):
        self.parent = parent

    @staticmethod
    def hanging_man(canvas, count):
        if count == 5:
            head = canvas.create_oval(985, 95, 1065, 175, fill='sky blue')
        elif count == 4:
            body = canvas.create_rectangle(1021, 173, 1030, 290, fill='sky blue', outline='sky blue')
        elif count == 3:
            arm_left = canvas.create_line(1023, 190, 981, 220, width='10', fill='sky blue')
        elif count == 2:
            arm_right = canvas.create_line(1028, 190, 1070, 220, width='10', fill='sky blue')
        elif count == 1:
            leg_left = canvas.create_line(1023, 288, 981, 318, width='10', fill='sky blue')
        elif count == 0:
            leg_right = canvas.create_line(1028, 288, 1070, 318, width='10', fill='sky blue')

    @staticmethod
    def LoadTitle(canvas):
        H_left = canvas.create_rectangle(255, 20, 265, 100, width='2', outline='red')
        H_right = canvas.create_rectangle(285, 20, 295, 100, width='2', outline='red')
        H_middle = canvas.create_rectangle(265, 55, 285, 65, width='2', outline='red')
        A_left1 = canvas.create_line(305, 100, 325, 20, width='2', fill='violet')
        A_left_bottom = canvas.create_line(305, 100, 315, 100, width='2', fill='violet')
        A_left2 = canvas.create_line(315, 100, 325, 50, width='2', fill='violet')
        A_right1 = canvas.create_line(325, 20, 345, 100, width='2', fill='violet')
        A_right_bottom = canvas.create_line(335, 100, 345, 100, width='2', fill='violet')
        A_right2 = canvas.create_line(325, 50, 335, 100, width='2', fill='violet')
        N_left = canvas.create_rectangle(355, 20, 365, 100, width='2', outline='blue')
        N_right = canvas.create_rectangle(385, 20, 395, 100, width='2', outline='blue')
        N_diagonal_upper = canvas.create_line(365, 20, 385, 80, width='2', fill='blue')
        N_diagonal_lower = canvas.create_line(365, 40, 385, 100, width='2', fill='blue')
        G_up = canvas.create_line(405, 20, 445, 20, width='2', fill='green')
        G_uple = canvas.create_line(445, 20, 445, 30, width='2', fill='green')
        G_upper = canvas.create_line(445, 30, 415, 30, width='2', fill='green')
        G_left = canvas.create_line(405, 20, 405, 100, width='2', fill='green')
        G_le = canvas.create_line(415, 30, 415, 90, width='2', fill='green')
        G_bottom = canvas.create_line(405, 100, 445, 100, width='2', fill='green')
        G_bo = canvas.create_line(415, 90, 435, 90, width='2', fill='green')
        G_right = canvas.create_line(445, 100, 445, 55, width='2', fill='green')
        G_right = canvas.create_line(435, 90, 435, 65, width='2', fill='green')
        G_middle = canvas.create_line(425, 65, 435, 65, width='2', fill='green')
        G_mid = canvas.create_line(425, 55, 445, 55, width='2', fill='green')
        G_mid_left = canvas.create_line(425, 55, 425, 65, width='2', fill='green')
        M_left = canvas.create_rectangle(455, 20, 465, 100, width='2', outline='yellow')
        M_right = canvas.create_rectangle(505, 20, 515, 100, width='2', outline='yellow')
        M_left1 = canvas.create_line(465, 20, 485, 50, width='2', fill='yellow')
        M_left2 = canvas.create_line(465, 35, 485, 65, width='2', fill='yellow')
        M_right1 = canvas.create_line(485, 50, 505, 20, width='2', fill='yellow')
        M_right2 = canvas.create_line(485, 65, 505, 35, width='2', fill='yellow')
        A2_left1 = canvas.create_line(525, 100, 545, 20, width='2', fill='orange')
        A2_left_bottom = canvas.create_line(525, 100, 535, 100, width='2', fill='orange')
        A2_left2 = canvas.create_line(535, 100, 545, 50, width='2', fill='orange')
        A2_right1 = canvas.create_line(545, 20, 565, 100, width='2', fill='orange')
        A2_right_bottom = canvas.create_line(555, 100, 565, 100, width='2', fill='orange')
        A2_right2 = canvas.create_line(545, 50, 555, 100, width='2', fill='orange')
        N2_left = canvas.create_rectangle(575, 20, 585, 100, width='2', outline='lime')
        N2_right = canvas.create_rectangle(605, 20, 615, 100, width='2', outline='lime')
        N2_diagonal_upper = canvas.create_line(585, 20, 605, 80, width='2', fill='lime')
        N2_diagonal_lower = canvas.create_line(585, 40, 605, 100, width='2', fill='lime')
