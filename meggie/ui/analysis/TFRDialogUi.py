# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TFRDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TFRDialog(object):
    def setupUi(self, TFRDialog):
        TFRDialog.setObjectName("TFRDialog")
        TFRDialog.resize(576, 482)
        self.gridLayout_2 = QtWidgets.QGridLayout(TFRDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(TFRDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(TFRDialog)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 558, 432))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBoxMisc = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxMisc.setObjectName("groupBoxMisc")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBoxMisc)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.spinBoxDecim = QtWidgets.QSpinBox(self.groupBoxMisc)
        self.spinBoxDecim.setMinimum(1)
        self.spinBoxDecim.setMaximum(1000)
        self.spinBoxDecim.setProperty("value", 1)
        self.spinBoxDecim.setObjectName("spinBoxDecim")
        self.gridLayout_10.addWidget(self.spinBoxDecim, 0, 1, 1, 1)
        self.labelDecim = QtWidgets.QLabel(self.groupBoxMisc)
        self.labelDecim.setObjectName("labelDecim")
        self.gridLayout_10.addWidget(self.labelDecim, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSubtractEvoked = QtWidgets.QLabel(self.groupBoxMisc)
        self.labelSubtractEvoked.setObjectName("labelSubtractEvoked")
        self.horizontalLayout.addWidget(self.labelSubtractEvoked)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBoxSubtractEvoked = QtWidgets.QCheckBox(self.groupBoxMisc)
        self.checkBoxSubtractEvoked.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxSubtractEvoked.setText("")
        self.checkBoxSubtractEvoked.setObjectName("checkBoxSubtractEvoked")
        self.horizontalLayout.addWidget(self.checkBoxSubtractEvoked)
        self.gridLayout_9.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxMisc, 4, 0, 1, 1)
        self.groupBoxFrequencies = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBoxFrequencies.sizePolicy().hasHeightForWidth())
        self.groupBoxFrequencies.setSizePolicy(sizePolicy)
        self.groupBoxFrequencies.setObjectName("groupBoxFrequencies")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxFrequencies)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelMinFreq = QtWidgets.QLabel(self.groupBoxFrequencies)
        self.labelMinFreq.setObjectName("labelMinFreq")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelMinFreq)
        self.doubleSpinBoxMinFreq = QtWidgets.QDoubleSpinBox(self.groupBoxFrequencies)
        self.doubleSpinBoxMinFreq.setMinimum(0.0)
        self.doubleSpinBoxMinFreq.setMaximum(1000.0)
        self.doubleSpinBoxMinFreq.setProperty("value", 5.0)
        self.doubleSpinBoxMinFreq.setObjectName("doubleSpinBoxMinFreq")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxMinFreq)
        self.labelMaxFreq = QtWidgets.QLabel(self.groupBoxFrequencies)
        self.labelMaxFreq.setObjectName("labelMaxFreq")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelMaxFreq)
        self.doubleSpinBoxMaxFreq = QtWidgets.QDoubleSpinBox(self.groupBoxFrequencies)
        self.doubleSpinBoxMaxFreq.setMinimum(0.0)
        self.doubleSpinBoxMaxFreq.setMaximum(1000.0)
        self.doubleSpinBoxMaxFreq.setProperty("value", 30.0)
        self.doubleSpinBoxMaxFreq.setObjectName("doubleSpinBoxMaxFreq")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxMaxFreq)
        self.labelFrequencyInterval = QtWidgets.QLabel(self.groupBoxFrequencies)
        self.labelFrequencyInterval.setObjectName("labelFrequencyInterval")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelFrequencyInterval)
        self.doubleSpinBoxFreqInterval = QtWidgets.QDoubleSpinBox(self.groupBoxFrequencies)
        self.doubleSpinBoxFreqInterval.setMinimum(0.1)
        self.doubleSpinBoxFreqInterval.setMaximum(99.99)
        self.doubleSpinBoxFreqInterval.setProperty("value", 0.5)
        self.doubleSpinBoxFreqInterval.setObjectName("doubleSpinBoxFreqInterval")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxFreqInterval)
        self.label_7 = QtWidgets.QLabel(self.groupBoxFrequencies)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.radioButtonFixed = QtWidgets.QRadioButton(self.groupBoxFrequencies)
        self.radioButtonFixed.setChecked(False)
        self.radioButtonFixed.setObjectName("radioButtonFixed")
        self.horizontalLayout_18.addWidget(self.radioButtonFixed)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_18)
        self.doubleSpinBoxNcycles = QtWidgets.QDoubleSpinBox(self.groupBoxFrequencies)
        self.doubleSpinBoxNcycles.setEnabled(False)
        self.doubleSpinBoxNcycles.setMinimum(1.0)
        self.doubleSpinBoxNcycles.setMaximum(100.0)
        self.doubleSpinBoxNcycles.setProperty("value", 5.0)
        self.doubleSpinBoxNcycles.setObjectName("doubleSpinBoxNcycles")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxNcycles)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.radioButtonAdapted = QtWidgets.QRadioButton(self.groupBoxFrequencies)
        self.radioButtonAdapted.setToolTip("")
        self.radioButtonAdapted.setCheckable(True)
        self.radioButtonAdapted.setChecked(True)
        self.radioButtonAdapted.setObjectName("radioButtonAdapted")
        self.horizontalLayout_19.addWidget(self.radioButtonAdapted)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_19)
        self.doubleSpinBoxCycleFactor = QtWidgets.QDoubleSpinBox(self.groupBoxFrequencies)
        self.doubleSpinBoxCycleFactor.setEnabled(True)
        self.doubleSpinBoxCycleFactor.setToolTip("")
        self.doubleSpinBoxCycleFactor.setMinimum(1.0)
        self.doubleSpinBoxCycleFactor.setMaximum(10.0)
        self.doubleSpinBoxCycleFactor.setSingleStep(1.0)
        self.doubleSpinBoxCycleFactor.setProperty("value", 2.0)
        self.doubleSpinBoxCycleFactor.setObjectName("doubleSpinBoxCycleFactor")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxCycleFactor)
        self.gridLayout_5.addLayout(self.formLayout, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxFrequencies, 3, 0, 1, 2)
        self.groupBoxGeneral = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxGeneral.setObjectName("groupBoxGeneral")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBoxGeneral)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelEpochName = QtWidgets.QLabel(self.groupBoxGeneral)
        self.labelEpochName.setObjectName("labelEpochName")
        self.gridLayout_6.addWidget(self.labelEpochName, 1, 0, 1, 1)
        self.lineEditEpochName = QtWidgets.QLineEdit(self.groupBoxGeneral)
        self.lineEditEpochName.setEnabled(False)
        self.lineEditEpochName.setObjectName("lineEditEpochName")
        self.gridLayout_6.addWidget(self.lineEditEpochName, 1, 1, 1, 1)
        self.labelTFRName = QtWidgets.QLabel(self.groupBoxGeneral)
        self.labelTFRName.setObjectName("labelTFRName")
        self.gridLayout_6.addWidget(self.labelTFRName, 2, 0, 1, 1)
        self.lineEditTFRName = QtWidgets.QLineEdit(self.groupBoxGeneral)
        self.lineEditTFRName.setObjectName("lineEditTFRName")
        self.gridLayout_6.addWidget(self.lineEditTFRName, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxGeneral, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(TFRDialog)
        self.buttonBox.accepted.connect(TFRDialog.accept)
        self.buttonBox.rejected.connect(TFRDialog.reject)
        self.radioButtonAdapted.toggled['bool'].connect(self.doubleSpinBoxCycleFactor.setEnabled)
        self.radioButtonFixed.toggled['bool'].connect(self.doubleSpinBoxNcycles.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(TFRDialog)
        TFRDialog.setTabOrder(self.scrollArea, self.radioButtonFixed)
        TFRDialog.setTabOrder(self.radioButtonFixed, self.radioButtonAdapted)
        TFRDialog.setTabOrder(self.radioButtonAdapted, self.buttonBox)

    def retranslateUi(self, TFRDialog):
        _translate = QtCore.QCoreApplication.translate
        TFRDialog.setWindowTitle(_translate("TFRDialog", "Meggie - Compute TFR"))
        self.groupBoxMisc.setTitle(_translate("TFRDialog", "Miscellaneous"))
        self.labelDecim.setText(_translate("TFRDialog", "Decimation factor:"))
        self.labelSubtractEvoked.setText(_translate("TFRDialog", "Subtract evoked:"))
        self.groupBoxFrequencies.setTitle(_translate("TFRDialog", "Frequency window"))
        self.labelMinFreq.setText(_translate("TFRDialog", "Min frequency:"))
        self.doubleSpinBoxMinFreq.setSuffix(_translate("TFRDialog", "Hz"))
        self.labelMaxFreq.setText(_translate("TFRDialog", "Max frequency:"))
        self.doubleSpinBoxMaxFreq.setSuffix(_translate("TFRDialog", "Hz"))
        self.labelFrequencyInterval.setText(_translate("TFRDialog", "Frequency interval:"))
        self.doubleSpinBoxFreqInterval.setSuffix(_translate("TFRDialog", "Hz"))
        self.label_7.setText(_translate("TFRDialog", "Number of cycles"))
        self.radioButtonFixed.setText(_translate("TFRDialog", "Fixed"))
        self.radioButtonAdapted.setText(_translate("TFRDialog", "Freqs divided by"))
        self.groupBoxGeneral.setTitle(_translate("TFRDialog", "General:"))
        self.labelEpochName.setText(_translate("TFRDialog", "Epoch name: "))
        self.labelTFRName.setText(_translate("TFRDialog", "TFR name:"))

