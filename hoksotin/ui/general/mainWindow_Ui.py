# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIehdotus12.ui'
#
# Created: Mon May 13 11:28:00 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os

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
        MainWindow.resize(973, 805)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 953, 697))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(937, 638))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabRaw = QtGui.QWidget()
        self.tabRaw.setObjectName(_fromUtf8("tabRaw"))
        self.gridLayout = QtGui.QGridLayout(self.tabRaw)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.metaBox = QtGui.QGroupBox(self.tabRaw)
        self.metaBox.setObjectName(_fromUtf8("metaBox"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.metaBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 291, 194))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelExperiment = QtGui.QLabel(self.formLayoutWidget_2)
        self.labelExperiment.setObjectName(_fromUtf8("labelExperiment"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelExperiment)
        self.labelExperimentName = QtGui.QLabel(self.formLayoutWidget_2)
        self.labelExperimentName.setObjectName(_fromUtf8("labelExperimentName"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelExperimentName)
        self.labelDate = QtGui.QLabel(self.formLayoutWidget_2)
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelDate)
        self.labelDateValue = QtGui.QLabel(self.formLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDateValue.sizePolicy().hasHeightForWidth())
        self.labelDateValue.setSizePolicy(sizePolicy)
        self.labelDateValue.setObjectName(_fromUtf8("labelDateValue"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelDateValue)
        self.labelSubject = QtGui.QLabel(self.formLayoutWidget_2)
        self.labelSubject.setObjectName(_fromUtf8("labelSubject"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelSubject)
        self.labelSubjectValue = QtGui.QLabel(self.formLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSubjectValue.sizePolicy().hasHeightForWidth())
        self.labelSubjectValue.setSizePolicy(sizePolicy)
        self.labelSubjectValue.setObjectName(_fromUtf8("labelSubjectValue"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.labelSubjectValue)
        self.labelAuthor = QtGui.QLabel(self.formLayoutWidget_2)
        self.labelAuthor.setObjectName(_fromUtf8("labelAuthor"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelAuthor)
        self.labelAuthorName = QtGui.QLabel(self.formLayoutWidget_2)
        self.labelAuthorName.setObjectName(_fromUtf8("labelAuthorName"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelAuthorName)
        self.label = QtGui.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        self.textBrowserExperimentDescription = QtGui.QTextBrowser(self.metaBox)
        self.textBrowserExperimentDescription.setGeometry(QtCore.QRect(30, 160, 221, 71))
        self.textBrowserExperimentDescription.setObjectName(_fromUtf8("textBrowserExperimentDescription"))
        self.horizontalLayout_3.addWidget(self.metaBox)
        self.channelsBox = QtGui.QGroupBox(self.tabRaw)
        self.channelsBox.setObjectName(_fromUtf8("channelsBox"))
        self.layoutWidget_7 = QtGui.QWidget(self.channelsBox)
        self.layoutWidget_7.setGeometry(QtCore.QRect(30, 30, 251, 112))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.labelEEG = QtGui.QLabel(self.layoutWidget_7)
        self.labelEEG.setObjectName(_fromUtf8("labelEEG"))
        self.horizontalLayout_6.addWidget(self.labelEEG)
        self.labelEEGValue = QtGui.QLabel(self.layoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEEGValue.sizePolicy().hasHeightForWidth())
        self.labelEEGValue.setSizePolicy(sizePolicy)
        self.labelEEGValue.setObjectName(_fromUtf8("labelEEGValue"))
        self.horizontalLayout_6.addWidget(self.labelEEGValue)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.labelGradMEG = QtGui.QLabel(self.layoutWidget_7)
        self.labelGradMEG.setObjectName(_fromUtf8("labelGradMEG"))
        self.horizontalLayout_7.addWidget(self.labelGradMEG)
        self.labelGradMEGValue = QtGui.QLabel(self.layoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGradMEGValue.sizePolicy().hasHeightForWidth())
        self.labelGradMEGValue.setSizePolicy(sizePolicy)
        self.labelGradMEGValue.setObjectName(_fromUtf8("labelGradMEGValue"))
        self.horizontalLayout_7.addWidget(self.labelGradMEGValue)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.labelMagMEG = QtGui.QLabel(self.layoutWidget_7)
        self.labelMagMEG.setObjectName(_fromUtf8("labelMagMEG"))
        self.horizontalLayout_8.addWidget(self.labelMagMEG)
        self.labelMagMEGValue = QtGui.QLabel(self.layoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMagMEGValue.sizePolicy().hasHeightForWidth())
        self.labelMagMEGValue.setSizePolicy(sizePolicy)
        self.labelMagMEGValue.setObjectName(_fromUtf8("labelMagMEGValue"))
        self.horizontalLayout_8.addWidget(self.labelMagMEGValue)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.labelSamples = QtGui.QLabel(self.layoutWidget_7)
        self.labelSamples.setObjectName(_fromUtf8("labelSamples"))
        self.horizontalLayout_9.addWidget(self.labelSamples)
        self.labelSamplesValue = QtGui.QLabel(self.layoutWidget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSamplesValue.sizePolicy().hasHeightForWidth())
        self.labelSamplesValue.setSizePolicy(sizePolicy)
        self.labelSamplesValue.setObjectName(_fromUtf8("labelSamplesValue"))
        self.horizontalLayout_9.addWidget(self.labelSamplesValue)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3.addWidget(self.channelsBox)
        self.filtersBox = QtGui.QGroupBox(self.tabRaw)
        self.filtersBox.setObjectName(_fromUtf8("filtersBox"))
        self.layoutWidget_6 = QtGui.QWidget(self.filtersBox)
        self.layoutWidget_6.setGeometry(QtCore.QRect(24, 32, 221, 65))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelLow = QtGui.QLabel(self.layoutWidget_6)
        self.labelLow.setLineWidth(1)
        self.labelLow.setScaledContents(True)
        self.labelLow.setObjectName(_fromUtf8("labelLow"))
        self.horizontalLayout_4.addWidget(self.labelLow)
        self.labelLowValue = QtGui.QLabel(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLowValue.sizePolicy().hasHeightForWidth())
        self.labelLowValue.setSizePolicy(sizePolicy)
        self.labelLowValue.setObjectName(_fromUtf8("labelLowValue"))
        self.horizontalLayout_4.addWidget(self.labelLowValue)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelHigh = QtGui.QLabel(self.layoutWidget_6)
        self.labelHigh.setObjectName(_fromUtf8("labelHigh"))
        self.horizontalLayout_5.addWidget(self.labelHigh)
        self.labelHighValue = QtGui.QLabel(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighValue.sizePolicy().hasHeightForWidth())
        self.labelHighValue.setSizePolicy(sizePolicy)
        self.labelHighValue.setObjectName(_fromUtf8("labelHighValue"))
        self.horizontalLayout_5.addWidget(self.labelHighValue)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addWidget(self.filtersBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.triggersBox = QtGui.QGroupBox(self.tabRaw)
        self.triggersBox.setObjectName(_fromUtf8("triggersBox"))
        self.listWidget = QtGui.QListWidget(self.triggersBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 241, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_4.addWidget(self.triggersBox)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonMNE_Browse_Raw = QtGui.QPushButton(self.tabRaw)
        self.pushButtonMNE_Browse_Raw.setObjectName(_fromUtf8("pushButtonMNE_Browse_Raw"))
        self.verticalLayout.addWidget(self.pushButtonMNE_Browse_Raw)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabRaw, _fromUtf8(""))
        self.tabPreprocessing = QtGui.QWidget()
        self.tabPreprocessing.setObjectName(_fromUtf8("tabPreprocessing"))
        self.formLayout = QtGui.QFormLayout(self.tabPreprocessing)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBoxAvailablePreprocessing = QtGui.QGroupBox(self.tabPreprocessing)
        self.groupBoxAvailablePreprocessing.setMaximumSize(QtCore.QSize(400, 170))
        self.groupBoxAvailablePreprocessing.setObjectName(_fromUtf8("groupBoxAvailablePreprocessing"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxAvailablePreprocessing)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonMaxFilter = QtGui.QPushButton(self.groupBoxAvailablePreprocessing)
        self.pushButtonMaxFilter.setObjectName(_fromUtf8("pushButtonMaxFilter"))
        self.gridLayout_3.addWidget(self.pushButtonMaxFilter, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonECG = QtGui.QPushButton(self.groupBoxAvailablePreprocessing)
        self.pushButtonECG.setObjectName(_fromUtf8("pushButtonECG"))
        self.horizontalLayout.addWidget(self.pushButtonECG)
        self.pushButtonApplyECG = QtGui.QPushButton(self.groupBoxAvailablePreprocessing)
        self.pushButtonApplyECG.setEnabled(False)
        self.pushButtonApplyECG.setObjectName(_fromUtf8("pushButtonApplyECG"))
        self.horizontalLayout.addWidget(self.pushButtonApplyECG)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.pushButtonEOG = QtGui.QPushButton(self.groupBoxAvailablePreprocessing)
        self.pushButtonEOG.setObjectName(_fromUtf8("pushButtonEOG"))
        self.horizontalLayout_12.addWidget(self.pushButtonEOG)
        self.pushButtonApplyEOG = QtGui.QPushButton(self.groupBoxAvailablePreprocessing)
        self.pushButtonApplyEOG.setEnabled(False)
        self.pushButtonApplyEOG.setObjectName(_fromUtf8("pushButtonApplyEOG"))
        self.horizontalLayout_12.addWidget(self.pushButtonApplyEOG)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.groupBoxAvailablePreprocessing)
        self.groupBoxPreprocessingCheckBoxes = QtGui.QGroupBox(self.tabPreprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxPreprocessingCheckBoxes.sizePolicy().hasHeightForWidth())
        self.groupBoxPreprocessingCheckBoxes.setSizePolicy(sizePolicy)
        self.groupBoxPreprocessingCheckBoxes.setMinimumSize(QtCore.QSize(60, 0))
        self.groupBoxPreprocessingCheckBoxes.setObjectName(_fromUtf8("groupBoxPreprocessingCheckBoxes"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBoxPreprocessingCheckBoxes)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.labelMaxFilterAccept_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelMaxFilterAccept_2.setText(_fromUtf8(""))
        self.labelMaxFilterAccept_2.setPixmap(QtGui.QPixmap(_fromUtf8("/home/jaolpeso/lahdekoodit/hoksotin/ui/trash/icons/Action-ok-icon.png")))
        self.labelMaxFilterAccept_2.setObjectName(_fromUtf8("labelMaxFilterAccept_2"))
        self.gridLayout_10.addWidget(self.labelMaxFilterAccept_2, 0, 0, 1, 1)
        self.labelECGAppliedAccept_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelECGAppliedAccept_2.setText(_fromUtf8(""))
        self.labelECGAppliedAccept_2.setPixmap(QtGui.QPixmap(_fromUtf8("/home/jaolpeso/lahdekoodit/hoksotin/ui/trash/icons/Action-ok-icon.png")))
        self.labelECGAppliedAccept_2.setObjectName(_fromUtf8("labelECGAppliedAccept_2"))
        self.gridLayout_10.addWidget(self.labelECGAppliedAccept_2, 1, 3, 1, 1)
        self.labelECGComputed_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelECGComputed_2.setObjectName(_fromUtf8("labelECGComputed_2"))
        self.gridLayout_10.addWidget(self.labelECGComputed_2, 1, 1, 1, 1)
        self.labelEOGComputedAccept_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelEOGComputedAccept_2.setText(_fromUtf8(""))
        self.labelEOGComputedAccept_2.setPixmap(QtGui.QPixmap(_fromUtf8("/home/jaolpeso/lahdekoodit/hoksotin/ui/trash/icons/Action-ok-icon.png")))
        self.labelEOGComputedAccept_2.setObjectName(_fromUtf8("labelEOGComputedAccept_2"))
        self.gridLayout_10.addWidget(self.labelEOGComputedAccept_2, 2, 0, 1, 1)
        self.labelEOGApplied_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelEOGApplied_2.setObjectName(_fromUtf8("labelEOGApplied_2"))
        self.gridLayout_10.addWidget(self.labelEOGApplied_2, 2, 4, 1, 1)
        self.labelEOGComputed_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelEOGComputed_2.setObjectName(_fromUtf8("labelEOGComputed_2"))
        self.gridLayout_10.addWidget(self.labelEOGComputed_2, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 2, 2, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.labelMaxFilter_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelMaxFilter_2.setObjectName(_fromUtf8("labelMaxFilter_2"))
        self.horizontalLayout_13.addWidget(self.labelMaxFilter_2)
        self.gridLayout_10.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)
        self.labelEOGAppliedAccept_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelEOGAppliedAccept_2.setText(_fromUtf8(""))
        self.labelEOGAppliedAccept_2.setPixmap(QtGui.QPixmap(_fromUtf8("/home/jaolpeso/lahdekoodit/hoksotin/ui/trash/icons/Action-ok-icon.png")))
        self.labelEOGAppliedAccept_2.setObjectName(_fromUtf8("labelEOGAppliedAccept_2"))
        self.gridLayout_10.addWidget(self.labelEOGAppliedAccept_2, 2, 3, 1, 1)
        self.labelECGApplied_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelECGApplied_2.setObjectName(_fromUtf8("labelECGApplied_2"))
        self.gridLayout_10.addWidget(self.labelECGApplied_2, 1, 4, 1, 1)
        self.labelECGComputedAccept_2 = QtGui.QLabel(self.groupBoxPreprocessingCheckBoxes)
        self.labelECGComputedAccept_2.setText(_fromUtf8(""))
        self.labelECGComputedAccept_2.setPixmap(QtGui.QPixmap(_fromUtf8("/home/jaolpeso/lahdekoodit/hoksotin/ui/trash/icons/Action-ok-icon.png")))
        self.labelECGComputedAccept_2.setObjectName(_fromUtf8("labelECGComputedAccept_2"))
        self.gridLayout_10.addWidget(self.labelECGComputedAccept_2, 1, 0, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_10)
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.groupBoxPreprocessingCheckBoxes)
        self.tabWidget.addTab(self.tabPreprocessing, _fromUtf8(""))
        self.tabEpoching = QtGui.QWidget()
        self.tabEpoching.setObjectName(_fromUtf8("tabEpoching"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabEpoching)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBoxAvailableEpoching = QtGui.QGroupBox(self.tabEpoching)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAvailableEpoching.sizePolicy().hasHeightForWidth())
        self.groupBoxAvailableEpoching.setSizePolicy(sizePolicy)
        self.groupBoxAvailableEpoching.setMaximumSize(QtCore.QSize(400, 90))
        self.groupBoxAvailableEpoching.setObjectName(_fromUtf8("groupBoxAvailableEpoching"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBoxAvailableEpoching)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayoutEpoching = QtGui.QVBoxLayout()
        self.verticalLayoutEpoching.setObjectName(_fromUtf8("verticalLayoutEpoching"))
        self.pushButtonEventlist = QtGui.QPushButton(self.groupBoxAvailableEpoching)
        self.pushButtonEventlist.setObjectName(_fromUtf8("pushButtonEventlist"))
        self.verticalLayoutEpoching.addWidget(self.pushButtonEventlist)
        self.gridLayout_4.addLayout(self.verticalLayoutEpoching, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBoxAvailableEpoching, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabEpoching, _fromUtf8(""))
        self.tabAveraging = QtGui.QWidget()
        self.tabAveraging.setObjectName(_fromUtf8("tabAveraging"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tabAveraging)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.groupBoxAvailableAveraging = QtGui.QGroupBox(self.tabAveraging)
        self.groupBoxAvailableAveraging.setMaximumSize(QtCore.QSize(500, 90))
        self.groupBoxAvailableAveraging.setObjectName(_fromUtf8("groupBoxAvailableAveraging"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBoxAvailableAveraging)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.pushButtonAverage = QtGui.QPushButton(self.groupBoxAvailableAveraging)
        self.pushButtonAverage.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.pushButtonAverage.setObjectName(_fromUtf8("pushButtonAverage"))
        self.gridLayout_11.addWidget(self.pushButtonAverage, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBoxAvailableAveraging, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabAveraging, _fromUtf8(""))
        self.tabTFR = QtGui.QWidget()
        self.tabTFR.setObjectName(_fromUtf8("tabTFR"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tabTFR)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBoxAvailableTFR = QtGui.QGroupBox(self.tabTFR)
        self.groupBoxAvailableTFR.setMaximumSize(QtCore.QSize(500, 180))
        self.groupBoxAvailableTFR.setObjectName(_fromUtf8("groupBoxAvailableTFR"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBoxAvailableTFR)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.pushButtonTFR = QtGui.QPushButton(self.groupBoxAvailableTFR)
        self.pushButtonTFR.setObjectName(_fromUtf8("pushButtonTFR"))
        self.verticalLayout_13.addWidget(self.pushButtonTFR)
        self.pushButtonTFRTopology = QtGui.QPushButton(self.groupBoxAvailableTFR)
        self.pushButtonTFRTopology.setObjectName(_fromUtf8("pushButtonTFRTopology"))
        self.verticalLayout_13.addWidget(self.pushButtonTFRTopology)
        self.gridLayout_6.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBoxAvailableTFR, 0, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem7, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabTFR, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 29))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCreate_experiment = QtGui.QAction(MainWindow)
        self.actionCreate_experiment.setObjectName(_fromUtf8("actionCreate_experiment"))
        self.actionOpen_experiment = QtGui.QAction(MainWindow)
        self.actionOpen_experiment.setObjectName(_fromUtf8("actionOpen_experiment"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionSet_workspace = QtGui.QAction(MainWindow)
        self.actionSet_workspace.setObjectName(_fromUtf8("actionSet_workspace"))
        self.menuFile.addAction(self.actionCreate_experiment)
        self.menuFile.addAction(self.actionOpen_experiment)
        self.menuFile.addAction(self.actionSet_workspace)
        self.menuTools.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.toolBar.addAction(self.actionCreate_experiment)
        self.toolBar.addAction(self.actionOpen_experiment)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.metaBox.setTitle(_translate("MainWindow", "Background", None))
        self.labelExperiment.setText(_translate("MainWindow", "Experiment:", None))
        self.labelExperimentName.setText(_translate("MainWindow", "TextLabel", None))
        self.labelDate.setText(_translate("MainWindow", "Date:", None))
        self.labelDateValue.setText(_translate("MainWindow", "DateValue", None))
        self.labelSubject.setText(_translate("MainWindow", "Subject:", None))
        self.labelSubjectValue.setText(_translate("MainWindow", "TextLabel", None))
        self.labelAuthor.setText(_translate("MainWindow", "Author:", None))
        self.labelAuthorName.setText(_translate("MainWindow", "TextLabel", None))
        self.label.setText(_translate("MainWindow", "Description:", None))
        self.channelsBox.setTitle(_translate("MainWindow", "Channels", None))
        self.labelEEG.setText(_translate("MainWindow", "EEG channels:", None))
        self.labelEEGValue.setText(_translate("MainWindow", "EEG value", None))
        self.labelGradMEG.setText(_translate("MainWindow", "Gradiometers:", None))
        self.labelGradMEGValue.setText(_translate("MainWindow", "Grad. MEG value", None))
        self.labelMagMEG.setText(_translate("MainWindow", "Magnetometers:", None))
        self.labelMagMEGValue.setText(_translate("MainWindow", "Mag. MEG value", None))
        self.labelSamples.setText(_translate("MainWindow", "Sampling frequency:", None))
        self.labelSamplesValue.setText(_translate("MainWindow", "SamplesValue", None))
        self.filtersBox.setTitle(_translate("MainWindow", "Filters", None))
        self.labelLow.setText(_translate("MainWindow", "Low-pass:", None))
        self.labelLowValue.setText(_translate("MainWindow", "Low-pass value", None))
        self.labelHigh.setText(_translate("MainWindow", "High-pass:", None))
        self.labelHighValue.setText(_translate("MainWindow", "High-pass value", None))
        self.triggersBox.setTitle(_translate("MainWindow", "Triggers", None))
        self.pushButtonMNE_Browse_Raw.setText(_translate("MainWindow", "View with MNE_Browse_Raw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRaw), _translate("MainWindow", "Raw", None))
        self.groupBoxAvailablePreprocessing.setTitle(_translate("MainWindow", "Available actions:", None))
        self.pushButtonMaxFilter.setText(_translate("MainWindow", "MaxFilter", None))
        self.pushButtonECG.setText(_translate("MainWindow", "Calculate ECG projections", None))
        self.pushButtonApplyECG.setText(_translate("MainWindow", "Apply ECG projections", None))
        self.pushButtonEOG.setText(_translate("MainWindow", "Calculate EOG projections", None))
        self.pushButtonApplyEOG.setText(_translate("MainWindow", "Apply EOG projections", None))
        self.groupBoxPreprocessingCheckBoxes.setTitle(_translate("MainWindow", "Preprocessing steps completed:", None))
        self.labelECGComputed_2.setText(_translate("MainWindow", "ECG computed", None))
        self.labelEOGApplied_2.setText(_translate("MainWindow", "EOG applied", None))
        self.labelEOGComputed_2.setText(_translate("MainWindow", "EOG computed", None))
        self.labelMaxFilter_2.setText(_translate("MainWindow", "MaxFilter", None))
        self.labelECGApplied_2.setText(_translate("MainWindow", "ECG applied", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPreprocessing), _translate("MainWindow", "Preprocessing", None))
        self.groupBoxAvailableEpoching.setTitle(_translate("MainWindow", "Available actions:", None))
        self.pushButtonEventlist.setText(_translate("MainWindow", "Create an epoch collection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEpoching), _translate("MainWindow", "Epoching", None))
        self.groupBoxAvailableAveraging.setTitle(_translate("MainWindow", "Available actions:", None))
        self.pushButtonAverage.setText(_translate("MainWindow", "Average selected epoch collection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAveraging), _translate("MainWindow", "Averaging", None))
        self.groupBoxAvailableTFR.setTitle(_translate("MainWindow", "Available actions:", None))
        self.pushButtonTFR.setText(_translate("MainWindow", "TFR visualization", None))
        self.pushButtonTFRTopology.setText(_translate("MainWindow", "TFR topology vizualization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTFR), _translate("MainWindow", "TFR", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionCreate_experiment.setText(_translate("MainWindow", "Create new experiment...", None))
        self.actionOpen_experiment.setText(_translate("MainWindow", "Open experiment...", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))
        self.actionSet_workspace.setText(_translate("MainWindow", "Set workspace...", None))

