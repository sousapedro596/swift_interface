# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window2.ui'
#
# Created: Thu Oct 15 13:07:55 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1366, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 631, 671))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(650, 320, 631, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 441, 311))
        self.tableWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(460, 10, 141, 299))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_2.addWidget(self.pushButton_6, 6, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 5, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_2.addWidget(self.pushButton_5, 10, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.1)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(650, 180, 491, 131))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 285, 79))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_9 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_3.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_3.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_3.addWidget(self.pushButton_11, 2, 1, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_3.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_7.setMidLineWidth(0)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 10, 141, 26))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(1150, 210, 131, 51))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 20, 631, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 224, 31))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet(_fromUtf8("background-color:red;"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_6.setText(_translate("MainWindow", "Clear All", None))
        self.pushButton_4.setText(_translate("MainWindow", "Read Current", None))
        self.pushButton_5.setText(_translate("MainWindow", "Update Velocity", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_2.setText(_translate("MainWindow", "Start", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindow", "Send", None))
        self.label_2.setText(_translate("MainWindow", "Vel:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Stop mission", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mission", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tele Operation", None))
        self.pushButton_9.setText(_translate("MainWindow", "Set Offboard", None))
        self.pushButton_8.setText(_translate("MainWindow", "Arm", None))
        self.pushButton_11.setText(_translate("MainWindow", "Disarm", None))
        self.pushButton_12.setText(_translate("MainWindow", "Set Manual", None))
        self.label_7.setText(_translate("MainWindow", "Manual", None))
        self.label_8.setText(_translate("MainWindow", "Disarmed", None))
        self.pushButton_7.setText(_translate("MainWindow", "Start Offboard", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Setup", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2", None))
        self.pushButton_13.setText(_translate("MainWindow", "STOP", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.label_4.setText(_translate("MainWindow", "Connection Lost", None))
        self.label.setText(_translate("MainWindow", "GPS", None))
        self.label_3.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
