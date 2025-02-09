# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 604)
        MainWindow.setMinimumSize(QtCore.QSize(650, 500))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"    border-radius: 2px;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: rgb(0, 60, 101);\n"
"    /*background-color: #1e1d23;*/\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#1e1d23;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #04b97f;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: none;\n"
"        border-width: 0px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    corner-radius: 2px;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFFFFF;\n"
"    selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setEnabled(True)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fTop = QtWidgets.QFrame(self.mainWidget)
        self.fTop.setMinimumSize(QtCore.QSize(0, 50))
        self.fTop.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fTop.setStyleSheet("")
        self.fTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fTop.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fTop.setObjectName("fTop")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fTop)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fTopOptionsToggle = QtWidgets.QFrame(self.fTop)
        self.fTopOptionsToggle.setMinimumSize(QtCore.QSize(50, 0))
        self.fTopOptionsToggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fTopOptionsToggle.setAutoFillBackground(False)
        self.fTopOptionsToggle.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.fTopOptionsToggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fTopOptionsToggle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fTopOptionsToggle.setObjectName("fTopOptionsToggle")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fTopOptionsToggle)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonShowMore = QtWidgets.QPushButton(self.fTopOptionsToggle)
        self.buttonShowMore.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(53, 53, 53);\n"
"}")
        self.buttonShowMore.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/options_burguer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonShowMore.setIcon(icon)
        self.buttonShowMore.setIconSize(QtCore.QSize(20, 20))
        self.buttonShowMore.setCheckable(True)
        self.buttonShowMore.setObjectName("buttonShowMore")
        self.gridLayout_2.addWidget(self.buttonShowMore, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.fTopOptionsToggle)
        self.fTopBar = QtWidgets.QFrame(self.fTop)
        self.fTopBar.setStyleSheet("background-color: rgb(0, 91, 153);")
        self.fTopBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fTopBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fTopBar.setObjectName("fTopBar")
        self.gridLayout = QtWidgets.QGridLayout(self.fTopBar)
        self.gridLayout.setObjectName("gridLayout")
        self.topBarText = QtWidgets.QLabel(self.fTopBar)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.topBarText.setFont(font)
        self.topBarText.setObjectName("topBarText")
        self.gridLayout.addWidget(self.topBarText, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.fTopBar)
        self.verticalLayout_2.addWidget(self.fTop)
        self.fBottom = QtWidgets.QFrame(self.mainWidget)
        self.fBottom.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.fBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fBottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fBottom.setObjectName("fBottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fBottom)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fLeftPanel = QtWidgets.QFrame(self.fBottom)
        self.fLeftPanel.setMinimumSize(QtCore.QSize(50, 50))
        self.fLeftPanel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fLeftPanel.setTabletTracking(False)
        self.fLeftPanel.setStyleSheet("QFrame{\n"
"    background-color: rgb(15, 15, 15);\n"
"    \n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(15, 15, 15);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(53, 53, 53);\n"
"    \n"
"}\n"
"QPushButton:checked{\n"
"    background-color: rgb(0, 60, 101);\n"
"    \n"
"}")
        self.fLeftPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fLeftPanel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fLeftPanel.setObjectName("fLeftPanel")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fLeftPanel)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttonInfo = QtWidgets.QPushButton(self.fLeftPanel)
        self.buttonInfo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/information-icon-white-6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonInfo.setIcon(icon1)
        self.buttonInfo.setIconSize(QtCore.QSize(30, 30))
        self.buttonInfo.setCheckable(True)
        self.buttonInfo.setChecked(False)
        self.buttonInfo.setAutoExclusive(True)
        self.buttonInfo.setAutoDefault(True)
        self.buttonInfo.setObjectName("buttonInfo")
        self.verticalLayout_3.addWidget(self.buttonInfo)
        self.buttonOpRetasRaizes = QtWidgets.QPushButton(self.fLeftPanel)
        self.buttonOpRetasRaizes.setEnabled(True)
        self.buttonOpRetasRaizes.setToolTipDuration(-1)
        self.buttonOpRetasRaizes.setWhatsThis("")
        self.buttonOpRetasRaizes.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons/Retas Raiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonOpRetasRaizes.setIcon(icon2)
        self.buttonOpRetasRaizes.setIconSize(QtCore.QSize(30, 30))
        self.buttonOpRetasRaizes.setCheckable(True)
        self.buttonOpRetasRaizes.setChecked(True)
        self.buttonOpRetasRaizes.setAutoExclusive(True)
        self.buttonOpRetasRaizes.setObjectName("buttonOpRetasRaizes")
        self.verticalLayout_3.addWidget(self.buttonOpRetasRaizes)
        self.buttonFx = QtWidgets.QPushButton(self.fLeftPanel)
        self.buttonFx.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttons/fx.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFx.setIcon(icon3)
        self.buttonFx.setIconSize(QtCore.QSize(30, 30))
        self.buttonFx.setCheckable(True)
        self.buttonFx.setChecked(False)
        self.buttonFx.setAutoExclusive(True)
        self.buttonFx.setObjectName("buttonFx")
        self.verticalLayout_3.addWidget(self.buttonFx)
        spacerItem = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.fLeftPanel)
        self.pages = QtWidgets.QStackedWidget(self.fBottom)
        self.pages.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pages.setFont(font)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pages.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pages.setLineWidth(1)
        self.pages.setObjectName("pages")
        self.pageInfo = QtWidgets.QWidget()
        self.pageInfo.setObjectName("pageInfo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pageInfo)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.equations = QtWidgets.QLabel(self.pageInfo)
        self.equations.setText("## Polinômio de 2º grau original *(plano Oxy)*\n"
">>\n"
">   <img src=\":/eqs/eq1.png\" />\n"
"## Parábola Discriminante *(plano Opq)*\n"
">>\n"
">   <img src=\":/eqs/eq2.png\" />\n"
"## Reta Raiz\n"
">>\n"
">   <img src=\":/eqs/eq3.png\" />\n"
"\n"
"## Pontos importantes:\n"
"### x do vértice:\n"
">>\n"
">   <img src=\":/eqs/eq4.png\" />\n"
"")
        self.equations.setTextFormat(QtCore.Qt.MarkdownText)
        self.equations.setScaledContents(False)
        self.equations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.equations.setWordWrap(True)
        self.equations.setOpenExternalLinks(True)
        self.equations.setObjectName("equations")
        self.gridLayout_4.addWidget(self.equations, 0, 0, 1, 1)
        self.pages.addWidget(self.pageInfo)
        self.pageRetasRaizes = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pageRetasRaizes.setFont(font)
        self.pageRetasRaizes.setObjectName("pageRetasRaizes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pageRetasRaizes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 6, 3, 1, 1)
        self.IntervaloP = QtWidgets.QFrame(self.pageRetasRaizes)
        self.IntervaloP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IntervaloP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IntervaloP.setObjectName("IntervaloP")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.IntervaloP)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.info1 = QtWidgets.QLabel(self.IntervaloP)
        self.info1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.info1.setFont(font)
        self.info1.setAutoFillBackground(False)
        self.info1.setTextFormat(QtCore.Qt.MarkdownText)
        self.info1.setObjectName("info1")
        self.horizontalLayout_4.addWidget(self.info1)
        self.pMin = QtWidgets.QDoubleSpinBox(self.IntervaloP)
        self.pMin.setWrapping(False)
        self.pMin.setFrame(False)
        self.pMin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pMin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.pMin.setProperty("showGroupSeparator", False)
        self.pMin.setMinimum(-999999.0)
        self.pMin.setMaximum(999999.0)
        self.pMin.setProperty("value", -10.0)
        self.pMin.setObjectName("pMin")
        self.horizontalLayout_4.addWidget(self.pMin)
        self.pMax = QtWidgets.QDoubleSpinBox(self.IntervaloP)
        self.pMax.setFrame(False)
        self.pMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pMax.setMinimum(-999999.0)
        self.pMax.setMaximum(999999.0)
        self.pMax.setProperty("value", 10.0)
        self.pMax.setObjectName("pMax")
        self.horizontalLayout_4.addWidget(self.pMax)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_3.addWidget(self.IntervaloP, 2, 0, 1, 4)
        self.line = QtWidgets.QFrame(self.pageRetasRaizes)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 4)
        self.infoResult = QtWidgets.QLabel(self.pageRetasRaizes)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.infoResult.setFont(font)
        self.infoResult.setStyleSheet("color: rgb(30, 215, 96);")
        self.infoResult.setText("")
        self.infoResult.setAlignment(QtCore.Qt.AlignCenter)
        self.infoResult.setWordWrap(True)
        self.infoResult.setObjectName("infoResult")
        self.gridLayout_3.addWidget(self.infoResult, 6, 0, 2, 3)
        self.buttonGo = QtWidgets.QPushButton(self.pageRetasRaizes)
        self.buttonGo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.buttonGo.sizePolicy().hasHeightForWidth())
        self.buttonGo.setSizePolicy(sizePolicy)
        self.buttonGo.setMaximumSize(QtCore.QSize(200, 50))
        self.buttonGo.setBaseSize(QtCore.QSize(0, 0))
        self.buttonGo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonGo.setAutoFillBackground(False)
        self.buttonGo.setStyleSheet("background-color: rgb(0,  91, 153);\n"
"margin: 0px 20px 0px 20px;")
        self.buttonGo.setObjectName("buttonGo")
        self.gridLayout_3.addWidget(self.buttonGo, 7, 3, 1, 1)
        self.tabX = QtWidgets.QTabWidget(self.pageRetasRaizes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabX.sizePolicy().hasHeightForWidth())
        self.tabX.setSizePolicy(sizePolicy)
        self.tabX.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabX.setIconSize(QtCore.QSize(55, 50))
        self.tabX.setElideMode(QtCore.Qt.ElideNone)
        self.tabX.setObjectName("tabX")
        self.tabSingleX = QtWidgets.QWidget()
        self.tabSingleX.setObjectName("tabSingleX")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabSingleX)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        self.xSingleValue = QtWidgets.QDoubleSpinBox(self.tabSingleX)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xSingleValue.setFont(font)
        self.xSingleValue.setFrame(False)
        self.xSingleValue.setMinimum(-999999.0)
        self.xSingleValue.setMaximum(999999.0)
        self.xSingleValue.setProperty("value", 1.0)
        self.xSingleValue.setObjectName("xSingleValue")
        self.gridLayout_5.addWidget(self.xSingleValue, 0, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/intervals/Screenshot 2022-06-01 000450.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabX.addTab(self.tabSingleX, icon4, "")
        self.tabMultiX = QtWidgets.QWidget()
        self.tabMultiX.setObjectName("tabMultiX")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabMultiX)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fMultiplosX = QtWidgets.QFrame(self.tabMultiX)
        self.fMultiplosX.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fMultiplosX.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fMultiplosX.setObjectName("fMultiplosX")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fMultiplosX)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.xMin = QtWidgets.QDoubleSpinBox(self.fMultiplosX)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xMin.setFont(font)
        self.xMin.setStyleSheet("")
        self.xMin.setFrame(False)
        self.xMin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xMin.setMinimum(-999999.0)
        self.xMin.setMaximum(999999.0)
        self.xMin.setProperty("value", -2.0)
        self.xMin.setObjectName("xMin")
        self.gridLayout_6.addWidget(self.xMin, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 3, 1, 1)
        self.xMax = QtWidgets.QDoubleSpinBox(self.fMultiplosX)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xMax.setFont(font)
        self.xMax.setStyleSheet("")
        self.xMax.setFrame(False)
        self.xMax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xMax.setMinimum(-999999.0)
        self.xMax.setMaximum(999999.0)
        self.xMax.setProperty("value", 2.0)
        self.xMax.setObjectName("xMax")
        self.gridLayout_6.addWidget(self.xMax, 0, 1, 1, 1)
        self.xStep = QtWidgets.QDoubleSpinBox(self.fMultiplosX)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xStep.setFont(font)
        self.xStep.setStyleSheet("")
        self.xStep.setWrapping(False)
        self.xStep.setFrame(False)
        self.xStep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xStep.setMinimum(0.01)
        self.xStep.setMaximum(999999.0)
        self.xStep.setSingleStep(0.5)
        self.xStep.setProperty("value", 0.5)
        self.xStep.setObjectName("xStep")
        self.gridLayout_6.addWidget(self.xStep, 0, 2, 1, 1)
        self.horizontalLayout_5.addWidget(self.fMultiplosX)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/intervals/dividing-line-interval-line-vector_2622234.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabX.addTab(self.tabMultiX, icon5, "")
        self.gridLayout_3.addWidget(self.tabX, 5, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.pageRetasRaizes)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 4)
        self.pages.addWidget(self.pageRetasRaizes)
        self.pageFx = QtWidgets.QWidget()
        self.pageFx.setObjectName("pageFx")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageFx)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.infoFx = QtWidgets.QLabel(self.pageFx)
        self.infoFx.setMaximumSize(QtCore.QSize(16777215, 150))
        self.infoFx.setTextFormat(QtCore.Qt.MarkdownText)
        self.infoFx.setWordWrap(True)
        self.infoFx.setObjectName("infoFx")
        self.verticalLayout_5.addWidget(self.infoFx)
        self.pqAsker = QtWidgets.QGridLayout()
        self.pqAsker.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.pqAsker.setObjectName("pqAsker")
        self.qLabel = QtWidgets.QLabel(self.pageFx)
        self.qLabel.setObjectName("qLabel")
        self.pqAsker.addWidget(self.qLabel, 1, 0, 1, 1)
        self.pLabel = QtWidgets.QLabel(self.pageFx)
        self.pLabel.setObjectName("pLabel")
        self.pqAsker.addWidget(self.pLabel, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.pageFx)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pqAsker.addWidget(self.line_2, 0, 4, 2, 1)
        self.buttonOpq = QtWidgets.QPushButton(self.pageFx)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonOpq.setFont(font)
        self.buttonOpq.setObjectName("buttonOpq")
        self.pqAsker.addWidget(self.buttonOpq, 0, 6, 2, 1)
        self.aValue = QtWidgets.QDoubleSpinBox(self.pageFx)
        self.aValue.setFrame(False)
        self.aValue.setMinimum(-99999999.0)
        self.aValue.setMaximum(99999999.0)
        self.aValue.setObjectName("aValue")
        self.pqAsker.addWidget(self.aValue, 1, 5, 1, 1)
        self.buttonOxy = QtWidgets.QPushButton(self.pageFx)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonOxy.setFont(font)
        self.buttonOxy.setIconSize(QtCore.QSize(16, 16))
        self.buttonOxy.setObjectName("buttonOxy")
        self.pqAsker.addWidget(self.buttonOxy, 0, 2, 2, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pqAsker.addItem(spacerItem5, 0, 8, 2, 1)
        self.aLabel = QtWidgets.QLabel(self.pageFx)
        self.aLabel.setObjectName("aLabel")
        self.pqAsker.addWidget(self.aLabel, 0, 5, 1, 1)
        self.qValue = QtWidgets.QDoubleSpinBox(self.pageFx)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.qValue.setFont(font)
        self.qValue.setWrapping(False)
        self.qValue.setFrame(False)
        self.qValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.qValue.setPrefix("")
        self.qValue.setMinimum(-99999999.0)
        self.qValue.setMaximum(99999999.0)
        self.qValue.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.qValue.setObjectName("qValue")
        self.pqAsker.addWidget(self.qValue, 1, 1, 1, 1)
        self.pValue = QtWidgets.QDoubleSpinBox(self.pageFx)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pValue.setFont(font)
        self.pValue.setWrapping(False)
        self.pValue.setFrame(False)
        self.pValue.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.pValue.setPrefix("")
        self.pValue.setMinimum(-99999999.0)
        self.pValue.setMaximum(99999999.0)
        self.pValue.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.pValue.setObjectName("pValue")
        self.pqAsker.addWidget(self.pValue, 0, 1, 1, 1)
        self.checkShowGraph = QtWidgets.QCheckBox(self.pageFx)
        self.checkShowGraph.setChecked(True)
        self.checkShowGraph.setObjectName("checkShowGraph")
        self.pqAsker.addWidget(self.checkShowGraph, 2, 0, 1, 2)
        self.checkShowRaizes = QtWidgets.QCheckBox(self.pageFx)
        self.checkShowRaizes.setTristate(False)
        self.checkShowRaizes.setObjectName("checkShowRaizes")
        self.pqAsker.addWidget(self.checkShowRaizes, 2, 3, 1, 3)
        self.verticalLayout_5.addLayout(self.pqAsker)
        self.InfoWidget = QtWidgets.QHBoxLayout()
        self.InfoWidget.setObjectName("InfoWidget")
        self.InfoLabel = QtWidgets.QLabel(self.pageFx)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setText("")
        self.InfoLabel.setTextFormat(QtCore.Qt.AutoText)
        self.InfoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.InfoLabel.setWordWrap(True)
        self.InfoLabel.setObjectName("InfoLabel")
        self.InfoWidget.addWidget(self.InfoLabel)
        self.verticalLayout_5.addLayout(self.InfoWidget)
        self.pages.addWidget(self.pageFx)
        self.horizontalLayout.addWidget(self.pages)
        self.verticalLayout_2.addWidget(self.fBottom)
        self.fBottom.raise_()
        self.fTop.raise_()
        MainWindow.setCentralWidget(self.mainWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(2)
        self.tabX.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topBarText.setText(_translate("MainWindow", "Ferramentas para Polinômios de 2º Grau"))
        self.buttonInfo.setToolTip(_translate("MainWindow", "Info"))
        self.buttonInfo.setStatusTip(_translate("MainWindow", "Informações sobre o Programa"))
        self.buttonOpRetasRaizes.setToolTip(_translate("MainWindow", "Plot de Retas Raízes"))
        self.buttonOpRetasRaizes.setStatusTip(_translate("MainWindow", "Mostra o gráfico das Retas Raízes"))
        self.buttonFx.setToolTip(_translate("MainWindow", "Análise de Trinômio"))
        self.buttonFx.setStatusTip(_translate("MainWindow", "Mostra o gráfico e os dados de um trinômio de 2º grau uma vez que são especificados seus coeficientes"))
        self.info1.setText(_translate("MainWindow", "### Intervalo p"))
        self.pMin.setPrefix(_translate("MainWindow", "De "))
        self.pMax.setPrefix(_translate("MainWindow", "Até "))
        self.buttonGo.setText(_translate("MainWindow", "Confirm"))
        self.xSingleValue.setPrefix(_translate("MainWindow", "                  x = "))
        self.tabX.setTabText(self.tabX.indexOf(self.tabSingleX), _translate("MainWindow", "Valor único de x"))
        self.xMin.setPrefix(_translate("MainWindow", "x: De "))
        self.xMax.setPrefix(_translate("MainWindow", "Até "))
        self.xStep.setPrefix(_translate("MainWindow", "Passo "))
        self.tabX.setTabText(self.tabX.indexOf(self.tabMultiX), _translate("MainWindow", "Vários valores de x"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Retas Raízes</span></p><p><span style=\" font-size:11pt;\">Para um polinômio de 2º grau do tipo </span><img src=\":/eqs/eq1.png\" height=\"22\"/><span style=\" font-size:11pt;\">, informe o intervalo de </span><span style=\" font-size:11pt; font-weight:600;\">p</span><span style=\" font-size:11pt;\"> no qual os gráficos serão gerados.</span></p><p><span style=\" font-size:11pt;\">Em seguida escolha se deseja ver a reta raíz para um valor único de </span><span style=\" font-size:11pt; font-style:italic;\">a</span><span style=\" font-size:11pt;\"> ou para vários valores.</span></p></body></html>"))
        self.infoFx.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Trinômios específicos</span></p><p><span style=\" font-size:11pt;\">Para um polinômio de 2º grau do tipo </span><img src=\":/eqs/eq1.png\" height=\"22\"/><span style=\" font-size:11pt;\">, informe os coeficientes </span><span style=\" font-size:11pt; font-weight:600;\">p</span><span style=\" font-size:11pt;\"> e </span><span style=\" font-size:11pt; font-weight:600;\">q</span><span style=\" font-size:11pt;\">.</span></p><p><span style=\" font-size:11pt;\">Para análise no plano </span><span style=\" font-size:11pt; font-style:italic;\">Opq</span><span style=\" font-size:11pt;\">, informe também o valor arbitrário </span><span style=\" font-size:11pt; font-style:italic;\">a</span></p></body></html>"))
        self.qLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">q = </span></p></body></html>"))
        self.pLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">p = </span></p></body></html>"))
        self.buttonOpq.setText(_translate("MainWindow", "Analisar\n"
"(Plano Opq)"))
        self.buttonOxy.setText(_translate("MainWindow", "Analisar\n"
"(Plano Oxy)"))
        self.aLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">a =</span></p></body></html>"))
        self.checkShowGraph.setText(_translate("MainWindow", "Mostrar Gráfico"))
        self.checkShowRaizes.setText(_translate("MainWindow", "Mostrar Raízes"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
