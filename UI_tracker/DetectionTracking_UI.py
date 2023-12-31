# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectionTracking_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1728, 972)
        MainWindow.setMinimumSize(QtCore.QSize(1728, 972))
        MainWindow.setMaximumSize(QtCore.QSize(1728, 972))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/newPrefix/images_test/background1.png);}\n"
"\n"
"#QInputDialog{border-image: url(:/newPrefix/images_test/light.png);}\n"
"\n"
"QLabel{border:5px;}\n"
"QLabel::hover {\n"
"border:0px;}\n"
"\n"
"QMenuBar{border-color:transparent;}\n"
"QToolButton[objectName=pushButton_doIt]{\n"
"border:5px;}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:hover {\n"
"image:url(:/newPrefix/images_test/run_hover.png);}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:pressed {\n"
"image:url(:/newPrefix/images_test/run_pressed.png);}\n"
"\n"
"QScrollBar:vertical{\n"
"background:transparent;\n"
"padding:2px;\n"
"border-radius:4px;\n"
"max-width:8px;}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#9acd32;\n"
"min-height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#9eb764;}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#9eb764;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"                               \n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;}\n"
"                                 \n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:transparent;\n"
"padding:0px;\n"
"border-radius:4px;\n"
"max-height:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#9acd32;\n"
"min-width:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"QToolButton::hover{\n"
"border:0px;\n"
"} ")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(810, 120, 141, 30))
        self.label_author.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_author.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_author.setObjectName("label_author")
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(1530, 384, 91, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_useTime.setFont(font)
        self.label_useTime.setObjectName("label_useTime")
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setGeometry(QtCore.QRect(1535, 630, 86, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_class.setFont(font)
        self.label_class.setObjectName("label_class")
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(1480, 384, 38, 38))
        self.label_picTime.setStyleSheet("border-image: url(:/newPrefix/images_test/net_speed.png);")
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(1480, 620, 41, 41))
        self.label_picResult.setStyleSheet("border-image: url(:/newPrefix/images_test/result.png);")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        self.label_display = QtWidgets.QLabel(self.centralwidget)
        self.label_display.setGeometry(QtCore.QRect(300, 270, 1152, 648))
        self.label_display.setMinimumSize(QtCore.QSize(1152, 648))
        self.label_display.setMaximumSize(QtCore.QSize(1152, 648))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_display.setFont(font)
        self.label_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_display.setStyleSheet("border-image: url(:/newPrefix/images_test/ini-image.png);")
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.textEdit_model = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_model.setGeometry(QtCore.QRect(50, 277, 240, 30))
        self.textEdit_model.setMinimumSize(QtCore.QSize(240, 30))
        self.textEdit_model.setMaximumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_model.setFont(font)
        self.textEdit_model.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color: rgb(0, 170, 255);")
        self.textEdit_model.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_model.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_model.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_model.setReadOnly(True)
        self.textEdit_model.setObjectName("textEdit_model")
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(0, 412, 50, 40))
        self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setStyleSheet("background-color: transparent;")
        self.toolButton_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/recovery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon1)
        self.toolButton_file.setIconSize(QtCore.QSize(50, 40))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_file")
        self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_camera.setGeometry(QtCore.QRect(50, 347, 240, 30))
        self.textEdit_camera.setMinimumSize(QtCore.QSize(240, 30))
        self.textEdit_camera.setMaximumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_camera.setFont(font)
        self.textEdit_camera.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.textEdit_camera.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_camera.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_camera.setReadOnly(True)
        self.textEdit_camera.setObjectName("textEdit_camera")
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(50, 417, 240, 30))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(240, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color: rgb(0, 170, 255);")
        self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_camera.setGeometry(QtCore.QRect(0, 337, 50, 45))
        self.toolButton_camera.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_camera.setAutoFillBackground(False)
        self.toolButton_camera.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.toolButton_camera.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_camera.setIcon(icon2)
        self.toolButton_camera.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_camera.setAutoRaise(False)
        self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_camera.setObjectName("toolButton_camera")
        self.toolButton_model = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_model.setGeometry(QtCore.QRect(0, 267, 50, 40))
        self.toolButton_model.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton_model.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_model.setAutoFillBackground(False)
        self.toolButton_model.setStyleSheet("background-color: transparent;")
        self.toolButton_model.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/folder_web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_model.setIcon(icon3)
        self.toolButton_model.setIconSize(QtCore.QSize(50, 40))
        self.toolButton_model.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_model.setAutoRaise(False)
        self.toolButton_model.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_model.setObjectName("toolButton_model")
        self.label_time_result = QtWidgets.QLabel(self.centralwidget)
        self.label_time_result.setGeometry(QtCore.QRect(1610, 390, 90, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_time_result.setFont(font)
        self.label_time_result.setObjectName("label_time_result")
        self.label_class_result = QtWidgets.QLabel(self.centralwidget)
        self.label_class_result.setGeometry(QtCore.QRect(1614, 628, 215, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_class_result.setFont(font)
        self.label_class_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_class_result.setObjectName("label_class_result")
        self.label_pic_detection = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_detection.setGeometry(QtCore.QRect(190, 711, 46, 51))
        self.label_pic_detection.setStyleSheet("border-image: url(:/newPrefix/images_test/Cute_Vehicle.png);")
        self.label_pic_detection.setText("")
        self.label_pic_detection.setObjectName("label_pic_detection")
        self.radioButton_detection = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_detection.setGeometry(QtCore.QRect(60, 716, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.radioButton_detection.setFont(font)
        self.radioButton_detection.setObjectName("radioButton_detection")
        self.radioButton_tracking = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_tracking.setGeometry(QtCore.QRect(60, 776, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.radioButton_tracking.setFont(font)
        self.radioButton_tracking.setObjectName("radioButton_tracking")
        self.radioButton_countting = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_countting.setGeometry(QtCore.QRect(60, 836, 121, 41))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.radioButton_countting.setFont(font)
        self.radioButton_countting.setObjectName("radioButton_countting")
        self.label_pic_tracking = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_tracking.setGeometry(QtCore.QRect(190, 776, 41, 41))
        self.label_pic_tracking.setStyleSheet("border-image: url(:/newPrefix/images_test/tracking.png);")
        self.label_pic_tracking.setText("")
        self.label_pic_tracking.setObjectName("label_pic_tracking")
        self.label_pic_coutting = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_coutting.setGeometry(QtCore.QRect(190, 836, 41, 41))
        self.label_pic_coutting.setStyleSheet("border-image: url(:/newPrefix/images_test/tally.png);")
        self.label_pic_coutting.setText("")
        self.label_pic_coutting.setObjectName("label_pic_coutting")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 676, 291, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(560, 50, 671, 51))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: italic 26pt \"隶书\";")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 886, 291, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(10, 556, 251, 121))
        self.label_pic.setStyleSheet("border-image: url(:/newPrefix/images_test/person.png);")
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        self.label_picNumber = QtWidgets.QLabel(self.centralwidget)
        self.label_picNumber.setGeometry(QtCore.QRect(1480, 460, 41, 41))
        self.label_picNumber.setStyleSheet("border-image: url(:/newPrefix/images_test/count.png);")
        self.label_picNumber.setText("")
        self.label_picNumber.setObjectName("label_picNumber")
        self.label_objNum = QtWidgets.QLabel(self.centralwidget)
        self.label_objNum.setGeometry(QtCore.QRect(1530, 470, 131, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_objNum.setFont(font)
        self.label_objNum.setObjectName("label_objNum")
        self.label_numer_result = QtWidgets.QLabel(self.centralwidget)
        self.label_numer_result.setGeometry(QtCore.QRect(1660, 465, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_numer_result.setFont(font)
        self.label_numer_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_numer_result.setObjectName("label_numer_result")
        self.comboBox_select = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_select.setGeometry(QtCore.QRect(1530, 560, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.comboBox_select.setFont(font)
        self.comboBox_select.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox_select.setStyleSheet("color: rgb(43, 89, 124);\n"
"font: italic 12pt \"Consolas\";")
        self.comboBox_select.setIconSize(QtCore.QSize(36, 36))
        self.comboBox_select.setObjectName("comboBox_select")
        self.comboBox_select.addItem("")
        self.label_picSelect = QtWidgets.QLabel(self.centralwidget)
        self.label_picSelect.setGeometry(QtCore.QRect(1475, 550, 51, 51))
        self.label_picSelect.setStyleSheet("border-image: url(:/newPrefix/images_test/selection.png);")
        self.label_picSelect.setText("")
        self.label_picSelect.setObjectName("label_picSelect")
        self.label_conf = QtWidgets.QLabel(self.centralwidget)
        self.label_conf.setGeometry(QtCore.QRect(1535, 700, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_conf.setFont(font)
        self.label_conf.setObjectName("label_conf")
        self.label_picConf = QtWidgets.QLabel(self.centralwidget)
        self.label_picConf.setGeometry(QtCore.QRect(1480, 690, 41, 41))
        self.label_picConf.setStyleSheet("border-image: url(:/newPrefix/images_test/Score.png);")
        self.label_picConf.setText("")
        self.label_picConf.setObjectName("label_picConf")
        self.label_score_result = QtWidgets.QLabel(self.centralwidget)
        self.label_score_result.setGeometry(QtCore.QRect(1638, 698, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_score_result.setFont(font)
        self.label_score_result.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_score_result.setObjectName("label_score_result")
        self.label_picLocation = QtWidgets.QLabel(self.centralwidget)
        self.label_picLocation.setGeometry(QtCore.QRect(1480, 780, 41, 41))
        self.label_picLocation.setStyleSheet("border-image: url(:/newPrefix/images_test/Ordinateur.png);")
        self.label_picLocation.setText("")
        self.label_picLocation.setObjectName("label_picLocation")
        self.label_location = QtWidgets.QLabel(self.centralwidget)
        self.label_location.setGeometry(QtCore.QRect(1530, 790, 131, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label_location.setFont(font)
        self.label_location.setObjectName("label_location")
        self.label_xmin = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin.setGeometry(QtCore.QRect(1480, 840, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_xmin.setFont(font)
        self.label_xmin.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_xmin.setObjectName("label_xmin")
        self.label_xmax = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax.setGeometry(QtCore.QRect(1480, 880, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_xmax.setFont(font)
        self.label_xmax.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_xmax.setObjectName("label_xmax")
        self.label_ymin = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin.setGeometry(QtCore.QRect(1610, 840, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_ymin.setFont(font)
        self.label_ymin.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_ymin.setObjectName("label_ymin")
        self.label_ymax = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax.setGeometry(QtCore.QRect(1610, 880, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_ymax.setFont(font)
        self.label_ymax.setStyleSheet("font: italic 14pt \"Consolas\";")
        self.label_ymax.setObjectName("label_ymax")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1460, 740, 271, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1460, 510, 271, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_website = QtWidgets.QLabel(self.centralwidget)
        self.label_website.setGeometry(QtCore.QRect(770, 170, 231, 31))
        self.label_website.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Times new roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_website.setFont(font)
        self.label_website.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: italic 18pt \"Times new roman\";")
        self.label_website.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_website.setObjectName("label_website")
        self.label_xmin_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin_result.setGeometry(QtCore.QRect(1545, 840, 51, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_xmin_result.setFont(font)
        self.label_xmin_result.setObjectName("label_xmin_result")
        self.label_ymin_result = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin_result.setGeometry(QtCore.QRect(1675, 840, 51, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_ymin_result.setFont(font)
        self.label_ymin_result.setObjectName("label_ymin_result")
        self.label_xmax_result = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax_result.setGeometry(QtCore.QRect(1545, 880, 51, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_xmax_result.setFont(font)
        self.label_xmax_result.setObjectName("label_xmax_result")
        self.label_ymax_result = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax_result.setGeometry(QtCore.QRect(1675, 880, 51, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_ymax_result.setFont(font)
        self.label_ymax_result.setObjectName("label_ymax_result")
        self.label_pic_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_pic_2.setGeometry(QtCore.QRect(1, 1, 161, 51))
        self.label_pic_2.setStyleSheet("border-image: url(:/newPrefix/images_test/menu.png);")
        self.label_pic_2.setText("")
        self.label_pic_2.setObjectName("label_pic_2")
        self.toolButton_saveing = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_saveing.setGeometry(QtCore.QRect(11, 11, 31, 26))
        self.toolButton_saveing.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_saveing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_saveing.setAutoFillBackground(False)
        self.toolButton_saveing.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.toolButton_saveing.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_saveing.setIcon(icon4)
        self.toolButton_saveing.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_saveing.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_saveing.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_saveing.setAutoRaise(False)
        self.toolButton_saveing.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_saveing.setObjectName("toolButton_saveing")
        self.toolButton_version = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_version.setGeometry(QtCore.QRect(118, 12, 31, 26))
        self.toolButton_version.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_version.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_version.setAutoFillBackground(False)
        self.toolButton_version.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.toolButton_version.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/versions.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_version.setIcon(icon5)
        self.toolButton_version.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_version.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_version.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_version.setAutoRaise(False)
        self.toolButton_version.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_version.setObjectName("toolButton_version")
        self.toolButton_author = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_author.setGeometry(QtCore.QRect(81, 11, 31, 26))
        self.toolButton_author.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_author.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_author.setAutoFillBackground(False)
        self.toolButton_author.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.toolButton_author.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/author.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_author.setIcon(icon6)
        self.toolButton_author.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_author.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_author.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_author.setAutoRaise(False)
        self.toolButton_author.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_author.setObjectName("toolButton_author")
        self.toolButton_settings = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_settings.setGeometry(QtCore.QRect(40, 8, 41, 31))
        self.toolButton_settings.setMaximumSize(QtCore.QSize(50, 45))
        self.toolButton_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_settings.setAutoFillBackground(False)
        self.toolButton_settings.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color:rgb(0, 170, 255);")
        self.toolButton_settings.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_settings.setIcon(icon7)
        self.toolButton_settings.setIconSize(QtCore.QSize(50, 39))
        self.toolButton_settings.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_settings.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_settings.setAutoRaise(False)
        self.toolButton_settings.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_settings.setObjectName("toolButton_settings")
        self.textEdit_video = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_video.setGeometry(QtCore.QRect(50, 486, 240, 30))
        self.textEdit_video.setMinimumSize(QtCore.QSize(240, 30))
        self.textEdit_video.setMaximumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_video.setFont(font)
        self.textEdit_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_video.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(0, 170, 255);\n"
"color: rgb(0, 170, 255);")
        self.textEdit_video.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_video.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_video.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_video.setReadOnly(True)
        self.textEdit_video.setObjectName("textEdit_video")
        self.toolButton_video = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_video.setGeometry(QtCore.QRect(0, 482, 50, 39))
        self.toolButton_video.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_video.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_video.setAutoFillBackground(False)
        self.toolButton_video.setStyleSheet("background-color: transparent;")
        self.toolButton_video.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/images_test/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_video.setIcon(icon8)
        self.toolButton_video.setIconSize(QtCore.QSize(33, 33))
        self.toolButton_video.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_video.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_video.setAutoRaise(False)
        self.toolButton_video.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_video.setObjectName("toolButton_video")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detection Tracking v1.0（思绪无限）"))
        self.label_author.setToolTip(_translate("MainWindow", "<html><head/><body><p>思绪无限（邮箱：sixuwuxian@aliyun.com）</p></body></html>"))
        self.label_author.setText(_translate("MainWindow", "思绪无限"))
        self.label_useTime.setText(_translate("MainWindow", "<html><head/><body><p>用时：</p></body></html>"))
        self.label_class.setText(_translate("MainWindow", "<html><head/><body><p>类别：<br/></p></body></html>"))
        self.label_display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit_model.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择模型</span></p></body></html>"))
        self.textEdit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">实时摄像未开启</span></p></body></html>"))
        self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择图片文件</span></p></body></html>"))
        self.label_time_result.setText(_translate("MainWindow", "0 s"))
        self.label_class_result.setText(_translate("MainWindow", "None"))
        self.radioButton_detection.setText(_translate("MainWindow", "目标检测"))
        self.radioButton_tracking.setText(_translate("MainWindow", "目标跟踪"))
        self.radioButton_countting.setText(_translate("MainWindow", "跟踪计数"))
        self.label_title.setToolTip(_translate("MainWindow", "<html><head/><body><p>version: v1.0</p><p>author: 思绪无限</p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "车辆行人检测与跟踪系统 v1.0"))
        self.label_objNum.setText(_translate("MainWindow", "<html><head/><body><p>目标数目：<br/></p></body></html>"))
        self.label_numer_result.setText(_translate("MainWindow", "0"))
        self.comboBox_select.setCurrentText(_translate("MainWindow", "所有目标"))
        self.comboBox_select.setItemText(0, _translate("MainWindow", "所有目标"))
        self.label_conf.setText(_translate("MainWindow", "<html><head/><body><p>置信度：<br/></p></body></html>"))
        self.label_score_result.setText(_translate("MainWindow", "0"))
        self.label_location.setText(_translate("MainWindow", "<html><head/><body><p>位 置：<br/></p></body></html>"))
        self.label_xmin.setText(_translate("MainWindow", "xmin: "))
        self.label_xmax.setText(_translate("MainWindow", "xmax: "))
        self.label_ymin.setText(_translate("MainWindow", "ymin: "))
        self.label_ymax.setText(_translate("MainWindow", "ymax: "))
        self.label_website.setToolTip(_translate("MainWindow", "<html><head/><body><p>wuxian.blog.csdn.net</p><p>www.wxblog.net</p></body></html>"))
        self.label_website.setText(_translate("MainWindow", "wuxian.blog.csdn.net"))
        self.label_xmin_result.setText(_translate("MainWindow", "0"))
        self.label_ymin_result.setText(_translate("MainWindow", "0"))
        self.label_xmax_result.setText(_translate("MainWindow", "0"))
        self.label_ymax_result.setText(_translate("MainWindow", "0"))
        self.textEdit_video.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择视频文件</span></p></body></html>"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))
import image1_rc
