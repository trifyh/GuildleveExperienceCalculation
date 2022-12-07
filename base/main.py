from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QGridLayout, QLabel, QLineEdit,
                             QTextEdit, QCheckBox)
from PyQt5.QtGui import QFont, QIcon
import sys
from PyQt5.QtCore import Qt
from UI.GuildleveExperienceCalculation import *


class MainLoop(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        Ui_Dialog().setupUi(self)
        self.setWindowIcon(QIcon('icon.ico'))
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '提示', "作者海柊月 报个bug：934472842\n"
                                                 "是否确认退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainLoop()
    sys.exit(app.exec_())
