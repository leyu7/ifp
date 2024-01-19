from demo1justTry import *

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MainWindow(QMainWindow, Ui_Init_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class LoginWindow(QWidget, Ui_Signin_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signin_pushbutton.clicked.connect(self.check)

    def check(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if username != 'warwickIFP' or password != 'itisperuke':
            QtWidgets.QMessageBox.warning(None, "Wrong!", "Sorry, your information isn't correct\nPlease try again")
        else:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    login_win = LoginWindow()
    main_win.start_pushButton.clicked.connect(login_win.show)  # 点击按钮start打开登录窗口
    main_win.show()
    sys.exit(app.exec_())
