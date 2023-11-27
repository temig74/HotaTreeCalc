import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMenu, QFileDialog
from PySide6.QtGui import QPainter, QTextDocument, QAction, QFont
from PySide6.QtCore import Qt
from PySide6.QtPrintSupport import QPrinter

from ui_main import Ui_MainWindow
from h3_data import skill_list, hero_classes_pri, hero_classes_sec, start_pri, magic_list
from herostate2 import HeroState, find_tree_number

# pyside6-uic.exe .\tree_calc.ui -o ui_main.py # to import new ui


# modified QTreeWidgetItem that keeps hero state on every step in skilltree
class SkillItem(QTreeWidgetItem):
    def __init__(self, herostate):
        super(SkillItem, self).__init__()
        self.herostate = herostate
        # set text of item on creating, it includes chosen skill, it's level and primary skills
        self.setText(0, f'lvl {herostate.cur_level} {herostate.chosen_skill} {herostate.sec_skills.get(herostate.chosen_skill, 0)} {herostate.pri_skills}')


class TreeCalc(QMainWindow):
    def __init__(self):
        super(TreeCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # fill hero classes
        for elem in hero_classes_pri:
            self.ui.cmb_hero_class.addItem(elem)

        # fill skills in comboboxes
        self.ui.cmb_start_1.addItem('')
        self.ui.cmb_start_2.addItem('')
        for elem in skill_list:
            self.ui.cmb_start_1.addItem(elem)
            self.ui.cmb_start_2.addItem(elem)
            self.ui.cmb_left2.addItem(elem)
            self.ui.cmb_right2.addItem(elem)
            self.ui.cmb_left3.addItem(elem)
            self.ui.cmb_right3.addItem(elem)
            self.ui.cmb_skill1.addItem(elem)
            self.ui.cmb_skill2.addItem(elem)
            self.ui.cmb_skill3.addItem(elem)
            self.ui.cmb_skill4.addItem(elem)
            self.ui.cmb_skill5.addItem(elem)
            self.ui.cmb_skill6.addItem(elem)
            self.ui.cmb_skill7.addItem(elem)
            self.ui.cmb_skill8.addItem(elem)
            self.ui.cmb_skill_search.addItem(elem)

        self.ui.cmb_skill_search.setCurrentText('earth magic')
        self.ui.btn_get_trees.clicked.connect(self.find_trees)
        self.ui.cb_levelup3.clicked.connect(self.enable_3_lev)
        # set skill for first level-up
        self.ui.cmb_start_1.currentIndexChanged.connect(lambda: self.ui.cmb_left2.setCurrentIndex(self.ui.cmb_start_1.currentIndex()-1))
        self.ui.btn_build_tree.clicked.connect(self.build_tree_root)
        # set default primary skills for class when class chosen
        self.ui.cmb_hero_class.currentIndexChanged.connect(self.set_heroclass_features)
        self.ui.tw_skills.itemExpanded.connect(self.calc_children)

        self.ui.btn_find_way.clicked.connect(self.find_way)

        self.ui.tw_skills.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tw_skills.customContextMenuRequested.connect(self.show_tw_menu)

    def show_tw_menu(self, pos):
        menu = QMenu()
        action_save_pdf = QAction('Save PDF', self)
        menu.addAction(action_save_pdf)
        action_save_pdf.triggered.connect(self.save_treeview_to_pdf)
        menu.exec(self.ui.tw_skills.mapToGlobal(pos))

    def save_treeview_to_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if file_path:
            printer = QPrinter()
            printer.setOutputFormat(QPrinter.PdfFormat)
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
        self.ui.sb_attack.setValue(start_pri[self.ui.cmb_hero_class.currentText()][0])
        self.ui.sb_defence.setValue(start_pri[self.ui.cmb_hero_class.currentText()][1])
        self.ui.sb_sp.setValue(start_pri[self.ui.cmb_hero_class.currentText()][2])
        self.ui.sb_knowledge.setValue(start_pri[self.ui.cmb_hero_class.currentText()][3])

        if self.ui.cmb_hero_class.currentText() == 'knight':
            self.ui.cmb_start_1.setCurrentText('leadership')
            self.ui.cmb_skill1.setCurrentText('leadership')

        if self.ui.cmb_hero_class.currentText() in ('death knight', 'necromancer'):
            self.ui.cmb_start_1.setCurrentText('necromancy')
            self.ui.cmb_skill1.setCurrentText('necromancy')

        if self.ui.cmb_hero_class.currentText() == 'barbarian':
            self.ui.cmb_start_1.setCurrentText('offense')
            self.ui.cmb_skill1.setCurrentText('offense')

        if self.ui.cmb_hero_class.currentText() == 'beastmaster':
            self.ui.cmb_start_1.setCurrentText('armorer')
            self.ui.cmb_skill1.setCurrentText('armorer')

        if self.ui.cmb_hero_class.currentText() in ('cleric', 'druid', 'wizard', 'heretic', 'warlock', 'battle mage', 'witch', 'elementalist', 'navigator'):
            self.ui.cmb_start_1.setCurrentText('wisdom')
            self.ui.cmb_skill1.setCurrentText('wisdom')

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
        hero_skills = {}
        hero_class = self.ui.cmb_hero_class.currentText()
        wisdom_counter = 0
        magic_counter = 0

        if self.ui.cmb_start_1.currentIndex() > 0 and self.ui.cmb_start1_level.currentIndex() > 0:
            hero_skills[self.ui.cmb_start_1.currentText()] = self.ui.cmb_start1_level.currentIndex()
        if self.ui.cmb_start_2.currentIndex() > 0 and self.ui.cmb_start2_level.currentIndex() > 0:
            hero_skills[self.ui.cmb_start_2.currentText()] = self.ui.cmb_start2_level.currentIndex()

        new_skills_table = hero_classes_sec[hero_class].copy()
        for banned_skill in self.ui.te_banned_skills.toPlainText().split('\n'):
            new_skills_table[banned_skill] = 0

        corr_trees = find_tree_number(hero_class, hero_skills, 1, self.ui.cmb_pri_2.currentText(), self.ui.cmb_left2.currentText(), self.ui.cmb_right2.currentText(), new_skills_table)

        if self.ui.cb_levelup3.isChecked():
            if self.ui.cmb_choice2.currentText() == 'left':
                hero_skills[self.ui.cmb_left2.currentText()] = hero_skills.get(self.ui.cmb_left2.currentText(), 0) + 1
            else:
                hero_skills[self.ui.cmb_right2.currentText()] = hero_skills.get(self.ui.cmb_right2.currentText(), 0) + 1

            if self.ui.cmb_left2.currentText() == 'wisdom' or self.ui.cmb_right2.currentText() == 'wisdom':
                wisdom_counter = 2
            if (self.ui.cmb_left2.currentText() in magic_list) or (self.ui.cmb_right2.currentText() in magic_list):
                magic_counter = 2

            corr_trees = find_tree_number(hero_class, hero_skills, 2, self.ui.cmb_pri_3.currentText(), self.ui.cmb_left3.currentText(), self.ui.cmb_right3.currentText(), new_skills_table, corr_trees, wisdom_counter, magic_counter)

        tree_text = []
        for tree_num in corr_trees:
            hero = HeroState(hero_skills,
                             3 if self.ui.cb_levelup3.isChecked() else 2,
                             tree_num,
                             hero_class,
                             new_skills_table,
                             '',
                             None,
                             wisdom_counter,
                             magic_counter)
            next_l, next_r, pri = hero.get_next_levelup()
            tree_text.append(f'{tree_num} {next_l.chosen_skill[:4]} {next_r.chosen_skill[:4]}')

        self.ui.te_tree_numbers.setText('\n'.join(map(str, tree_text)))

    def build_tree_root(self):
        self.ui.tw_skills.clear()
        root_pri_skills = [self.ui.sb_attack.value(), self.ui.sb_defence.value(), self.ui.sb_sp.value(), self.ui.sb_knowledge.value()]
        root_sec_skills = {}
        if self.ui.cmb_skill1_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill1.currentText()] = self.ui.cmb_skill1_level.currentIndex()
        if self.ui.cmb_skill2_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill2.currentText()] = self.ui.cmb_skill2_level.currentIndex()
        if self.ui.cmb_skill3_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill3.currentText()] = self.ui.cmb_skill3_level.currentIndex()
        if self.ui.cmb_skill4_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill4.currentText()] = self.ui.cmb_skill4_level.currentIndex()
        if self.ui.cmb_skill5_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill5.currentText()] = self.ui.cmb_skill5_level.currentIndex()
        if self.ui.cmb_skill6_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill6.currentText()] = self.ui.cmb_skill6_level.currentIndex()
        if self.ui.cmb_skill7_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill7.currentText()] = self.ui.cmb_skill7_level.currentIndex()
        if self.ui.cmb_skill8_level.currentIndex() > 0:
            root_sec_skills[self.ui.cmb_skill8.currentText()] = self.ui.cmb_skill8_level.currentIndex()

        new_skills_table = hero_classes_sec[self.ui.cmb_hero_class.currentText()].copy()
        for banned_skill in self.ui.te_banned_skills.toPlainText().split('\n'):
            new_skills_table[banned_skill] = 0

        root_item = SkillItem(HeroState(root_sec_skills, self.ui.sb_cur_level.value(), self.ui.sb_tree_num.value(), self.ui.cmb_hero_class.currentText(), new_skills_table, 'Start', root_pri_skills, self.ui.sb_wisdom_counter.value(), self.ui.sb_magic_counter.value()))
        root_item.setText(0, f'lvl{self.ui.sb_cur_level.value()} {self.ui.cmb_hero_class.currentText()} {root_pri_skills}')
        self.ui.tw_skills.addTopLevelItem(root_item)

        left_state, right_state, pri_skill = root_item.herostate.get_next_levelup()
        left_item = SkillItem(left_state)
        right_item = SkillItem(right_state)
        root_item.addChild(left_item)
        root_item.addChild(right_item)
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
        if self.ui.tw_skills.topLevelItem(0):
            hero = self.ui.tw_skills.topLevelItem(0).herostate
            skillway_list = []
            for max_level in range(hero.cur_level, 23):
                hero.recursive_tree_search(max_level, {self.ui.cmb_skill_search.currentText(): self.ui.cmb_skill_search_level.currentIndex()+1}, skillway_list)
                if skillway_list:
                    break
            self.ui.te_skill_ways.clear()
            self.ui.te_skill_ways.setText('\n'.join(skillway_list))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeCalc()
    window.show()
    sys.exit(app.exec())
