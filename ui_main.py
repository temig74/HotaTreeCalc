# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tree_calc.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(866, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(865, 760))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setIconSize(QSize(64, 64))
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.label)

        self.cmb_hero_class = QComboBox(self.centralwidget)
        self.cmb_hero_class.setObjectName(u"cmb_hero_class")
        self.cmb_hero_class.setMinimumSize(QSize(90, 0))
        self.cmb_hero_class.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.cmb_hero_class)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.label_4)

        self.te_banned_skills = QTextEdit(self.centralwidget)
        self.te_banned_skills.setObjectName(u"te_banned_skills")
        self.te_banned_skills.setMinimumSize(QSize(90, 0))
        self.te_banned_skills.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.te_banned_skills)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout.addWidget(self.label_14)

        self.te_tree_numbers = QTextEdit(self.centralwidget)
        self.te_tree_numbers.setObjectName(u"te_tree_numbers")
        self.te_tree_numbers.setMinimumSize(QSize(90, 0))
        self.te_tree_numbers.setMaximumSize(QSize(90, 16777215))
        self.te_tree_numbers.setReadOnly(True)

        self.verticalLayout.addWidget(self.te_tree_numbers)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(750, 500))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(6, 6, 461, 116))
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
        self.cmb_start_1.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.cmb_start_1)

        self.cmb_start1_level = QComboBox(self.layoutWidget)
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.addItem("")
        self.cmb_start1_level.setObjectName(u"cmb_start1_level")

        self.horizontalLayout_3.addWidget(self.cmb_start1_level)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.cmb_start_2 = QComboBox(self.layoutWidget)
        self.cmb_start_2.setObjectName(u"cmb_start_2")
        self.cmb_start_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.cmb_start_2)

        self.cmb_start2_level = QComboBox(self.layoutWidget)
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.addItem("")
        self.cmb_start2_level.setObjectName(u"cmb_start2_level")

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

        self.horizontalLayout_4.addWidget(self.cmb_pri_2)

        self.cmb_left2 = QComboBox(self.layoutWidget)
        self.cmb_left2.setObjectName(u"cmb_left2")
        self.cmb_left2.setMinimumSize(QSize(115, 0))
        self.cmb_left2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.cmb_left2)

        self.cmb_right2 = QComboBox(self.layoutWidget)
        self.cmb_right2.setObjectName(u"cmb_right2")
        self.cmb_right2.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_4.addWidget(self.cmb_right2)

        self.cmb_choice2 = QComboBox(self.layoutWidget)
        self.cmb_choice2.addItem("")
        self.cmb_choice2.addItem("")
        self.cmb_choice2.setObjectName(u"cmb_choice2")
        self.cmb_choice2.setMinimumSize(QSize(50, 0))
        self.cmb_choice2.setMaximumSize(QSize(50, 16777215))

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

        self.horizontalLayout_5.addWidget(self.cmb_pri_3)

        self.cmb_left3 = QComboBox(self.layoutWidget)
        self.cmb_left3.setObjectName(u"cmb_left3")
        self.cmb_left3.setEnabled(False)
        self.cmb_left3.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_5.addWidget(self.cmb_left3)

        self.cmb_right3 = QComboBox(self.layoutWidget)
        self.cmb_right3.setObjectName(u"cmb_right3")
        self.cmb_right3.setEnabled(False)
        self.cmb_right3.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_5.addWidget(self.cmb_right3)

        self.cmb_choice3 = QComboBox(self.layoutWidget)
        self.cmb_choice3.addItem("")
        self.cmb_choice3.addItem("")
        self.cmb_choice3.setObjectName(u"cmb_choice3")
        self.cmb_choice3.setEnabled(False)
        self.cmb_choice3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.cmb_choice3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.btn_get_trees = QPushButton(self.layoutWidget)
        self.btn_get_trees.setObjectName(u"btn_get_trees")

        self.verticalLayout_2.addWidget(self.btn_get_trees)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(190, 520))
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 171, 251))
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 21, 153, 220))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.cmb_skill1 = QComboBox(self.layoutWidget1)
        self.cmb_skill1.setObjectName(u"cmb_skill1")
        self.cmb_skill1.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cmb_skill1)

        self.cmb_skill1_level = QComboBox(self.layoutWidget1)
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.addItem("")
        self.cmb_skill1_level.setObjectName(u"cmb_skill1_level")
        self.cmb_skill1_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmb_skill1_level)

        self.cmb_skill2 = QComboBox(self.layoutWidget1)
        self.cmb_skill2.setObjectName(u"cmb_skill2")
        self.cmb_skill2.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cmb_skill2)

        self.cmb_skill2_level = QComboBox(self.layoutWidget1)
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.addItem("")
        self.cmb_skill2_level.setObjectName(u"cmb_skill2_level")
        self.cmb_skill2_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cmb_skill2_level)

        self.cmb_skill3 = QComboBox(self.layoutWidget1)
        self.cmb_skill3.setObjectName(u"cmb_skill3")
        self.cmb_skill3.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cmb_skill3)

        self.cmb_skill3_level = QComboBox(self.layoutWidget1)
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.addItem("")
        self.cmb_skill3_level.setObjectName(u"cmb_skill3_level")
        self.cmb_skill3_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cmb_skill3_level)

        self.cmb_skill4 = QComboBox(self.layoutWidget1)
        self.cmb_skill4.setObjectName(u"cmb_skill4")
        self.cmb_skill4.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.cmb_skill4)

        self.cmb_skill4_level = QComboBox(self.layoutWidget1)
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.addItem("")
        self.cmb_skill4_level.setObjectName(u"cmb_skill4_level")
        self.cmb_skill4_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cmb_skill4_level)

        self.cmb_skill5 = QComboBox(self.layoutWidget1)
        self.cmb_skill5.setObjectName(u"cmb_skill5")
        self.cmb_skill5.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cmb_skill5)

        self.cmb_skill5_level = QComboBox(self.layoutWidget1)
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.addItem("")
        self.cmb_skill5_level.setObjectName(u"cmb_skill5_level")
        self.cmb_skill5_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cmb_skill5_level)

        self.cmb_skill6 = QComboBox(self.layoutWidget1)
        self.cmb_skill6.setObjectName(u"cmb_skill6")
        self.cmb_skill6.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.cmb_skill6)

        self.cmb_skill6_level = QComboBox(self.layoutWidget1)
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.addItem("")
        self.cmb_skill6_level.setObjectName(u"cmb_skill6_level")
        self.cmb_skill6_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cmb_skill6_level)

        self.cmb_skill7 = QComboBox(self.layoutWidget1)
        self.cmb_skill7.setObjectName(u"cmb_skill7")
        self.cmb_skill7.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.cmb_skill7)

        self.cmb_skill7_level = QComboBox(self.layoutWidget1)
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.addItem("")
        self.cmb_skill7_level.setObjectName(u"cmb_skill7_level")
        self.cmb_skill7_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cmb_skill7_level)

        self.cmb_skill8 = QComboBox(self.layoutWidget1)
        self.cmb_skill8.setObjectName(u"cmb_skill8")
        self.cmb_skill8.setMinimumSize(QSize(85, 0))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.cmb_skill8)

        self.cmb_skill8_level = QComboBox(self.layoutWidget1)
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.addItem("")
        self.cmb_skill8_level.setObjectName(u"cmb_skill8_level")
        self.cmb_skill8_level.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.cmb_skill8_level)

        self.btn_build_tree = QPushButton(self.groupBox_2)
        self.btn_build_tree.setObjectName(u"btn_build_tree")
        self.btn_build_tree.setGeometry(QRect(10, 490, 171, 24))
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(13, 267, 170, 220))
        self.formLayout_2 = QFormLayout(self.layoutWidget2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.sb_tree_num = QSpinBox(self.layoutWidget2)
        self.sb_tree_num.setObjectName(u"sb_tree_num")
        self.sb_tree_num.setMinimum(1)
        self.sb_tree_num.setMaximum(255)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sb_tree_num)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.sb_cur_level = QSpinBox(self.layoutWidget2)
        self.sb_cur_level.setObjectName(u"sb_cur_level")
        self.sb_cur_level.setMinimum(1)
        self.sb_cur_level.setMaximum(30)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sb_cur_level)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.sb_wisdom_counter = QSpinBox(self.layoutWidget2)
        self.sb_wisdom_counter.setObjectName(u"sb_wisdom_counter")
        self.sb_wisdom_counter.setMinimum(0)
        self.sb_wisdom_counter.setMaximum(30)
        self.sb_wisdom_counter.setValue(0)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.sb_wisdom_counter)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.sb_magic_counter = QSpinBox(self.layoutWidget2)
        self.sb_magic_counter.setObjectName(u"sb_magic_counter")
        self.sb_magic_counter.setMinimum(0)
        self.sb_magic_counter.setMaximum(30)
        self.sb_magic_counter.setValue(0)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.sb_magic_counter)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.sb_attack = QSpinBox(self.layoutWidget2)
        self.sb_attack.setObjectName(u"sb_attack")
        self.sb_attack.setValue(2)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.sb_attack)

        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_11)

        self.sb_defence = QSpinBox(self.layoutWidget2)
        self.sb_defence.setObjectName(u"sb_defence")
        self.sb_defence.setValue(2)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.sb_defence)

        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_12)

        self.sb_sp = QSpinBox(self.layoutWidget2)
        self.sb_sp.setObjectName(u"sb_sp")
        self.sb_sp.setMinimum(1)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.sb_sp)

        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_13)

        self.sb_knowledge = QSpinBox(self.layoutWidget2)
        self.sb_knowledge.setObjectName(u"sb_knowledge")
        self.sb_knowledge.setMinimum(1)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.sb_knowledge)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 520, 171, 71))
        self.cmb_skill_search = QComboBox(self.groupBox_3)
        self.cmb_skill_search.setObjectName(u"cmb_skill_search")
        self.cmb_skill_search.setGeometry(QRect(6, 17, 91, 22))
        self.cmb_skill_search.setMinimumSize(QSize(85, 0))
        self.cmb_skill_search_level = QComboBox(self.groupBox_3)
        self.cmb_skill_search_level.addItem("")
        self.cmb_skill_search_level.addItem("")
        self.cmb_skill_search_level.addItem("")
        self.cmb_skill_search_level.setObjectName(u"cmb_skill_search_level")
        self.cmb_skill_search_level.setGeometry(QRect(106, 17, 60, 22))
        self.cmb_skill_search_level.setMinimumSize(QSize(60, 0))
        self.cmb_skill_search_level.setMaximumSize(QSize(60, 16777215))
        self.btn_find_way = QPushButton(self.groupBox_3)
        self.btn_find_way.setObjectName(u"btn_find_way")
        self.btn_find_way.setGeometry(QRect(5, 42, 161, 24))

        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.tw_skills = QTreeWidget(self.tab_2)
        self.tw_skills.setObjectName(u"tw_skills")
        sizePolicy2.setHeightForWidth(self.tw_skills.sizePolicy().hasHeightForWidth())
        self.tw_skills.setSizePolicy(sizePolicy2)
        self.tw_skills.setMinimumSize(QSize(0, 450))
        self.tw_skills.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tw_skills.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout_2.addWidget(self.tw_skills)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.te_skill_ways = QTextEdit(self.tab_2)
        self.te_skill_ways.setObjectName(u"te_skill_ways")
        self.te_skill_ways.setEnabled(True)
        self.te_skill_ways.setMaximumSize(QSize(16777215, 70))
        self.te_skill_ways.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.te_skill_ways)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 721, 331))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setOpenExternalLinks(True)
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.cmb_start1_level.setCurrentIndex(1)
        self.cmb_start2_level.setCurrentIndex(1)
        self.cmb_skill1_level.setCurrentIndex(1)
        self.cmb_skill2_level.setCurrentIndex(1)
        self.cmb_skill3_level.setCurrentIndex(0)
        self.cmb_skill4_level.setCurrentIndex(0)
        self.cmb_skill5_level.setCurrentIndex(0)
        self.cmb_skill6_level.setCurrentIndex(0)
        self.cmb_skill7_level.setCurrentIndex(0)
        self.cmb_skill8_level.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hota tree calc", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hero class", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Banned skills:", None))
        self.te_banned_skills.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">resistance</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">navigation</p></body></html>", None))
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

        self.btn_get_trees.setText(QCoreApplication.translate("MainWindow", u"find trees", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Get tree number", None))
        self.groupBox_2.setTitle("")
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

        self.btn_build_tree.setText(QCoreApplication.translate("MainWindow", u"Build tree", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tree number", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Current level", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Last level wisdom given", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Last level magic given", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Defence", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SP", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Knowledge", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Fastest ways to", None))
        self.cmb_skill_search_level.setItemText(0, QCoreApplication.translate("MainWindow", u"Basic", None))
        self.cmb_skill_search_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.cmb_skill_search_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Expert", None))

        self.btn_find_way.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        ___qtreewidgetitem = self.tw_skills.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Skill Tree", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tree browser", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Hota tree calc 1.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author: Temig (temig7487@gmail.com)</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\">Idea and design based on <a href=\"https://handbookhmm.ru/forum/viewtopic.php?f=8&amp;t=42\"><span style=\" text-decoration: underline; color:#0078d4;\">LMOracle.</span></a> Thanks to it's author - AlexSpl</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some information about tree generation can be found <a href=\"http://heroescommunity.com/viewthread.php3?TID=17812&amp;pagenumber=12\"><span style=\" text-decoration: underline; color:#0078d4;\">here</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0101;\">This program does NOT interact with Hota memory, it's just a help resource (like </span><a href=\"https://www.heroes3assist.com/\"><span style=\" text-decoration: underline; color:#0078d4;\">Heroes3 assist</span></a><span style=\" color:#ff0101;\">) that can calculate tree n"
                        "umber from a given first level-ups and build a specific tree.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Another useful information resources:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://vk.com/fizmig\"><span style=\" text-decoration: underline; color:#0078d4;\">Fizmig</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

