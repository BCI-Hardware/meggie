# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'powerSpectrumDialogUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_PowerSpectrumDialog(object):
    def setupUi(self, PowerSpectrumDialog):
        PowerSpectrumDialog.setObjectName(_fromUtf8("PowerSpectrumDialog"))
        PowerSpectrumDialog.resize(724, 672)
        self.gridLayout = QtGui.QGridLayout(PowerSpectrumDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(PowerSpectrumDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 704, 607))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 410))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.groupBoxConditions = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxConditions.setGeometry(QtCore.QRect(10, 10, 681, 191))
        self.groupBoxConditions.setObjectName(_fromUtf8("groupBoxConditions"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxConditions)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelFmin = QtGui.QLabel(self.groupBoxConditions)
        self.labelFmin.setObjectName(_fromUtf8("labelFmin"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelFmin)
        self.spinBoxFmin = QtGui.QSpinBox(self.groupBoxConditions)
        self.spinBoxFmin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.spinBoxFmin.setObjectName(_fromUtf8("spinBoxFmin"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBoxFmin)
        self.labelFmax = QtGui.QLabel(self.groupBoxConditions)
        self.labelFmax.setObjectName(_fromUtf8("labelFmax"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelFmax)
        self.spinBoxFmax = QtGui.QSpinBox(self.groupBoxConditions)
        self.spinBoxFmax.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.spinBoxFmax.setMaximum(150)
        self.spinBoxFmax.setProperty("value", 40)
        self.spinBoxFmax.setObjectName(_fromUtf8("spinBoxFmax"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBoxFmax)
        self.labelChannels = QtGui.QLabel(self.groupBoxConditions)
        self.labelChannels.setObjectName(_fromUtf8("labelChannels"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelChannels)
        self.comboBoxChannels = QtGui.QComboBox(self.groupBoxConditions)
        self.comboBoxChannels.setObjectName(_fromUtf8("comboBoxChannels"))
        self.comboBoxChannels.addItem(_fromUtf8(""))
        self.comboBoxChannels.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBoxChannels)
        self.horizontalLayout_5.addLayout(self.formLayout_2)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.labelNfft = QtGui.QLabel(self.groupBoxConditions)
        self.labelNfft.setObjectName(_fromUtf8("labelNfft"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelNfft)
        self.spinBoxNfft = QtGui.QSpinBox(self.groupBoxConditions)
        self.spinBoxNfft.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.spinBoxNfft.setMaximum(10000)
        self.spinBoxNfft.setProperty("value", 2048)
        self.spinBoxNfft.setObjectName(_fromUtf8("spinBoxNfft"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBoxNfft)
        self.labelOverlap = QtGui.QLabel(self.groupBoxConditions)
        self.labelOverlap.setObjectName(_fromUtf8("labelOverlap"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelOverlap)
        self.spinBoxOverlap = QtGui.QSpinBox(self.groupBoxConditions)
        self.spinBoxOverlap.setMaximum(10000)
        self.spinBoxOverlap.setProperty("value", 1024)
        self.spinBoxOverlap.setObjectName(_fromUtf8("spinBoxOverlap"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBoxOverlap)
        self.checkBoxLogarithm = QtGui.QCheckBox(self.groupBoxConditions)
        self.checkBoxLogarithm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxLogarithm.setAutoFillBackground(False)
        self.checkBoxLogarithm.setChecked(True)
        self.checkBoxLogarithm.setObjectName(_fromUtf8("checkBoxLogarithm"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkBoxLogarithm)
        self.checkBoxSaveData = QtGui.QCheckBox(self.groupBoxConditions)
        self.checkBoxSaveData.setObjectName(_fromUtf8("checkBoxSaveData"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBoxSaveData)
        self.horizontalLayout_5.addLayout(self.formLayout_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 200, 671, 251))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBoxIntervals = QtGui.QGroupBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxIntervals.sizePolicy().hasHeightForWidth())
        self.groupBoxIntervals.setSizePolicy(sizePolicy)
        self.groupBoxIntervals.setMaximumSize(QtCore.QSize(260, 16777215))
        self.groupBoxIntervals.setObjectName(_fromUtf8("groupBoxIntervals"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBoxIntervals)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 235, 171))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelTmin = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelTmin.setObjectName(_fromUtf8("labelTmin"))
        self.horizontalLayout_4.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxTmin.setMaximum(1000000000.0)
        self.doubleSpinBoxTmin.setObjectName(_fromUtf8("doubleSpinBoxTmin"))
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxTmin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.labelTmax = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelTmax.setObjectName(_fromUtf8("labelTmax"))
        self.horizontalLayout_6.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBoxTmax.setMaximum(1000000000.0)
        self.doubleSpinBoxTmax.setObjectName(_fromUtf8("doubleSpinBoxTmax"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxTmax)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.pushButtonAdd = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.verticalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonClear = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.verticalLayout.addWidget(self.pushButtonClear)
        self.checkBoxAverage = QtGui.QCheckBox(self.groupBoxIntervals)
        self.checkBoxAverage.setGeometry(QtCore.QRect(20, 210, 94, 26))
        self.checkBoxAverage.setChecked(True)
        self.checkBoxAverage.setObjectName(_fromUtf8("checkBoxAverage"))
        self.horizontalLayout_3.addWidget(self.groupBoxIntervals)
        self.listWidgetIntervals = QtGui.QListWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetIntervals.sizePolicy().hasHeightForWidth())
        self.listWidgetIntervals.setSizePolicy(sizePolicy)
        self.listWidgetIntervals.setObjectName(_fromUtf8("listWidgetIntervals"))
        self.horizontalLayout_3.addWidget(self.listWidgetIntervals)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PowerSpectrumDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonReject = QtGui.QPushButton(PowerSpectrumDialog)
        self.pushButtonReject.setObjectName(_fromUtf8("pushButtonReject"))
        self.horizontalLayout_2.addWidget(self.pushButtonReject)
        self.pushButtonAccept = QtGui.QPushButton(PowerSpectrumDialog)
        self.pushButtonAccept.setObjectName(_fromUtf8("pushButtonAccept"))
        self.horizontalLayout_2.addWidget(self.pushButtonAccept)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(PowerSpectrumDialog)
        QtCore.QObject.connect(self.pushButtonAccept, QtCore.SIGNAL(_fromUtf8("clicked()")), PowerSpectrumDialog.accept)
        QtCore.QObject.connect(self.pushButtonReject, QtCore.SIGNAL(_fromUtf8("clicked()")), PowerSpectrumDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PowerSpectrumDialog)

    def retranslateUi(self, PowerSpectrumDialog):
        PowerSpectrumDialog.setWindowTitle(_translate("PowerSpectrumDialog", "Power spectrum", None))
        self.groupBoxConditions.setTitle(_translate("PowerSpectrumDialog", "Conditions", None))
        self.labelFmin.setToolTip(_translate("PowerSpectrumDialog", "Set the lower limit for the frequencies.", None))
        self.labelFmin.setText(_translate("PowerSpectrumDialog", "Min frequency of interest:", None))
        self.spinBoxFmin.setToolTip(_translate("PowerSpectrumDialog", "Set the lower limit for the frequencies.", None))
        self.spinBoxFmin.setSuffix(_translate("PowerSpectrumDialog", "Hz", None))
        self.labelFmax.setToolTip(_translate("PowerSpectrumDialog", "Set the upper limit for the frequencies.", None))
        self.labelFmax.setText(_translate("PowerSpectrumDialog", "Max frequency of interest:", None))
        self.spinBoxFmax.setToolTip(_translate("PowerSpectrumDialog", "Set the upper limit for the frequencies.", None))
        self.spinBoxFmax.setSuffix(_translate("PowerSpectrumDialog", "Hz", None))
        self.labelChannels.setText(_translate("PowerSpectrumDialog", "Channels", None))
        self.comboBoxChannels.setItemText(0, _translate("PowerSpectrumDialog", "MEG", None))
        self.comboBoxChannels.setItemText(1, _translate("PowerSpectrumDialog", "EEG", None))
        self.labelNfft.setToolTip(_translate("PowerSpectrumDialog", "<html><head/><body><p>The length of the tapers ie. the windows (hanning). The smaller it is the smoother are the PSDs.</p></body></html>", None))
        self.labelNfft.setText(_translate("PowerSpectrumDialog", "Length of the tapers (ie. the windows):", None))
        self.spinBoxNfft.setToolTip(_translate("PowerSpectrumDialog", "<html><head/><body><p>The length of the tapers ie. the windows (hanning). The smaller it is the smoother are the PSDs.</p></body></html>", None))
        self.labelOverlap.setToolTip(_translate("PowerSpectrumDialog", "<html><head/><body><p>Number of overlapping points between the blocks.</p></body></html>", None))
        self.labelOverlap.setText(_translate("PowerSpectrumDialog", "Overlap", None))
        self.spinBoxOverlap.setToolTip(_translate("PowerSpectrumDialog", "<html><head/><body><p>Number of overlapping points between the blocks.</p></body></html>", None))
        self.checkBoxLogarithm.setToolTip(_translate("PowerSpectrumDialog", "Use logarithmic scale.", None))
        self.checkBoxLogarithm.setText(_translate("PowerSpectrumDialog", "Use logarithmic scale", None))
        self.checkBoxSaveData.setText(_translate("PowerSpectrumDialog", "Save data to file", None))
        self.groupBoxIntervals.setTitle(_translate("PowerSpectrumDialog", "Select time intervals", None))
        self.labelTmin.setText(_translate("PowerSpectrumDialog", "Start time:", None))
        self.doubleSpinBoxTmin.setSuffix(_translate("PowerSpectrumDialog", " s", None))
        self.labelTmax.setText(_translate("PowerSpectrumDialog", "End time:", None))
        self.doubleSpinBoxTmax.setSuffix(_translate("PowerSpectrumDialog", " s", None))
        self.pushButtonAdd.setText(_translate("PowerSpectrumDialog", "Add to list >>", None))
        self.pushButtonClear.setText(_translate("PowerSpectrumDialog", "Clear list <<", None))
        self.checkBoxAverage.setText(_translate("PowerSpectrumDialog", "Average", None))
        self.pushButtonReject.setText(_translate("PowerSpectrumDialog", "Cancel", None))
        self.pushButtonAccept.setText(_translate("PowerSpectrumDialog", "Start", None))

