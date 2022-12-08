from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtGui import QIcon, QGuiApplication
import sys
from UI.GuildleveExperienceCalculation import *


class MainLoop(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Ui_Dialog().setupUi(self)
        # 禁用窗口缩放
        self.setFixedSize(self.width(), self.height())
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
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    ex = MainLoop()
    sys.exit(app.exec_())
