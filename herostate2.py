from h3_data import skill_list, hero_classes_pri, magic_list

# File contains herostate class and tree search function
# Author: Temig (https://github.com/temig74/)
# Thanks to AlexSpl


def rand(rold):
    rnew = (214013 * rold + 2531011) & 0b11111111111111111111111111111111
    q = (rnew // 0x10000) & 0b111111111111111
    return rnew, q


class HeroState:
    def __init__(self, sec_skills, cur_level, tree_number, hero_class, skill_weights, chosen_skill, pri_skills=None, wisdom_counter=0, magic_counter=0, skillway=''):
        if pri_skills is None:
            pri_skills = [0, 0, 0, 0]
        self.sec_skills = sec_skills
        self.cur_level = cur_level
        self.tree_number = tree_number
        self.hero_class = hero_class
        self.skill_weights = skill_weights
        self.chosen_skill = chosen_skill
        self.pri_skills = pri_skills
        self.wisdom_counter = wisdom_counter
        self.magic_counter = magic_counter
        self.skillway = skillway    # stores all chosen skills from start

        # Recursive generation of full tree
        # self.leftstate, self.rightstate, pri = self.get_next_levelup()

    def rnd_new_magic(self, sec, exclude_skill=None):
        available_magics = {}
        for elem in magic_list:
            if elem not in self.sec_skills and self.skill_weights[elem] != 0 and exclude_skill != elem:
                available_magics[elem] = self.skill_weights[elem]

        if len(available_magics) == 0:
            return None

        magic_sum = sum(available_magics.values())
        if magic_sum > 1:
            sec, q = rand(sec)
            q = q % magic_sum + 1
        else:
            q = 1
        for elem in available_magics:
            q -= available_magics[elem]
            if q <= 0:
                return elem, sec

    def rnd_upgrade_magic(self, sec, exclude_skill=None):
        available_magics = []
        for elem in magic_list:
            if (self.sec_skills.get(elem, 3) < 3) and elem != exclude_skill:
                available_magics.append(elem)
        if len(available_magics) > 1:
            sec, q = rand(sec)
            q = q % len(available_magics) + 1
        else:
            q = 1
        return available_magics[q-1], sec

    def rnd_new_skill(self, sec, exclude_skill=None):
        available_skills = {}
        for elem in skill_list:
            if (elem not in self.sec_skills) and (self.skill_weights[elem] != 0) and elem != exclude_skill:
                available_skills[elem] = self.skill_weights[elem]
        skill_sum = sum(available_skills.values())
        if skill_sum > 1:
            sec, q = rand(sec)
            q = q % skill_sum + 1
        else:
            q = 1
        for elem in available_skills:
            q -= available_skills[elem]
            if q <= 0:
                return elem, sec

    def rnd_upgrade_skill(self, sec, exclude_skill=None):
        available_skills = {}
        for elem in skill_list:
            if self.sec_skills.get(elem, 3) != 3 and elem != exclude_skill:
                w = self.skill_weights[elem]
                if w == 0:
                    w = 1
                available_skills[elem] = w
        skill_sum = sum(available_skills.values())
        if skill_sum > 1:
            sec, q = rand(sec)
            q = q % skill_sum + 1
        else:
            q = 1
        for elem in available_skills:
            q -= available_skills[elem]
            if q <= 0:
                return elem, sec

    def get_next_primary_skill(self):
        seed = 214013 * (self.cur_level + 1) + 156823 * self.tree_number + 154079
        sec, pri = rand(seed)
        q = pri % 100 + 1
        if self.cur_level+1 <= 9:
            skill_chances = hero_classes_pri[self.hero_class][0]
        else:
            skill_chances = hero_classes_pri[self.hero_class][1]

        if q <= skill_chances[0]:
            new_skill = 'attack'
        else:
            q -= skill_chances[0]
            if q <= skill_chances[1]:
                new_skill = 'defence'
            else:
                q -= skill_chances[1]
                if q <= skill_chances[2]:
                    new_skill = 'sp'
                else:
                    new_skill = 'knowledge'
        return new_skill, sec

    def get_next_levelup(self):
        new_level = self.cur_level + 1
        pri_skill, sec = self.get_next_primary_skill()

        if self.hero_class in ('knight', 'ranger', 'alchemist', 'demoniac', 'death knight', 'overlord', 'barbarian', 'beastmaster', 'planeswalker', 'captain', 'mercenary'):
            delta_wisdom = 6
            delta_magic = 4
        else:
            delta_wisdom = 3
            delta_magic = 3

        wisdom_exception = (self.wisdom_counter + delta_wisdom <= new_level) and self.skill_weights['wisdom'] > 0
        magic_exception = (self.magic_counter + delta_magic <= new_level)

        expert_skills_count = 0
        for elem in self.sec_skills.values():
            if elem == 3:
                expert_skills_count += 1
        all_skills_count = len(self.sec_skills)

        has_magic_to_upgrade = False
        magic_skills_are_available = False

        for elem in magic_list:
            if self.sec_skills.get(elem, 3) < 3:
                has_magic_to_upgrade = True
            if elem not in self.sec_skills and self.skill_weights[elem] != 0:
                magic_skills_are_available = True

        ################################################
        if expert_skills_count == all_skills_count:
            if all_skills_count == 8:
                left_skill = None
                right_skill = None
            elif 'wisdom' in self.sec_skills:
                if magic_exception and magic_skills_are_available:
                    left_skill, sec = self.rnd_new_magic(sec)
                else:
                    left_skill, sec = self.rnd_new_skill(sec)
                right_skill, sec = self.rnd_new_skill(sec, left_skill)
            else:
                if wisdom_exception: #and self.skill_weights['wisdom'] > 0:
                    left_skill = 'wisdom'
                    if magic_exception and magic_skills_are_available:
                        right_skill, sec = self.rnd_new_magic(sec, left_skill)
                    else:
                        right_skill, sec = self.rnd_new_skill(sec, left_skill)
                else:
                    if magic_exception and magic_skills_are_available:
                        left_skill, sec = self.rnd_new_magic(sec)
                    else:
                        left_skill, sec = self.rnd_new_skill(sec)
                    right_skill, sec = self.rnd_new_skill(sec, left_skill)
        else:  # if not all skills are experts, we upgrade a skill in a left slot:
            if wisdom_exception and (self.sec_skills.get('wisdom', 3) < 3):
                left_skill = 'wisdom'
            elif magic_exception and has_magic_to_upgrade:
                left_skill, sec = self.rnd_upgrade_magic(sec)
                magic_exception = False
            else:
                left_skill, sec = self.rnd_upgrade_skill(sec)

            if all_skills_count < 8:  # if there is a free slot
                if wisdom_exception and ('wisdom' not in self.sec_skills): # and self.skill_weights['wisdom'] > 0:
                    right_skill = 'wisdom'
                # elif magic_exception and magic_skills_are_available and ((not has_magic_to_upgrade) or wisdom_exception):   # Why wisdom exception here????
                elif magic_exception and magic_skills_are_available:
                    right_skill, sec = self.rnd_new_magic(sec, left_skill)
                else:
                    right_skill, sec = self.rnd_new_skill(sec, left_skill)
            elif all_skills_count - expert_skills_count > 1:  # if two or more skills can be upgraded, we try to upgrade second skill
                if wisdom_exception and magic_exception and has_magic_to_upgrade:
                    right_skill, sec = self.rnd_upgrade_magic(sec, left_skill)
                else:
                    right_skill, sec = self.rnd_upgrade_skill(sec, left_skill)
            else:
                right_skill = None

        new_pri_skills = self.pri_skills[:]
        if pri_skill == 'attack':
            new_pri_skills[0] += 1
        if pri_skill == 'defence':
            new_pri_skills[1] += 1
        if pri_skill == 'sp':
            new_pri_skills[2] += 1
        if pri_skill == 'knowledge':
            new_pri_skills[3] += 1

        if (left_skill == 'wisdom') or (right_skill == 'wisdom'):
            new_wisdom_counter = new_level
        else:
            new_wisdom_counter = self.wisdom_counter

        if (left_skill in magic_list) or (right_skill in magic_list):
            new_magic_counter = new_level
        else:
            new_magic_counter = self.magic_counter

        new_left_herostate = None
        new_right_herostate = None

        if left_skill:
            new_left_sec_skills = self.sec_skills.copy()
            new_left_sec_skills[left_skill] = new_left_sec_skills.get(left_skill, 0) + 1
            new_left_herostate = HeroState(new_left_sec_skills, new_level, self.tree_number, self.hero_class, self.skill_weights, left_skill, new_pri_skills, new_wisdom_counter, new_magic_counter, self.skillway + '-' + left_skill + str(new_left_sec_skills[left_skill]))

        if right_skill:
            new_right_sec_skills = self.sec_skills.copy()
            new_right_sec_skills[right_skill] = new_right_sec_skills.get(right_skill, 0) + 1
            new_right_herostate = HeroState(new_right_sec_skills, new_level, self.tree_number, self.hero_class, self.skill_weights, right_skill, new_pri_skills, new_wisdom_counter, new_magic_counter, self.skillway + '-' + right_skill + str(new_right_sec_skills[right_skill]))

        return new_left_herostate, new_right_herostate, pri_skill

    # find fastest ways to aquire skills
    def recursive_tree_search(self, max_level, target_skills, skillways: list, unwanted_skills: list):
        for skill in target_skills:
            if len(self.sec_skills) == 8 and skill not in self.sec_skills:
                return

        flag = True
        for skill in target_skills:
            if self.sec_skills.get(skill, 0) < target_skills[skill]:
                flag = False
                break

        for skill in unwanted_skills:
            if skill in self.sec_skills:
                return

        if flag:
            skillways.append(self.skillway)
            return

        if self.cur_level <= max_level:
            next_left_state, next_right_state, pri = self.get_next_levelup()
            if next_left_state:
                next_left_state.recursive_tree_search(max_level, target_skills, skillways, unwanted_skills)
            if next_right_state:
                next_right_state.recursive_tree_search(max_level, target_skills, skillways, unwanted_skills)


def find_tree_number(hero_class, hero_skills, hero_level, pri_skill, left_skill, right_skill, new_classes_sec, available_trees=None, last_wisdom=0, last_magic=0):
    correct_trees = []
    if available_trees is None:
        available_trees = []
        for i in range(1, 256):
            available_trees.append(i)

    for tree_num in available_trees:
        hero = HeroState(hero_skills, hero_level, tree_num, hero_class, new_classes_sec, None, wisdom_counter=last_wisdom, magic_counter=last_magic)
        left_state, right_state, new_pri_skill = hero.get_next_levelup()
        if left_state.chosen_skill == left_skill and right_state.chosen_skill == right_skill and new_pri_skill == pri_skill:
            correct_trees.append(tree_num)

    return correct_trees
