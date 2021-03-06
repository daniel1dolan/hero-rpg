#!/usr/bin/env python
import random
import asci_art
import time

class Character: 
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = 0
        self.evade = 0
    def attack(self, enemy):
        if enemy.evade > 0:
            if random.randint(1, ((20/enemy.evade) + 1)) == 3:
                print(f"{enemy.name} has evaded the attack from {self.name}!")
            else: 
                self.damage = self.power - enemy.armor
                enemy.health -= self.damage
                print(f"{self.name} does {self.damage} damage to the {enemy.name}.")
        else: 
            self.damage = self.power - enemy.armor
            enemy.health -= self.damage
            time.sleep(1.5)
            print(f"{self.name} does {self.damage} damage to the {enemy.name}.")
            time.sleep(1.5)
        if enemy.health <= 0:
            print(f"{enemy.name} is dead!")
            quit()
    def alive(self):
        if self.health <= 0:
            return False
        else: 
            return True
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    inventory = []
    def attack(self, enemy):
        #Crit value is a multiplier of power and doubles 20% of the time
        self.damage = (self.power * self.crit_multiplier()) - enemy.armor
        time.sleep(1.5)
        print(f"{self.name} does {self.damage} damage to the {enemy.name}.")
        enemy.health -= self.damage
        if not enemy.alive():
            time.sleep(1.5)
            print(f"{enemy.name} is dead!")
            self.coins += enemy.coins
            time.sleep(1.5)
            print(f"{self.name} has received the bounty for {enemy.name} of {enemy.coins}.")
            time.sleep(1.5)
    def crit_multiplier(self):
        self.crit_mult = 1
        if random.randint(1, 6) == 3:
            self.crit_mult = 2
            time.sleep(0.5)
            print(f"{self.name} has dealt a critical strike!")
        return self.crit_mult
    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            self.inventory.append(item)
            item.count += 1
            time.sleep(1.5)
            print(f"{item.name} added to {self.name}\'s inventory.")
        else: 
            time.sleep(1.5)
            print("You do not have enough coins to purchase this item.")
    def use_item(self):
        if len(self.inventory) > 0:
            time.sleep(1.5)
            print("*" + "-" * 60 + "*")
            print("Which item do you wish to use?")
            for i in range(len(self.inventory)):
                item = self.inventory[i]
                print("{}. use {} ({})".format(i + 1, item.name, item.count))
            print(str((len(self.inventory) + 1)) + ". leave")
            raw_imp = int(input("> "))
            time.sleep(1.5)
            if raw_imp == len(self.inventory) + 1:
                print("*" + "-" * 60 + "*")
            elif raw_imp > len(self.inventory) + 1:
                time.sleep(1.5)
                print("Invalid input.")
            else:
                ItemToUse = self.inventory[raw_imp - 1]
                item = ItemToUse
                time.sleep(1.5)
                item.apply(self)
                self.inventory.remove(item)
        else: 
            time.sleep(1.5)
            print(f"{self.name} has no items.")


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
        print(f"{self.name}: ", self.knightly_quotes[self.rand_index])

class Yogi(Character):
    pass

class SuperTonic:
    def __init__(self):
        self.cost = 5
        self.name = "tonic"
        self.count = 0
    def apply(self, character):
        character.health += 10
        print(f"{character.name}\'s health increased to {character.health}.")

class Armor:
    def __init__(self):
        self.cost = 10
        self.name = "armor"
        self.count = 0
    def apply(self, character):
        character.armor += 2
        print(f"{character.name}\'s armor has been increased to {character.armor}.")

class Evade:
    def __init__(self):
        self.cost = 10
        self.name = "evade"
        self.use_count = 0
        self.count = 0
    def apply(self, character):
        self.use_count += 1
        if self.use_count <= 2:
            character.evade += 2
            print(f"{character.name}\'s evade has been increased to {character.evade}.")
        else: 
            character.coins += self.cost
            print(f"{self.name} is sold out. Here are your coins back.")

class Sword:
    def __init__(self):
        self.cost = 10
        self.name = "sword"
        self.count = 0
    def apply(self,character):
        character.power += 5
        print(f"{character.name}\'s power has been increased to {character.power}.")


class Store:
    tonic = SuperTonic()
    armor = Armor()
    evade = Evade()
    sword = Sword()
    items = [tonic, armor, evade, sword]
    def do_shopping(self, hero):
        while True:
            time.sleep(1.5)
            print("*" + "-" * 60 + "*")
            the_store = "The Store"
            print(the_store.center(62))
            print("*" + "-" * 60 + "*")
            asci_art.shop_art()
            print("*" + "-" * 60 + "*")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(self.items)):
                item = self.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("5. leave")
            print("*" + "-" * 72 + "*")
            raw_imp = int(input("> "))
            print("*" + "-" * 72 + "*")
            if raw_imp == 5:
                time.sleep(1.5)
                break
            elif raw_imp > 5:
                print("Invalid input.")
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                hero.buy(item)
    def go_shopping(self, character):
        print("*" + "-" * 72 + "*")
        asci_art.road_art()
        print("*" + "-" * 72 + "*")
        print("1. Enter the store.")
        print("Press another number to battle.")
        print("*" + "-" * 72 + "*")
        store_status = int(input("> "))
        if store_status == 1:
            time.sleep(1.5)
            self.do_shopping(character)
        else: 
            time.sleep(1.5)


def main():
    hero = Hero("Carl", 100, 4, 0) #name, health, power, coins/bounty
    goblin = Goblin("General Wartface", 15, 2, 5)
    zombie = Zombie("Experiment 254", 1, 2, 100)
    medic = Medic("Idaho Farm Boy David Bleak", 10, 2, 10)
    ghost = Ghost("Floating White Sheet", 1, 3, 10)
    knight = Knight("Sir Gawayne the Handsome", 10, 4, 10)
    yogi = Yogi("Ravi Shankar", 1, 1, 0)
    store = Store()

    while goblin.alive() and hero.alive():
        print("*" + "-" * 60 + "*")
        print(goblin.name.center(62))
        print("*" + "-" * 60 + "*")
        asci_art.goblin_art()
        print("*" + "-" * 60 + "*")
        hero.print_status()
        goblin.print_status()
        print("*" + "-" * 60 + "*")
        print("What do you want to do?")
        print(f"1. fight {goblin.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. access inventory")
        print("*" + "-" * 60 + "*")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            time.sleep(1.5)
            print(f"{goblin.name} laughs.")
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
        
    store.go_shopping(hero)

    while zombie.alive() and hero.alive():
        print("*" + "-" * 60 + "*")
        print(zombie.name.center(62))
        print("*" + "-" * 60 + "*")
        asci_art.zombie_art()
        print("*" + "-" * 60 + "*")
        hero.print_status()
        zombie.print_status()
        print("*" + "-" * 60 + "*")
        print("What do you want to do?")
        print(f"1. fight {zombie.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. access inventory")
        print("*" + "-" * 60 + "*")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{zombie.name} laughs.")
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))

        if zombie.alive():
            # Zombie attacks hero
            zombie.attack(hero)
    
    store.go_shopping(hero)
    
    while medic.alive() and hero.alive():
        print("*" + "-" * 60 + "*")
        print(medic.name.center(62))
        print("*" + "-" * 60 + "*")
        asci_art.medic_art()
        print("*" + "-" * 60 + "*")
        hero.print_status()
        medic.print_status()
        print("*" + "-" * 60 + "*")
        print("What do you want to do?")
        print(f"1. fight {medic.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. access inventory")
        print("*" + "-" * 60 + "*")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks medic
            hero.attack(medic)
            medic.health_recuperate()
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{medic.name} laughs.")
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))

        if medic.alive():
            # Medic attacks hero
            medic.attack(hero)
    
    store.go_shopping(hero)
    
    while ghost.alive() and hero.alive():
        print("*" + "-" * 60 + "*")
        print(ghost.name.center(62))
        print("*" + "-" * 60 + "*")
        asci_art.ghost_art()
        print("*" + "-" * 60 + "*")
        hero.print_status()
        ghost.print_status()
        print("*" + "-" * 60 + "*")
        print("What do you want to do?")
        print(f"1. fight {ghost.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. access inventory")
        print("*" + "-" * 60 + "*")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks ghost
            if random.randint(1, 11) == 2:
                hero.attack(ghost)
            else:
                time.sleep(1.5)
                print(f"{ghost.name} has dodged {hero.name}\'s attack!")

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{ghost.name} laughs.")
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))

        if ghost.alive():
            # Ghost attacks hero
            ghost.attack(hero)
        
    store.go_shopping(hero)
    
    while knight.alive() and hero.alive():
        print("*" + "-" * 60 + "*")
        print(knight.name.center(62))
        print("*" + "-" * 60 + "*")
        asci_art.knight_art()
        print("*" + "-" * 60 + "*")
        hero.print_status()
        knight.print_status()
        knight.dialogue(hero)
        print("*" + "-" * 60 + "*")
        print("What do you want to do?")
        print(f"1. fight {knight.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. access inventory")
        print("*" + "-" * 60 + "*")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks knight
            hero.attack(knight)

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print(f"{knight.name} laughs.")
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))

        if knight.alive():
            # Knight attacks hero
            knight.attack(hero)
    
    store.go_shopping(hero)
    
    while yogi.alive() and hero.alive():
        print("*" + "-" * 60 + "*")
        print(yogi.name.center(62))
        print("*" + "-" * 60 + "*")
        asci_art.yogi_art()
        print("*" + "-" * 60 + "*")
        hero.print_status()
        yogi.print_status()
        print("*" + "-" * 60 + "*")
        print("What do you want to do?")
        print(f"1. fight {yogi.name}")
        print("2. do nothing")
        print("3. flee")
        print("4. access inventory")
        print("*" + "-" * 60 + "*")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks yogi but yogi forces hero to flee
            time.sleep(2)
            print("Violence is not the answer.")
            break
        elif raw_input == "2":
            #yogi blesses the hero
            time.sleep(2)
            print()
            print("I bless you with my powers.")
            hero.health += 5
            print(f"{yogi.name} has healed you.")
            hero.print_status()
            break
        elif raw_input == "3":
            time.sleep(2)
            print(f"{yogi.name} waves goodbye in a Downward Dog.")
            time.sleep(1)
            break
        elif raw_input == "4":
            hero.use_item()
        else:
            print("Invalid input {}".format(raw_input))


main()