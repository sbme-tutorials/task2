# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.size_2 = QtWidgets.QComboBox(self.centralwidget)
        self.size_2.setStyleSheet("")
        self.size_2.setEditable(True)
        self.size_2.setIconSize(QtCore.QSize(40, 40))
        self.size_2.setDuplicatesEnabled(False)
        self.size_2.setObjectName("size_2")
        self.size_2.addItem("")
        self.size_2.addItem("")
        self.size_2.addItem("")
        self.size_2.addItem("")
        self.size_2.addItem("")
        self.size_2.addItem("")
        self.verticalLayout_3.addWidget(self.size_2)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setStyleSheet("")
        self.browse.setObjectName("browse")
        self.verticalLayout_3.addWidget(self.browse)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.property_2 = QtWidgets.QComboBox(self.centralwidget)
        self.property_2.setStyleSheet("")
        self.property_2.setEditable(True)
        self.property_2.setIconSize(QtCore.QSize(40, 40))
        self.property_2.setObjectName("property_2")
        self.property_2.addItem("")
        self.property_2.addItem("")
        self.property_2.addItem("")
        self.property_2.addItem("")
        self.horizontalLayout_4.addWidget(self.property_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TE_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.TE_Edit.setText("")
        self.TE_Edit.setObjectName("TE_Edit")
        self.horizontalLayout.addWidget(self.TE_Edit)
        self.TR_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.TR_Edit.setText("")
        self.TR_Edit.setObjectName("TR_Edit")
        self.horizontalLayout.addWidget(self.TR_Edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Preparetion_Box = QtWidgets.QComboBox(self.centralwidget)
        self.Preparetion_Box.setStyleSheet("")
        self.Preparetion_Box.setObjectName("Preparetion_Box")
        self.Preparetion_Box.addItem("")
        self.Preparetion_Box.addItem("")
        self.Preparetion_Box.addItem("")
        self.Preparetion_Box.addItem("")
        self.horizontalLayout_3.addWidget(self.Preparetion_Box)
        self.Acquisition_Box = QtWidgets.QComboBox(self.centralwidget)
        self.Acquisition_Box.setStyleSheet("")
        self.Acquisition_Box.setObjectName("Acquisition_Box")
        self.Acquisition_Box.addItem("")
        self.Acquisition_Box.addItem("")
        self.Acquisition_Box.addItem("")
        self.Acquisition_Box.addItem("")
        self.horizontalLayout_3.addWidget(self.Acquisition_Box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.Zooming_Box = QtWidgets.QComboBox(self.centralwidget)
        self.Zooming_Box.setStyleSheet("")
        self.Zooming_Box.setObjectName("Zooming_Box")
        self.Zooming_Box.addItem("")
        self.Zooming_Box.addItem("")
        self.Zooming_Box.addItem("")
        self.verticalLayout_10.addWidget(self.Zooming_Box)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_10.addWidget(self.comboBox)
        self.Ernst_Angle = QtWidgets.QPushButton(self.centralwidget)
        self.Ernst_Angle.setStyleSheet("")
        self.Ernst_Angle.setObjectName("Ernst_Angle")
        self.verticalLayout_10.addWidget(self.Ernst_Angle)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.graphicsView_phantom = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_phantom.setObjectName("graphicsView_phantom")
        self.gridLayout.addWidget(self.graphicsView_phantom, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Start_seq1 = QtWidgets.QPushButton(self.tab)
        self.Start_seq1.setStyleSheet("")
        self.Start_seq1.setObjectName("Start_seq1")
        self.verticalLayout_4.addWidget(self.Start_seq1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        self.graphicsView_seq1 = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView_seq1.setObjectName("graphicsView_seq1")
        self.gridLayout_4.addWidget(self.graphicsView_seq1, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.GV_prep = PlotWidget(self.tab)
        self.GV_prep.setObjectName("GV_prep")
        self.verticalLayout_4.addWidget(self.GV_prep)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.GV_aqua = PlotWidget(self.tab)
        self.GV_aqua.setObjectName("GV_aqua")
        self.verticalLayout_4.addWidget(self.GV_aqua)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_4.addLayout(self.verticalLayout_13)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Start_seq2 = QtWidgets.QPushButton(self.tab_2)
        self.Start_seq2.setStyleSheet("")
        self.Start_seq2.setObjectName("Start_seq2")
        self.verticalLayout_14.addWidget(self.Start_seq2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphicsView_seq2 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_seq2.setMouseTracking(False)
        self.graphicsView_seq2.setObjectName("graphicsView_seq2")
        self.gridLayout_5.addWidget(self.graphicsView_seq2, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 2, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout_5)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_14.addLayout(self.verticalLayout_16)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_14.addWidget(self.label_3)
        self.graphicsView_3 = PlotWidget(self.tab_2)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_14.addWidget(self.graphicsView_3)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_14.addWidget(self.label_4)
        self.graphicsView_4 = PlotWidget(self.tab_2)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_14.addWidget(self.graphicsView_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.image = QtWidgets.QLabel(self.tab_3)
        self.image.setGeometry(QtCore.QRect(10, 10, 191, 211))
        self.image.setFrameShape(QtWidgets.QFrame.Box)
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 230, 301, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graph_t2 = PlotWidget(self.layoutWidget)
        self.graph_t2.setObjectName("graph_t2")
        self.verticalLayout_7.addWidget(self.graph_t2)
        self.Recovery_label = QtWidgets.QLabel(self.layoutWidget)
        self.Recovery_label.setScaledContents(True)
        self.Recovery_label.setObjectName("Recovery_label")
        self.verticalLayout_7.addWidget(self.Recovery_label)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graph_t1 = PlotWidget(self.layoutWidget)
        self.graph_t1.setObjectName("graph_t1")
        self.verticalLayout_6.addWidget(self.graph_t1)
        self.Decay_label = QtWidgets.QLabel(self.layoutWidget)
        self.Decay_label.setScaledContents(True)
        self.Decay_label.setObjectName("Decay_label")
        self.verticalLayout_6.addWidget(self.Decay_label)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.Brightness_slider = QtWidgets.QSlider(self.tab_3)
        self.Brightness_slider.setGeometry(QtCore.QRect(0, 590, 341, 16))
        self.Brightness_slider.setMinimum(-10)
        self.Brightness_slider.setMaximum(10)
        self.Brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Brightness_slider.setObjectName("Brightness_slider")
        self.Contrast_slider = QtWidgets.QSlider(self.tab_3)
        self.Contrast_slider.setGeometry(QtCore.QRect(0, 560, 341, 16))
        self.Contrast_slider.setMinimum(-10)
        self.Contrast_slider.setMaximum(10)
        self.Contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Contrast_slider.setObjectName("Contrast_slider")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_8.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.size_2.setCurrentText(_translate("MainWindow", "Size"))
        self.size_2.setItemText(0, _translate("MainWindow", "Size"))
        self.size_2.setItemText(1, _translate("MainWindow", "20"))
        self.size_2.setItemText(2, _translate("MainWindow", "64"))
        self.size_2.setItemText(3, _translate("MainWindow", "128"))
        self.size_2.setItemText(4, _translate("MainWindow", "256"))
        self.size_2.setItemText(5, _translate("MainWindow", "512"))
        self.browse.setText(_translate("MainWindow", "Broswe"))
        self.property_2.setCurrentText(_translate("MainWindow", "Property"))
        self.property_2.setItemText(0, _translate("MainWindow", "Property"))
        self.property_2.setItemText(1, _translate("MainWindow", "T1"))
        self.property_2.setItemText(2, _translate("MainWindow", "T2"))
        self.property_2.setItemText(3, _translate("MainWindow", "Phantom"))
        self.TE_Edit.setPlaceholderText(_translate("MainWindow", "Enter TE"))
        self.TR_Edit.setPlaceholderText(_translate("MainWindow", "Enter TR"))
        self.Preparetion_Box.setItemText(0, _translate("MainWindow", "Preparetion"))
        self.Preparetion_Box.setItemText(1, _translate("MainWindow", "T1 Prep (IR)"))
        self.Preparetion_Box.setItemText(2, _translate("MainWindow", "T2  Prep"))
        self.Preparetion_Box.setItemText(3, _translate("MainWindow", "Tagging Prep"))
        self.Acquisition_Box.setItemText(0, _translate("MainWindow", "Acquisition"))
        self.Acquisition_Box.setItemText(1, _translate("MainWindow", "GRE"))
        self.Acquisition_Box.setItemText(2, _translate("MainWindow", "SSFP"))
        self.Acquisition_Box.setItemText(3, _translate("MainWindow", "SE"))
        self.Zooming_Box.setCurrentText(_translate("MainWindow", "Zooming"))
        self.Zooming_Box.setItemText(0, _translate("MainWindow", "Zooming"))
        self.Zooming_Box.setItemText(1, _translate("MainWindow", "Without Link"))
        self.Zooming_Box.setItemText(2, _translate("MainWindow", "With Link"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Artifacts"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Alaising"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bluring"))
        self.Ernst_Angle.setText(_translate("MainWindow", "Ernst Angle"))
        self.Start_seq1.setText(_translate("MainWindow", "Start Sequence"))
        self.label.setText(_translate("MainWindow", "Prepration"))
        self.label_2.setText(_translate("MainWindow", "Acquazition"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "View Port 1"))
        self.Start_seq2.setText(_translate("MainWindow", "Start Sequence"))
        self.label_3.setText(_translate("MainWindow", "Prepration"))
        self.label_4.setText(_translate("MainWindow", "Acquazition"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View Port 2"))
        self.image.setText(_translate("MainWindow", "TextLabel"))
        self.Recovery_label.setText(_translate("MainWindow", " Recovey"))
        self.Decay_label.setText(_translate("MainWindow", "Decay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Phantom"))

from pyqtgraph import PlotWidget
