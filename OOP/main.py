import enemy
import zombie
import ogre
import Hero
import weapon


def battle(e1: enemy.Enemy, e2: enemy.Enemy ):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left!')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left!')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('-----------')
    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} win!')
    else:
        print(f'{e2.get_type_of_enemy()} win!')


def hero_battle(hero: Hero.Hero, enemy: enemy.Enemy ):
    enemy.talk()

    while hero.health_points > 0 and enemy.health_points > 0:
        print('------------')
        enemy.special_attack()
        print(f'Hero: {hero.health_points} HP left!')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left!')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('-----------')
    if hero.health_points > 0:
        print(f'Hero win!')
    else:
        print(f'{enemy.get_type_of_enemy()} win!')


zombie = zombie.Zombie( 10, 2)
ogre = ogre.Ogre(20,3)
hero = Hero.Hero(10, 1)
weapon = weapon.Weapon('Sword', 12)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, ogre)


