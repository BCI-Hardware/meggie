# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createEpochsFromEventsDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateEpochsFromEventsDialog(object):
    def setupUi(self, CreateEpochsFromEventsDialog):
        CreateEpochsFromEventsDialog.setObjectName("CreateEpochsFromEventsDialog")
        CreateEpochsFromEventsDialog.setWindowModality(QtCore.Qt.WindowModal)
        CreateEpochsFromEventsDialog.resize(777, 783)
        self.gridLayout = QtWidgets.QGridLayout(CreateEpochsFromEventsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(CreateEpochsFromEventsDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_10.addWidget(self.pushButtonCancel)
        self.pushButtonComputeBatch = QtWidgets.QPushButton(CreateEpochsFromEventsDialog)
        self.pushButtonComputeBatch.setObjectName("pushButtonComputeBatch")
        self.horizontalLayout_10.addWidget(self.pushButtonComputeBatch)
        self.pushButtonCompute = QtWidgets.QPushButton(CreateEpochsFromEventsDialog)
        self.pushButtonCompute.setObjectName("pushButtonCompute")
        self.horizontalLayout_10.addWidget(self.pushButtonCompute)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(CreateEpochsFromEventsDialog)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 734))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBoxEventsList = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxEventsList.setObjectName("groupBoxEventsList")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxEventsList)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidgetEvents = QtWidgets.QListWidget(self.groupBoxEventsList)
        self.listWidgetEvents.setObjectName("listWidgetEvents")
        self.gridLayout_3.addWidget(self.listWidgetEvents, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBoxEventsList, 1, 1, 2, 1)
        self.groupBoxRejection = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxRejection.setObjectName("groupBoxRejection")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxRejection)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkBoxGrad = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxGrad.setChecked(True)
        self.checkBoxGrad.setObjectName("checkBoxGrad")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBoxGrad)
        self.doubleSpinBoxGradReject = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxGradReject.setPrefix("")
        self.doubleSpinBoxGradReject.setMinimum(-1.0)
        self.doubleSpinBoxGradReject.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject.setSingleStep(100.0)
        self.doubleSpinBoxGradReject.setProperty("value", 3000.0)
        self.doubleSpinBoxGradReject.setObjectName("doubleSpinBoxGradReject")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxGradReject)
        self.checkBoxMag = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxMag.setChecked(True)
        self.checkBoxMag.setObjectName("checkBoxMag")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxMag)
        self.doubleSpinBoxMagReject = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxMagReject.setMinimum(-1.0)
        self.doubleSpinBoxMagReject.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject.setSingleStep(100.0)
        self.doubleSpinBoxMagReject.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject.setObjectName("doubleSpinBoxMagReject")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxMagReject)
        self.checkBoxEeg = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxEeg.setChecked(False)
        self.checkBoxEeg.setObjectName("checkBoxEeg")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBoxEeg)
        self.doubleSpinBoxEEGReject = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxEEGReject.setEnabled(False)
        self.doubleSpinBoxEEGReject.setMinimum(-1.0)
        self.doubleSpinBoxEEGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject.setProperty("value", 70.0)
        self.doubleSpinBoxEEGReject.setObjectName("doubleSpinBoxEEGReject")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxEEGReject)
        self.gridLayout_7.addWidget(self.groupBoxRejection, 0, 1, 1, 1)
        self.groupBoxEpochs = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxEpochs.setObjectName("groupBoxEpochs")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxEpochs)
        self.formLayout.setObjectName("formLayout")
        self.labelCollectionName = QtWidgets.QLabel(self.groupBoxEpochs)
        self.labelCollectionName.setObjectName("labelCollectionName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelCollectionName)
        self.lineEditCollectionName = QtWidgets.QLineEdit(self.groupBoxEpochs)
        self.lineEditCollectionName.setObjectName("lineEditCollectionName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCollectionName)
        self.labelTmin = QtWidgets.QLabel(self.groupBoxEpochs)
        self.labelTmin.setObjectName("labelTmin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTmin)
        self.doubleSpinBoxTmin = QtWidgets.QDoubleSpinBox(self.groupBoxEpochs)
        self.doubleSpinBoxTmin.setDecimals(3)
        self.doubleSpinBoxTmin.setMinimum(-10.0)
        self.doubleSpinBoxTmin.setSingleStep(0.1)
        self.doubleSpinBoxTmin.setProperty("value", -0.2)
        self.doubleSpinBoxTmin.setObjectName("doubleSpinBoxTmin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxTmin)
        self.labelTmax = QtWidgets.QLabel(self.groupBoxEpochs)
        self.labelTmax.setObjectName("labelTmax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelTmax)
        self.doubleSpinBoxTmax = QtWidgets.QDoubleSpinBox(self.groupBoxEpochs)
        self.doubleSpinBoxTmax.setDecimals(3)
        self.doubleSpinBoxTmax.setMaximum(9.9)
        self.doubleSpinBoxTmax.setSingleStep(0.1)
        self.doubleSpinBoxTmax.setProperty("value", 0.5)
        self.doubleSpinBoxTmax.setObjectName("doubleSpinBoxTmax")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxTmax)
        self.labelBaselineStart = QtWidgets.QLabel(self.groupBoxEpochs)
        self.labelBaselineStart.setObjectName("labelBaselineStart")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelBaselineStart)
        self.doubleSpinBoxBaselineStart = QtWidgets.QDoubleSpinBox(self.groupBoxEpochs)
        self.doubleSpinBoxBaselineStart.setDecimals(3)
        self.doubleSpinBoxBaselineStart.setMinimum(-10.0)
        self.doubleSpinBoxBaselineStart.setProperty("value", -0.2)
        self.doubleSpinBoxBaselineStart.setObjectName("doubleSpinBoxBaselineStart")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxBaselineStart)
        self.labelBaselineEnd = QtWidgets.QLabel(self.groupBoxEpochs)
        self.labelBaselineEnd.setObjectName("labelBaselineEnd")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelBaselineEnd)
        self.doubleSpinBoxBaselineEnd = QtWidgets.QDoubleSpinBox(self.groupBoxEpochs)
        self.doubleSpinBoxBaselineEnd.setDecimals(3)
        self.doubleSpinBoxBaselineEnd.setMinimum(-10.0)
        self.doubleSpinBoxBaselineEnd.setProperty("value", 0.0)
        self.doubleSpinBoxBaselineEnd.setObjectName("doubleSpinBoxBaselineEnd")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBoxBaselineEnd)
        self.gridLayout_7.addWidget(self.groupBoxEpochs, 0, 0, 1, 1)
        self.groupBoxBatching = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxBatching.setObjectName("groupBoxBatching")
        self.gridLayoutBatching = QtWidgets.QGridLayout(self.groupBoxBatching)
        self.gridLayoutBatching.setObjectName("gridLayoutBatching")
        self.batchingWidgetPlaceholder = QtWidgets.QWidget(self.groupBoxBatching)
        self.batchingWidgetPlaceholder.setMinimumSize(QtCore.QSize(300, 300))
        self.batchingWidgetPlaceholder.setObjectName("batchingWidgetPlaceholder")
        self.gridLayoutBatching.addWidget(self.batchingWidgetPlaceholder, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBoxBatching, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 4, 0, 1, 1)
        self.groupBoxEvent = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxEvent.setObjectName("groupBoxEvent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxEvent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelMask = QtWidgets.QLabel(self.groupBoxEvent)
        self.labelMask.setObjectName("labelMask")
        self.gridLayout_2.addWidget(self.labelMask, 1, 0, 1, 1)
        self.labelEventID = QtWidgets.QLabel(self.groupBoxEvent)
        self.labelEventID.setObjectName("labelEventID")
        self.gridLayout_2.addWidget(self.labelEventID, 0, 0, 1, 1)
        self.spinBoxMask = QtWidgets.QSpinBox(self.groupBoxEvent)
        self.spinBoxMask.setMaximum(9999999)
        self.spinBoxMask.setObjectName("spinBoxMask")
        self.gridLayout_2.addWidget(self.spinBoxMask, 1, 1, 1, 1)
        self.spinBoxEventID = QtWidgets.QSpinBox(self.groupBoxEvent)
        self.spinBoxEventID.setMinimum(0)
        self.spinBoxEventID.setMaximum(9999999)
        self.spinBoxEventID.setObjectName("spinBoxEventID")
        self.gridLayout_2.addWidget(self.spinBoxEventID, 0, 1, 1, 1)
        self.pushButtonEdit = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.gridLayout_2.addWidget(self.pushButtonEdit, 0, 2, 1, 1)
        self.pushButtonHelp = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonHelp.setObjectName("pushButtonHelp")
        self.gridLayout_2.addWidget(self.pushButtonHelp, 1, 2, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout_2.addWidget(self.pushButtonAdd, 3, 0, 1, 3)
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout_2.addWidget(self.pushButtonClear, 4, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBoxEvent, 1, 0, 2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(CreateEpochsFromEventsDialog)
        self.pushButtonCompute.clicked.connect(CreateEpochsFromEventsDialog.accept)
        self.pushButtonCancel.clicked.connect(CreateEpochsFromEventsDialog.reject)
        self.checkBoxGrad.toggled['bool'].connect(self.doubleSpinBoxGradReject.setEnabled)
        self.checkBoxMag.toggled['bool'].connect(self.doubleSpinBoxMagReject.setEnabled)
        self.checkBoxEeg.toggled['bool'].connect(self.doubleSpinBoxEEGReject.setEnabled)
        self.pushButtonComputeBatch.clicked.connect(CreateEpochsFromEventsDialog.acceptBatch)
        QtCore.QMetaObject.connectSlotsByName(CreateEpochsFromEventsDialog)
        CreateEpochsFromEventsDialog.setTabOrder(self.scrollArea, self.pushButtonCompute)

    def retranslateUi(self, CreateEpochsFromEventsDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateEpochsFromEventsDialog.setWindowTitle(_translate("CreateEpochsFromEventsDialog", "Create epochs"))
        self.pushButtonCancel.setText(_translate("CreateEpochsFromEventsDialog", "Cancel"))
        self.pushButtonComputeBatch.setText(_translate("CreateEpochsFromEventsDialog", "Batch"))
        self.pushButtonCompute.setText(_translate("CreateEpochsFromEventsDialog", "Apply"))
        self.groupBoxEventsList.setTitle(_translate("CreateEpochsFromEventsDialog", "List of given <event ID>, <event name>"))
        self.groupBoxRejection.setTitle(_translate("CreateEpochsFromEventsDialog", "Channel types to include and their rejection limits"))
        self.checkBoxGrad.setToolTip(_translate("CreateEpochsFromEventsDialog", "Include or exclude grad channels"))
        self.checkBoxGrad.setText(_translate("CreateEpochsFromEventsDialog", "Grad"))
        self.doubleSpinBoxGradReject.setSuffix(_translate("CreateEpochsFromEventsDialog", " fT/cm"))
        self.checkBoxMag.setToolTip(_translate("CreateEpochsFromEventsDialog", "Include or exclude mag channels"))
        self.checkBoxMag.setText(_translate("CreateEpochsFromEventsDialog", "Mag"))
        self.doubleSpinBoxMagReject.setSuffix(_translate("CreateEpochsFromEventsDialog", " fT"))
        self.checkBoxEeg.setToolTip(_translate("CreateEpochsFromEventsDialog", "Include or exclude eeg channels"))
        self.checkBoxEeg.setText(_translate("CreateEpochsFromEventsDialog", "EEG"))
        self.doubleSpinBoxEEGReject.setSuffix(_translate("CreateEpochsFromEventsDialog", " uV"))
        self.groupBoxEpochs.setTitle(_translate("CreateEpochsFromEventsDialog", "Epoch collection"))
        self.labelCollectionName.setText(_translate("CreateEpochsFromEventsDialog", "Collection name:"))
        self.lineEditCollectionName.setText(_translate("CreateEpochsFromEventsDialog", "Epochs"))
        self.labelTmin.setText(_translate("CreateEpochsFromEventsDialog", "Start time:"))
        self.doubleSpinBoxTmin.setSuffix(_translate("CreateEpochsFromEventsDialog", " s"))
        self.labelTmax.setText(_translate("CreateEpochsFromEventsDialog", "End time:"))
        self.doubleSpinBoxTmax.setSuffix(_translate("CreateEpochsFromEventsDialog", " s"))
        self.labelBaselineStart.setText(_translate("CreateEpochsFromEventsDialog", "Baseline start:"))
        self.doubleSpinBoxBaselineStart.setSuffix(_translate("CreateEpochsFromEventsDialog", "s"))
        self.labelBaselineEnd.setText(_translate("CreateEpochsFromEventsDialog", "Baseline end:"))
        self.doubleSpinBoxBaselineEnd.setSuffix(_translate("CreateEpochsFromEventsDialog", "s"))
        self.groupBoxBatching.setTitle(_translate("CreateEpochsFromEventsDialog", "Batching"))
        self.groupBoxEvent.setTitle(_translate("CreateEpochsFromEventsDialog", "Select events to include in epoch collection"))
        self.labelMask.setText(_translate("CreateEpochsFromEventsDialog", "Mask:"))
        self.labelEventID.setText(_translate("CreateEpochsFromEventsDialog", "Event ID:"))
        self.pushButtonEdit.setText(_translate("CreateEpochsFromEventsDialog", "Edit..."))
        self.pushButtonHelp.setText(_translate("CreateEpochsFromEventsDialog", "Help..."))
        self.pushButtonAdd.setText(_translate("CreateEpochsFromEventsDialog", "Add to list >>"))
        self.pushButtonClear.setText(_translate("CreateEpochsFromEventsDialog", "Clear list <<"))

