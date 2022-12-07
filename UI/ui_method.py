import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QHeaderView
from base.loadlifuxlsx import *


class ui_method(object):

    def load_list(self, tableWidget):
        # 选择整行
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 列宽
        tableWidget.horizontalHeader().resizeSection(0, 30)
        tableWidget.horizontalHeader().resizeSection(1, 250)
        tableWidget.horizontalHeader().resizeSection(2, 100)
        tableWidget.horizontalHeader().resizeSection(3, 80)
        tableWidget.horizontalHeader().resizeSection(4, 50)
        tableWidget.horizontalHeader().resizeSection(5, 150)
        # self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 不可编辑
        # self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)

        items = LoadLifuXlsx().get_value('刻木匠', 5)
        for i in range(len(items)):
            item = items[i]
            row = tableWidget.rowCount()
            tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                tableWidget.setItem(row, j, item)
