# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radar_images_dialog_base.ui'
#
# Created: Thu Sep 17 16:57:19 2015
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

class Ui_RadarImagesDialogBase(object):
    def setupUi(self, RadarImagesDialogBase):
        RadarImagesDialogBase.setObjectName(_fromUtf8("RadarImagesDialogBase"))
        RadarImagesDialogBase.resize(432, 108)
        self.button_box = QtGui.QDialogButtonBox(RadarImagesDialogBase)
        self.button_box.setGeometry(QtCore.QRect(70, 60, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.lineEdit = QtGui.QLineEdit(RadarImagesDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 241, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(RadarImagesDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(290, 20, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(RadarImagesDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), RadarImagesDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), RadarImagesDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(RadarImagesDialogBase)

    def retranslateUi(self, RadarImagesDialogBase):
        RadarImagesDialogBase.setWindowTitle(_translate("RadarImagesDialogBase", "Radar Images", None))
        self.lineEdit.setText(_translate("RadarImagesDialogBase", "Browse to the file", None))
        self.pushButton.setText(_translate("RadarImagesDialogBase", "Browse", None))

