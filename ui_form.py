# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 600)
        font = QFont()
        font.setFamilies([u"Yu Gothic"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionLoad_Json = QAction(MainWindow)
        self.actionLoad_Json.setObjectName(u"actionLoad_Json")
        icon = QIcon()
        icon.addFile(u"images/loadJson.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLoad_Json.setIcon(icon)
        self.actionSave_Json = QAction(MainWindow)
        self.actionSave_Json.setObjectName(u"actionSave_Json")
        icon1 = QIcon()
        icon1.addFile(u"images/saveJson.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_Json.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u"images/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionApply_Tax_to_All_Sections = QAction(MainWindow)
        self.actionApply_Tax_to_All_Sections.setObjectName(u"actionApply_Tax_to_All_Sections")
        self.actionRemove_Tax_from_All_Sections = QAction(MainWindow)
        self.actionRemove_Tax_from_All_Sections.setObjectName(u"actionRemove_Tax_from_All_Sections")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.taxList = QComboBox(self.centralwidget)
        self.taxList.setObjectName(u"taxList")

        self.gridLayout_3.addWidget(self.taxList, 1, 1, 1, 1)

        self.labelTax = QLabel(self.centralwidget)
        self.labelTax.setObjectName(u"labelTax")

        self.gridLayout_3.addWidget(self.labelTax, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.optionSetModification = QGroupBox(self.centralwidget)
        self.optionSetModification.setObjectName(u"optionSetModification")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionSetModification.sizePolicy().hasHeightForWidth())
        self.optionSetModification.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.optionSetModification)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addOS = QPushButton(self.optionSetModification)
        self.addOS.setObjectName(u"addOS")

        self.gridLayout_4.addWidget(self.addOS, 3, 0, 1, 2)

        self.osList = QComboBox(self.optionSetModification)
        self.osList.setObjectName(u"osList")

        self.gridLayout_4.addWidget(self.osList, 1, 0, 1, 2)

        self.labelOS = QLabel(self.optionSetModification)
        self.labelOS.setObjectName(u"labelOS")

        self.gridLayout_4.addWidget(self.labelOS, 0, 0, 1, 2, Qt.AlignHCenter)

        self.taxImpOS = QPushButton(self.optionSetModification)
        self.taxImpOS.setObjectName(u"taxImpOS")

        self.gridLayout_4.addWidget(self.taxImpOS, 5, 0, 1, 2)

        self.optionsList = QComboBox(self.optionSetModification)
        self.optionsList.setObjectName(u"optionsList")

        self.gridLayout_4.addWidget(self.optionsList, 2, 0, 1, 2)

        self.addedOS = QTextEdit(self.optionSetModification)
        self.addedOS.setObjectName(u"addedOS")

        self.gridLayout_4.addWidget(self.addedOS, 4, 0, 1, 2)


        self.gridLayout_3.addWidget(self.optionSetModification, 2, 2, 1, 1)

        self.itemsModification = QGroupBox(self.centralwidget)
        self.itemsModification.setObjectName(u"itemsModification")
        sizePolicy.setHeightForWidth(self.itemsModification.sizePolicy().hasHeightForWidth())
        self.itemsModification.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.itemsModification)
        self.gridLayout.setObjectName(u"gridLayout")
        self.taxImpIt = QPushButton(self.itemsModification)
        self.taxImpIt.setObjectName(u"taxImpIt")

        self.gridLayout.addWidget(self.taxImpIt, 6, 0, 1, 2)

        self.itemsList = QComboBox(self.itemsModification)
        self.itemsList.setObjectName(u"itemsList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.itemsList.sizePolicy().hasHeightForWidth())
        self.itemsList.setSizePolicy(sizePolicy1)
        self.itemsList.setModelColumn(0)

        self.gridLayout.addWidget(self.itemsList, 1, 0, 1, 2)

        self.addedItems = QTextEdit(self.itemsModification)
        self.addedItems.setObjectName(u"addedItems")

        self.gridLayout.addWidget(self.addedItems, 5, 0, 1, 2)

        self.labelItems = QLabel(self.itemsModification)
        self.labelItems.setObjectName(u"labelItems")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic"])
        font1.setPointSize(10)
        self.labelItems.setFont(font1)

        self.gridLayout.addWidget(self.labelItems, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addItem = QPushButton(self.itemsModification)
        self.addItem.setObjectName(u"addItem")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addItem.sizePolicy().hasHeightForWidth())
        self.addItem.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.addItem, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.itemsModification, 2, 1, 1, 1)

        self.sectionModification = QGroupBox(self.centralwidget)
        self.sectionModification.setObjectName(u"sectionModification")
        sizePolicy.setHeightForWidth(self.sectionModification.sizePolicy().hasHeightForWidth())
        self.sectionModification.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.sectionModification)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sectionList = QComboBox(self.sectionModification)
        self.sectionList.setObjectName(u"sectionList")
        self.sectionList.setEnabled(True)

        self.gridLayout_2.addWidget(self.sectionList, 1, 0, 1, 2)

        self.taxImpSec = QPushButton(self.sectionModification)
        self.taxImpSec.setObjectName(u"taxImpSec")

        self.gridLayout_2.addWidget(self.taxImpSec, 6, 0, 1, 2)

        self.addedSections = QTextEdit(self.sectionModification)
        self.addedSections.setObjectName(u"addedSections")

        self.gridLayout_2.addWidget(self.addedSections, 5, 0, 1, 2)

        self.labelSection = QLabel(self.sectionModification)
        self.labelSection.setObjectName(u"labelSection")
        self.labelSection.setFont(font1)

        self.gridLayout_2.addWidget(self.labelSection, 0, 0, 1, 2, Qt.AlignHCenter)

        self.addSection = QPushButton(self.sectionModification)
        self.addSection.setObjectName(u"addSection")

        self.gridLayout_2.addWidget(self.addSection, 3, 0, 1, 2)


        self.gridLayout_3.addWidget(self.sectionModification, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 29))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTax_Options = QMenu(self.menuEdit)
        self.menuTax_Options.setObjectName(u"menuTax_Options")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionLoad_Json)
        self.menuFile.addAction(self.actionSave_Json)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.menuTax_Options.menuAction())
        self.menuTax_Options.addAction(self.actionApply_Tax_to_All_Sections)
        self.menuTax_Options.addAction(self.actionRemove_Tax_from_All_Sections)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Json.setText(QCoreApplication.translate("MainWindow", u"Load Json", None))
#if QT_CONFIG(shortcut)
        self.actionLoad_Json.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Json.setText(QCoreApplication.translate("MainWindow", u"Save Json", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Json.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionApply_Tax_to_All_Sections.setText(QCoreApplication.translate("MainWindow", u"Apply Tax to All Sections", None))
#if QT_CONFIG(shortcut)
        self.actionApply_Tax_to_All_Sections.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemove_Tax_from_All_Sections.setText(QCoreApplication.translate("MainWindow", u"Remove Tax from All Sections", None))
#if QT_CONFIG(shortcut)
        self.actionRemove_Tax_from_All_Sections.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.labelTax.setText(QCoreApplication.translate("MainWindow", u"Please Select Tax Values", None))
        self.optionSetModification.setTitle(QCoreApplication.translate("MainWindow", u"Option Set Modifications", None))
        self.addOS.setText(QCoreApplication.translate("MainWindow", u"Add Option", None))
        self.labelOS.setText(QCoreApplication.translate("MainWindow", u"Select the OS to Modify", None))
        self.taxImpOS.setText(QCoreApplication.translate("MainWindow", u"Implement OS Tax", None))
        self.itemsModification.setTitle(QCoreApplication.translate("MainWindow", u"Item Modifications", None))
        self.taxImpIt.setText(QCoreApplication.translate("MainWindow", u"Implement Item Tax", None))
        self.labelItems.setText(QCoreApplication.translate("MainWindow", u"Select the Items to Modify", None))
        self.addItem.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.sectionModification.setTitle(QCoreApplication.translate("MainWindow", u"Section Modifications", None))
        self.taxImpSec.setText(QCoreApplication.translate("MainWindow", u"Implement Sections Tax", None))
        self.labelSection.setText(QCoreApplication.translate("MainWindow", u"Select the Sections to Modify", None))
        self.addSection.setText(QCoreApplication.translate("MainWindow", u"Add Section", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTax_Options.setTitle(QCoreApplication.translate("MainWindow", u"Tax Options", None))
    # retranslateUi

