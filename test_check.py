import datetime

from herostate2 import HeroState
from h3_data import hero_classes_sec

hero_class = 'navigator'
new_w = hero_classes_sec[hero_class]
banned_skills = ['resistance', 'navigation']
for elem in banned_skills:
    new_w[elem] = 0

test_hero = HeroState({'wisdom': 1, 'sorcery': 1}, 1, 201, hero_class, new_w, None, [2,0,1,2], 0, 0)
skillway_list = []
for max_level in range(test_hero.cur_level, 23):
    test_hero.recursive_tree_search(max_level, {'offense': 1}, skillway_list)
    if skillway_list:
        break
print(skillway_list)


##TEST##
#test_hero = HeroState({'wisdom': 1, 'fire magic': 1, 'sorcery': 1, 'earth magic': 1, 'water magic': 1, 'eagle eye': 1, 'scholar': 1}, 6, 75, 'elementalist', new_w, 'scholar', wisdom_counter=6, magic_counter=4)
#test_hero = HeroState({'wisdom': 1, 'fire magic': 1, 'sorcery': 1}, 2, 75, 'elementalist', new_w, None, wisdom_counter=2, magic_counter=0)
#test_hero = HeroState({'wisdom': 2, 'fire magic': 1}, 2, 75, 'elementalist', new_w, None, wisdom_counter=2, magic_counter=0)
#test_hero = HeroState({'wisdom': 3, 'sorcery': 3, 'air magic': 3, 'eagle eye': 2, 'earth magic': 2, 'archery': 1}, 13, 201, 'navigator', new_w, None, None, 7, 11)
#left_state, right_state, pri = test_hero.get_next_levelup()
#print(f'{left_state.chosen_skill} {right_state.chosen_skill} {pri}')
