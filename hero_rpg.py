#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character: 
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to the {enemy.name}.")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead.")
    def alive(self):
        if self.health <= 0:
            return False
        else: 
            return True
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True


def main():
    hero = Hero("Carl", 10, 5)
    goblin = Goblin("General Wartface", 6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{goblin.name} laughs.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)

# main()

def main2():
    hero = Hero("Carl", 10, 5)
    zombie = Zombie("Rick Grimes", 1, 1)

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{zombie.name} laughs.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.alive():
            # Goblin attacks hero
            zombie.attack(hero)

main2()

