#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character: 
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to the {enemy.name}.")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead!")
    def alive(self):
        if self.health <= 0:
            return False
        else: 
            return True
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def attack(self, enemy):
        #Crit value is a multiplier of power and doubles 20% of the time
        self.damage = self.power * self.crit_multiplier()
        print(f"{self.name} does {self.damage} damage to the {enemy.name}.")
        enemy.health -= self.damage
        if enemy.health <= 0:
            print(f"{enemy.name} is dead!")
    def crit_multiplier(self):
        self.crit_mult = 1
        if random.randint(1, 6) == 3:
            self.crit_mult = 2
            print(f"{self.name} has dealt a critical strike!")
        return self.crit_mult

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True
        #Zombie never does and while loop will never exit unless flee is chosen or hero dies.

class Medic(Character):
    def health_recuperate(self):
        if random.randint(1, 6) == 2:
            self.health += 2
            print(f"{self.name} has healed for 2.\n")
    
class Ghost(Character):
    pass

class Knight(Hero):
    def dialogue(self, hero):
        self.knightly_quotes = ["Tis' just a fleshwound.", f"My task is set, {hero.name} you will be defeated!", "You are a fool for challenging me.", "Knighthood lies above eternity; it doesn't live off fame, but rather deeds.", "Did somebody lose thier sweet roll?", "Time to cleanse the empire of its filth."]
        self.rand_index = 0
        self.rand_index = random.randint(0, (len(self.knightly_quotes)-1))
        print(self.knightly_quotes[self.rand_index])

class Yogi(Character):
    pass


def main():
    hero = Hero("Carl", 100, 4)
    goblin = Goblin("General Wartface", 25, 2)
    zombie = Zombie("Experiment 254", 1, 2)
    medic = Medic("Idaho Farm Boy David Bleak", 10, 2)
    ghost = Ghost("Floating White Sheet", 1, 3)
    knight = Knight("Sir Gawayne the Handsome", 10, 4)
    yogi = Yogi("Ravi Shankar", 1, 1)
    print()
    print(f"{goblin.name} approaches.")

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {goblin.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-" * 43)
        print()
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

    print()
    print(f"{zombie.name} approaches.")

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {zombie.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-" * 43)
        if raw_input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{zombie.name} laughs.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.alive():
            # Zombie attacks hero
            zombie.attack(hero)
    
    print()
    print(f"{medic.name} approaches.")
    
    while medic.alive() and hero.alive():
        hero.print_status()
        medic.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {medic.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-" * 43)
        if raw_input == "1":
            # Hero attacks medic
            hero.attack(medic)
            medic.health_recuperate()
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{medic.name} laughs.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if medic.alive():
            # Medic attacks hero
            medic.attack(hero)
    
    print()
    print(f"{ghost.name} approaches.")
    
    while ghost.alive() and hero.alive():
        hero.print_status()
        ghost.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {ghost.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-" * 43)
        if raw_input == "1":
            # Hero attacks ghost
            if random.randint(1, 11) == 2:
                hero.attack(ghost)
            else:
                print(f"{ghost.name} has dodged {hero.name}\'s attack!")

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{ghost.name} laughs.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if ghost.alive():
            # Ghost attacks hero
            ghost.attack(hero)
        
    print()
    print(f"{knight.name} approaches.")
    
    while knight.alive() and hero.alive():
        hero.print_status()
        knight.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {knight.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-" * 43)
        if raw_input == "1":
            # Hero attacks knight
            hero.attack(knight)

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{knight.name} laughs.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if knight.alive():
            # Ghost attacks hero
            print()
            knight.dialogue(hero)
            print()
            knight.attack(hero)
    
    print()
    print(f"{yogi.name} approaches.")
    
    while yogi.alive() and hero.alive():
        hero.print_status()
        yogi.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {yogi.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print("-" * 43)
        if raw_input == "1":
            # Hero attacks yogi
            print("Violence is not the answer.")
            break
        elif raw_input == "2":
            print()
            print("I bless you with my powers.")
            hero.health += 5
            print(f"{yogi.name} has healed you.")
            hero.print_status()
            break
        elif raw_input == "3":
            print(f"{yogi.name} waves goodbye in a Downward Dog.")
            break
        else:
            print("Invalid input {}".format(raw_input))


main()