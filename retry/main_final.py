from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
import time

from start_window import Ui_Form
from login import Ui_Signin_Window
from sixdisc_window import Ui_Form_6
from onedisc_window_test import Ui_Form_1
from choose_num import Ui_choose_num_window
from choose_window import Ui_Form_option
import window_one_final
import window_six_try


# 窗口切换的方法：https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161

class Login(QtWidgets.QWidget, Ui_Signin_Window):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.signin_pushbutton.clicked.connect(self.check)
        self.cancel_pushbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)  # 退出整个程序
        self.signup_pushbutton.clicked.connect(self.signup)

    def signup(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        user_dataframe = pd.read_csv('user_info.csv')
        user_dataframe.loc[user_dataframe.index.max() + 1] = [username, password]
        user_dataframe.to_csv('user_info.csv', index=False)
        QtWidgets.QMessageBox.information(self, 'Welcome!', 'Created the account successfully. You can log in now.')

    def check(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        user_dataframe = pd.read_csv('user_info.csv')
        match = user_dataframe[(user_dataframe['name'] == username) & (user_dataframe['password'] == password)]
        if match.empty:   # 依旧返回bool
            QtWidgets.QMessageBox.warning(None, "Wrong!", "Sorry, your information isn't correct\nPlease try again")
        else:
            self.pushbutton_handler()

        # if username != 'w' or password != '1':
        #     QtWidgets.QMessageBox.warning(None, "Wrong!", "Sorry, your information isn't correct\nPlease try again")
        # else:
        #     self.pushbutton_handler()

    def pushbutton_handler(self):
        self.switch_window.emit()


class MainWindow(QtWidgets.QWidget, Ui_Form):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.start_pushButton.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


class ChoiceWindow(QtWidgets.QWidget, Ui_Form_option):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.pushButton_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)  # 退出整个程序
        self.pushButton1.clicked.connect(self.choose)
        self.pushButton6.clicked.connect(self.choose)

    #     self.pushButton1.clicked.connect(self.button_released)
    #
    # def button_released(self):
    #     sending_button = self.sender()
    #     print('%s Clicked!' % str(sending_button.objectName()))

    def choose(self):
        sending_button = str(self.sender().objectName())
        # https://stackoverflow.com/questions/13050810/pyqt-button-clicked-name?msclkid=b8e1d6d1c03b11ec92db09df42ec9df9
        if sending_button == 'pushButton1':
            self.close()
            window_one_final.main()
            # window_one_try.WindowOneDisc.pushButton_quit.clicked.connect(self.choose())
        elif sending_button == 'pushButton6':
            self.close()
            window_six_try.main()
            # self.switch_window.emit()
        # else:     # 这里是点击1 disc界面中的quit时能return to choice window
        #     self.one.close()
        #     time.sleep(0.01)   # 设置暂停让切换显得不那么突然，因为和其他的算法不同导致切换界面时的动画有差异
        #     self.show()

    # def choose_one(self):
    #     # window_one_try.main()
    #     # self.one = window_one_try.main()
    #     # self.one.show()
    #     # self.one.exec()
    #
    #     self.one = WindowOne()
    #     self.one.show()
    #     self.one.pushButton_quit.clicked.connect(self.choose)

        # self.window_one.switch_window.connect(self.show_window_choice)
        # self.form = QtWidgets.QWidget()
        # self.ui = Ui_Form_1()
        # self.ui.setupUi(self.form)
        # self.pushButton.clicked.connect(lambda: self.__init__())
        # self.form.show()


# class WindowOne(window_one_try):
#
#     # switch_window = QtCore.pyqtSignal()
#
#     def __init__(self):
#         super(WindowOne, self).__init__(self)
#         self.setupUi(self)

# class WindowOne(QtWidgets.QWidget, Ui_Form_1):
#
#     # switch_window = QtCore.pyqtSignal()
#
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         self.setupUi(self)

    #     self.pushButton_choose_p1.clicked.connect(self.button_released)
    #
    # def button_released(self):
    #     sending_button = self.sender()
    #     print('%s Clicked!' % str(sending_button.objectName()))

        # self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    # def pushbutton_handler(self):
    #     self.switch_window.emit()


# class WindowSix(QtWidgets.QWidget, Ui_Form_6):
#
#     switch_window = QtCore.pyqtSignal()
#
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         self.setupUi(self)
#
#         self.pushButton_quit.clicked.connect(self.pushbutton_handler)
#         # self.pushButton_quit.clicked.connect(self.return_choose)
#
#     def pushbutton_handler(self):
#         self.switch_window.emit()

    # def return_choose(self):
    #     self.hide()
    #     win = self.ChoiceWindow()
    #     # self.ui = Ui_Form_1()
    #     # self.ui.setupUi(self.form)
    #     win.show()
    #     # win.exec_()


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_choice)
        self.login.close()
        self.window.show()

    def show_window_choice(self):
        self.window_choice = ChoiceWindow()
        # self.window_choice.switch_window.connect(self.show_window_six)
        self.window.close()
        # self.window_six.close()
        self.window_choice.show()

    # def show_window_one(self):
    #     self.window_one = WindowOne()
    #     self.window_one.switch_window.connect(self.show_window_choice)
    #     self.window_choice.close()
    #     self.window_one.show()

    # def show_window_six(self):
    #     self.window_six = WindowSix()
    #     self.window_six.switch_window.connect(self.show_window_choice6)
    #     self.window_choice.hide()
    #     self.window_six.show()
    #
    # def show_window_choice6(self):
    #     self.window_choice = ChoiceWindow()
    #     self.window_choice.switch_window.connect(self.show_window_six)
    #     self.window_six.close()
    #     self.window_choice.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()

    # w1 = WindowOne()
    # w2 = WindowChooseNum()
    # def show_w2():
    #     w2.show()
    # w1.pushButton_choose_p1.clicked.connect(show_w2)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w1 = Ui_Form_1()
#     w2 = WindowChooseNum()
#     w1.show()
#  def show_w2():
#         w2.show()
#  # w1.pushButton.clicked.connect(w1.close_w1)
#     w1.pushButton.clicked.connect(show_w2)
#     app.exec_()
