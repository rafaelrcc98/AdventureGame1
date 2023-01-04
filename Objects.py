#Houses all classes

import random
import time


class Story:
    def __init__(self, victory=False, done_looting=False):
        self.victory = victory
        self.done_looting = done_looting

    @staticmethod
    def game_won():
        print("\nCongratulations! You won the game!\n")


class Player:
    def __init__(self, health=.8, fight=.3, dead=False, fifty_warning=False, thirty_warning=False, ten_warning=False, weapon=False, radio=False, distance_known=False):
        self.health = health
        self.fight = fight
        self.dead = dead
        self.fifty_warning = fifty_warning
        self.thirty_warning = thirty_warning
        self.ten_warning = ten_warning
        self.weapon = weapon
        self.radio = radio
        self.distance_known = distance_known

    def tictoc(self):
        self.health = self.health - (0.1*random.uniform(0,1))
        if self.health <= .5 and not self.fifty_warning and not self.dead:
            self.fifty_warning = True
            print("\nYour wounds have not gotten better and you have lost a lot of blood. Your health is deteriorating...\n")
            time.sleep(3)
        if self.health <= .3 and not self.thirty_warning and not self.dead:
            self.thirty_warning = True
            print("\nYour health keep worsening and you feel much weaker. Your ability to fight is reduced...\n")
            time.sleep(3)
        if self.health <= .1 and not self.ten_warning and not self.dead:
            self.ten_warning = True
            print("\nYou have lost too much blood and are hanging by a threat. You must get to safety immediately...\n")
            time.sleep(3)
        if self.health <= 0 and not self.dead:
            print("After much blood loss, you have succumbed to your injuries...")
            self.death_scene()

    def death_scene(self):
        self.dead = True
        print("Player Dead. Game Over!")
        return True

class Animal:
    all = []

    def __init__(self, fight:float, name: str, encounter=False,):
        self.fight = fight
        self.name = name
        self.encounter = encounter

        Animal.all.append(self)

    def encounter_event(self, odds):
        chance = random.uniform(0, 1)
        if chance <= odds:
            self.encounter = True

class Weapon:
    def __init__(self, damage: float, name: str):
        self.damage = damage
        self.name = name

class Destination:
    def __init__(self, name: str, destination_odds):
        self.name = name
        self.destination_odds = destination_odds

class River(Destination):
    def __init__(self, name: str, destination_odds):
        super().__init__(name, destination_odds)
        self.distance = random.randint(5, 10)
        self.distance_left = self.distance

class Village(Destination):
    def __init__(self, name: str, destination_odds):
        super().__init__(name, destination_odds)
        self.distance = random.randint(3, 6)
        self.distance_left = self.distance

class OriginalDestination(Destination):
    def __init__(self, name: str, destination_odds):
        super().__init__(name, destination_odds)
        self.distance = random.randint(3, 6)
        self.distance_left = self.distance
