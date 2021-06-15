from list_of_things import things_we_did, birthday_message
from ui.window_generated import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import os
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interface = Ui_MainWindow()
        self.interface.setupUi(self)
        self.interface.showAll.clicked.connect(self.show_everything)
        self.interface.showOne.clicked.connect(self.show_single)
        self.interface.clear.clicked.connect(self.clear)
        self.interface.happyBirthday.clicked.connect(self.happy_birthday)

    def happy_birthday(self):
        self.interface.listWidget.clear()
        self.interface.listWidget.addItem(birthday_message)

    def show_everything(self):
        self.interface.listWidget.clear()
        random.shuffle(things_we_did)
        for thing in things_we_did:
            string = f"In 2020 {thing}."
            self.interface.listWidget.addItem(string)

    def show_single(self):
        self.interface.listWidget.clear()
        random.shuffle(things_we_did)
        string = f"In 2020 {things_we_did[0]}."
        self.interface.listWidget.addItem(string)

    def clear(self):
        self.interface.listWidget.clear()


def main():
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except BaseException as ex:
        print(str(ex))


if __name__ == "__main__":
    main()
