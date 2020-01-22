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

class Hero(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")
    def alive(self):
        if self.health



class Goblin(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")
    def alive(self):



def main():
    hero = Hero("Carl", 10, 5)
    goblin = Goblin("General Wartface", 6, 2)

    while goblin.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
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
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()

