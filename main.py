import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMenu, QFileDialog, QListWidgetItem
from PySide6.QtGui import QPainter, QTextDocument, QAction, QFont, QIcon
from PySide6.QtCore import Qt, QCoreApplication, QSize
from PySide6.QtPrintSupport import QPrinter

from ui_main import Ui_MainWindow
from h3_data import skill_list, hero_classes_pri, hero_classes_sec, start_pri, magic_list, pri_ru, hero_classes_ru
from herostate2 import HeroState, find_tree_number
from about import ru_about, en_about

# pyside6-uic.exe .\tree_calc.ui -o ui_main.py # to import new ui

##################################################################
# Hota Tree Calc
# Author: Temig (https://github.com/temig74/)
# Idea and design based on LMOracle by AlexSpl: https://handbookhmm.ru/forum/viewtopic.php?f=8&t=42
##################################################################


# modified QTreeWidgetItem that keeps hero state on every step in skilltree
class SkillItem(QTreeWidgetItem):
    def __init__(self, herostate):
        super(SkillItem, self).__init__()
        self.herostate = herostate
        # set text of item on creating, it includes chosen skill, it's level and primary skills
        self.setText(0, f'lvl {herostate.cur_level} {herostate.chosen_skill} {herostate.sec_skills.get(herostate.chosen_skill, 0)} {herostate.pri_skills}')

        if herostate.chosen_skill in skill_list:
            self.setIcon(0, QIcon(f'img/{herostate.chosen_skill}{herostate.sec_skills.get(herostate.chosen_skill, 0)}.png'))


class TreeCalc(QMainWindow):
    def __init__(self):
        super(TreeCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet('background-image: url(img/back1.bmp);color: rgb(240, 220, 121);')
        self.ui.cmb_hero_class.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_start_1.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_start1_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_start_2.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_start2_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_pri_2.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_left2.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_right2.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_choice2.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_pri_3.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_left3.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_right3.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_choice3.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill1.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill1_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill2.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill2_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill3.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill3_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill4.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill4_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill5.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill5_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill6.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill6_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill7.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill7_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill8.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_skill8_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_tree_num.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_cur_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_wisdom_counter.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_magic_counter.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_learning_level.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_attack.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_defence.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_sp.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.sb_knowledge.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.tabWidget.setStyleSheet('QTabWidget::pane {background-image: url(img/back1.bmp); color: rgb(240, 220, 121)} QTabBar::tab {background-image: url(img/back1.bmp);	color: rgb(240, 220, 121); border: 1px solid #F0DC79; padding: 5px;} QTabBar::tab:selected, QTabBar::tab:hover {background-image: url(img/back1.bmp); color: rgb(240, 220, 121)}')
        self.ui.tw_skills.setStyleSheet('QHeaderView::section { background-color: rgb(106, 70, 40); color: rgb(240, 220, 121); } QScrollBar:vertical { background: rgb(106, 70, 40); } QScrollBar:horizontal { background: rgb(106, 70, 40); }')
        self.ui.cmb_ban_skill.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_wanted_unwanted.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_wanted_unwanted_level.setStyleSheet('background-color: rgb(106, 70, 40);')

        self.ui.lw_wanted_skills.setStyleSheet('QScrollBar:vertical { background: rgb(106, 70, 40); } QScrollBar:horizontal { background: rgb(106, 70, 40); }')
        self.ui.lw_unwanted_skills.setStyleSheet('QScrollBar:vertical { background: rgb(106, 70, 40); } QScrollBar:horizontal { background: rgb(106, 70, 40); }')

        self.ui.cmb_language.addItem(QIcon(f'img/en.png'), 'EN')
        self.ui.cmb_language.addItem(QIcon(f'img/ru.png'), 'RU')
        self.ui.cmb_language.setStyleSheet('background-color: rgb(106, 70, 40);')
        self.ui.cmb_language.currentIndexChanged.connect(self.change_language)

        # fill hero classes
        self.ui.cmb_hero_class.addItems(hero_classes_pri.keys())

        # fill skills in comboboxes
        self.cmb_skill_list = [[self.ui.cmb_skill1, self.ui.cmb_skill1_level],
                               [self.ui.cmb_skill2, self.ui.cmb_skill2_level],
                               [self.ui.cmb_skill3, self.ui.cmb_skill3_level],
                               [self.ui.cmb_skill4, self.ui.cmb_skill4_level],
                               [self.ui.cmb_skill5, self.ui.cmb_skill5_level],
                               [self.ui.cmb_skill6, self.ui.cmb_skill6_level],
                               [self.ui.cmb_skill7, self.ui.cmb_skill7_level],
                               [self.ui.cmb_skill8, self.ui.cmb_skill8_level]]

        sorted_skill_list = [''] + sorted(skill_list)

        for elem in sorted_skill_list:
            icon = QIcon(f'img/{elem}.png')
            self.ui.cmb_start_1.addItem(icon, elem)
            self.ui.cmb_start_2.addItem(icon, elem)
            self.ui.cmb_left2.addItem(icon, elem)
            self.ui.cmb_right2.addItem(icon, elem)
            self.ui.cmb_left3.addItem(icon, elem)
            self.ui.cmb_right3.addItem(icon, elem)
            self.ui.cmb_ban_skill.addItem(icon, elem)
            self.ui.cmb_wanted_unwanted.addItem(icon, elem)

            for cmb in self.cmb_skill_list:
                cmb[0].addItem(icon, elem)

        self.ui.btn_get_trees.clicked.connect(self.find_trees)
        self.ui.cb_levelup3.clicked.connect(self.enable_3_lev)

        self.ui.btn_build_tree.clicked.connect(self.build_tree_root)
        # set default primary skills for class when class chosen
        self.ui.cmb_hero_class.currentIndexChanged.connect(self.set_heroclass_features)
        self.ui.tw_skills.itemExpanded.connect(self.calc_children)

        self.ui.btn_find_way.clicked.connect(self.find_way)

        self.ui.tw_skills.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tw_skills.customContextMenuRequested.connect(self.show_tw_menu)

        self.ui.btn_export_all_trees.clicked.connect(self.export_all_trees)

        self.ui.btn_ban_skill.clicked.connect(self.add_banned_skill)
        self.ui.lw_banned_skills.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_banned_skills.customContextMenuRequested.connect(self.show_lw_skills_menu)

        default_ban = ('resistance', 'navigation')
        for elem in default_ban:
            self.ui.lw_banned_skills.addItem(QListWidgetItem(QIcon(f'img/{elem}.png'), elem))

        self.ui.btn_add_wanted.clicked.connect(self.add_wanted_skill)
        self.ui.lw_wanted_skills.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_wanted_skills.customContextMenuRequested.connect(self.show_lw_skills_menu)
        default_wanted = ('earth magic3',)
        for elem in default_wanted:
            self.ui.lw_wanted_skills.addItem(QListWidgetItem(QIcon(f'img/{elem[:-1]}.png'), elem))

        self.ui.btn_add_unwanted.clicked.connect(self.add_unwanted_skill)
        self.ui.lw_unwanted_skills.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_unwanted_skills.customContextMenuRequested.connect(self.show_lw_skills_menu)

        default_unwanted = ('eagle eye',)
        for elem in default_unwanted:
            self.ui.lw_unwanted_skills.addItem(QListWidgetItem(QIcon(f'img/{elem}.png'), elem))

        self.ui.lw_tree_numbers.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_tree_numbers.customContextMenuRequested.connect(self.show_tree_numbers_menu)

        self.ui.tw_skills.setIconSize(QSize(33, 33))


    def reset_tree_browser(self):
        pass

    def change_language(self):
        if self.ui.cmb_language.currentIndex() == 0:
            for elem in self.cmb_skill_list:
                index = elem[1].currentIndex()
                elem[1].clear()
                elem[1].addItems(['None', 'Basic', 'Advanced', 'Expert'])
                elem[1].setCurrentIndex(index)

            index = self.ui.cmb_start1_level.currentIndex()
            self.ui.cmb_start1_level.clear()
            self.ui.cmb_start1_level.addItems(['None', 'Basic', 'Advanced', 'Expert'])
            self.ui.cmb_start1_level.setCurrentIndex(index)

            index = self.ui.cmb_start2_level.currentIndex()
            self.ui.cmb_start2_level.clear()
            self.ui.cmb_start2_level.addItems(['None', 'Basic', 'Advanced', 'Expert'])
            self.ui.cmb_start2_level.setCurrentIndex(index)

            self.ui.label.setText('Hero class:')
            self.ui.btn_ban_skill.setText('Ban skill:')
            self.ui.label_4.setFont(QFont('Segoe UI', 9))
            self.ui.label_4.setText('Banned skills:')
            self.ui.label_14.setText('Tree numbers:')
            self.ui.tabWidget.setTabText(0, 'Get tree number')
            self.ui.tabWidget.setTabText(1, 'Tree browser')
            self.ui.tabWidget.setTabText(2, 'About')
            self.ui.label_2.setFont(QFont('Segoe UI', 9))
            self.ui.label_2.setText('Start 1')
            self.ui.label_5.setFont(QFont('Segoe UI', 9))
            self.ui.label_5.setText('Start 2')
            self.ui.label_3.setText('2 levelup')
            self.ui.cb_levelup3.setText('3 levelup')
            self.ui.btn_get_trees.setText('Find trees')
            self.ui.groupBox.setTitle('Current skills:')
            self.ui.label_6.setText('Tree №')
            self.ui.label_7.setFont(QFont('Segoe UI', 9))
            self.ui.label_7.setText('Cur. level')
            self.ui.label_8.setText('Last level wisdom given')
            self.ui.label_9.setText('Last level magic given')
            self.ui.label_13.setText('Last level learning adv.')
            self.ui.label_10.setText('PRIM')
            self.ui.btn_build_tree.setFont(QFont('Segoe UI', 9))
            self.ui.btn_build_tree.setText('Build tree')
            self.ui.btn_export_all_trees.setFont(QFont('Segoe UI', 9))
            self.ui.btn_export_all_trees.setText('Export all trees')
            self.ui.groupBox_3.setTitle('Way finder')
            self.ui.btn_find_way.setText('Find')
            self.ui.btn_add_wanted.setFont(QFont('Segoe UI', 9))
            self.ui.btn_add_wanted.setText('Add wanted')
            self.ui.btn_add_unwanted.setFont(QFont('Segoe UI', 9))
            self.ui.btn_add_unwanted.setText('Add unwanted')
            self.ui.label_12.setText('Wanted skills:')
            self.ui.label_11.setText('Unwanted skills:')

            self.ui.cmb_wanted_unwanted_level.clear()
            self.ui.cmb_wanted_unwanted_level.addItems(['Basic', 'Advanced', 'Expert'])

            index = self.ui.cmb_choice2.currentIndex()
            self.ui.cmb_choice2.clear()
            self.ui.cmb_choice2.addItems(['Left', 'Right'])
            self.ui.cmb_choice2.setCurrentIndex(index)

            index = self.ui.cmb_choice3.currentIndex()
            self.ui.cmb_choice3.clear()
            self.ui.cmb_choice3.addItems(['Left', 'Right'])
            self.ui.cmb_choice3.setCurrentIndex(index)

            index = self.ui.cmb_pri_2.currentIndex()
            self.ui.cmb_pri_2.clear()
            self.ui.cmb_pri_2.addItems(pri_ru.values())
            self.ui.cmb_pri_2.setCurrentIndex(index)

            index = self.ui.cmb_pri_3.currentIndex()
            self.ui.cmb_pri_3.clear()
            self.ui.cmb_pri_3.addItems(pri_ru.values())
            self.ui.cmb_pri_3.setCurrentIndex(index)

            index = self.ui.cmb_hero_class.currentIndex()
            self.ui.cmb_hero_class.clear()
            self.ui.cmb_hero_class.addItems(hero_classes_pri.keys())
            self.ui.cmb_hero_class.setCurrentIndex(index)

            self.ui.label_15.setText(en_about)

        elif self.ui.cmb_language.currentIndex() == 1:
            for elem in self.cmb_skill_list:
                index = elem[1].currentIndex()
                elem[1].clear()
                elem[1].addItems(['Нет', 'Базовый', 'Продв.', 'Эксперт'])
                elem[1].setCurrentIndex(index)

            index = self.ui.cmb_start1_level.currentIndex()
            self.ui.cmb_start1_level.clear()
            self.ui.cmb_start1_level.addItems(['Нет', 'Базовый', 'Продв.', 'Эксперт'])
            self.ui.cmb_start1_level.setCurrentIndex(index)

            index = self.ui.cmb_start2_level.currentIndex()
            self.ui.cmb_start2_level.clear()
            self.ui.cmb_start2_level.addItems(['Нет', 'Базовый', 'Продв.', 'Эксперт'])
            self.ui.cmb_start2_level.setCurrentIndex(index)

            self.ui.label.setText('Класс героя:')
            self.ui.btn_ban_skill.setText('Запретить навык:')
            self.ui.label_4.setFont(QFont('Segoe UI', 8))
            self.ui.label_4.setText('Запрещенные навыки:')
            self.ui.label_14.setText('Номера деревьев:')
            self.ui.tabWidget.setTabText(0, 'Определение номера дерева')
            self.ui.tabWidget.setTabText(1, 'Просмотр деревьев')
            self.ui.tabWidget.setTabText(2, 'О программе')
            self.ui.label_2.setFont(QFont('Segoe UI', 8))
            self.ui.label_2.setText('Старт 1')
            self.ui.label_5.setFont(QFont('Segoe UI', 8))
            self.ui.label_5.setText('Старт 2')
            self.ui.label_3.setText('2 уровень')
            self.ui.cb_levelup3.setText('3 уровень')
            self.ui.btn_get_trees.setText('Найти деревья')
            self.ui.groupBox.setTitle('Текущие навыки:')
            self.ui.label_6.setText('№ дерева')
            self.ui.label_7.setFont(QFont('Segoe UI', 8))
            self.ui.label_7.setText('Текущ. ур.')
            self.ui.label_8.setText('Ур., когда давали мудрость')
            self.ui.label_9.setText('Ур., когда давали магию')
            self.ui.label_13.setText('Ур., когда продв. обуч-сть')
            self.ui.label_10.setText('Перв.')
            self.ui.btn_build_tree.setFont(QFont('Segoe UI', 8))
            self.ui.btn_build_tree.setText('Построить дерево')
            self.ui.btn_export_all_trees.setFont(QFont('Segoe UI', 8))
            self.ui.btn_export_all_trees.setText('Экспорт всех')
            self.ui.groupBox_3.setTitle('Поиск пути до навыков')
            self.ui.btn_find_way.setText('Найти')
            self.ui.btn_add_wanted.setFont(QFont('Segoe UI', 8))
            self.ui.btn_add_wanted.setText('Доб желаемый')
            self.ui.btn_add_unwanted.setFont(QFont('Segoe UI', 8))
            self.ui.btn_add_unwanted.setText('Доб нежелательный')
            self.ui.label_12.setText('Желаемые навыки:')
            self.ui.label_11.setText('Нежелательные навыки:')

            self.ui.cmb_wanted_unwanted_level.clear()
            self.ui.cmb_wanted_unwanted_level.addItems(['Базовый', 'Продв.', 'Эксперт'])

            index = self.ui.cmb_choice2.currentIndex()
            self.ui.cmb_choice2.clear()
            self.ui.cmb_choice2.addItems(['Лево', 'Право'])
            self.ui.cmb_choice2.setCurrentIndex(index)

            index = self.ui.cmb_choice3.currentIndex()
            self.ui.cmb_choice3.clear()
            self.ui.cmb_choice3.addItems(['Лево', 'Право'])
            self.ui.cmb_choice3.setCurrentIndex(index)

            index = self.ui.cmb_pri_2.currentIndex()
            self.ui.cmb_pri_2.clear()
            self.ui.cmb_pri_2.addItems(pri_ru.keys())
            self.ui.cmb_pri_2.setCurrentIndex(index)

            index = self.ui.cmb_pri_3.currentIndex()
            self.ui.cmb_pri_3.clear()
            self.ui.cmb_pri_3.addItems(pri_ru.keys())
            self.ui.cmb_pri_3.setCurrentIndex(index)

            index = self.ui.cmb_hero_class.currentIndex()
            self.ui.cmb_hero_class.clear()
            self.ui.cmb_hero_class.addItems(hero_classes_ru.keys())
            self.ui.cmb_hero_class.setCurrentIndex(index)

            self.ui.label_15.setText(ru_about)

    def show_tree_numbers_menu(self, event):
        contex_menu = QMenu(self)
        use_tree_action = QAction('Build this tree', self)
        use_tree_action.triggered.connect(self.build_chosen_tree)
        contex_menu.addAction(use_tree_action)
        contex_menu.exec(self.ui.lw_tree_numbers.mapToGlobal(event))

    def build_chosen_tree(self):
        treenum = int(self.ui.lw_tree_numbers.currentItem().text().split()[0])
        self.ui.sb_tree_num.setValue(treenum)
        self.ui.sb_cur_level.setValue(1)
        self.ui.sb_wisdom_counter.setValue(0)
        self.ui.sb_magic_counter.setValue(0)
        self.ui.sb_learning_level.setValue(1)
        self.ui.sb_attack.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][0])
        self.ui.sb_defence.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][1])
        self.ui.sb_sp.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][2])
        self.ui.sb_knowledge.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][3])

        for cmb in self.cmb_skill_list:
            cmb[0].setCurrentIndex(0)
            cmb[1].setCurrentIndex(0)
        self.ui.cmb_skill1.setCurrentIndex(self.ui.cmb_start_1.currentIndex())
        self.ui.cmb_skill1_level.setCurrentIndex(self.ui.cmb_start1_level.currentIndex())
        self.ui.cmb_skill2.setCurrentIndex(self.ui.cmb_start_2.currentIndex())
        self.ui.cmb_skill2_level.setCurrentIndex(self.ui.cmb_start2_level.currentIndex())

        self.build_tree_root()
        self.ui.tabWidget.setCurrentIndex(1)

    def add_wanted_skill(self):
        skill = self.ui.cmb_wanted_unwanted.currentText()
        items_text = [self.ui.lw_wanted_skills.item(index).text()[:-1] for index in range(self.ui.lw_wanted_skills.count())]
        if skill not in items_text and skill:
            self.ui.lw_wanted_skills.addItem(QListWidgetItem(QIcon(f'img/{skill}.png'), skill+str(self.ui.cmb_wanted_unwanted_level.currentIndex()+1)))

    def add_unwanted_skill(self):
        skill = self.ui.cmb_wanted_unwanted.currentText()
        items_text = [self.ui.lw_unwanted_skills.item(index).text() for index in range(self.ui.lw_unwanted_skills.count())]
        if skill and skill not in items_text:
            self.ui.lw_unwanted_skills.addItem(QListWidgetItem(QIcon(f'img/{skill}.png'), skill))

    def show_lw_skills_menu(self, event):
        context_menu = QMenu(self)
        delete_action = QAction("Delete item", self)
        delete_action.triggered.connect(lambda: self.delete_item(self.sender()))
        context_menu.addAction(delete_action)
        context_menu.exec(self.sender().mapToGlobal(event))

    def delete_item(self, sender):
        selected_item = sender.currentItem()
        if selected_item:
            sender.takeItem(sender.row(selected_item))

    def add_banned_skill(self):
        skill = self.ui.cmb_ban_skill.currentText()
        items_text = [self.ui.lw_banned_skills.item(index).text() for index in range(self.ui.lw_banned_skills.count())]
        if skill and skill not in items_text:
            self.ui.lw_banned_skills.addItem(QListWidgetItem(QIcon(f'img/{skill}.png'), skill))

    def export_all_trees(self):
        max_level = 4

        def expand_to_level(elem: SkillItem, maxlev):
            if elem.herostate.cur_level > maxlev:
                return
            child1 = elem.child(0)
            if child1:
                child1.setExpanded(True)
                expand_to_level(child1, maxlev)
            child2 = elem.child(1)
            if child2:
                child2.setExpanded(True)
                expand_to_level(child2, maxlev)

        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if file_path:
            printer = QPrinter()
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_path)

            painter = QPainter()
            painter.begin(printer)

            self.ui.sb_cur_level.setValue(1)
            self.ui.sb_wisdom_counter.setValue(0)
            self.ui.sb_magic_counter.setValue(0)


            for treenum in range(1, 256):
                self.ui.sb_tree_num.setValue(treenum)
                self.build_tree_root()
                top_item = self.ui.tw_skills.topLevelItem(0)
                left_state, right_state, pri_skill = top_item.herostate.get_next_levelup()
                top_item.child(0).setExpanded(True)
                top_item.child(1).setExpanded(True)
                expand_to_level(top_item.child(0), max_level)
                expand_to_level(top_item.child(1), max_level)
                top_item.setText(0, f'Tree {treenum} {pri_skill} {left_state.chosen_skill} {right_state.chosen_skill}')
                document = QTextDocument(self.get_skilltree_text())
                document.setDefaultFont(QFont("Arial", 11))
                document.drawContents(painter)
                printer.newPage()
                QCoreApplication.processEvents()
            painter.end()

    def show_tw_menu(self, pos):
        item = self.ui.tw_skills.itemAt(pos)
        menu = QMenu()

        action_save_pdf = QAction('Save PDF', self)
        menu.addAction(action_save_pdf)
        action_save_pdf.triggered.connect(self.save_treeview_to_pdf)

        action_rebuild_tree = QAction('Rebuild tree', self)
        menu.addAction(action_rebuild_tree)
        action_rebuild_tree.triggered.connect(lambda: self.rebuild_tree(item))

        menu.exec(self.ui.tw_skills.mapToGlobal(pos))

    def rebuild_tree(self, clicked_item):
        if clicked_item:
            cur_herostate = clicked_item.herostate
            for cmb in self.cmb_skill_list:
                cmb[0].setCurrentIndex(0)
                cmb[1].setCurrentIndex(0)
            for i, skill in enumerate(cur_herostate.sec_skills):
                self.cmb_skill_list[i][0].setCurrentText(skill)
                self.cmb_skill_list[i][1].setCurrentIndex(cur_herostate.sec_skills[skill])
            self.ui.sb_cur_level.setValue(cur_herostate.cur_level)
            self.ui.sb_wisdom_counter.setValue(cur_herostate.wisdom_counter)
            self.ui.sb_magic_counter.setValue(cur_herostate.magic_counter)
            self.ui.sb_learning_level.setValue(cur_herostate.get_learning_level)
            self.ui.sb_attack.setValue(cur_herostate.pri_skills[0])
            self.ui.sb_defence.setValue(cur_herostate.pri_skills[1])
            self.ui.sb_sp.setValue(cur_herostate.pri_skills[2])
            self.ui.sb_knowledge.setValue(cur_herostate.pri_skills[3])
            self.ui.tw_skills.clear()
            self.build_tree_root()

    def save_treeview_to_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if file_path:
            printer = QPrinter()
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(file_path)
            document = QTextDocument()
            document.setPlainText(self.get_skilltree_text())

            painter = QPainter()
            document.setDefaultFont(QFont("Arial", 12))
            painter.begin(printer)
            document.drawContents(painter)
            painter.end()

    def get_skilltree_text(self):
        top = self.ui.tw_skills.topLevelItem(0)

        def recursive_get_text(item: SkillItem):
            text = item.text(0)
            if item.child(0) and item.isExpanded():
                text += '\n' + '       ' * (item.child(0).herostate.cur_level - top.herostate.cur_level) + recursive_get_text(item.child(0))
            if item.child(1) and item.isExpanded():
                text += '\n' + '       ' * (item.child(1).herostate.cur_level - top.herostate.cur_level) + recursive_get_text(item.child(1))
            return text
        return recursive_get_text(top)

    # function that sets primary skills of chosen class
    def set_heroclass_features(self):
        self.ui.cmb_start1_level.setCurrentIndex(1)
        if self.ui.cmb_hero_class.currentText():
            self.ui.sb_attack.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][0])
            self.ui.sb_defence.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][1])
            self.ui.sb_sp.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][2])
            self.ui.sb_knowledge.setValue(start_pri[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())][3])

        if self.ui.cmb_hero_class.currentText() in ('knight', 'рыцарь'):
            self.ui.cmb_start_1.setCurrentText('leadership')

        if self.ui.cmb_hero_class.currentText() in ('death knight', 'necromancer', 'рыцарь смерти', 'некромант'):
            self.ui.cmb_start_1.setCurrentText('necromancy')

        if self.ui.cmb_hero_class.currentText() in ('barbarian', 'варвар'):
            self.ui.cmb_start_1.setCurrentText('offense')

        if self.ui.cmb_hero_class.currentText() in ('beastmaster', 'повелитель зверей'):
            self.ui.cmb_start_1.setCurrentText('armorer')

        if self.ui.cmb_hero_class.currentText() in ('cleric', 'druid', 'wizard', 'heretic', 'warlock', 'battle mage', 'witch', 'elementalist', 'navigator', 'artificer', 'священник', 'друид', 'волшебник', 'еретик', 'чернокнижник', 'боевой маг', 'ведьма', 'элементалист', 'навигатор', 'изобретатель'):
            self.ui.cmb_start_1.setCurrentText('wisdom')

    def enable_3_lev(self):
        if self.ui.cb_levelup3.isChecked():
            self.ui.cmb_pri_3.setEnabled(True)
            self.ui.cmb_left3.setEnabled(True)
            self.ui.cmb_right3.setEnabled(True)
            self.ui.cmb_choice3.setEnabled(True)
        else:
            self.ui.cmb_pri_3.setEnabled(False)
            self.ui.cmb_left3.setEnabled(False)
            self.ui.cmb_right3.setEnabled(False)
            self.ui.cmb_choice3.setEnabled(False)

    # function that runs on expanding, that adds childs of childs of expanded item
    def find_trees(self):
        self.ui.lw_tree_numbers.clear()
        hero_skills = {}
        hero_class = hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())
        wisdom_counter = 0
        magic_counter = 0
        learning_level = 1

        if self.ui.cmb_start_1.currentIndex() > 0 and self.ui.cmb_start1_level.currentIndex() > 0:
            hero_skills[self.ui.cmb_start_1.currentText()] = self.ui.cmb_start1_level.currentIndex()
        if self.ui.cmb_start_2.currentIndex() > 0 and self.ui.cmb_start2_level.currentIndex() > 0:
            hero_skills[self.ui.cmb_start_2.currentText()] = self.ui.cmb_start2_level.currentIndex()

        new_skills_table = hero_classes_sec[hero_class].copy()
        for banned_skill in [self.ui.lw_banned_skills.item(i).text() for i in range(self.ui.lw_banned_skills.count())]:
            new_skills_table[banned_skill] = 0

        corr_trees = find_tree_number(hero_class, hero_skills, 1, pri_ru.get(self.ui.cmb_pri_2.currentText(), self.ui.cmb_pri_2.currentText()), self.ui.cmb_left2.currentText(), self.ui.cmb_right2.currentText(), new_skills_table)

        if self.ui.cmb_choice2.currentIndex() == 0:
            hero_skills[self.ui.cmb_left2.currentText()] = hero_skills.get(self.ui.cmb_left2.currentText(), 0) + 1
            if self.ui.cmb_left2.currentText() == 'learning':
                learning_level = 2
        else:
            hero_skills[self.ui.cmb_right2.currentText()] = hero_skills.get(self.ui.cmb_right2.currentText(), 0) + 1
            if self.ui.cmb_right2.currentText() == 'learning':
                learning_level = 2

        if self.ui.cmb_left2.currentText() == 'wisdom' or self.ui.cmb_right2.currentText() == 'wisdom':
            wisdom_counter = 2
        if (self.ui.cmb_left2.currentText() in magic_list) or (self.ui.cmb_right2.currentText() in magic_list):
            magic_counter = 2

        if self.ui.cb_levelup3.isChecked():
            corr_trees = find_tree_number(hero_class, hero_skills, 2, pri_ru.get(self.ui.cmb_pri_3.currentText(), self.ui.cmb_pri_3.currentText()), self.ui.cmb_left3.currentText(), self.ui.cmb_right3.currentText(), new_skills_table, corr_trees, wisdom_counter, magic_counter)

            if self.ui.cmb_choice3.currentIndex() == 0:
                hero_skills[self.ui.cmb_left3.currentText()] = hero_skills.get(self.ui.cmb_left3.currentText(), 0) + 1
                if self.ui.cmb_left3.currentText() == 'learning':
                    learning_level = 3
            else:
                hero_skills[self.ui.cmb_right3.currentText()] = hero_skills.get(self.ui.cmb_right3.currentText(), 0) + 1
                if self.ui.cmb_right3.currentText() == 'learning':
                    learning_level = 3

            if self.ui.cmb_left3.currentText() == 'wisdom' or self.ui.cmb_right3.currentText() == 'wisdom':
                wisdom_counter = 3
            if (self.ui.cmb_left3.currentText() in magic_list) or (self.ui.cmb_right3.currentText() in magic_list):
                magic_counter = 3

        for tree_num in corr_trees:
            hero = HeroState(hero_skills,
                             3 if self.ui.cb_levelup3.isChecked() else 2,
                             tree_num,
                             hero_class,
                             new_skills_table,
                             '',
                             None,
                             wisdom_counter,
                             magic_counter,
                             '',
                             learning_level)
            next_l, next_r, pri = hero.get_next_levelup()
            self.ui.lw_tree_numbers.addItem(f'{tree_num} {next_l.chosen_skill[:7]} {next_r.chosen_skill[:7]}')

    def build_tree_root(self):
        self.ui.tw_skills.clear()
        self.ui.te_skill_ways.clear()
        root_pri_skills = [self.ui.sb_attack.value(), self.ui.sb_defence.value(), self.ui.sb_sp.value(), self.ui.sb_knowledge.value()]
        root_sec_skills = {}

        for cmb in self.cmb_skill_list:
            if cmb[1].currentIndex() and cmb[0].currentText():
                root_sec_skills[cmb[0].currentText()] = cmb[1].currentIndex()

        new_skills_table = hero_classes_sec[hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText())].copy()
        for banned_skill in [self.ui.lw_banned_skills.item(i).text() for i in range(self.ui.lw_banned_skills.count())]:
            new_skills_table[banned_skill] = 0

        root_item = SkillItem(HeroState(root_sec_skills, self.ui.sb_cur_level.value(), self.ui.sb_tree_num.value(), hero_classes_ru.get(self.ui.cmb_hero_class.currentText(), self.ui.cmb_hero_class.currentText()), new_skills_table, 'Start', root_pri_skills, self.ui.sb_wisdom_counter.value(), self.ui.sb_magic_counter.value(),'',self.ui.sb_learning_level.value()))
        root_item.setText(0, f'lvl{self.ui.sb_cur_level.value()} {self.ui.cmb_hero_class.currentText()} {root_pri_skills}')
        self.ui.tw_skills.addTopLevelItem(root_item)

        left_state, right_state, pri_skill = root_item.herostate.get_next_levelup()
        if left_state:
            root_item.addChild(SkillItem(left_state))
        if right_state:
            root_item.addChild(SkillItem(right_state))
        root_item.setExpanded(True)

    def calc_children(self, item: SkillItem):
        if item.child(0) and item.child(0).childCount() == 0:
            left_state1, right_state1, pri_skill = item.child(0).herostate.get_next_levelup()
            if left_state1:
                item.child(0).addChild(SkillItem(left_state1))
            if right_state1:
                item.child(0).addChild(SkillItem(right_state1))
        if item.child(1) and item.child(1).childCount() == 0:
            left_state2, right_state2, pri_skill = item.child(1).herostate.get_next_levelup()
            if left_state2:
                item.child(1).addChild(SkillItem(left_state2))
            if right_state2:
                item.child(1).addChild(SkillItem(right_state2))

    def find_way(self):
        self.ui.te_skill_ways.clear()
        if self.ui.tw_skills.topLevelItem(0):
            hero = self.ui.tw_skills.topLevelItem(0).herostate
            skillway_list = []
            unwanted_skills = set()
            wanted_skills = {}

            for wanted_skill in [self.ui.lw_wanted_skills.item(i).text() for i in range(self.ui.lw_wanted_skills.count())]:
                wanted_skills[wanted_skill[:-1]] = int(wanted_skill[-1])

            for unwanted_skill in [self.ui.lw_unwanted_skills.item(i).text() for i in range(self.ui.lw_unwanted_skills.count())]:
                unwanted_skills.add(unwanted_skill.lower())

            for max_level in range(hero.cur_level, 23):
                hero.recursive_tree_search(max_level, wanted_skills, skillway_list, unwanted_skills)
                if skillway_list:
                    break

            if skillway_list:
                self.ui.te_skill_ways.setText('\n'.join(skillway_list))
            else:
                self.ui.te_skill_ways.setText('No trees found')
        else:
            self.ui.te_skill_ways.setText('Tree is not built')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeCalc()
    window.show()
    sys.exit(app.exec())
