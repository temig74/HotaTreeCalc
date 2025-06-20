# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tree_calc.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(875, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(875, 700))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setIconSize(QSize(64, 64))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.cmb_language = QComboBox(self.centralwidget)
        self.cmb_language.setObjectName(u"cmb_language")

        self.verticalLayout.addWidget(self.cmb_language)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.label)

        self.cmb_hero_class = QComboBox(self.centralwidget)
        self.cmb_hero_class.setObjectName(u"cmb_hero_class")
        self.cmb_hero_class.setMinimumSize(QSize(112, 0))
        self.cmb_hero_class.setMaximumSize(QSize(90, 16777215))
        self.cmb_hero_class.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.cmb_hero_class)

        self.btn_ban_skill = QPushButton(self.centralwidget)
        self.btn_ban_skill.setObjectName(u"btn_ban_skill")
        self.btn_ban_skill.setMinimumSize(QSize(112, 0))
        self.btn_ban_skill.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.btn_ban_skill)

        self.cmb_ban_skill = QComboBox(self.centralwidget)
        self.cmb_ban_skill.setObjectName(u"cmb_ban_skill")
        self.cmb_ban_skill.setMinimumSize(QSize(112, 25))
        self.cmb_ban_skill.setMaximumSize(QSize(90, 16777215))
        font = QFont()
        font.setPointSize(8)
        self.cmb_ban_skill.setFont(font)
        self.cmb_ban_skill.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.cmb_ban_skill)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lw_banned_skills = QListWidget(self.centralwidget)
        self.lw_banned_skills.setObjectName(u"lw_banned_skills")
        self.lw_banned_skills.setMinimumSize(QSize(112, 0))
        self.lw_banned_skills.setMaximumSize(QSize(90, 16777215))
        self.lw_banned_skills.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.lw_banned_skills)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout.addWidget(self.label_14)

        self.lw_tree_numbers = QListWidget(self.centralwidget)
        self.lw_tree_numbers.setObjectName(u"lw_tree_numbers")
        self.lw_tree_numbers.setMinimumSize(QSize(112, 0))
        self.lw_tree_numbers.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.lw_tree_numbers)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(750, 500))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(6, 6, 495, 149))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.cmb_start_1 = QComboBox(self.layoutWidget)
        self.cmb_start_1.setObjectName(u"cmb_start_1")
        self.cmb_start_1.setMinimumSize(QSize(120, 33))
        self.cmb_start_1.setFont(font)
        self.cmb_start_1.setStyleSheet(u"")
        self.cmb_start_1.setIconSize(QSize(33, 33))

        self.horizontalLayout_3.addWidget(self.cmb_start_1)

        self.cmb_start1_level = QComboBox(self.layoutWidget)
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.setObjectName(u"cmb_start1_level")
        self.cmb_start1_level.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.cmb_start1_level)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.cmb_start_2 = QComboBox(self.layoutWidget)
        self.cmb_start_2.setObjectName(u"cmb_start_2")
        self.cmb_start_2.setMinimumSize(QSize(120, 33))
        self.cmb_start_2.setFont(font)
        self.cmb_start_2.setStyleSheet(u"")
        self.cmb_start_2.setIconSize(QSize(33, 33))

        self.horizontalLayout_3.addWidget(self.cmb_start_2)

        self.cmb_start2_level = QComboBox(self.layoutWidget)
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.setObjectName(u"cmb_start2_level")
        self.cmb_start2_level.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.cmb_start2_level)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cmb_pri_2 = QComboBox(self.layoutWidget)
        self.cmb_pri_2.addItem("")
        self.cmb_pri_2.addItem("")
        self.cmb_pri_2.addItem("")
        self.cmb_pri_2.addItem("")
        self.cmb_pri_2.setObjectName(u"cmb_pri_2")
        self.cmb_pri_2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.cmb_pri_2)

        self.cmb_left2 = QComboBox(self.layoutWidget)
        self.cmb_left2.setObjectName(u"cmb_left2")
        self.cmb_left2.setMinimumSize(QSize(120, 33))
        self.cmb_left2.setMaximumSize(QSize(50, 16777215))
        self.cmb_left2.setFont(font)
        self.cmb_left2.setStyleSheet(u"")
        self.cmb_left2.setIconSize(QSize(33, 33))

        self.horizontalLayout_4.addWidget(self.cmb_left2)

        self.cmb_right2 = QComboBox(self.layoutWidget)
        self.cmb_right2.setObjectName(u"cmb_right2")
        self.cmb_right2.setMinimumSize(QSize(120, 33))
        self.cmb_right2.setFont(font)
        self.cmb_right2.setStyleSheet(u"")
        self.cmb_right2.setIconSize(QSize(33, 33))

        self.horizontalLayout_4.addWidget(self.cmb_right2)

        self.cmb_choice2 = QComboBox(self.layoutWidget)
        self.cmb_choice2.addItem("")
        self.cmb_choice2.addItem("")
        self.cmb_choice2.setObjectName(u"cmb_choice2")
        self.cmb_choice2.setMinimumSize(QSize(50, 0))
        self.cmb_choice2.setMaximumSize(QSize(50, 16777215))
        self.cmb_choice2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.cmb_choice2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cb_levelup3 = QCheckBox(self.layoutWidget)
        self.cb_levelup3.setObjectName(u"cb_levelup3")
        self.cb_levelup3.setChecked(False)

        self.horizontalLayout_5.addWidget(self.cb_levelup3)

        self.cmb_pri_3 = QComboBox(self.layoutWidget)
        self.cmb_pri_3.addItem("")
        self.cmb_pri_3.addItem("")
        self.cmb_pri_3.addItem("")
        self.cmb_pri_3.addItem("")
        self.cmb_pri_3.setObjectName(u"cmb_pri_3")
        self.cmb_pri_3.setEnabled(False)
        self.cmb_pri_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.cmb_pri_3)

        self.cmb_left3 = QComboBox(self.layoutWidget)
        self.cmb_left3.setObjectName(u"cmb_left3")
        self.cmb_left3.setEnabled(False)
        self.cmb_left3.setMinimumSize(QSize(120, 33))
        self.cmb_left3.setFont(font)
        self.cmb_left3.setStyleSheet(u"")
        self.cmb_left3.setIconSize(QSize(33, 33))

        self.horizontalLayout_5.addWidget(self.cmb_left3)

        self.cmb_right3 = QComboBox(self.layoutWidget)
        self.cmb_right3.setObjectName(u"cmb_right3")
        self.cmb_right3.setEnabled(False)
        self.cmb_right3.setMinimumSize(QSize(120, 33))
        self.cmb_right3.setFont(font)
        self.cmb_right3.setStyleSheet(u"")
        self.cmb_right3.setIconSize(QSize(33, 33))

        self.horizontalLayout_5.addWidget(self.cmb_right3)

        self.cmb_choice3 = QComboBox(self.layoutWidget)
        self.cmb_choice3.addItem("")
        self.cmb_choice3.addItem("")
        self.cmb_choice3.setObjectName(u"cmb_choice3")
        self.cmb_choice3.setEnabled(False)
        self.cmb_choice3.setMaximumSize(QSize(50, 16777215))
        self.cmb_choice3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.cmb_choice3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.btn_get_trees = QPushButton(self.layoutWidget)
        self.btn_get_trees.setObjectName(u"btn_get_trees")

        self.verticalLayout_2.addWidget(self.btn_get_trees)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 250))
        self.groupBox.setMaximumSize(QSize(200, 240))
        self.groupBox.setCheckable(False)
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(7, 19, 183, 223))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.cmb_skill1 = QComboBox(self.layoutWidget1)
        self.cmb_skill1.setObjectName(u"cmb_skill1")
        self.cmb_skill1.setMinimumSize(QSize(115, 25))
        self.cmb_skill1.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill1.setFont(font)
        self.cmb_skill1.setStyleSheet(u"")
        self.cmb_skill1.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cmb_skill1)

        self.cmb_skill1_level = QComboBox(self.layoutWidget1)
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.setObjectName(u"cmb_skill1_level")
        self.cmb_skill1_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill1_level.setMaximumSize(QSize(60, 16777215))
        self.cmb_skill1_level.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmb_skill1_level)

        self.cmb_skill2 = QComboBox(self.layoutWidget1)
        self.cmb_skill2.setObjectName(u"cmb_skill2")
        self.cmb_skill2.setMinimumSize(QSize(115, 25))
        self.cmb_skill2.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill2.setFont(font)
        self.cmb_skill2.setStyleSheet(u"")
        self.cmb_skill2.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cmb_skill2)

        self.cmb_skill2_level = QComboBox(self.layoutWidget1)
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.setObjectName(u"cmb_skill2_level")
        self.cmb_skill2_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill2_level.setMaximumSize(QSize(60, 16777215))
        self.cmb_skill2_level.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cmb_skill2_level)

        self.cmb_skill3 = QComboBox(self.layoutWidget1)
        self.cmb_skill3.setObjectName(u"cmb_skill3")
        self.cmb_skill3.setMinimumSize(QSize(115, 25))
        self.cmb_skill3.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill3.setFont(font)
        self.cmb_skill3.setStyleSheet(u"")
        self.cmb_skill3.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cmb_skill3)

        self.cmb_skill3_level = QComboBox(self.layoutWidget1)
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.setObjectName(u"cmb_skill3_level")
        self.cmb_skill3_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill3_level.setMaximumSize(QSize(60, 16777215))
        self.cmb_skill3_level.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cmb_skill3_level)

        self.cmb_skill4 = QComboBox(self.layoutWidget1)
        self.cmb_skill4.setObjectName(u"cmb_skill4")
        self.cmb_skill4.setMinimumSize(QSize(115, 25))
        self.cmb_skill4.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill4.setFont(font)
        self.cmb_skill4.setStyleSheet(u"")
        self.cmb_skill4.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.cmb_skill4)

        self.cmb_skill4_level = QComboBox(self.layoutWidget1)
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.setObjectName(u"cmb_skill4_level")
        self.cmb_skill4_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill4_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cmb_skill4_level)

        self.cmb_skill5 = QComboBox(self.layoutWidget1)
        self.cmb_skill5.setObjectName(u"cmb_skill5")
        self.cmb_skill5.setMinimumSize(QSize(115, 25))
        self.cmb_skill5.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill5.setFont(font)
        self.cmb_skill5.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cmb_skill5)

        self.cmb_skill5_level = QComboBox(self.layoutWidget1)
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.setObjectName(u"cmb_skill5_level")
        self.cmb_skill5_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill5_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cmb_skill5_level)

        self.cmb_skill6 = QComboBox(self.layoutWidget1)
        self.cmb_skill6.setObjectName(u"cmb_skill6")
        self.cmb_skill6.setMinimumSize(QSize(115, 25))
        self.cmb_skill6.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill6.setFont(font)
        self.cmb_skill6.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.cmb_skill6)

        self.cmb_skill6_level = QComboBox(self.layoutWidget1)
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.setObjectName(u"cmb_skill6_level")
        self.cmb_skill6_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill6_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cmb_skill6_level)

        self.cmb_skill7 = QComboBox(self.layoutWidget1)
        self.cmb_skill7.setObjectName(u"cmb_skill7")
        self.cmb_skill7.setMinimumSize(QSize(115, 25))
        self.cmb_skill7.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill7.setFont(font)
        self.cmb_skill7.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.cmb_skill7)

        self.cmb_skill7_level = QComboBox(self.layoutWidget1)
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.setObjectName(u"cmb_skill7_level")
        self.cmb_skill7_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill7_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cmb_skill7_level)

        self.cmb_skill8 = QComboBox(self.layoutWidget1)
        self.cmb_skill8.setObjectName(u"cmb_skill8")
        self.cmb_skill8.setMinimumSize(QSize(115, 25))
        self.cmb_skill8.setMaximumSize(QSize(16777215, 25))
        self.cmb_skill8.setFont(font)
        self.cmb_skill8.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.cmb_skill8)

        self.cmb_skill8_level = QComboBox(self.layoutWidget1)
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.setObjectName(u"cmb_skill8_level")
        self.cmb_skill8_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill8_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.cmb_skill8_level)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8.setWordWrap(True)

        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 4)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)

        self.sb_cur_level = QSpinBox(self.groupBox_2)
        self.sb_cur_level.setObjectName(u"sb_cur_level")
        self.sb_cur_level.setMaximumSize(QSize(40, 16777215))
        self.sb_cur_level.setMinimum(1)
        self.sb_cur_level.setMaximum(30)

        self.gridLayout.addWidget(self.sb_cur_level, 0, 6, 1, 2)

        self.sb_tree_num = QSpinBox(self.groupBox_2)
        self.sb_tree_num.setObjectName(u"sb_tree_num")
        self.sb_tree_num.setMaximumSize(QSize(40, 16777215))
        self.sb_tree_num.setMinimum(1)
        self.sb_tree_num.setMaximum(255)

        self.gridLayout.addWidget(self.sb_tree_num, 0, 2, 1, 1)

        self.sb_wisdom_counter = QSpinBox(self.groupBox_2)
        self.sb_wisdom_counter.setObjectName(u"sb_wisdom_counter")
        self.sb_wisdom_counter.setMaximumSize(QSize(40, 16777215))
        self.sb_wisdom_counter.setMinimum(0)
        self.sb_wisdom_counter.setMaximum(30)
        self.sb_wisdom_counter.setValue(0)

        self.gridLayout.addWidget(self.sb_wisdom_counter, 1, 6, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9.setWordWrap(True)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 2, 1)

        self.sb_magic_counter = QSpinBox(self.groupBox_2)
        self.sb_magic_counter.setObjectName(u"sb_magic_counter")
        self.sb_magic_counter.setMaximumSize(QSize(40, 16777215))
        self.sb_magic_counter.setMinimum(0)
        self.sb_magic_counter.setMaximum(30)
        self.sb_magic_counter.setValue(0)

        self.gridLayout.addWidget(self.sb_magic_counter, 2, 6, 1, 2)

        self.sb_learning_level = QSpinBox(self.groupBox_2)
        self.sb_learning_level.setObjectName(u"sb_learning_level")
        self.sb_learning_level.setValue(1)

        self.gridLayout.addWidget(self.sb_learning_level, 3, 6, 1, 2)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_13.setWordWrap(True)

        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 4)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.sb_attack = QSpinBox(self.groupBox_2)
        self.sb_attack.setObjectName(u"sb_attack")
        self.sb_attack.setMinimumSize(QSize(37, 0))
        self.sb_attack.setMaximumSize(QSize(40, 16777215))
        self.sb_attack.setValue(2)

        self.horizontalLayout_8.addWidget(self.sb_attack)

        self.sb_defence = QSpinBox(self.groupBox_2)
        self.sb_defence.setObjectName(u"sb_defence")
        self.sb_defence.setMinimumSize(QSize(37, 0))
        self.sb_defence.setMaximumSize(QSize(40, 16777215))
        self.sb_defence.setValue(2)

        self.horizontalLayout_8.addWidget(self.sb_defence)

        self.sb_sp = QSpinBox(self.groupBox_2)
        self.sb_sp.setObjectName(u"sb_sp")
        self.sb_sp.setMinimumSize(QSize(37, 0))
        self.sb_sp.setMaximumSize(QSize(40, 16777215))
        self.sb_sp.setMinimum(1)

        self.horizontalLayout_8.addWidget(self.sb_sp)

        self.sb_knowledge = QSpinBox(self.groupBox_2)
        self.sb_knowledge.setObjectName(u"sb_knowledge")
        self.sb_knowledge.setMinimumSize(QSize(37, 0))
        self.sb_knowledge.setMaximumSize(QSize(40, 16777215))
        self.sb_knowledge.setMinimum(1)

        self.horizontalLayout_8.addWidget(self.sb_knowledge)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.btn_build_tree = QPushButton(self.groupBox_2)
        self.btn_build_tree.setObjectName(u"btn_build_tree")
        self.btn_build_tree.setMinimumSize(QSize(0, 25))
        self.btn_build_tree.setMaximumSize(QSize(100, 25))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_build_tree.setFont(font1)

        self.horizontalLayout_6.addWidget(self.btn_build_tree)

        self.btn_export_all_trees = QPushButton(self.groupBox_2)
        self.btn_export_all_trees.setObjectName(u"btn_export_all_trees")
        self.btn_export_all_trees.setMinimumSize(QSize(0, 25))
        self.btn_export_all_trees.setMaximumSize(QSize(100, 25))
        font2 = QFont()
        font2.setPointSize(9)
        self.btn_export_all_trees.setFont(font2)

        self.horizontalLayout_6.addWidget(self.btn_export_all_trees)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(200, 230))
        self.groupBox_3.setMaximumSize(QSize(200, 1000))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.btn_find_way = QPushButton(self.groupBox_3)
        self.btn_find_way.setObjectName(u"btn_find_way")

        self.verticalLayout_4.addWidget(self.btn_find_way)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_add_wanted = QPushButton(self.groupBox_3)
        self.btn_add_wanted.setObjectName(u"btn_add_wanted")

        self.horizontalLayout_9.addWidget(self.btn_add_wanted)

        self.btn_add_unwanted = QPushButton(self.groupBox_3)
        self.btn_add_unwanted.setObjectName(u"btn_add_unwanted")

        self.horizontalLayout_9.addWidget(self.btn_add_unwanted)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cmb_wanted_unwanted = QComboBox(self.groupBox_3)
        self.cmb_wanted_unwanted.setObjectName(u"cmb_wanted_unwanted")
        self.cmb_wanted_unwanted.setMinimumSize(QSize(120, 0))
        self.cmb_wanted_unwanted.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_7.addWidget(self.cmb_wanted_unwanted)

        self.cmb_wanted_unwanted_level = QComboBox(self.groupBox_3)
        self.cmb_wanted_unwanted_level.addItem("")
        self.cmb_wanted_unwanted_level.addItem("")
        self.cmb_wanted_unwanted_level.addItem("")
        self.cmb_wanted_unwanted_level.setObjectName(u"cmb_wanted_unwanted_level")
        self.cmb_wanted_unwanted_level.setMinimumSize(QSize(60, 0))
        self.cmb_wanted_unwanted_level.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_7.addWidget(self.cmb_wanted_unwanted_level)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.lw_wanted_skills = QListWidget(self.groupBox_3)
        self.lw_wanted_skills.setObjectName(u"lw_wanted_skills")
        self.lw_wanted_skills.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.lw_wanted_skills)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.lw_unwanted_skills = QListWidget(self.groupBox_3)
        self.lw_unwanted_skills.setObjectName(u"lw_unwanted_skills")
        self.lw_unwanted_skills.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.lw_unwanted_skills)


        self.verticalLayout_6.addWidget(self.groupBox_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.tw_skills = QTreeWidget(self.tab_2)
        self.tw_skills.setObjectName(u"tw_skills")
        sizePolicy2.setHeightForWidth(self.tw_skills.sizePolicy().hasHeightForWidth())
        self.tw_skills.setSizePolicy(sizePolicy2)
        self.tw_skills.setMinimumSize(QSize(0, 450))
        self.tw_skills.setStyleSheet(u"")
        self.tw_skills.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tw_skills.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.tw_skills)

        self.te_skill_ways = QTextEdit(self.tab_2)
        self.te_skill_ways.setObjectName(u"te_skill_ways")
        self.te_skill_ways.setEnabled(True)
        self.te_skill_ways.setMaximumSize(QSize(16777215, 70))
        self.te_skill_ways.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.te_skill_ways)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 721, 611))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_15.setFont(font3)
        self.label_15.setWordWrap(True)
        self.label_15.setOpenExternalLinks(True)
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.cmb_start1_level.setCurrentIndex(1)
        self.cmb_start2_level.setCurrentIndex(1)
        self.cmb_skill1_level.setCurrentIndex(1)
        self.cmb_skill2_level.setCurrentIndex(0)
        self.cmb_skill3_level.setCurrentIndex(0)
        self.cmb_skill4_level.setCurrentIndex(0)
        self.cmb_skill5_level.setCurrentIndex(0)
        self.cmb_skill6_level.setCurrentIndex(0)
        self.cmb_skill7_level.setCurrentIndex(0)
        self.cmb_skill8_level.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hota tree calc 1.08", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hero class", None))
        self.btn_ban_skill.setText(QCoreApplication.translate("MainWindow", u"Ban skill:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Banned skills:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tree numbers:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start 1", None))
        self.cmb_start1_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_start1_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_start1_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_start1_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Start 2", None))
        self.cmb_start2_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_start2_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_start2_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_start2_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2 levelup", None))
        self.cmb_pri_2.setItemText(0, QCoreApplication.translate("MainWindow", u"attack", None))
        self.cmb_pri_2.setItemText(1, QCoreApplication.translate("MainWindow", u"defence", None))
        self.cmb_pri_2.setItemText(2, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cmb_pri_2.setItemText(3, QCoreApplication.translate("MainWindow", u"knowledge", None))

        self.cmb_choice2.setItemText(0, QCoreApplication.translate("MainWindow", u"left", None))
        self.cmb_choice2.setItemText(1, QCoreApplication.translate("MainWindow", u"right", None))

        self.cb_levelup3.setText(QCoreApplication.translate("MainWindow", u"3 levelup", None))
        self.cmb_pri_3.setItemText(0, QCoreApplication.translate("MainWindow", u"attack", None))
        self.cmb_pri_3.setItemText(1, QCoreApplication.translate("MainWindow", u"defence", None))
        self.cmb_pri_3.setItemText(2, QCoreApplication.translate("MainWindow", u"sp", None))
        self.cmb_pri_3.setItemText(3, QCoreApplication.translate("MainWindow", u"knowledge", None))

        self.cmb_choice3.setItemText(0, QCoreApplication.translate("MainWindow", u"left", None))
        self.cmb_choice3.setItemText(1, QCoreApplication.translate("MainWindow", u"right", None))

        self.btn_get_trees.setText(QCoreApplication.translate("MainWindow", u"Find trees", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Get tree number", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Current skills:", None))
        self.cmb_skill1_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill1_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill1_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill1_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill2_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill2_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill2_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill2_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill3_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill3_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill3_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill3_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill4_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill4_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill4_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill4_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill5_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill5_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill5_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill5_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill6_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill6_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill6_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill6_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill7_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill7_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill7_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill7_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.cmb_skill8_level.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cmb_skill8_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill8_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill8_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.groupBox_2.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Last level wisdom given", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cur. level", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tree \u2116", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Last level magic given", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Last level learning adv.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PRIM", None))
        self.btn_build_tree.setText(QCoreApplication.translate("MainWindow", u"Build tree", None))
        self.btn_export_all_trees.setText(QCoreApplication.translate("MainWindow", u"Export all trees", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Way finder", None))
        self.btn_find_way.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.btn_add_wanted.setText(QCoreApplication.translate("MainWindow", u"Add wanted", None))
        self.btn_add_unwanted.setText(QCoreApplication.translate("MainWindow", u"Add unwanted", None))
        self.cmb_wanted_unwanted_level.setItemText(0, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_wanted_unwanted_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_wanted_unwanted_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Wanted skills:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Unwanted skills:", None))
        ___qtreewidgetitem = self.tw_skills.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Skill Tree", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tree browser", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt; font-weight:696;\">Hota tree calc 1.08</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696;\">Author: Temig (temig7487@gmail.com)</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-w"
                        "eight:696;\">Idea and design based on </span><a href=\"https://handbookhmm.ru/forum/viewtopic.php?f=8&amp;t=42\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">LMOracle.</span></a><span style=\" font-family:'Segoe UI'; font-weight:696;\"> Thanks to it's author - AlexSpl</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696;\">Some information about tree generation can be found </span><a href=\"http://heroescommunity.com/viewthread.php3?TID=17812&amp;pagenumber=12\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">here</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696; color:#ff0101;\">This prog"
                        "ram does NOT interact with Hota memory, it's just a help resource (like </span><a href=\"https://www.heroes3assist.com/\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">Heroes3 assist</span></a><span style=\" font-family:'Segoe UI'; font-weight:696; color:#ff0101;\">) that can calculate tree number from a given first level-ups and build a specific tree.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:696;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696;\">Another useful information resources:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://vk.com/fizmig\"><span style"
                        "=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">Fizmig</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:696;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696;\">If you like this program, you can </span><a href=\"https://github.com/temig74/HotaTreeCalc/blob/master/README.md\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">donate</span></a><span style=\" font-family:'Segoe UI'; font-weight:696;\"> author (view readme)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:696;\"><br /></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696;\">Video instructions can be found </span><a href=\"https://www.youtube.com/@temig74\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">here</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:696;\">Check for new versions </span><a href=\"https://github.com/temig74/HotaTreeCalc/releases\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">here on github</span>"
                        "</a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:696;\">I also inform, that 03.12.2023 </span><a href=\"https://h3hota.com/en/rules\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">rules</span></a><span style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:696;\"> of rated games </span><a href=\"https://forum.heroesworld.ru/showthread.php?t=7340&amp;page=149\"><span style=\" font-family:'Segoe UI'; font-weight:696; text-decoration: underline; color:#0078d4;\">were updated</span></a><span style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:696;\">:</spa"
                        "n></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt; font-weight:696;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:696;\">&quot;Browsing the map content or hero levelling tree with side programs (no matter if they read data from game memory, use side databases, generators or other methods) is the same level of a violation as map-hacking.&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt; font-weight:696;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fam"
                        "ily:'Segoe UI'; font-size:10pt; font-weight:696;\">You can use this program in non-rated games by mutual agreement of both players and for educational purposes.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

