# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maxFilterDialogNew.ui'
#
# Created: Wed May 15 14:38:17 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(705, 805)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.labelLab = QtGui.QLabel(Dialog)
        self.labelLab.setObjectName(_fromUtf8("labelLab"))
        self.horizontalLayout_10.addWidget(self.labelLab)
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.comboBoxLab = QtGui.QComboBox(Dialog)
        self.comboBoxLab.setObjectName(_fromUtf8("comboBoxLab"))
        self.horizontalLayout_10.addWidget(self.comboBoxLab)
        spacerItem1 = QtGui.QSpacerItem(85, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 687, 709))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(626, 669))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.layoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 7, 595, 714))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidgetMaxFilterSettings = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidgetMaxFilterSettings.setObjectName(_fromUtf8("tabWidgetMaxFilterSettings"))
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setObjectName(_fromUtf8("tabGeneral"))
        self.formLayout_2 = QtGui.QFormLayout(self.tabGeneral)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.groupBoxOrigin = QtGui.QGroupBox(self.tabGeneral)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxOrigin.sizePolicy().hasHeightForWidth())
        self.groupBoxOrigin.setSizePolicy(sizePolicy)
        self.groupBoxOrigin.setObjectName(_fromUtf8("groupBoxOrigin"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBoxOrigin)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame_6 = QtGui.QFrame(self.groupBoxOrigin)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBoxFit = QtGui.QCheckBox(self.frame_6)
        self.checkBoxFit.setObjectName(_fromUtf8("checkBoxFit"))
        self.gridLayout_2.addWidget(self.checkBoxFit, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelX0 = QtGui.QLabel(self.frame_6)
        self.labelX0.setObjectName(_fromUtf8("labelX0"))
        self.horizontalLayout_3.addWidget(self.labelX0)
        self.doubleSpinBoxX0 = QtGui.QDoubleSpinBox(self.frame_6)
        self.doubleSpinBoxX0.setObjectName(_fromUtf8("doubleSpinBoxX0"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxX0)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelY0 = QtGui.QLabel(self.frame_6)
        self.labelY0.setObjectName(_fromUtf8("labelY0"))
        self.horizontalLayout_4.addWidget(self.labelY0)
        self.doubleSpinBoxY0 = QtGui.QDoubleSpinBox(self.frame_6)
        self.doubleSpinBoxY0.setObjectName(_fromUtf8("doubleSpinBoxY0"))
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxY0)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelZ0 = QtGui.QLabel(self.frame_6)
        self.labelZ0.setObjectName(_fromUtf8("labelZ0"))
        self.horizontalLayout.addWidget(self.labelZ0)
        self.doubleSpinBoxZ0 = QtGui.QDoubleSpinBox(self.frame_6)
        self.doubleSpinBoxZ0.setProperty("value", 40.0)
        self.doubleSpinBoxZ0.setObjectName(_fromUtf8("doubleSpinBoxZ0"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxZ0)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBoxOrigin)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.LabelRole, self.horizontalLayout_7)
        self.groupBoxDataSkips = QtGui.QGroupBox(self.tabGeneral)
        self.groupBoxDataSkips.setObjectName(_fromUtf8("groupBoxDataSkips"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBoxDataSkips)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame_5 = QtGui.QFrame(self.groupBoxDataSkips)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.checkBoxSkip_1 = QtGui.QCheckBox(self.frame_5)
        self.checkBoxSkip_1.setObjectName(_fromUtf8("checkBoxSkip_1"))
        self.gridLayout_12.addWidget(self.checkBoxSkip_1, 1, 0, 1, 1)
        self.checkBoxSkip_2 = QtGui.QCheckBox(self.frame_5)
        self.checkBoxSkip_2.setObjectName(_fromUtf8("checkBoxSkip_2"))
        self.gridLayout_12.addWidget(self.checkBoxSkip_2, 2, 0, 1, 1)
        self.spinBoxSkipEnd_3 = QtGui.QSpinBox(self.frame_5)
        self.spinBoxSkipEnd_3.setEnabled(False)
        self.spinBoxSkipEnd_3.setMaximum(100000)
        self.spinBoxSkipEnd_3.setObjectName(_fromUtf8("spinBoxSkipEnd_3"))
        self.gridLayout_12.addWidget(self.spinBoxSkipEnd_3, 3, 2, 1, 1)
        self.spinBoxSkipStart_3 = QtGui.QSpinBox(self.frame_5)
        self.spinBoxSkipStart_3.setEnabled(False)
        self.spinBoxSkipStart_3.setMaximum(100000)
        self.spinBoxSkipStart_3.setObjectName(_fromUtf8("spinBoxSkipStart_3"))
        self.gridLayout_12.addWidget(self.spinBoxSkipStart_3, 3, 1, 1, 1)
        self.checkBoxSkip_3 = QtGui.QCheckBox(self.frame_5)
        self.checkBoxSkip_3.setObjectName(_fromUtf8("checkBoxSkip_3"))
        self.gridLayout_12.addWidget(self.checkBoxSkip_3, 3, 0, 1, 1)
        self.spinBoxSkipEnd_1 = QtGui.QSpinBox(self.frame_5)
        self.spinBoxSkipEnd_1.setEnabled(False)
        self.spinBoxSkipEnd_1.setMaximum(100000)
        self.spinBoxSkipEnd_1.setObjectName(_fromUtf8("spinBoxSkipEnd_1"))
        self.gridLayout_12.addWidget(self.spinBoxSkipEnd_1, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_12.addWidget(self.label_5, 0, 1, 1, 1)
        self.spinBoxSkipStart_2 = QtGui.QSpinBox(self.frame_5)
        self.spinBoxSkipStart_2.setEnabled(False)
        self.spinBoxSkipStart_2.setMaximum(100000)
        self.spinBoxSkipStart_2.setObjectName(_fromUtf8("spinBoxSkipStart_2"))
        self.gridLayout_12.addWidget(self.spinBoxSkipStart_2, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem2, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_12.addWidget(self.label_6, 0, 2, 1, 1)
        self.spinBoxSkipStart_1 = QtGui.QSpinBox(self.frame_5)
        self.spinBoxSkipStart_1.setEnabled(False)
        self.spinBoxSkipStart_1.setMaximum(100000)
        self.spinBoxSkipStart_1.setObjectName(_fromUtf8("spinBoxSkipStart_1"))
        self.gridLayout_12.addWidget(self.spinBoxSkipStart_1, 1, 1, 1, 1)
        self.spinBoxSkipEnd_2 = QtGui.QSpinBox(self.frame_5)
        self.spinBoxSkipEnd_2.setEnabled(False)
        self.spinBoxSkipEnd_2.setMaximum(100000)
        self.spinBoxSkipEnd_2.setObjectName(_fromUtf8("spinBoxSkipEnd_2"))
        self.gridLayout_12.addWidget(self.spinBoxSkipEnd_2, 2, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.groupBoxDataSkips)
        self.groupBox = QtGui.QGroupBox(self.tabGeneral)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.labelOrderIn = QtGui.QLabel(self.groupBox)
        self.labelOrderIn.setObjectName(_fromUtf8("labelOrderIn"))
        self.horizontalLayout_8.addWidget(self.labelOrderIn)
        self.spinBoxOrderIn = QtGui.QSpinBox(self.groupBox)
        self.spinBoxOrderIn.setMinimum(5)
        self.spinBoxOrderIn.setMaximum(11)
        self.spinBoxOrderIn.setProperty("value", 8)
        self.spinBoxOrderIn.setObjectName(_fromUtf8("spinBoxOrderIn"))
        self.horizontalLayout_8.addWidget(self.spinBoxOrderIn)
        self.labelOrderOut = QtGui.QLabel(self.groupBox)
        self.labelOrderOut.setObjectName(_fromUtf8("labelOrderOut"))
        self.horizontalLayout_8.addWidget(self.labelOrderOut)
        self.spinBoxOrderOut = QtGui.QSpinBox(self.groupBox)
        self.spinBoxOrderOut.setMinimum(1)
        self.spinBoxOrderOut.setMaximum(5)
        self.spinBoxOrderOut.setProperty("value", 3)
        self.spinBoxOrderOut.setObjectName(_fromUtf8("spinBoxOrderOut"))
        self.horizontalLayout_8.addWidget(self.spinBoxOrderOut)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.groupBox)
        self.groupBoxBadChannel = QtGui.QGroupBox(self.tabGeneral)
        self.groupBoxBadChannel.setObjectName(_fromUtf8("groupBoxBadChannel"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBoxBadChannel)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.frame_3 = QtGui.QFrame(self.groupBoxBadChannel)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.labelBadLimit = QtGui.QLabel(self.frame_3)
        self.labelBadLimit.setObjectName(_fromUtf8("labelBadLimit"))
        self.horizontalLayout_6.addWidget(self.labelBadLimit)
        self.doubleSpinBoxBadLimit = QtGui.QDoubleSpinBox(self.frame_3)
        self.doubleSpinBoxBadLimit.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxBadLimit.setProperty("value", 7.0)
        self.doubleSpinBoxBadLimit.setObjectName(_fromUtf8("doubleSpinBoxBadLimit"))
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxBadLimit)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelBad = QtGui.QLabel(self.frame_3)
        self.labelBad.setObjectName(_fromUtf8("labelBad"))
        self.horizontalLayout_5.addWidget(self.labelBad)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.lineEditBad = QtGui.QLineEdit(self.frame_3)
        self.lineEditBad.setEnabled(False)
        self.lineEditBad.setObjectName(_fromUtf8("lineEditBad"))
        self.horizontalLayout_5.addWidget(self.lineEditBad)
        self.gridLayout_7.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.checkBoxAutobad = QtGui.QCheckBox(self.frame_3)
        self.checkBoxAutobad.setChecked(True)
        self.checkBoxAutobad.setObjectName(_fromUtf8("checkBoxAutobad"))
        self.gridLayout_7.addWidget(self.checkBoxAutobad, 3, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_3, 0, 1, 1, 1)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.groupBoxBadChannel)
        self.tabWidgetMaxFilterSettings.addTab(self.tabGeneral, _fromUtf8(""))
        self.tabTSSS = QtGui.QWidget()
        self.tabTSSS.setObjectName(_fromUtf8("tabTSSS"))
        self.checkBoxtSSS = QtGui.QCheckBox(self.tabTSSS)
        self.checkBoxtSSS.setEnabled(True)
        self.checkBoxtSSS.setGeometry(QtCore.QRect(10, 10, 351, 26))
        self.checkBoxtSSS.setChecked(False)
        self.checkBoxtSSS.setObjectName(_fromUtf8("checkBoxtSSS"))
        self.frame = QtGui.QFrame(self.tabTSSS)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(20, 40, 361, 91))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayoutWidget = QtGui.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 71))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelDataBufferLength = QtGui.QLabel(self.formLayoutWidget)
        self.labelDataBufferLength.setObjectName(_fromUtf8("labelDataBufferLength"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelDataBufferLength)
        self.labelSubspaceCorrelationLimit = QtGui.QLabel(self.formLayoutWidget)
        self.labelSubspaceCorrelationLimit.setObjectName(_fromUtf8("labelSubspaceCorrelationLimit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelSubspaceCorrelationLimit)
        self.spinBoxBufferLength = QtGui.QSpinBox(self.formLayoutWidget)
        self.spinBoxBufferLength.setMaximum(120)
        self.spinBoxBufferLength.setProperty("value", 20)
        self.spinBoxBufferLength.setObjectName(_fromUtf8("spinBoxBufferLength"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBoxBufferLength)
        self.doubleSpinBoxCorr = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBoxCorr.setMaximum(1.0)
        self.doubleSpinBoxCorr.setSingleStep(0.01)
        self.doubleSpinBoxCorr.setProperty("value", 0.98)
        self.doubleSpinBoxCorr.setObjectName(_fromUtf8("doubleSpinBoxCorr"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxCorr)
        self.tabWidgetMaxFilterSettings.addTab(self.tabTSSS, _fromUtf8(""))
        self.tabMC = QtGui.QWidget()
        self.tabMC.setObjectName(_fromUtf8("tabMC"))
        self.checkBoxMaxMove = QtGui.QCheckBox(self.tabMC)
        self.checkBoxMaxMove.setEnabled(True)
        self.checkBoxMaxMove.setGeometry(QtCore.QRect(10, 49, 300, 26))
        self.checkBoxMaxMove.setChecked(False)
        self.checkBoxMaxMove.setObjectName(_fromUtf8("checkBoxMaxMove"))
        self.spinBoxLineFreq = QtGui.QSpinBox(self.tabMC)
        self.spinBoxLineFreq.setGeometry(QtCore.QRect(117, 11, 68, 31))
        self.spinBoxLineFreq.setMinimum(50)
        self.spinBoxLineFreq.setMaximum(60)
        self.spinBoxLineFreq.setSingleStep(10)
        self.spinBoxLineFreq.setObjectName(_fromUtf8("spinBoxLineFreq"))
        self.labelLineFreq = QtGui.QLabel(self.tabMC)
        self.labelLineFreq.setGeometry(QtCore.QRect(11, 16, 100, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLineFreq.sizePolicy().hasHeightForWidth())
        self.labelLineFreq.setSizePolicy(sizePolicy)
        self.labelLineFreq.setObjectName(_fromUtf8("labelLineFreq"))
        self.tabWidgetMaxFilterSettings.addTab(self.tabMC, _fromUtf8(""))
        self.tabHP = QtGui.QWidget()
        self.tabHP.setObjectName(_fromUtf8("tabHP"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tabHP)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBoxStorePosition = QtGui.QCheckBox(self.tabHP)
        self.checkBoxStorePosition.setObjectName(_fromUtf8("checkBoxStorePosition"))
        self.verticalLayout.addWidget(self.checkBoxStorePosition)
        self.checkBoxTransform = QtGui.QCheckBox(self.tabHP)
        self.checkBoxTransform.setChecked(False)
        self.checkBoxTransform.setObjectName(_fromUtf8("checkBoxTransform"))
        self.verticalLayout.addWidget(self.checkBoxTransform)
        self.frame_2 = QtGui.QFrame(self.tabHP)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.layoutWidget1 = QtGui.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 311, 139))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radioButtonPositionDefault = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButtonPositionDefault.setEnabled(False)
        self.radioButtonPositionDefault.setChecked(False)
        self.radioButtonPositionDefault.setAutoExclusive(True)
        self.radioButtonPositionDefault.setObjectName(_fromUtf8("radioButtonPositionDefault"))
        self.buttonGroupMaxMove = QtGui.QButtonGroup(Dialog)
        self.buttonGroupMaxMove.setObjectName(_fromUtf8("buttonGroupMaxMove"))
        self.buttonGroupMaxMove.addButton(self.radioButtonPositionDefault)
        self.verticalLayout_4.addWidget(self.radioButtonPositionDefault)
        self.radioButtonPositionFile = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButtonPositionFile.setEnabled(False)
        self.radioButtonPositionFile.setChecked(False)
        self.radioButtonPositionFile.setAutoExclusive(True)
        self.radioButtonPositionFile.setObjectName(_fromUtf8("radioButtonPositionFile"))
        self.buttonGroupMaxMove.addButton(self.radioButtonPositionFile)
        self.verticalLayout_4.addWidget(self.radioButtonPositionFile)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lineEditFile = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditFile.setEnabled(False)
        self.lineEditFile.setInputMask(_fromUtf8(""))
        self.lineEditFile.setObjectName(_fromUtf8("lineEditFile"))
        self.horizontalLayout_9.addWidget(self.lineEditFile)
        self.pushButtonBrowsePositionFile = QtGui.QPushButton(self.layoutWidget1)
        self.pushButtonBrowsePositionFile.setEnabled(False)
        self.pushButtonBrowsePositionFile.setObjectName(_fromUtf8("pushButtonBrowsePositionFile"))
        self.horizontalLayout_9.addWidget(self.pushButtonBrowsePositionFile)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.radioButtonPositionAverage = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButtonPositionAverage.setEnabled(False)
        self.radioButtonPositionAverage.setChecked(False)
        self.radioButtonPositionAverage.setAutoExclusive(True)
        self.radioButtonPositionAverage.setObjectName(_fromUtf8("radioButtonPositionAverage"))
        self.buttonGroupMaxMove.addButton(self.radioButtonPositionAverage)
        self.verticalLayout_4.addWidget(self.radioButtonPositionAverage)
        self.verticalLayout.addWidget(self.frame_2)
        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidgetMaxFilterSettings.addTab(self.tabHP, _fromUtf8(""))
        self.tabCustom = QtGui.QWidget()
        self.tabCustom.setObjectName(_fromUtf8("tabCustom"))
        self.layoutWidget2 = QtGui.QWidget(self.tabCustom)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 491, 211))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelCustom = QtGui.QLabel(self.layoutWidget2)
        self.labelCustom.setObjectName(_fromUtf8("labelCustom"))
        self.verticalLayout_3.addWidget(self.labelCustom)
        self.textEditCustom = QtGui.QTextEdit(self.layoutWidget2)
        self.textEditCustom.setObjectName(_fromUtf8("textEditCustom"))
        self.verticalLayout_3.addWidget(self.textEditCustom)
        self.label = QtGui.QLabel(self.tabCustom)
        self.label.setGeometry(QtCore.QRect(20, 250, 491, 51))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidgetMaxFilterSettings.addTab(self.tabCustom, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidgetMaxFilterSettings)
        self.labelComputeMaxFilter = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelComputeMaxFilter.setFont(font)
        self.labelComputeMaxFilter.setScaledContents(False)
        self.labelComputeMaxFilter.setObjectName(_fromUtf8("labelComputeMaxFilter"))
        self.verticalLayout_2.addWidget(self.labelComputeMaxFilter)
        self.progressBarComputeMaxFilter = QtGui.QProgressBar(self.layoutWidget)
        self.progressBarComputeMaxFilter.setMinimum(0)
        self.progressBarComputeMaxFilter.setMaximum(0)
        self.progressBarComputeMaxFilter.setProperty("value", 0)
        self.progressBarComputeMaxFilter.setTextVisible(True)
        self.progressBarComputeMaxFilter.setObjectName(_fromUtf8("progressBarComputeMaxFilter"))
        self.verticalLayout_2.addWidget(self.progressBarComputeMaxFilter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem4)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_15.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_15.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.retranslateUi(Dialog)
        self.tabWidgetMaxFilterSettings.setCurrentIndex(0)
        QtCore.QObject.connect(self.checkBoxAutobad, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.labelBad.setDisabled)
        QtCore.QObject.connect(self.checkBoxSkip_1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxSkipStart_1.setEnabled)
        QtCore.QObject.connect(self.checkBoxSkip_3, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxSkipStart_3.setEnabled)
        QtCore.QObject.connect(self.checkBoxSkip_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxSkipEnd_2.setEnabled)
        QtCore.QObject.connect(self.checkBoxSkip_1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxSkipEnd_1.setEnabled)
        QtCore.QObject.connect(self.checkBoxSkip_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxSkipStart_2.setEnabled)
        QtCore.QObject.connect(self.checkBoxFit, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxX0.setDisabled)
        QtCore.QObject.connect(self.checkBoxFit, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxY0.setDisabled)
        QtCore.QObject.connect(self.checkBoxFit, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxZ0.setDisabled)
        QtCore.QObject.connect(self.checkBoxAutobad, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditBad.setDisabled)
        QtCore.QObject.connect(self.checkBoxSkip_3, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxSkipEnd_3.setEnabled)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.checkBoxtSSS, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame.setEnabled)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.checkBoxTransform, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.radioButtonPositionDefault.setEnabled)
        QtCore.QObject.connect(self.checkBoxTransform, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.radioButtonPositionFile.setEnabled)
        QtCore.QObject.connect(self.checkBoxTransform, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.radioButtonPositionAverage.setEnabled)
        QtCore.QObject.connect(self.radioButtonPositionFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEditFile.setEnabled)
        QtCore.QObject.connect(self.radioButtonPositionFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.pushButtonBrowsePositionFile.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.checkBoxFit, self.doubleSpinBoxX0)
        Dialog.setTabOrder(self.doubleSpinBoxX0, self.doubleSpinBoxY0)
        Dialog.setTabOrder(self.doubleSpinBoxY0, self.doubleSpinBoxZ0)
        Dialog.setTabOrder(self.doubleSpinBoxZ0, self.doubleSpinBoxBadLimit)
        Dialog.setTabOrder(self.doubleSpinBoxBadLimit, self.spinBoxOrderOut)
        Dialog.setTabOrder(self.spinBoxOrderOut, self.spinBoxOrderIn)
        Dialog.setTabOrder(self.spinBoxOrderIn, self.checkBoxAutobad)
        Dialog.setTabOrder(self.checkBoxAutobad, self.spinBoxBufferLength)
        Dialog.setTabOrder(self.spinBoxBufferLength, self.doubleSpinBoxCorr)
        Dialog.setTabOrder(self.doubleSpinBoxCorr, self.checkBoxMaxMove)
        Dialog.setTabOrder(self.checkBoxMaxMove, self.textEditCustom)
        Dialog.setTabOrder(self.textEditCustom, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.checkBoxSkip_1)
        Dialog.setTabOrder(self.checkBoxSkip_1, self.checkBoxSkip_2)
        Dialog.setTabOrder(self.checkBoxSkip_2, self.spinBoxSkipEnd_3)
        Dialog.setTabOrder(self.spinBoxSkipEnd_3, self.spinBoxSkipStart_3)
        Dialog.setTabOrder(self.spinBoxSkipStart_3, self.checkBoxSkip_3)
        Dialog.setTabOrder(self.checkBoxSkip_3, self.spinBoxSkipEnd_1)
        Dialog.setTabOrder(self.spinBoxSkipEnd_1, self.spinBoxSkipStart_2)
        Dialog.setTabOrder(self.spinBoxSkipStart_2, self.spinBoxSkipStart_1)
        Dialog.setTabOrder(self.spinBoxSkipStart_1, self.spinBoxSkipEnd_2)
        Dialog.setTabOrder(self.spinBoxSkipEnd_2, self.checkBoxtSSS)
        Dialog.setTabOrder(self.checkBoxtSSS, self.spinBoxLineFreq)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "MaxFilter Settings", None))
        self.labelLab.setText(_translate("Dialog", "Choose the laboratory whose calibration files are to be used:", None))
        self.groupBoxOrigin.setTitle(_translate("Dialog", "Origin", None))
        self.checkBoxFit.setText(_translate("Dialog", "Fit to isotrak points", None))
        self.labelX0.setText(_translate("Dialog", "x0", None))
        self.doubleSpinBoxX0.setSuffix(_translate("Dialog", " mm", None))
        self.labelY0.setText(_translate("Dialog", "y0", None))
        self.doubleSpinBoxY0.setSuffix(_translate("Dialog", " mm", None))
        self.labelZ0.setText(_translate("Dialog", "z0", None))
        self.doubleSpinBoxZ0.setSuffix(_translate("Dialog", " mm", None))
        self.groupBoxDataSkips.setTitle(_translate("Dialog", "Data skips", None))
        self.checkBoxSkip_1.setText(_translate("Dialog", "S1", None))
        self.checkBoxSkip_2.setText(_translate("Dialog", "S2", None))
        self.spinBoxSkipEnd_3.setSuffix(_translate("Dialog", " s", None))
        self.spinBoxSkipStart_3.setSuffix(_translate("Dialog", " s", None))
        self.checkBoxSkip_3.setText(_translate("Dialog", "S3", None))
        self.spinBoxSkipEnd_1.setSuffix(_translate("Dialog", " s", None))
        self.label_5.setText(_translate("Dialog", "Start", None))
        self.spinBoxSkipStart_2.setSuffix(_translate("Dialog", " s", None))
        self.label_6.setText(_translate("Dialog", "End", None))
        self.spinBoxSkipStart_1.setSuffix(_translate("Dialog", " s", None))
        self.spinBoxSkipEnd_2.setSuffix(_translate("Dialog", " s", None))
        self.groupBox.setTitle(_translate("Dialog", "Set expansion order", None))
        self.labelOrderIn.setText(_translate("Dialog", "Order in:", None))
        self.labelOrderOut.setText(_translate("Dialog", "Order out:", None))
        self.groupBoxBadChannel.setTitle(_translate("Dialog", "Bad channel selection", None))
        self.labelBadLimit.setText(_translate("Dialog", "Threshold for bad channel detection:", None))
        self.labelBad.setText(_translate("Dialog", "Bad channels (e.g. 0323 1042 2631) :", None))
        self.checkBoxAutobad.setText(_translate("Dialog", "Autobad", None))
        self.tabWidgetMaxFilterSettings.setTabText(self.tabWidgetMaxFilterSettings.indexOf(self.tabGeneral), _translate("Dialog", "General and SSS", None))
        self.checkBoxtSSS.setText(_translate("Dialog", "tSSS filtering enabled", None))
        self.labelDataBufferLength.setText(_translate("Dialog", "Data buffer length:", None))
        self.labelSubspaceCorrelationLimit.setText(_translate("Dialog", "Subspace correlation limit:", None))
        self.spinBoxBufferLength.setSuffix(_translate("Dialog", " s", None))
        self.tabWidgetMaxFilterSettings.setTabText(self.tabWidgetMaxFilterSettings.indexOf(self.tabTSSS), _translate("Dialog", "tSSS", None))
        self.checkBoxMaxMove.setText(_translate("Dialog", "Motion compensation (MaxMove) enabled", None))
        self.spinBoxLineFreq.setSuffix(_translate("Dialog", " Hz", None))
        self.labelLineFreq.setText(_translate("Dialog", "Line frequency:", None))
        self.tabWidgetMaxFilterSettings.setTabText(self.tabWidgetMaxFilterSettings.indexOf(self.tabMC), _translate("Dialog", "Motion compensation", None))
        self.checkBoxStorePosition.setText(_translate("Dialog", "Store head position data in an ASCII file", None))
        self.checkBoxTransform.setText(_translate("Dialog", "Transform head position", None))
        self.radioButtonPositionDefault.setText(_translate("Dialog", "Transform data into default head position", None))
        self.radioButtonPositionFile.setText(_translate("Dialog", "Transform data to head position in a file:", None))
        self.pushButtonBrowsePositionFile.setText(_translate("Dialog", "Browse...", None))
        self.radioButtonPositionAverage.setText(_translate("Dialog", "Transform data into averaged head position", None))
        self.tabWidgetMaxFilterSettings.setTabText(self.tabWidgetMaxFilterSettings.indexOf(self.tabHP), _translate("Dialog", "Head position", None))
        self.labelCustom.setText(_translate("Dialog", "Custom parameters:", None))
        self.label.setText(_translate("Dialog", "Fill field with custom commands separated with a single space, for example: -history -force -def -maint", None))
        self.tabWidgetMaxFilterSettings.setTabText(self.tabWidgetMaxFilterSettings.indexOf(self.tabCustom), _translate("Dialog", "Custom", None))
        self.labelComputeMaxFilter.setText(_translate("Dialog", "Computing MaxFilter (this may take several minutes) ...", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))
        self.pushButton.setText(_translate("Dialog", "Compute", None))

