from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from ui_start_window_demo import Ui_Form
from ui_login_demo import Ui_Signin_Window
from ui_sixdisc_window_demo import Ui_Form_6
from ui_onedisc_window_demo import Ui_Form_1
from ui_choose_window_demo import Ui_Form_option


# https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161

class Login(QtWidgets.QWidget, Ui_Signin_Window):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.signin_pushbutton.clicked.connect(self.check)
        self.cancel_pushbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def check(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        if username != 'w' or password != '1':
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

        self.pushButton_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton1.clicked.connect(self.choose)
        self.pushButton6.clicked.connect(self.choose)

    #     self.pushButton1.clicked.connect(self.button_released)
    #
    # def button_released(self):
    #     sending_button = self.sender()
    #     print('%s Clicked!' % str(sending_button.objectName()))

    def choose(self):
        sending_button = str(self.sender().objectName())
        if sending_button == 'pushButton1':
            print('%s Clicked!' % sending_button)
            self.choose_one()
            self.close()
        elif sending_button == 'pushButton6':
            self.switch_window.emit()
        else:     # click 1 disc window 'quit' button: return to choice window
            self.one.close()
            self.show()

    def choose_one(self):
        self.one = WindowOne()
        self.one.show()
        self.one.pushButton_quit.clicked.connect(self.choose)


class WindowOne(QtWidgets.QWidget, Ui_Form_1):

    # switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    #     self.pushButton_choose_p1.clicked.connect(self.button_released)
    #
    # def button_released(self):
    #     sending_button = self.sender()
    #     print('%s Clicked!' % str(sending_button.objectName()))

        # self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

    # def pushbutton_handler(self):
    #     self.switch_window.emit()


class WindowSix(QtWidgets.QWidget, Ui_Form_6):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.pushButton_quit.clicked.connect(self.pushbutton_handler)
        # self.pushButton_quit.clicked.connect(self.return_choose)

    def pushbutton_handler(self):
        self.switch_window.emit()

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
        self.window_choice.switch_window.connect(self.show_window_six)
        self.window.close()
        # self.window_six.close()
        self.window_choice.show()

    # def show_window_one(self):
    #     self.window_one = WindowOne()
    #     self.window_one.switch_window.connect(self.show_window_choice)
    #     self.window_choice.close()
    #     self.window_one.show()

    def show_window_six(self):
        self.window_six = WindowSix()
        self.window_six.switch_window.connect(self.show_window_choice6)
        self.window_choice.hide()
        self.window_six.show()

    def show_window_choice6(self):
        self.window_choice = ChoiceWindow()
        self.window_choice.switch_window.connect(self.show_window_six)
        self.window_six.close()
        self.window_choice.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
