import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from ui_choose_num import Ui_choose_num_window
from ui_onedisc_window_changed import Ui_Form_1
import ui_resource_discs   # image resource (although it's grey, it has been used in this file)

import os
import datetime


class WindowOneDisc(QtWidgets.QWidget, Ui_Form_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_roll.setEnabled(False)   # at first only choose buttons are clickable
        self.pushButton_disc_p1.setEnabled(False)
        self.pushButton_disc_p2.setEnabled(False)
        self.pushButton_pass_1.setEnabled(False)
        self.pushButton_pass_2.setEnabled(False)


class ChooseNumWindow(Ui_choose_num_window):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


'''
To make main.py run without error,
needs to put '#' before:
app = QApplication(sys.argv)
app.exec_()
if __name__ == '__main__':
    main()
'''
count = 0
dice_num = ''
p1_num = ''
p2_num = ''


def main():
    # app = QApplication(sys.argv)
    main_window = WindowOneDisc()
    main_window.show()
    game_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')

    def write_log(update):
        game_log = open("./one_disc_log/%s.txt" % game_time, "a")
        game_log.write(update)
        game_log.close()

    def turn_arrow():
        global count
        if count % 2 == 0:  # Player 1's turn
            main_window.label_turn_p1.setVisible(True)
            main_window.label_turn_p2.setVisible(False)
        else:  # Player 2's turn
            main_window.label_turn_p1.setVisible(False)
            main_window.label_turn_p2.setVisible(True)

    def num_chosen(player):
        global p1_num, p2_num
        if player == '1':
            choose_window = choose_window1
            choose_button = main_window.pushButton_choose_p1
            disc_button = main_window.pushButton_disc_p1
        else:
            choose_window = choose_window2
            choose_button = main_window.pushButton_choose_p2
            disc_button = main_window.pushButton_disc_p2
        sending_button = choose_window.sender()
        num = str(sending_button.objectName())[-1]
        if num != '':
            choose_window.close()
            choose_button.setEnabled(False)
            disc_button.setStyleSheet("border-image: url(:/player %s/%s_%s_f.png);" % (player, player, num))

        def dice():
            # countdown
            main_window.count = 10
            main_window.time = QtCore.QTimer(main_window)
            main_window.time.setInterval(1000)
            main_window.time.timeout.connect(lambda: time_refresh(main_window))
            main_window.time.start()
            main_window.pushButton_roll.setEnabled(False)

            def time_refresh(self):
                if self.count > 0:
                    self.timer_num.setText(str(self.count))
                    self.count -= 1
                    if self.pushButton_roll.isEnabled():
                        self.time.stop()
                else:
                    self.pushButton_pass_1.setEnabled(False)
                    self.pushButton_pass_2.setEnabled(False)
                    self.timer_num.setText(str(self.count))
                    self.time.stop()
                    self.pushButton_roll.setEnabled(True)
                    self.pushButton_disc_p1.setEnabled(False)
                    self.pushButton_disc_p2.setEnabled(False)
                    global count
                    if count % 2 == 0:
                        write_log("TIME'S UP. Player 1's turn finished.\n")
                    else:
                        write_log("TIME'S UP. Player 2's turn finished.\n")
                    count += 1
                    turn_arrow()
                    self.count = 10

            global count, dice_num, p1_num, p2_num
            dice_num = roll_dice()

            main_window.pushButton_disc_p1.setEnabled(True)
            main_window.pushButton_disc_p2.setEnabled(True)
            if count % 2 == 0:  # player1
                main_window.pushButton_pass_1.setEnabled(True)
            else:
                main_window.pushButton_pass_2.setEnabled(True)
            # str(main_window.pushButton_disc_p1.styleSheet()) == 'border-image: url(:/player 1/1_5_f.png);'
            # so '-9'
            p1_num = str(main_window.pushButton_disc_p1.styleSheet())[-9]
            p2_num = str(main_window.pushButton_disc_p2.styleSheet())[-9]
            if p1_num != dice_num:
                main_window.pushButton_disc_p1.setEnabled(False)
            if p2_num != dice_num:
                main_window.pushButton_disc_p2.setEnabled(False)
            write_log('Round %s:  Dice-%s  (P1:%s  P2:%s)\n' % (str(count+1), dice_num, p1_num, p2_num))

        def check_num():
            main_window.pushButton_disc_p1.setEnabled(False)
            main_window.pushButton_disc_p2.setEnabled(False)
            main_window.pushButton_pass_1.setEnabled(False)
            main_window.pushButton_pass_2.setEnabled(False)

            button_clicked = str(main_window.sender().objectName())

            global count, dice_num
            if count % 2 == 0:   # player1
                if button_clicked[-1] == '1':  # p1's disc flip
                    p1_disc_img = str(main_window.pushButton_disc_p1.styleSheet())   # 'f' or 'b'
                    if p1_disc_img.endswith("f.png);"):
                        main_window.pushButton_disc_p1.setStyleSheet("border-image: url(:/player 1/1_%s_b.png);" % dice_num)
                        write_log("Player 1 PROTECTED own disc.\n")
                    else:
                        main_window.pushButton_disc_p1.setStyleSheet("border-image: url(:/player 1/1_%s_f.png);" % dice_num)
                        write_log("Player 1 UNPROTECTED own disc.\n")
                else:   # p2 which side?
                    p2_disc_img = str(main_window.pushButton_disc_p2.styleSheet())
                    if p2_disc_img.endswith("f.png);"):   # p1 wins
                        main_window.label_congrats.setVisible(True)
                        main_window.label_winner.setVisible(True)
                        main_window.label_winner.setText('PLAYER 1')
                        write_log("Player 1 CAPTURED Player 2's disc.\nWINNER: Player 1\nGAME ENDED.")
                    else:  # flip p2's disc
                        main_window.pushButton_disc_p2.setStyleSheet("border-image: url(:/player 2/2_%s_f.png);" % dice_num)
                        write_log("Player 1 UNPROTECTED Player 2's disc.\n")
            else:   # player2
                if button_clicked[-1] == '2':
                    p2_disc_img = str(main_window.pushButton_disc_p2.styleSheet())   # 'f' or 'b'
                    if p2_disc_img.endswith("f.png);"):
                        main_window.pushButton_disc_p2.setStyleSheet("border-image: url(:/player 2/2_%s_b.png);" % dice_num)
                        write_log("Player 2 PROTECTED own disc.\n")
                    else:
                        main_window.pushButton_disc_p2.setStyleSheet("border-image: url(:/player 2/2_%s_f.png);" % dice_num)
                        write_log("Player 2 UNPROTECTED own disc.\n")
                else:   # p1 which side?
                    p1_disc_img = str(main_window.pushButton_disc_p1.styleSheet())
                    if p1_disc_img.endswith("f.png);"):   # p2 wins
                        main_window.label_congrats.setVisible(True)
                        main_window.label_winner.setVisible(True)
                        main_window.label_winner.setText('PLAYER 2')
                        write_log("Player 2 CAPTURED Player 1's disc.\nWINNER: Player 2\nGAME ENDED.")
                    else:  # flip p1's
                        main_window.pushButton_disc_p1.setStyleSheet("border-image: url(:/player 1/1_%s_f.png);" % dice_num)
                        write_log("Player 2 UNPROTECTED Player 1's disc.\n")
            count += 1
            turn_arrow()
            main_window.pushButton_roll.setEnabled(True)

        def next_player():
            main_window.pushButton_disc_p1.setEnabled(False)
            main_window.pushButton_disc_p2.setEnabled(False)
            main_window.pushButton_pass_1.setEnabled(False)
            main_window.pushButton_pass_2.setEnabled(False)

            global count
            if count % 2 == 0:   # player1
                write_log("Player 1 chose PASS.\n")
            else:
                write_log("Player 2 chose PASS.\n")
            count += 1
            turn_arrow()
            main_window.pushButton_roll.setEnabled(True)

        check_p1 = main_window.pushButton_choose_p1.isEnabled()
        check_p2 = main_window.pushButton_choose_p2.isEnabled()
        if (str(check_p1), str(check_p2)) == ('False', 'False'):   # when p1&p2 all have chosen
            turn_arrow()
            main_window.pushButton_roll.setEnabled(True)
            main_window.pushButton_roll.clicked.connect(dice)

            main_window.pushButton_disc_p1.clicked.connect(check_num)
            main_window.pushButton_disc_p2.clicked.connect(check_num)

            main_window.pushButton_pass_1.clicked.connect(next_player)
            main_window.pushButton_pass_2.clicked.connect(next_player)

    def disc_show(player):
        if player == '1':
            choose_window1.show()
            choose_window1.pushbutton1.clicked.connect(lambda: num_chosen(player))
            choose_window1.pushbutton2.clicked.connect(lambda: num_chosen(player))
            choose_window1.pushbutton3.clicked.connect(lambda: num_chosen(player))
            choose_window1.pushbutton4.clicked.connect(lambda: num_chosen(player))
            choose_window1.pushbutton5.clicked.connect(lambda: num_chosen(player))
            choose_window1.pushbutton6.clicked.connect(lambda: num_chosen(player))
        else:
            choose_window2.show()
            choose_window2.pushbutton1.clicked.connect(lambda: num_chosen(player))
            choose_window2.pushbutton2.clicked.connect(lambda: num_chosen(player))
            choose_window2.pushbutton3.clicked.connect(lambda: num_chosen(player))
            choose_window2.pushbutton4.clicked.connect(lambda: num_chosen(player))
            choose_window2.pushbutton5.clicked.connect(lambda: num_chosen(player))
            choose_window2.pushbutton6.clicked.connect(lambda: num_chosen(player))

    choose_window1 = ChooseNumWindow()
    choose_window2 = ChooseNumWindow()
    main_window.pushButton_choose_p1.clicked.connect(lambda: disc_show('1'))
    main_window.pushButton_choose_p2.clicked.connect(lambda: disc_show('2'))

    def roll_dice():
        dice_value = str(ord(os.urandom(1)) % 6 + 1)
        # much more random than 'random'
        # +1 is to change the result from 0-5 to 1-6
        img_path = '../dice_img/%s.png' % dice_value
        dice_img = QtGui.QPixmap(img_path).scaled(main_window.dice_num.width(), main_window.dice_num.height())
        main_window.dice_num.setPixmap(dice_img)
        return dice_value

#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()
