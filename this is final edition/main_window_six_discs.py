import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from sixdisc_window import Ui_Form_6
import ui_resource_discs

import os
import datetime


class WindowSixDisc(QtWidgets.QWidget, Ui_Form_6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


'''
要使main.py正常运行，等下要把
app = QApplication(sys.argv)
app.exec_()
if __name__ == '__main__':
    main()
注释掉
'''
count = 0
dice_num_list = []
p1_score = 0
p2_score = 0


def main():
    app = QApplication(sys.argv)
    main_window = WindowSixDisc()
    main_window.show()
    game_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')

    def write_log(update):
        game_log = open("./six_disc_log/%s.txt" % game_time, "a")
        game_log.write(update)
        game_log.close()

    def all_disc_button_control(bool_val):
        main_window.pushButton_p11_1.setEnabled(bool_val)
        main_window.pushButton_p11_2.setEnabled(bool_val)
        main_window.pushButton_p11_3.setEnabled(bool_val)
        main_window.pushButton_p11_4.setEnabled(bool_val)
        main_window.pushButton_p11_5.setEnabled(bool_val)
        main_window.pushButton_p11_6.setEnabled(bool_val)
        main_window.pushButton_p12_1.setEnabled(bool_val)
        main_window.pushButton_p12_2.setEnabled(bool_val)
        main_window.pushButton_p12_3.setEnabled(bool_val)
        main_window.pushButton_p12_4.setEnabled(bool_val)
        main_window.pushButton_p12_5.setEnabled(bool_val)
        main_window.pushButton_p12_6.setEnabled(bool_val)
        main_window.pushButton_p21_1.setEnabled(bool_val)
        main_window.pushButton_p21_2.setEnabled(bool_val)
        main_window.pushButton_p21_3.setEnabled(bool_val)
        main_window.pushButton_p21_4.setEnabled(bool_val)
        main_window.pushButton_p21_5.setEnabled(bool_val)
        main_window.pushButton_p21_6.setEnabled(bool_val)
        main_window.pushButton_p22_1.setEnabled(bool_val)
        main_window.pushButton_p22_2.setEnabled(bool_val)
        main_window.pushButton_p22_3.setEnabled(bool_val)
        main_window.pushButton_p22_4.setEnabled(bool_val)
        main_window.pushButton_p22_5.setEnabled(bool_val)
        main_window.pushButton_p22_6.setEnabled(bool_val)

    def turn_arrow():
        global count
        if count % 2 == 0:  # Player 1's turn
            main_window.label_turn_p1.setVisible(True)
            main_window.label_turn_p2.setVisible(False)
        else:  # Player 2's turn
            main_window.label_turn_p1.setVisible(False)
            main_window.label_turn_p2.setVisible(True)

    def num_list_check(num_list):
        all_disc_button_control(False)
        if not num_list:
            global count
            count += 1
            main_window.pushButton_rollDice.setEnabled(True)
            turn_arrow()
        if '1' in num_list:
            main_window.pushButton_p11_1.setEnabled(True)
            main_window.pushButton_p12_1.setEnabled(True)
            main_window.pushButton_p21_1.setEnabled(True)
            main_window.pushButton_p22_1.setEnabled(True)
        if '2' in num_list:
            main_window.pushButton_p11_2.setEnabled(True)
            main_window.pushButton_p12_2.setEnabled(True)
            main_window.pushButton_p21_2.setEnabled(True)
            main_window.pushButton_p22_2.setEnabled(True)
        if '3' in num_list:
            main_window.pushButton_p11_3.setEnabled(True)
            main_window.pushButton_p12_3.setEnabled(True)
            main_window.pushButton_p21_3.setEnabled(True)
            main_window.pushButton_p22_3.setEnabled(True)
        if '4' in num_list:
            main_window.pushButton_p11_4.setEnabled(True)
            main_window.pushButton_p12_4.setEnabled(True)
            main_window.pushButton_p21_4.setEnabled(True)
            main_window.pushButton_p22_4.setEnabled(True)
        if '5' in num_list:
            main_window.pushButton_p11_5.setEnabled(True)
            main_window.pushButton_p12_5.setEnabled(True)
            main_window.pushButton_p21_5.setEnabled(True)
            main_window.pushButton_p22_5.setEnabled(True)
        if '6' in num_list:
            main_window.pushButton_p11_6.setEnabled(True)
            main_window.pushButton_p12_6.setEnabled(True)
            main_window.pushButton_p21_6.setEnabled(True)
            main_window.pushButton_p22_6.setEnabled(True)

    def roll_dice():
        dice_value_list = []
        for i in range(3):
            dice_value = str(ord(os.urandom(1)) % 6 + 1)
            # 更随机  https://blog.csdn.net/a19990412/article/details/80934268
            # 随机数，除以6取余，再加1（结果由0-5变成1-6）
            dice_value_list.append(dice_value)
        img_path1 = '../resources/images/dice/%s.png' % dice_value_list[0]
        dice_img1 = QtGui.QPixmap(img_path1).scaled(main_window.label_dice_1.width(), main_window.label_dice_1.height())
        main_window.label_dice_1.setPixmap(dice_img1)
        img_path2 = '../resources/images/dice/%s.png' % dice_value_list[1]
        dice_img2 = QtGui.QPixmap(img_path2).scaled(main_window.label_dice_2.width(), main_window.label_dice_2.height())
        main_window.label_dice_2.setPixmap(dice_img2)
        img_path3 = '../resources/images/dice/%s.png' % dice_value_list[2]
        dice_img3 = QtGui.QPixmap(img_path3).scaled(main_window.label_dice_3.width(), main_window.label_dice_3.height())
        main_window.label_dice_3.setPixmap(dice_img3)
        return dice_value_list

    def dice():
        # 倒计时：https://zhuanlan.zhihu.com/p/32239438?msclkid=67ff8b7ec11c11eca5998beaf66bb888
        main_window.count = 10
        main_window.time = QtCore.QTimer(main_window)
        main_window.time.setInterval(1000)
        main_window.time.timeout.connect(lambda: time_refresh(main_window))
        main_window.time.start()
        main_window.pushButton_rollDice.setEnabled(False)

        def time_refresh(self):
            if self.count > 0:
                self.timer_num.setText(str(self.count))
                self.count -= 1
                if self.pushButton_rollDice.isEnabled():
                    self.time.stop()
            else:
                self.pushButton_pass_1.setEnabled(False)
                self.pushButton_pass_2.setEnabled(False)
                self.timer_num.setText(str(self.count))
                self.time.stop()
                self.pushButton_rollDice.setEnabled(True)
                all_disc_button_control(False)
                global count
                if count % 2 == 0:
                    write_log("TIME'S UP. Player 1's turn finished.\n")
                else:
                    write_log("TIME'S UP. Player 2's turn finished.\n")
                count += 1
                turn_arrow()
                self.count = 10

        global count, dice_num_list
        dice_num_list = roll_dice()

        if count % 2 == 0:  # player1
            main_window.pushButton_pass_1.setEnabled(True)
            main_window.pushButton_pass_2.setEnabled(False)
        else:  # player2
            main_window.pushButton_pass_1.setEnabled(False)
            main_window.pushButton_pass_2.setEnabled(True)

        num_list_check(dice_num_list)
        write_log('Round %s:  Dice-%s  (P1:%s  P2:%s)\n' % (str(count + 1), str(dice_num_list), p1_score, p2_score))

    def play():

        def flip(button):  # button == main_window.xbutton
            disc_img = str(button.styleSheet())
            if disc_img.endswith("f.png);"):
                disc_img_new = disc_img.replace("f.png);", "b.png);")
                button.setStyleSheet(disc_img_new)
            else:
                disc_img_new = disc_img.replace("b.png);", "f.png);")
                button.setStyleSheet(disc_img_new)

        def get_button(button_name):
            if button_name == 'pushButton_p11_1':
                button = main_window.pushButton_p11_1
            elif button_name == 'pushButton_p11_2':
                button = main_window.pushButton_p11_2
            elif button_name == 'pushButton_p11_3':
                button = main_window.pushButton_p11_3
            elif button_name == 'pushButton_p11_4':
                button = main_window.pushButton_p11_4
            elif button_name == 'pushButton_p11_5':
                button = main_window.pushButton_p11_5
            elif button_name == 'pushButton_p11_6':
                button = main_window.pushButton_p11_6
            elif button_name == 'pushButton_p12_1':
                button = main_window.pushButton_p12_1
            elif button_name == 'pushButton_p12_2':
                button = main_window.pushButton_p12_2
            elif button_name == 'pushButton_p12_3':
                button = main_window.pushButton_p12_3
            elif button_name == 'pushButton_p12_4':
                button = main_window.pushButton_p12_4
            elif button_name == 'pushButton_p12_5':
                button = main_window.pushButton_p12_5
            elif button_name == 'pushButton_p12_6':
                button = main_window.pushButton_p12_6
            elif button_name == 'pushButton_p21_1':
                button = main_window.pushButton_p21_1
            elif button_name == 'pushButton_p21_2':
                button = main_window.pushButton_p21_2
            elif button_name == 'pushButton_p21_3':
                button = main_window.pushButton_p21_3
            elif button_name == 'pushButton_p21_4':
                button = main_window.pushButton_p21_4
            elif button_name == 'pushButton_p21_5':
                button = main_window.pushButton_p21_5
            elif button_name == 'pushButton_p21_6':
                button = main_window.pushButton_p21_6
            elif button_name == 'pushButton_p22_1':
                button = main_window.pushButton_p22_1
            elif button_name == 'pushButton_p22_2':
                button = main_window.pushButton_p22_2
            elif button_name == 'pushButton_p22_3':
                button = main_window.pushButton_p22_3
            elif button_name == 'pushButton_p22_4':
                button = main_window.pushButton_p22_4
            elif button_name == 'pushButton_p22_5':
                button = main_window.pushButton_p22_5
            else:  # button_name == 'pushButton_p22_6'
                button = main_window.pushButton_p22_6
            return button

        button_clicked_name = str(main_window.sender().objectName())  # 'pushButton_p11_1'
        clicked_num = button_clicked_name[-1]
        clicked_row = button_clicked_name[-3]
        button_clicked = get_button(button_clicked_name)
        disc_style = str(button_clicked.styleSheet())

        global count, dice_num_list, p1_score, p2_score

        if count % 2 == 0:  # player1
            if 'p1' in button_clicked_name:  # 如果点的是p1自己的disc，那么就翻个面
                flip(button_clicked)
                if disc_style.endswith("f.png);"):
                    write_log("Player 1 PROTECTED own disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
                else:
                    write_log("Player 1 UNPROTECTED own disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
            else:  # 点了p2的， 需要判断一下是f还是b，分两种情况讨论
                if disc_style.endswith("f.png);"):  # p1得到这个disc
                    p1_score += int(clicked_num)
                    main_window.label_p1_score.setText(str(p1_score))
                    button_clicked.setVisible(False)
                    write_log("Player 1 CAPTURED Player 2's disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
                else:  # 背面朝上，翻个面
                    flip(button_clicked)
                    write_log("Player 1 UNPROTECTED Player 2's disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
        else:  # player2
            if 'p2' in button_clicked_name:  # 点的是p2自己的disc，翻个面
                flip(button_clicked)
                if disc_style.endswith("f.png);"):
                    write_log("Player 2 PROTECTED own disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
                else:
                    write_log("Player 2 UNPROTECTED own disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
            else:  # 点了p1的disc
                if disc_style.endswith("f.png);"):  # p2得到这个disc
                    p2_score += int(clicked_num)
                    main_window.label_p2_score.setText(str(p2_score))
                    button_clicked.setVisible(False)
                    write_log("Player 2 CAPTURED Player 1's disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))
                else:  # 背面朝上就翻个面
                    flip(button_clicked)
                    write_log("Player 2 UNPROTECTED Player 1's disc.(Row-%s Num-%s)\n" % (clicked_row, clicked_num))

        dice_num_list.remove(clicked_num)
        num_list_check(dice_num_list)

        def which_one_empty():
            if not main_window.pushButton_p11_1.isVisible():
                if not main_window.pushButton_p11_2.isVisible():
                    if not main_window.pushButton_p11_3.isVisible():
                        if not main_window.pushButton_p11_4.isVisible():
                            if not main_window.pushButton_p11_5.isVisible():
                                if not main_window.pushButton_p11_6.isVisible():
                                    calculate_final_score('1')

            if not main_window.pushButton_p21_1.isVisible():
                if not main_window.pushButton_p21_2.isVisible():
                    if not main_window.pushButton_p21_3.isVisible():
                        if not main_window.pushButton_p21_4.isVisible():
                            if not main_window.pushButton_p21_5.isVisible():
                                if not main_window.pushButton_p21_6.isVisible():
                                    calculate_final_score('2')

        which_one_empty()

    def next_player():
        all_disc_button_control(False)
        main_window.pushButton_pass_1.setEnabled(False)
        main_window.pushButton_pass_2.setEnabled(False)

        global count
        if count % 2 == 0:  # player1
            write_log("Player 1 chose PASS.\n")
        else:  # player2
            write_log("Player 2 chose PASS.\n")
        count += 1
        turn_arrow()
        main_window.pushButton_rollDice.setEnabled(True)

    def calculate_final_score(whose_1_empty):
        main_window.pushButton_rollDice.setEnabled(True)
        all_disc_button_control(False)
        main_window.pushButton_pass_1.setEnabled(False)
        main_window.pushButton_pass_2.setEnabled(False)

        global p1_score, p2_score
        # 可以先判断p1和p2的第二行，因为不影响，都是一样的
        if main_window.pushButton_p12_1.isVisible():
            if str(main_window.pushButton_p12_1.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                p2_score += 1
            else:
                p1_score += 1
        if main_window.pushButton_p12_2.isVisible():
            if str(main_window.pushButton_p12_2.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                p2_score += 2
            else:
                p1_score += 2
        if main_window.pushButton_p12_3.isVisible():
            if str(main_window.pushButton_p12_3.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                p2_score += 3
            else:
                p1_score += 3
        if main_window.pushButton_p12_4.isVisible():
            if str(main_window.pushButton_p12_4.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                p2_score += 4
            else:
                p1_score += 4
        if main_window.pushButton_p12_5.isVisible():
            if str(main_window.pushButton_p12_5.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                p2_score += 5
            else:
                p1_score += 5
        if main_window.pushButton_p12_6.isVisible():
            if str(main_window.pushButton_p12_6.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                p2_score += 6
            else:
                p1_score += 6

        if main_window.pushButton_p22_1.isVisible():
            if str(main_window.pushButton_p22_1.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                p1_score += 1
            else:
                p2_score += 1
        if main_window.pushButton_p22_2.isVisible():
            if str(main_window.pushButton_p22_2.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                p1_score += 2
            else:
                p2_score += 2
        if main_window.pushButton_p22_3.isVisible():
            if str(main_window.pushButton_p22_3.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                p1_score += 3
            else:
                p2_score += 3
        if main_window.pushButton_p22_4.isVisible():
            if str(main_window.pushButton_p22_4.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                p1_score += 4
            else:
                p2_score += 4
        if main_window.pushButton_p22_5.isVisible():
            if str(main_window.pushButton_p22_5.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                p1_score += 5
            else:
                p2_score += 5
        if main_window.pushButton_p22_6.isVisible():
            if str(main_window.pushButton_p22_6.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                p1_score += 6
            else:
                p2_score += 6

        if whose_1_empty == '1':  # p1的第一行空了，那么只需要判断p2的第一行
            write_log("Player 1's primary row is empty.\nGAME ENDED.\n")
            if main_window.pushButton_p21_1.isVisible():
                if str(main_window.pushButton_p21_1.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                    p1_score += 1
                else:
                    p2_score += 1
            if main_window.pushButton_p21_2.isVisible():
                if str(main_window.pushButton_p21_2.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                    p1_score += 2
                else:
                    p2_score += 2
            if main_window.pushButton_p21_3.isVisible():
                if str(main_window.pushButton_p21_3.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                    p1_score += 3
                else:
                    p2_score += 3
            if main_window.pushButton_p21_4.isVisible():
                if str(main_window.pushButton_p21_4.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                    p1_score += 4
                else:
                    p2_score += 4
            if main_window.pushButton_p21_5.isVisible():
                if str(main_window.pushButton_p21_5.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                    p1_score += 5
                else:
                    p2_score += 5
            if main_window.pushButton_p21_6.isVisible():
                if str(main_window.pushButton_p21_6.styleSheet()).endswith("f.png);"):  # 分算到p1那里
                    p1_score += 6
                else:
                    p2_score += 6
        if whose_1_empty == '2':  # p2的第一行空了，那么只需要判断p1的第一行
            write_log("Player 2's primary row is empty.\nGAME ENDED.\n")
            if main_window.pushButton_p11_1.isVisible():
                if str(main_window.pushButton_p11_1.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                    p2_score += 1
                else:
                    p1_score += 1
            if main_window.pushButton_p11_2.isVisible():
                if str(main_window.pushButton_p11_2.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                    p2_score += 2
                else:
                    p1_score += 2
            if main_window.pushButton_p11_3.isVisible():
                if str(main_window.pushButton_p11_3.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                    p2_score += 3
                else:
                    p1_score += 3
            if main_window.pushButton_p11_4.isVisible():
                if str(main_window.pushButton_p11_4.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                    p2_score += 4
                else:
                    p1_score += 4
            if main_window.pushButton_p11_5.isVisible():
                if str(main_window.pushButton_p11_5.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                    p2_score += 5
                else:
                    p1_score += 5
            if main_window.pushButton_p11_6.isVisible():
                if str(main_window.pushButton_p11_6.styleSheet()).endswith("f.png);"):  # 分算到p2那里
                    p2_score += 6
                else:
                    p1_score += 6
        main_window.label_p1_score.setText(str(p1_score))
        main_window.label_p2_score.setText(str(p2_score))
        if p1_score > p2_score:
            result = 'PLAYER 1'
        elif p1_score == p2_score:
            result = 'P1 & P2'
        else:
            result = 'PLAYER 2'
        main_window.label_congrats.setVisible(True)
        main_window.label_winner.setVisible(True)
        main_window.label_winner.setText(result)
        write_log("Player1: %s,  Player2: %s" % (str(p1_score), str(p2_score)))
        write_log("WINNER: %s" % result)

    main_window.pushButton_pass_1.setEnabled(False)
    main_window.pushButton_pass_2.setEnabled(False)
    all_disc_button_control(False)
    turn_arrow()

    main_window.pushButton_rollDice.clicked.connect(dice)

    main_window.pushButton_pass_1.clicked.connect(next_player)
    main_window.pushButton_pass_2.clicked.connect(next_player)

    main_window.pushButton_p11_1.clicked.connect(play)
    main_window.pushButton_p11_2.clicked.connect(play)
    main_window.pushButton_p11_3.clicked.connect(play)
    main_window.pushButton_p11_4.clicked.connect(play)
    main_window.pushButton_p11_5.clicked.connect(play)
    main_window.pushButton_p11_6.clicked.connect(play)
    main_window.pushButton_p12_1.clicked.connect(play)
    main_window.pushButton_p12_2.clicked.connect(play)
    main_window.pushButton_p12_3.clicked.connect(play)
    main_window.pushButton_p12_4.clicked.connect(play)
    main_window.pushButton_p12_5.clicked.connect(play)
    main_window.pushButton_p12_6.clicked.connect(play)
    main_window.pushButton_p21_1.clicked.connect(play)
    main_window.pushButton_p21_2.clicked.connect(play)
    main_window.pushButton_p21_3.clicked.connect(play)
    main_window.pushButton_p21_4.clicked.connect(play)
    main_window.pushButton_p21_5.clicked.connect(play)
    main_window.pushButton_p21_6.clicked.connect(play)
    main_window.pushButton_p22_1.clicked.connect(play)
    main_window.pushButton_p22_2.clicked.connect(play)
    main_window.pushButton_p22_3.clicked.connect(play)
    main_window.pushButton_p22_4.clicked.connect(play)
    main_window.pushButton_p22_5.clicked.connect(play)
    main_window.pushButton_p22_6.clicked.connect(play)

    app.exec_()


if __name__ == '__main__':
    main()
