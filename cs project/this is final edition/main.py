from PyQt5 import QtCore, QtWidgets
import sys
import pandas as pd

from ui_start_window import Ui_Form
from ui_login import Ui_Signin_Window
from ui_choose_window import Ui_Form_option
import main_window_one_disc
import main_window_six_discs


# switch windows：https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161

class Login(QtWidgets.QWidget, Ui_Signin_Window):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.signin_pushbutton.clicked.connect(self.check)
        self.cancel_pushbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)  # exit the program
        self.signup_pushbutton.clicked.connect(self.signup)

    def signup(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        user_dataframe = pd.read_csv('user_info.csv')
        user_dataframe.loc[user_dataframe.index.max() + 1] = [username, password]   # add user's info
        user_dataframe.to_csv('user_info.csv', index=False)
        QtWidgets.QMessageBox.information(self, 'Welcome!', 'Created the account successfully. You can log in now.')

    def check(self):   # check the info
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        user_dataframe = pd.read_csv('user_info.csv')
        match = user_dataframe[(user_dataframe['name'] == username) & (user_dataframe['password'] == password)]
        if match.empty:   # return boolean
            QtWidgets.QMessageBox.warning(None, "Wrong!", "Sorry, your information isn't correct\nPlease try again")
        else:
            self.pushbutton_handler()

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

        self.pushButton_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)  # exit the program
        self.pushButton1.clicked.connect(self.choose)
        self.pushButton6.clicked.connect(self.choose)

    def choose(self):
        sending_button = str(self.sender().objectName())
        if sending_button == 'pushButton1':
            self.close()
            main_window_one_disc.main()   # open one disc window
        elif sending_button == 'pushButton6':
            self.close()
            main_window_six_discs.main()   # open six discs window


class Controller:   # control the window switching
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
        self.window.close()
        self.window_choice.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
