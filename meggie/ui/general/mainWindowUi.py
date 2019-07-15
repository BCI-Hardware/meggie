# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1521, 1014)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 400))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(600, 600))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1165, 839))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(800, 750))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(200, 400))
        self.tabWidget.setMaximumSize(QtCore.QSize(20000, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_22.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_22, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.textEditConsole = QtWidgets.QTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEditConsole.sizePolicy().hasHeightForWidth())
        self.textEditConsole.setSizePolicy(sizePolicy)
        self.textEditConsole.setReadOnly(True)
        self.textEditConsole.setObjectName("textEditConsole")
        self.gridLayout_7.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1521, 20))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetSubjects = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetSubjects.setMinimumSize(QtCore.QSize(330, 757))
        self.dockWidgetSubjects.setFloating(False)
        self.dockWidgetSubjects.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable)
        self.dockWidgetSubjects.setObjectName("dockWidgetSubjects")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBoxSubjectInfo = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBoxSubjectInfo.setObjectName("groupBoxSubjectInfo")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBoxSubjectInfo)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.labelEvents = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelEvents.setFont(font)
        self.labelEvents.setObjectName("labelEvents")
        self.gridLayout_10.addWidget(self.labelEvents, 3, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.labelFilters = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFilters.setFont(font)
        self.labelFilters.setObjectName("labelFilters")
        self.verticalLayout_12.addWidget(self.labelFilters)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.labelLow = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelLow.setLineWidth(1)
        self.labelLow.setScaledContents(True)
        self.labelLow.setWordWrap(False)
        self.labelLow.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelLow.setObjectName("labelLow")
        self.horizontalLayout_30.addWidget(self.labelLow)
        self.labelLowValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLowValue.sizePolicy().hasHeightForWidth())
        self.labelLowValue.setSizePolicy(sizePolicy)
        self.labelLowValue.setText("")
        self.labelLowValue.setWordWrap(True)
        self.labelLowValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelLowValue.setObjectName("labelLowValue")
        self.horizontalLayout_30.addWidget(self.labelLowValue)
        self.verticalLayout_12.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.labelHigh = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelHigh.setWordWrap(False)
        self.labelHigh.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelHigh.setObjectName("labelHigh")
        self.horizontalLayout_31.addWidget(self.labelHigh)
        self.labelHighValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighValue.sizePolicy().hasHeightForWidth())
        self.labelHighValue.setSizePolicy(sizePolicy)
        self.labelHighValue.setText("")
        self.labelHighValue.setWordWrap(True)
        self.labelHighValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelHighValue.setObjectName("labelHighValue")
        self.horizontalLayout_31.addWidget(self.labelHighValue)
        self.verticalLayout_12.addLayout(self.horizontalLayout_31)
        self.gridLayout_10.addLayout(self.verticalLayout_12, 1, 0, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.labelChannels = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelChannels.setFont(font)
        self.labelChannels.setObjectName("labelChannels")
        self.verticalLayout_11.addWidget(self.labelChannels)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.labelEEG = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelEEG.setWordWrap(False)
        self.labelEEG.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelEEG.setObjectName("labelEEG")
        self.horizontalLayout_25.addWidget(self.labelEEG)
        self.labelEEGValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEEGValue.sizePolicy().hasHeightForWidth())
        self.labelEEGValue.setSizePolicy(sizePolicy)
        self.labelEEGValue.setText("")
        self.labelEEGValue.setWordWrap(True)
        self.labelEEGValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelEEGValue.setObjectName("labelEEGValue")
        self.horizontalLayout_25.addWidget(self.labelEEGValue)
        self.verticalLayout_11.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.labelGradMEG = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelGradMEG.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelGradMEG.setObjectName("labelGradMEG")
        self.horizontalLayout_27.addWidget(self.labelGradMEG)
        self.labelGradMEGValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGradMEGValue.sizePolicy().hasHeightForWidth())
        self.labelGradMEGValue.setSizePolicy(sizePolicy)
        self.labelGradMEGValue.setText("")
        self.labelGradMEGValue.setWordWrap(True)
        self.labelGradMEGValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelGradMEGValue.setObjectName("labelGradMEGValue")
        self.horizontalLayout_27.addWidget(self.labelGradMEGValue)
        self.verticalLayout_11.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.labelMagMEG = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelMagMEG.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelMagMEG.setObjectName("labelMagMEG")
        self.horizontalLayout_28.addWidget(self.labelMagMEG)
        self.labelMagMEGValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMagMEGValue.sizePolicy().hasHeightForWidth())
        self.labelMagMEGValue.setSizePolicy(sizePolicy)
        self.labelMagMEGValue.setText("")
        self.labelMagMEGValue.setWordWrap(True)
        self.labelMagMEGValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelMagMEGValue.setObjectName("labelMagMEGValue")
        self.horizontalLayout_28.addWidget(self.labelMagMEGValue)
        self.verticalLayout_11.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.labelSamples = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelSamples.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSamples.setObjectName("labelSamples")
        self.horizontalLayout_29.addWidget(self.labelSamples)
        self.labelSamplesValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSamplesValue.sizePolicy().hasHeightForWidth())
        self.labelSamplesValue.setSizePolicy(sizePolicy)
        self.labelSamplesValue.setText("")
        self.labelSamplesValue.setWordWrap(True)
        self.labelSamplesValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSamplesValue.setObjectName("labelSamplesValue")
        self.horizontalLayout_29.addWidget(self.labelSamplesValue)
        self.verticalLayout_11.addLayout(self.horizontalLayout_29)
        self.gridLayout_10.addLayout(self.verticalLayout_11, 2, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelSubjectGeneral = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSubjectGeneral.setFont(font)
        self.labelSubjectGeneral.setTextFormat(QtCore.Qt.AutoText)
        self.labelSubjectGeneral.setObjectName("labelSubjectGeneral")
        self.verticalLayout_9.addWidget(self.labelSubjectGeneral)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.labelSubject = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelSubject.setWordWrap(False)
        self.labelSubject.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSubject.setObjectName("labelSubject")
        self.horizontalLayout_23.addWidget(self.labelSubject)
        self.labelSubjectValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSubjectValue.sizePolicy().hasHeightForWidth())
        self.labelSubjectValue.setSizePolicy(sizePolicy)
        self.labelSubjectValue.setText("")
        self.labelSubjectValue.setWordWrap(True)
        self.labelSubjectValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelSubjectValue.setObjectName("labelSubjectValue")
        self.horizontalLayout_23.addWidget(self.labelSubjectValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.labelDate = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelDate.setWordWrap(False)
        self.labelDate.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelDate.setObjectName("labelDate")
        self.horizontalLayout_24.addWidget(self.labelDate)
        self.labelDateValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDateValue.sizePolicy().hasHeightForWidth())
        self.labelDateValue.setSizePolicy(sizePolicy)
        self.labelDateValue.setText("")
        self.labelDateValue.setWordWrap(True)
        self.labelDateValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelDateValue.setObjectName("labelDateValue")
        self.horizontalLayout_24.addWidget(self.labelDateValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.labelLength = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        self.labelLength.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelLength.setObjectName("labelLength")
        self.horizontalLayout_40.addWidget(self.labelLength)
        self.labelLengthValue = QtWidgets.QLabel(self.groupBoxSubjectInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLengthValue.sizePolicy().hasHeightForWidth())
        self.labelLengthValue.setSizePolicy(sizePolicy)
        self.labelLengthValue.setText("")
        self.labelLengthValue.setObjectName("labelLengthValue")
        self.horizontalLayout_40.addWidget(self.labelLengthValue)
        self.verticalLayout_9.addLayout(self.horizontalLayout_40)
        self.gridLayout_10.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.textBrowserEvents = QtWidgets.QTextBrowser(self.groupBoxSubjectInfo)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowserEvents.setPalette(palette)
        self.textBrowserEvents.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowserEvents.setObjectName("textBrowserEvents")
        self.gridLayout_10.addWidget(self.textBrowserEvents, 4, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBoxSubjectInfo, 1, 0, 1, 1)
        self.groupBoxSubject_2 = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBoxSubject_2.setObjectName("groupBoxSubject_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBoxSubject_2)
        self.gridLayout_12.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonActivateSubject = QtWidgets.QPushButton(self.groupBoxSubject_2)
        self.pushButtonActivateSubject.setObjectName("pushButtonActivateSubject")
        self.gridLayout_5.addWidget(self.pushButtonActivateSubject, 0, 0, 1, 1)
        self.pushButtonAddSubjects = QtWidgets.QPushButton(self.groupBoxSubject_2)
        self.pushButtonAddSubjects.setObjectName("pushButtonAddSubjects")
        self.gridLayout_5.addWidget(self.pushButtonAddSubjects, 0, 1, 1, 1)
        self.pushButtonRemoveSubject = QtWidgets.QPushButton(self.groupBoxSubject_2)
        self.pushButtonRemoveSubject.setObjectName("pushButtonRemoveSubject")
        self.gridLayout_5.addWidget(self.pushButtonRemoveSubject, 1, 0, 1, 1)
        self.pushButtonLayout = QtWidgets.QPushButton(self.groupBoxSubject_2)
        self.pushButtonLayout.setObjectName("pushButtonLayout")
        self.gridLayout_5.addWidget(self.pushButtonLayout, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.listWidgetSubjects = QtWidgets.QListWidget(self.groupBoxSubject_2)
        self.listWidgetSubjects.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidgetSubjects.setObjectName("listWidgetSubjects")
        self.gridLayout_12.addWidget(self.listWidgetSubjects, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBoxSubject_2, 0, 0, 1, 1)
        self.dockWidgetSubjects.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetSubjects)
        self.actionCreate_experiment = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolBarIcons/images/createExperiment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_experiment.setIcon(icon)
        self.actionCreate_experiment.setObjectName("actionCreate_experiment")
        self.actionOpen_experiment = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolBarIcons/images/openExperiment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_experiment.setIcon(icon1)
        self.actionOpen_experiment.setObjectName("actionOpen_experiment")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionSet_workspace = QtWidgets.QAction(MainWindow)
        self.actionSet_workspace.setObjectName("actionSet_workspace")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionShowExperimentInfo = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolBarIcons/images/showExperimentInfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowExperimentInfo.setIcon(icon2)
        self.actionShowExperimentInfo.setObjectName("actionShowExperimentInfo")
        self.actionHide_Show_subject_list_and_info = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/toolBarIcons/images/subjectList.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHide_Show_subject_list_and_info.setIcon(icon3)
        self.actionHide_Show_subject_list_and_info.setObjectName("actionHide_Show_subject_list_and_info")
        self.actionDirectToConsole = QtWidgets.QAction(MainWindow)
        self.actionDirectToConsole.setCheckable(True)
        self.actionDirectToConsole.setChecked(True)
        self.actionDirectToConsole.setObjectName("actionDirectToConsole")
        self.actionShow_log = QtWidgets.QAction(MainWindow)
        self.actionShow_log.setObjectName("actionShow_log")
        self.menuFile.addAction(self.actionCreate_experiment)
        self.menuFile.addAction(self.actionOpen_experiment)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionShowExperimentInfo)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionDirectToConsole)
        self.menuTools.addAction(self.actionShow_log)
        self.menuTools.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionCreate_experiment)
        self.toolBar.addAction(self.actionOpen_experiment)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionShowExperimentInfo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHide_Show_subject_list_and_info)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.textEditConsole)
        MainWindow.setTabOrder(self.textEditConsole, self.textBrowserEvents)
        MainWindow.setTabOrder(self.textBrowserEvents, self.pushButtonActivateSubject)
        MainWindow.setTabOrder(self.pushButtonActivateSubject, self.pushButtonAddSubjects)
        MainWindow.setTabOrder(self.pushButtonAddSubjects, self.pushButtonRemoveSubject)
        MainWindow.setTabOrder(self.pushButtonRemoveSubject, self.listWidgetSubjects)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Meggie"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.groupBoxSubjectInfo.setTitle(_translate("MainWindow", "Subject info"))
        self.labelEvents.setText(_translate("MainWindow", "Events:"))
        self.labelFilters.setText(_translate("MainWindow", "Filters:"))
        self.labelLow.setText(_translate("MainWindow", "Low-pass:"))
        self.labelHigh.setText(_translate("MainWindow", "High-pass:"))
        self.labelChannels.setText(_translate("MainWindow", "Channels:"))
        self.labelEEG.setText(_translate("MainWindow", "EEG channels:"))
        self.labelGradMEG.setText(_translate("MainWindow", "Gradiometers:"))
        self.labelMagMEG.setText(_translate("MainWindow", "Magnetometers:"))
        self.labelSamples.setText(_translate("MainWindow", "Sampling frequency:"))
        self.labelSubjectGeneral.setText(_translate("MainWindow", "General:"))
        self.labelSubject.setText(_translate("MainWindow", "Name:"))
        self.labelDate.setText(_translate("MainWindow", "Date:"))
        self.labelLength.setText(_translate("MainWindow", "Length:"))
        self.groupBoxSubject_2.setTitle(_translate("MainWindow", "Subjects (active in bold):"))
        self.pushButtonActivateSubject.setText(_translate("MainWindow", "Activate selected"))
        self.pushButtonAddSubjects.setText(_translate("MainWindow", "Add new..."))
        self.pushButtonRemoveSubject.setText(_translate("MainWindow", "Remove selected"))
        self.pushButtonLayout.setText(_translate("MainWindow", "Change layout..."))
        self.actionCreate_experiment.setText(_translate("MainWindow", "Create New Experiment..."))
        self.actionOpen_experiment.setText(_translate("MainWindow", "Open Experiment..."))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionSet_workspace.setText(_translate("MainWindow", "Set Workspace..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionShowExperimentInfo.setText(_translate("MainWindow", "Show experiment info"))
        self.actionShowExperimentInfo.setToolTip(_translate("MainWindow", "Show more info about experiment"))
        self.actionHide_Show_subject_list_and_info.setText(_translate("MainWindow", "Hide/show subject list and info"))
        self.actionHide_Show_subject_list_and_info.setToolTip(_translate("MainWindow", "Hide/show subject list and info"))
        self.actionDirectToConsole.setText(_translate("MainWindow", "Direct output to console"))
        self.actionShow_log.setText(_translate("MainWindow", "Show log"))

