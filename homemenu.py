# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homemenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 441)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 10, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.radioMultiPlayer = QtWidgets.QRadioButton(self.groupBox)
        self.radioMultiPlayer.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.radioMultiPlayer.setChecked(True)
        self.radioMultiPlayer.setObjectName("radioMultiPlayer")
        self.radioComputer = QtWidgets.QRadioButton(self.groupBox)
        self.radioComputer.setGeometry(QtCore.QRect(140, 30, 171, 20))
        self.radioComputer.setObjectName("radioComputer")
        self.radioComputers = QtWidgets.QRadioButton(self.groupBox)
        self.radioComputers.setGeometry(QtCore.QRect(320, 30, 201, 20))
        self.radioComputers.setObjectName("radioComputers")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(340, 400, 211, 28))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.o_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.o_checkbox.setGeometry(QtCore.QRect(10, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.o_checkbox.setFont(font)
        self.o_checkbox.setAutoExclusive(True)
        self.o_checkbox.setObjectName("o_checkbox")
        self.sound_check = QtWidgets.QCheckBox(self.groupBox_2)
        self.sound_check.setGeometry(QtCore.QRect(150, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sound_check.setFont(font)
        self.sound_check.setObjectName("sound_check")
        self.x_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.x_checkbox.setGeometry(QtCore.QRect(10, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.x_checkbox.setFont(font)
        self.x_checkbox.setAutoExclusive(True)
        self.x_checkbox.setObjectName("x_checkbox")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 150, 291, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.x_color = QtWidgets.QPushButton(self.groupBox_3)
        self.x_color.setGeometry(QtCore.QRect(10, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.x_color.setFont(font)
        self.x_color.setFlat(False)
        self.x_color.setObjectName("x_color")
        self.o_color = QtWidgets.QPushButton(self.groupBox_3)
        self.o_color.setGeometry(QtCore.QRect(110, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.o_color.setFont(font)
        self.o_color.setStyleSheet("")
        self.o_color.setFlat(False)
        self.o_color.setObjectName("o_color")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.marker_size = QtWidgets.QComboBox(self.groupBox_3)
        self.marker_size.setGeometry(QtCore.QRect(110, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.marker_size.setFont(font)
        self.marker_size.setObjectName("marker_size")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.marker_size.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 280, 531, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 30, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("")
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.groupBox.setTitle(_translate("Dialog", "Game Mode"))
        self.radioMultiPlayer.setText(_translate("Dialog", "Multiplayer"))
        self.radioComputer.setText(_translate("Dialog", "against Computer"))
        self.radioComputers.setText(_translate("Dialog", "Computer vs Computer"))
        self.groupBox_2.setTitle(_translate("Dialog", "Options"))
        self.o_checkbox.setText(_translate("Dialog", "Play with O"))
        self.sound_check.setText(_translate("Dialog", "Sound"))
        self.x_checkbox.setText(_translate("Dialog", "Play with X"))
        self.groupBox_3.setTitle(_translate("Dialog", "Style"))
        self.x_color.setText(_translate("Dialog", "X color"))
        self.o_color.setText(_translate("Dialog", "O color"))
        self.label_2.setText(_translate("Dialog", "Marker size"))
        self.marker_size.setCurrentText(_translate("Dialog", "1"))
        self.marker_size.setItemText(0, _translate("Dialog", "1"))
        self.marker_size.setItemText(1, _translate("Dialog", "2"))
        self.marker_size.setItemText(2, _translate("Dialog", "3"))
        self.marker_size.setItemText(3, _translate("Dialog", "4"))
        self.marker_size.setItemText(4, _translate("Dialog", "5"))
        self.marker_size.setItemText(5, _translate("Dialog", "6"))
        self.marker_size.setItemText(6, _translate("Dialog", "7"))
        self.marker_size.setItemText(7, _translate("Dialog", "8"))
        self.marker_size.setItemText(8, _translate("Dialog", "9"))
        self.marker_size.setItemText(9, _translate("Dialog", "10"))
        self.marker_size.setItemText(10, _translate("Dialog", "11"))
        self.marker_size.setItemText(11, _translate("Dialog", "12"))
        self.marker_size.setItemText(12, _translate("Dialog", "13"))
        self.marker_size.setItemText(13, _translate("Dialog", "14"))
        self.marker_size.setItemText(14, _translate("Dialog", "15"))
        self.marker_size.setItemText(15, _translate("Dialog", "30"))
        self.marker_size.setItemText(16, _translate("Dialog", "50"))
        self.groupBox_4.setTitle(_translate("Dialog", "Other options"))
        self.checkBox.setText(_translate("Dialog", "Automatically reset the board"))
        self.checkBox_2.setText(_translate("Dialog", "Show Moves"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())