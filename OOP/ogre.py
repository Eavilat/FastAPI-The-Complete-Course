import enemy
import random

class Ogre(enemy.Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage += 2
            print('Ogre gets angry ans increases attack by 2')