# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evokedStatsDialog.ui'
#
# Created: Sun Sep 29 15:30:59 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_EvokedStatsDialog(object):
    def setupUi(self, EvokedStatsDialog):
        EvokedStatsDialog.setObjectName(_fromUtf8("EvokedStatsDialog"))
        EvokedStatsDialog.resize(1042, 871)
        EvokedStatsDialog.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_3 = QtGui.QVBoxLayout(EvokedStatsDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(EvokedStatsDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1022, 814))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(980, 780))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.layoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 951, 744))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBoxEvoked = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxEvoked.setObjectName(_fromUtf8("comboBoxEvoked"))
        self.verticalLayout.addWidget(self.comboBoxEvoked)
        self.labelChannels = QtGui.QLabel(self.layoutWidget)
        self.labelChannels.setObjectName(_fromUtf8("labelChannels"))
        self.verticalLayout.addWidget(self.labelChannels)
        self.listWidgetChannels = QtGui.QListWidget(self.layoutWidget)
        self.listWidgetChannels.setMinimumSize(QtCore.QSize(0, 400))
        self.listWidgetChannels.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetChannels.setObjectName(_fromUtf8("listWidgetChannels"))
        self.verticalLayout.addWidget(self.listWidgetChannels)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelSelectedChannel = QtGui.QLabel(self.layoutWidget)
        self.labelSelectedChannel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSelectedChannel.setObjectName(_fromUtf8("labelSelectedChannel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.labelSelectedChannel)
        self.labelStart = QtGui.QLabel(self.layoutWidget)
        self.labelStart.setObjectName(_fromUtf8("labelStart"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelStart)
        self.doubleSpinBoxStart = QtGui.QDoubleSpinBox(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 99, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.doubleSpinBoxStart.setPalette(palette)
        self.doubleSpinBoxStart.setReadOnly(True)
        self.doubleSpinBoxStart.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxStart.setDecimals(3)
        self.doubleSpinBoxStart.setMinimum(-99.0)
        self.doubleSpinBoxStart.setSingleStep(0.001)
        self.doubleSpinBoxStart.setObjectName(_fromUtf8("doubleSpinBoxStart"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxStart)
        self.labelStop = QtGui.QLabel(self.layoutWidget)
        self.labelStop.setObjectName(_fromUtf8("labelStop"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelStop)
        self.doubleSpinBoxStop = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxStop.setReadOnly(True)
        self.doubleSpinBoxStop.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxStop.setDecimals(3)
        self.doubleSpinBoxStop.setMinimum(-99.0)
        self.doubleSpinBoxStop.setSingleStep(0.001)
        self.doubleSpinBoxStop.setObjectName(_fromUtf8("doubleSpinBoxStop"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxStop)
        self.labelMin = QtGui.QLabel(self.layoutWidget)
        self.labelMin.setObjectName(_fromUtf8("labelMin"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelMin)
        self.doubleSpinBoxMinAmplitude = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMinAmplitude.setReadOnly(True)
        self.doubleSpinBoxMinAmplitude.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxMinAmplitude.setDecimals(3)
        self.doubleSpinBoxMinAmplitude.setMinimum(-99.0)
        self.doubleSpinBoxMinAmplitude.setSingleStep(0.001)
        self.doubleSpinBoxMinAmplitude.setProperty("value", 0.0)
        self.doubleSpinBoxMinAmplitude.setObjectName(_fromUtf8("doubleSpinBoxMinAmplitude"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMinAmplitude)
        self.labelMinTime = QtGui.QLabel(self.layoutWidget)
        self.labelMinTime.setObjectName(_fromUtf8("labelMinTime"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelMinTime)
        self.doubleSpinBoxMinTime = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMinTime.setReadOnly(True)
        self.doubleSpinBoxMinTime.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxMinTime.setDecimals(3)
        self.doubleSpinBoxMinTime.setMinimum(-99.0)
        self.doubleSpinBoxMinTime.setSingleStep(0.001)
        self.doubleSpinBoxMinTime.setObjectName(_fromUtf8("doubleSpinBoxMinTime"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMinTime)
        self.labelMax = QtGui.QLabel(self.layoutWidget)
        self.labelMax.setObjectName(_fromUtf8("labelMax"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.labelMax)
        self.doubleSpinBoxMaxAmplitude = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMaxAmplitude.setReadOnly(True)
        self.doubleSpinBoxMaxAmplitude.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxMaxAmplitude.setDecimals(3)
        self.doubleSpinBoxMaxAmplitude.setMinimum(-99.0)
        self.doubleSpinBoxMaxAmplitude.setSingleStep(0.001)
        self.doubleSpinBoxMaxAmplitude.setProperty("value", 0.0)
        self.doubleSpinBoxMaxAmplitude.setObjectName(_fromUtf8("doubleSpinBoxMaxAmplitude"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMaxAmplitude)
        self.labelMaxTime = QtGui.QLabel(self.layoutWidget)
        self.labelMaxTime.setObjectName(_fromUtf8("labelMaxTime"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.labelMaxTime)
        self.doubleSpinBoxMaxTime = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMaxTime.setReadOnly(True)
        self.doubleSpinBoxMaxTime.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxMaxTime.setDecimals(3)
        self.doubleSpinBoxMaxTime.setMinimum(-99.0)
        self.doubleSpinBoxMaxTime.setSingleStep(0.001)
        self.doubleSpinBoxMaxTime.setObjectName(_fromUtf8("doubleSpinBoxMaxTime"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMaxTime)
        self.labelHalfMax = QtGui.QLabel(self.layoutWidget)
        self.labelHalfMax.setObjectName(_fromUtf8("labelHalfMax"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.labelHalfMax)
        self.doubleSpinBoxHalfMaxAmplitude = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxHalfMaxAmplitude.setReadOnly(True)
        self.doubleSpinBoxHalfMaxAmplitude.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxHalfMaxAmplitude.setDecimals(3)
        self.doubleSpinBoxHalfMaxAmplitude.setMinimum(-99.0)
        self.doubleSpinBoxHalfMaxAmplitude.setSingleStep(0.001)
        self.doubleSpinBoxHalfMaxAmplitude.setProperty("value", 0.0)
        self.doubleSpinBoxHalfMaxAmplitude.setObjectName(_fromUtf8("doubleSpinBoxHalfMaxAmplitude"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxHalfMaxAmplitude)
        self.labelHalfMaxBefore = QtGui.QLabel(self.layoutWidget)
        self.labelHalfMaxBefore.setObjectName(_fromUtf8("labelHalfMaxBefore"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.labelHalfMaxBefore)
        self.doubleSpinBoxHalfMaxBefore = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxHalfMaxBefore.setReadOnly(True)
        self.doubleSpinBoxHalfMaxBefore.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxHalfMaxBefore.setDecimals(3)
        self.doubleSpinBoxHalfMaxBefore.setMinimum(-99.0)
        self.doubleSpinBoxHalfMaxBefore.setSingleStep(0.001)
        self.doubleSpinBoxHalfMaxBefore.setObjectName(_fromUtf8("doubleSpinBoxHalfMaxBefore"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxHalfMaxBefore)
        self.labelMaxTimeAfter = QtGui.QLabel(self.layoutWidget)
        self.labelMaxTimeAfter.setObjectName(_fromUtf8("labelMaxTimeAfter"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.labelMaxTimeAfter)
        self.doubleSpinBoxHalfMaxAfter = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxHalfMaxAfter.setReadOnly(True)
        self.doubleSpinBoxHalfMaxAfter.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxHalfMaxAfter.setDecimals(3)
        self.doubleSpinBoxHalfMaxAfter.setMinimum(-99.0)
        self.doubleSpinBoxHalfMaxAfter.setSingleStep(0.001)
        self.doubleSpinBoxHalfMaxAfter.setObjectName(_fromUtf8("doubleSpinBoxHalfMaxAfter"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxHalfMaxAfter)
        self.labelDuration = QtGui.QLabel(self.layoutWidget)
        self.labelDuration.setObjectName(_fromUtf8("labelDuration"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.labelDuration)
        self.doubleSpinBoxDuration = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxDuration.setReadOnly(True)
        self.doubleSpinBoxDuration.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxDuration.setDecimals(3)
        self.doubleSpinBoxDuration.setMinimum(-99.0)
        self.doubleSpinBoxDuration.setSingleStep(0.001)
        self.doubleSpinBoxDuration.setObjectName(_fromUtf8("doubleSpinBoxDuration"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxDuration)
        self.labelIntegral = QtGui.QLabel(self.layoutWidget)
        self.labelIntegral.setObjectName(_fromUtf8("labelIntegral"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.labelIntegral)
        self.doubleSpinBoxIntegral = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxIntegral.setReadOnly(True)
        self.doubleSpinBoxIntegral.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBoxIntegral.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxIntegral.setDecimals(3)
        self.doubleSpinBoxIntegral.setMinimum(-99.0)
        self.doubleSpinBoxIntegral.setSingleStep(0.001)
        self.doubleSpinBoxIntegral.setProperty("value", 0.0)
        self.doubleSpinBoxIntegral.setObjectName(_fromUtf8("doubleSpinBoxIntegral"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxIntegral)
        self.pushButtonVisualize = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonVisualize.setObjectName(_fromUtf8("pushButtonVisualize"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.pushButtonVisualize)
        self.pushButtonCSV = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonCSV.setObjectName(_fromUtf8("pushButtonCSV"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.pushButtonCSV)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout.setLayout(13, QtGui.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButtonSetSelected = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonSetSelected.setObjectName(_fromUtf8("pushButtonSetSelected"))
        self.horizontalLayout_4.addWidget(self.pushButtonSetSelected)
        self.pushButtonClearSelections = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonClearSelections.setObjectName(_fromUtf8("pushButtonClearSelections"))
        self.horizontalLayout_4.addWidget(self.pushButtonClearSelections)
        self.pushButtonAverage = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonAverage.setObjectName(_fromUtf8("pushButtonAverage"))
        self.horizontalLayout_4.addWidget(self.pushButtonAverage)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBoxLobes = QtGui.QGroupBox(self.layoutWidget)
        self.groupBoxLobes.setObjectName(_fromUtf8("groupBoxLobes"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxLobes)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBoxRFrontal = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxRFrontal.setObjectName(_fromUtf8("checkBoxRFrontal"))
        self.gridLayout.addWidget(self.checkBoxRFrontal, 4, 2, 1, 1)
        self.checkBoxRParietal = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxRParietal.setObjectName(_fromUtf8("checkBoxRParietal"))
        self.gridLayout.addWidget(self.checkBoxRParietal, 2, 2, 1, 1)
        self.checkBoxLOcci = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxLOcci.setObjectName(_fromUtf8("checkBoxLOcci"))
        self.gridLayout.addWidget(self.checkBoxLOcci, 3, 0, 1, 1)
        self.checkBoxROcci = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxROcci.setObjectName(_fromUtf8("checkBoxROcci"))
        self.gridLayout.addWidget(self.checkBoxROcci, 3, 2, 1, 1)
        self.checkBoxLFrontal = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxLFrontal.setObjectName(_fromUtf8("checkBoxLFrontal"))
        self.gridLayout.addWidget(self.checkBoxLFrontal, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(123, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.checkBoxLTemp = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxLTemp.setObjectName(_fromUtf8("checkBoxLTemp"))
        self.gridLayout.addWidget(self.checkBoxLTemp, 1, 0, 1, 1)
        self.checkBoxRTemp = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxRTemp.setObjectName(_fromUtf8("checkBoxRTemp"))
        self.gridLayout.addWidget(self.checkBoxRTemp, 1, 2, 1, 1)
        self.checkBoxLParietal = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxLParietal.setObjectName(_fromUtf8("checkBoxLParietal"))
        self.gridLayout.addWidget(self.checkBoxLParietal, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(116, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.checkBoxVertex = QtGui.QCheckBox(self.groupBoxLobes)
        self.checkBoxVertex.setTristate(False)
        self.checkBoxVertex.setObjectName(_fromUtf8("checkBoxVertex"))
        self.gridLayout.addWidget(self.checkBoxVertex, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBoxLobes)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(EvokedStatsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(EvokedStatsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EvokedStatsDialog.reject)
        QtCore.QObject.connect(self.pushButtonClearSelections, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidgetChannels.clearSelection)
        QtCore.QMetaObject.connectSlotsByName(EvokedStatsDialog)
        EvokedStatsDialog.setTabOrder(self.scrollArea, self.comboBoxEvoked)
        EvokedStatsDialog.setTabOrder(self.comboBoxEvoked, self.listWidgetChannels)
        EvokedStatsDialog.setTabOrder(self.listWidgetChannels, self.pushButtonSetSelected)
        EvokedStatsDialog.setTabOrder(self.pushButtonSetSelected, self.pushButtonClearSelections)
        EvokedStatsDialog.setTabOrder(self.pushButtonClearSelections, self.pushButtonAverage)
        EvokedStatsDialog.setTabOrder(self.pushButtonAverage, self.checkBoxVertex)
        EvokedStatsDialog.setTabOrder(self.checkBoxVertex, self.checkBoxLTemp)
        EvokedStatsDialog.setTabOrder(self.checkBoxLTemp, self.checkBoxRTemp)
        EvokedStatsDialog.setTabOrder(self.checkBoxRTemp, self.checkBoxLParietal)
        EvokedStatsDialog.setTabOrder(self.checkBoxLParietal, self.checkBoxRParietal)
        EvokedStatsDialog.setTabOrder(self.checkBoxRParietal, self.checkBoxLOcci)
        EvokedStatsDialog.setTabOrder(self.checkBoxLOcci, self.checkBoxROcci)
        EvokedStatsDialog.setTabOrder(self.checkBoxROcci, self.checkBoxLFrontal)
        EvokedStatsDialog.setTabOrder(self.checkBoxLFrontal, self.checkBoxRFrontal)
        EvokedStatsDialog.setTabOrder(self.checkBoxRFrontal, self.pushButtonVisualize)
        EvokedStatsDialog.setTabOrder(self.pushButtonVisualize, self.pushButtonCSV)
        EvokedStatsDialog.setTabOrder(self.pushButtonCSV, self.buttonBox)
        EvokedStatsDialog.setTabOrder(self.buttonBox, self.doubleSpinBoxStart)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxStart, self.doubleSpinBoxStop)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxStop, self.doubleSpinBoxIntegral)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxIntegral, self.doubleSpinBoxHalfMaxAmplitude)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxHalfMaxAmplitude, self.doubleSpinBoxHalfMaxBefore)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxHalfMaxBefore, self.doubleSpinBoxHalfMaxAfter)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxHalfMaxAfter, self.doubleSpinBoxDuration)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxDuration, self.doubleSpinBoxMinTime)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxMinTime, self.doubleSpinBoxMaxAmplitude)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxMaxAmplitude, self.doubleSpinBoxMaxTime)
        EvokedStatsDialog.setTabOrder(self.doubleSpinBoxMaxTime, self.doubleSpinBoxMinAmplitude)

    def retranslateUi(self, EvokedStatsDialog):
        EvokedStatsDialog.setWindowTitle(_translate("EvokedStatsDialog", "Evoked data statistics", None))
        self.comboBoxEvoked.setToolTip(_translate("EvokedStatsDialog", "Selected set of evokeds", None))
        self.labelChannels.setText(_translate("EvokedStatsDialog", "Channels:", None))
        self.labelSelectedChannel.setText(_translate("EvokedStatsDialog", "No channel selected", None))
        self.labelStart.setText(_translate("EvokedStatsDialog", "Start:", None))
        self.doubleSpinBoxStart.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelStop.setText(_translate("EvokedStatsDialog", "Stop:", None))
        self.doubleSpinBoxStop.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelMin.setText(_translate("EvokedStatsDialog", "Minimum amplitude:", None))
        self.doubleSpinBoxMinAmplitude.setSuffix(_translate("EvokedStatsDialog", "µT", None))
        self.labelMinTime.setText(_translate("EvokedStatsDialog", "Time of minimum:", None))
        self.doubleSpinBoxMinTime.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelMax.setText(_translate("EvokedStatsDialog", "Maximum amplitude:", None))
        self.doubleSpinBoxMaxAmplitude.setSuffix(_translate("EvokedStatsDialog", "µT", None))
        self.labelMaxTime.setText(_translate("EvokedStatsDialog", "Time of maximum:", None))
        self.doubleSpinBoxMaxTime.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelHalfMax.setText(_translate("EvokedStatsDialog", "Half maximum:", None))
        self.doubleSpinBoxHalfMaxAmplitude.setSuffix(_translate("EvokedStatsDialog", "µT", None))
        self.labelHalfMaxBefore.setText(_translate("EvokedStatsDialog", "Time before max:", None))
        self.doubleSpinBoxHalfMaxBefore.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelMaxTimeAfter.setText(_translate("EvokedStatsDialog", "Time after max:", None))
        self.doubleSpinBoxHalfMaxAfter.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelDuration.setText(_translate("EvokedStatsDialog", "Duration:", None))
        self.doubleSpinBoxDuration.setSuffix(_translate("EvokedStatsDialog", "s", None))
        self.labelIntegral.setText(_translate("EvokedStatsDialog", "Integral:", None))
        self.pushButtonVisualize.setText(_translate("EvokedStatsDialog", "Visualize channel/average", None))
        self.pushButtonCSV.setText(_translate("EvokedStatsDialog", "Save CSV", None))
        self.pushButtonSetSelected.setText(_translate("EvokedStatsDialog", "Set selections", None))
        self.pushButtonClearSelections.setText(_translate("EvokedStatsDialog", "Clear selections", None))
        self.pushButtonAverage.setText(_translate("EvokedStatsDialog", "Average selected channels", None))
        self.groupBoxLobes.setTitle(_translate("EvokedStatsDialog", "Lobes", None))
        self.checkBoxRFrontal.setToolTip(_translate("EvokedStatsDialog", "MEG 0813|MEG 0812|MEG 0912|MEG 0913|MEG 0922|\n"
"MEG 0923|MEG 1212|MEG 1213|MEG 1223|MEG 1222|\n"
"MEG 1412|MEG 1413|MEG 0943|MEG 0942|MEG 0933|\n"
"MEG 0932|MEG 1232|MEG 1233|MEG 1012|MEG 1013|\n"
"MEG 1022|MEG 1023|MEG 1243|MEG 1242|MEG 1033|\n"
"MEG 1032|MEG 0811|MEG 0911|MEG 0921|MEG 1211|\n"
"MEG 1221|MEG 1411|MEG 0941|MEG 0931|MEG 1231|\n"
"MEG 1011|MEG 1021|MEG 1241|MEG 1031", None))
        self.checkBoxRFrontal.setText(_translate("EvokedStatsDialog", "Right-frontal", None))
        self.checkBoxRParietal.setToolTip(_translate("EvokedStatsDialog", "MEG 1043|MEG 1042|MEG 1112|MEG 1113|MEG 1123|\n"
"MEG 1122|MEG 0722|MEG 0723|MEG 1142|MEG 1143|\n"
"MEG 1133|MEG 1132|MEG 0732|MEG 0733|MEG 2212|\n"
"MEG 2213|MEG 2223|MEG 2222|MEG 2242|MEG 2243|\n"
"MEG 2232|MEG 2233|MEG 2442|MEG 2443|MEG 2023|\n"
"MEG 2022|MEG 1041|MEG 1111|MEG 1121|MEG 0721|\n"
"MEG 1141|MEG 1131|MEG 0731|MEG 2211|MEG 2221|\n"
"MEG 2241|MEG 2231|MEG 2441|MEG 2021", None))
        self.checkBoxRParietal.setText(_translate("EvokedStatsDialog", "Right-parietal", None))
        self.checkBoxLOcci.setToolTip(_translate("EvokedStatsDialog", "MEG 2042|MEG 2043|MEG 1913|MEG 1912|MEG 2113|\n"
"MEG 2112|MEG 1922|MEG 1923|MEG 1942|MEG 1943|\n"
"MEG 1642|MEG 1643|MEG 1933|MEG 1932|MEG 1733|\n"
"MEG 1732|MEG 1723|MEG 1722|MEG 2143|MEG 2142|\n"
"MEG 1742|MEG 1743|MEG 1712|MEG 1713|MEG 2041|\n"
"MEG 1911|MEG 2111|MEG 1921|MEG 1941|MEG 1641|\n"
"MEG 1931|MEG 1731|MEG 1721|MEG 2141|MEG 1741|\n"
"MEG 1711", None))
        self.checkBoxLOcci.setText(_translate("EvokedStatsDialog", "Left-occipital", None))
        self.checkBoxROcci.setToolTip(_translate("EvokedStatsDialog", "MEG 2032|MEG 2033|MEG 2313|MEG 2312|MEG 2342|\n"
"MEG 2343|MEG 2322|MEG 2323|MEG 2433|MEG 2432|\n"
"MEG 2122|MEG 2123|MEG 2333|MEG 2332|MEG 2513|\n"
"MEG 2512|MEG 2523|MEG 2522|MEG 2133|MEG 2132|\n"
"MEG 2542|MEG 2543|MEG 2532|MEG 2533|MEG 2031|\n"
"MEG 2311|MEG 2341|MEG 2321|MEG 2431|MEG 2121|\n"
"MEG 2331|MEG 2511|MEG 2521|MEG 2131|MEG 2541|\n"
"MEG 2531", None))
        self.checkBoxROcci.setText(_translate("EvokedStatsDialog", "Right-occipital", None))
        self.checkBoxLFrontal.setToolTip(_translate("EvokedStatsDialog", "MEG 0522|MEG 0523|MEG 0512|MEG 0513|MEG 0312|\n"
"MEG 0313|MEG 0342|MEG 0343|MEG 0122|MEG 0123|\n"
"MEG 0822|MEG 0823|MEG 0533|MEG 0532|MEG 0543|\n"
"MEG 0542|MEG 0322|MEG 0323|MEG 0612|MEG 0613|\n"
"MEG 0333|MEG 0332|MEG 0622|MEG 0623|MEG 0643|\n"
"MEG 0642|MEG 0521|MEG 0511|MEG 0311|MEG 0341|\n"
"MEG 0121|MEG 0821|MEG 0531|MEG 0541|MEG 0321|\n"
"MEG 0611|MEG 0331|MEG 0621|MEG 0641", None))
        self.checkBoxLFrontal.setText(_translate("EvokedStatsDialog", "Left-frontal", None))
        self.checkBoxLTemp.setToolTip(_translate("EvokedStatsDialog", "MEG 0223|MEG 0222|MEG 0212|MEG 0213|MEG 0133|\n"
"MEG 0132|MEG 0112|MEG 0113|MEG 0233|MEG 0232|\n"
"MEG 0243|MEG 0242|MEG 1512|MEG 1513|MEG 0143|\n"
"MEG 0142|MEG 1623|MEG 1622|MEG 1613|MEG 1612|\n"
"MEG 1523|MEG 1522|MEG 1543|MEG 1542|MEG 1533|\n"
"MEG 1532|MEG 0221|MEG 0211|MEG 0131|MEG 0111|\n"
"MEG 0231|MEG 0241|MEG 1511|MEG 0141|MEG 1621|\n"
"MEG 1611|MEG 1521|MEG 1541|MEG 1531", None))
        self.checkBoxLTemp.setText(_translate("EvokedStatsDialog", "Left-temporal", None))
        self.checkBoxRTemp.setToolTip(_translate("EvokedStatsDialog", "MEG 1312|MEG 1313|MEG 1323|MEG 1322|MEG 1442|\n"
"MEG 1443|MEG 1423|MEG 1422|MEG 1342|MEG 1343|\n"
"MEG 1333|MEG 1332|MEG 2612|MEG 2613|MEG 1433|\n"
"MEG 1432|MEG 2413|MEG 2412|MEG 2422|MEG 2423|\n"
"MEG 2642|MEG 2643|MEG 2623|MEG 2622|MEG 2633|\n"
"MEG 2632|MEG 1311|MEG 1321|MEG 1441|MEG 1421|\n"
"MEG 1341|MEG 1331|MEG 2611|MEG 1431|MEG 2411|\n"
"MEG 2421|MEG 2641|MEG 2621|MEG 2631", None))
        self.checkBoxRTemp.setText(_translate("EvokedStatsDialog", "Right-temporal", None))
        self.checkBoxLParietal.setToolTip(_translate("EvokedStatsDialog", "MEG 0633|MEG 0632|MEG 0423|MEG 0422|MEG 0412|\n"
"MEG 0413|MEG 0712|MEG 0713|MEG 0433|MEG 0432|\n"
"MEG 0442|MEG 0443|MEG 0742|MEG 0743|MEG 1822|\n"
"MEG 1823|MEG 1813|MEG 1812|MEG 1832|MEG 1833|\n"
"MEG 1843|MEG 1842|MEG 1632|MEG 1633|MEG 2013|\n"
"MEG 2012|MEG 0631|MEG 0421|MEG 0411|MEG 0711|\n"
"MEG 0431|MEG 0441|MEG 0741|MEG 1821|MEG 1811|\n"
"MEG 1831|MEG 1841|MEG 1631|MEG 2011", None))
        self.checkBoxLParietal.setText(_translate("EvokedStatsDialog", "Left-parietal", None))
        self.checkBoxVertex.setToolTip(_translate("EvokedStatsDialog", "MEG 0633|MEG 0632|MEG 0423|MEG 0422|MEG 0712|\n"
"MEG 0713|MEG 0433|MEG 0432|MEG 0742|MEG 0743|\n"
"MEG 1822|MEG 1823|MEG 1043|MEG 1042|MEG 1112|\n"
"MEG 1113|MEG 0722|MEG 0723|MEG 1142|MEG 1143|\n"
"MEG 0732|MEG 0733|MEG 2212|MEG 2213|MEG 0631|\n"
"MEG 0431|MEG 0711|MEG 0431|MEG 0741|MEG 1821|\n"
"MEG 1041|MEG 1111|MEG 0721|MEG 1141|MEG 0731|\n"
"MEG 2211", None))
        self.checkBoxVertex.setText(_translate("EvokedStatsDialog", "Vertex", None))
