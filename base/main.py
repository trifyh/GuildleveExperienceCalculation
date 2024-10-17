from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtGui import QFont
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


if __name__ == '__main__':
    # 自适应缩放和高dpi
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)
    # QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    font = QFont()
    font.setPixelSize(12)  # 设置默认的像素字体大小
    app.setFont(font)  # 设置应用程序的默认字体

    ex = MainLoop()
    sys.exit(app.exec_())
