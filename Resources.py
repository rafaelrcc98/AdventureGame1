#This houses all the probability-based functions and their corresponding prompts, as well as
# all story beats or checkpoints.

#Classes are kepts on a separate file just as personal preference, however they are initialized here.

from Objects import *
choices = []
index = -1

UserAnswers = {
    'y' : 'Yes,yes,Y,y',
    'n' : 'No,no,N,n',
    'cont' : 'continue, skip, ready, start',
    'SOS' : 'SOS, sos, SoS'
}


def dotdotdot():
    time.sleep(.5)
    print(".", end="")
    time.sleep(.5)
    print(".", end="")
    time.sleep(.5)
    print(".", end="")
    time.sleep(1)
    print("\n")

def pause():
    time.sleep(.5)

def long_pause():
    time.sleep(3.5)

player1 = Player()
story = Story()
river = River('river', .25)
village = Village('village', .25)
original_destination = OriginalDestination('original destination', .40)

#Creates the animals that will be in the game
Wolf = Animal(0.6, 'Wolf')
Bear = Animal(0.8, 'Bear')
Boar = Animal(0.4, 'Boar')
Coyote = Animal(0.3, 'Coyote')
wild_animals = [Wolf,Bear,Boar,Coyote]

#Weapons that will be in the game
AR = Weapon(0.8, "assault rifle")
rifle = Weapon(0.6, "hunting rifle")
handgun = Weapon(0.4, "handgun")
knife = Weapon(0.3, "knife")
weapons = [AR, rifle, handgun, knife]

#The odds
animal_normal_odds = .30

def animal_event(odds):
    chosen_animal = wild_animals[random.choices([0,1,2,3], weights=(15,15,35,35), k=1)[0]]
    chosen_animal.encounter_event(odds)
    loopend = False
    if chosen_animal.encounter == True:
        while not loopend:
            try:
                print("*crunch*")
                pause()
                print("A wild " + chosen_animal.name.lower() + " has appeared, and has begun charging at you!!!")
                long_pause()
                ans1 = int(input("\n[1] Fight \n"
                     "[2] Run away \n"))
                dotdotdot()
                if ans1 == 1:
                    animal_combat(chosen_animal, player1)
                    loopend = True
                elif ans1 == 2:
                    animal_escape(chosen_animal, player1)
                    loopend = True
                else: print("\n!!! Please input either option [1] or [2] in number form\n")
            except: print("\n!!!Please input either option [1] or [2] in number form\n")


def animal_combat(animal, player):
    victory = False
    if not player.weapon:
        result = random.uniform(0, animal.fight)
        if result <= .10:
            print("Against all odds, you used your bare fists to kill the " + animal.name + ". However, you have been"
                                                                                            " left wounded from the fight.\n")
            long_pause()
            player.health = player.health - result
        else:
            print("Without a weapon to defend yourself, you tried to fight the " + animal.name + " with your bare"
                                                                                                 " firsts. Unsuprisingly, the " + animal.name.lower() + " got the better of you...\n")
            pause()
            player.death_scene()
    elif player.weapon and player.weapon.damage >= animal.fight:
        print("You were able to use your " + player.weapon.name + " to kill the " + animal.name + ".")
        pause()
        print("The battle has costed you the use of your weapon.\n")
        long_pause()
        victory = True
        player.weapon = None
        return victory
    elif player.weapon:
        leftover = animal.fight - player.weapon.damage
        healths = []
        for i in wild_animals:
            healths.append(i.fight)
        highest_health = max(healths)
        if random.uniform(0,highest_health) >= leftover:
            print("After some brutal fighting, you were able to use your " + player.weapon.name + " to kill"
                   " the " + animal.name +". However, you have been left wounded from the fight." )
            long_pause()
            print("The battle has costed you the use of your weapon.\n")
            long_pause()
            player.health = player.health-leftover
            victory = True
            player.weapon = None
            return victory
        else:
            print("You bravely took on the " + animal.name + ", however, you were not able to prevail...")
            long_pause()
            player.death_scene()


def animal_escape(animal, player):
    bonus = player.health/animal.fight
    damages = []
    for i in weapons:
        damages.append(i.damage)
    lowest_damage = min(damages)
    baseline = round((1/lowest_damage)*100)
    if random.randint(0,baseline) >= ((baseline/2)+bonus):
        print("You have successfully escaped from the " + animal.name + "!")
        long_pause()
    else:
        print("Your attempt to escape was unsuccessful, and you have been killed by the " + animal.name)
        long_pause()
        player.death_scene()


def helicopter_explosion(odds):
    explosion = False
    if random.randint(0,100) > odds:
        explosion = True
    return explosion


def look_for_radio():
    radio = False,
    if random.randint(0,100) > 50:
        radio = True
        print("After much searching, you have found the radio. Still functional, however low on batteries. You may only get one chance at broadcasting a call for help... ")
        long_pause()
        player1.radio = True
    else:
        print("You looked for quite a bit, but you have not found the radio.")
        long_pause()
    return radio


def look_for_weapon():
    found_weapons = []
    weapon = False
    if random.randint(0,100) > 50:
        chosen_weapon = weapons[random.choices([0, 1, 2, 3], weights=(10, 10, 40, 40), k=1)[0]]
        weapon = True
        if chosen_weapon.name in found_weapons:
            print("Once again, you have found a " + chosen_weapon.name + ".")
        else:
            print("You have found a " + chosen_weapon.name)
        if chosen_weapon.name not in found_weapons:
            found_weapons.append(chosen_weapon.name)
        pause()
        print("Do you want to keep this, or try your luck and look for something better?\n")
        loopend = False
        while not loopend:
            try:
                ans1 = int(input("[1] Keep the " + chosen_weapon.name + "\n"
                                                                "[2] Keep looking \n"))
                dotdotdot()
                if ans1 == 1:
                    player1.weapon = chosen_weapon
                    loopend = True
                    print("You've decided to keep the " + chosen_weapon.name + ".\n")
                    long_pause()
                elif ans1 == 2:
                    print("You've decided to continue searching...\n")
                    long_pause()
                    loopend = True
            except: print("\n!!!Please input either option [1] or [2] in number form\n")
    else:
        print("You looked for quite a bit, but you have not found a weapon...")
        long_pause()
    return weapon


def checkpoint1():
    global choices
    global index
    print("You are injured from the crash and are bleeding -- you can still move, but your wounds are a concern.")
    long_pause()
    print("You remember there was a first aid kit in the helicopter, however, the fire is still raging and there is a possibility that the helicopter might explode...\n\n")
    long_pause()
    print("Do you risk looking for the first aid kit, or do you leave the wreckage?\n")
    loopend = False
    while not loopend:
        try:
            ans1 = int(input("[1]: Look for the first aid kit.\n"
                        "[2]: Leave the wreckage\n"))
            dotdotdot()
            if ans1 == 1 or ans1 == 2:
                loopend = True
            else: print("\n!!!Please input either option [1] or [2] in number form\n")
        except: print("\n!!!Please input either option [1] or [2] in number form\n")
    choices.append(ans1)
    index = index + 1


def checkpoint2():
    global choices
    global index
    look_for_radio = ""
    look_for_weapon = ""
    if not player1.radio: look_for_radio = "[1] Look for the radio.\n"
    if not player1.weapon: look_for_weapon = "[2] Look for a weapon (you may only hold onto one at a time!)\n"
    leave = "[3] Leave the area and look for help.\n"
    loopend = False
    while not loopend:
        try:
            ans1 = int(input("\n" + look_for_radio + look_for_weapon + leave))
            dotdotdot()
            if ans1 == 1 and player1.radio:
                print("\n!!!Please input either option in number form\n")
            elif ans1 == 1 or ans1 == 2 or ans1 == 3:
                loopend = True
            else: print("\n!!!Please input either option in number form\n")
        except: print("\n!!!Please input either option in number form\n")
    choices.append(ans1)
    index =+ 1


def checkpoint2_1():
    skip = False
    while not skip:
        look_for_radio()
        if player1.radio: skip = True
        if not player1.radio:
            loopend = False
            while not loopend:
                try:
                    ans1 = int(input("Do you want to continue searching? \n[1] yes\n[2] no\n"))
                    dotdotdot()
                    if ans1 == 2:
                        skip = True
                        loopend = True
                        print("You've given up trying to find the radio...")
                        long_pause()
                    elif ans1 == 1:
                        loopend = True
                    else: print("\n!!!Please input either option [1] or [2] in number form\n")
                except: print("\n!!!Please input either option [1] or [2] in number form\n")
        animal_event(animal_normal_odds)
        player1.tictoc()
        if player1.dead:
            skip = True


def checkpoint2_2():
    skip = False
    while not skip and not player1.dead:
        found_gun = look_for_weapon()
        if not player1.weapon and not found_gun:
            loopend = False
            while not loopend:
                try:
                    ans1 = int(input("Do you want to continue searching?\n[1] yes\n[2] no\n"))
                    dotdotdot()
                    if ans1 == 1:
                        loopend = True
                    elif ans1 == 2:
                        skip = True
                        loopend = True
                        print("You've given up trying to find a weapon...")
                        long_pause()
                    else: print("\n!!!Please input either option [1] or [2] in number form\n")
                except: print("\n!!!Please input either option [1] or [2] in number form\n")
        elif player1.weapon:
            skip = True
        animal_event(animal_normal_odds)
        player1.tictoc()


def checkpoint3():
    global choices
    global index
    loopend = False
    while not loopend:
        try:
            if player1.radio: radio_prompt = " (can use radio to call for help at the top)"
            else: radio_prompt = ""
            print("[1] Go towards vantage point" + radio_prompt + ".")
            print("[2] Follow river (unknown length, could require more travel than your health allows)")
            print("[3] Follow flight path route (shorter travel length, but animal encounters more likely)")
            ans1 = int(input())
            dotdotdot()
            possible_choices = [1,2,3]
            if ans1 in possible_choices:
                loopend = True
            else: print("\n!!!Please input either option in number form\n")
        except: print("\n!!!Please input either option in number form\n")
    choices.append(ans1)
    index =+ 1

def vantage_point():
    print("You've chosen to make your way to the vantage point...")
    dotdotdot()
    animal_event(animal_normal_odds)
    player1.tictoc()
    if not player1.dead:
        print("You are halfway there...")
        dotdotdot()
        animal_event(animal_normal_odds)
        player1.tictoc()
    if not player1.dead:
        print("You've made it to the top...")
        long_pause()
        at_the_top_radio()
    if not player1.dead:
        at_the_top_survey()

def at_the_top_radio():
    if player1.radio:
        print("Now that you are at the highest vantage point you could find, this is the best time to use that radio you found to send out a distress signal...")
        long_pause()
        print("you will only have enough charge to broadcast for a short duration...\n")
        long_pause()
        loopend = False
        while not loopend:
            try:
                ans1 = input("Type 'SOS' to begin your distress call...")
                dotdotdot()
                if ans1 in UserAnswers.get('SOS'):
                    loopend = True
                else:
                    print("Incorrect input! Please type in 'SOS'...")
            except: print("Incorrect input! Please type in 'SOS'...")
        print("'Hello? Is there anyone out there?...'")
        dotdotdot()
        print("'I was a passenger of flight H421, we crashed on route to base...I am low on food, water, and bleeding badly...'")
        dotdotdot()
        print("'Can anybody hear me?...'")
        dotdotdot()
        if chance_of_rescue(60):
            print("'This is the U.S. Coast Guard. We can hear you and will send a rescue team to your location...tell us exactly where you are!'")
            long_pause()
            print("Your choice to send a distress signal at the top of the hill has paid off, and help is on the way!")
            pause()
            player1.dead = True
            story.victory = True
        else:
            print("You sent out a distress call, but no one responded...")
            long_pause()
            player1.radio = False


def chance_of_rescue(odds):
    rescue = False
    if random.randint(0,100) < odds:
        rescue = True
    return rescue

def at_the_top_survey():
    global choices
    global index
    player1.distance_known = True
    loopend = False
    while not loopend:
        try:
            print("\nFrom this vantage point, you can see the lights of a village. It seems to be about " + str(village.distance) + " miles away...")
            long_pause()
            print("You can also see where the river leads -- there are lights as well, and it looks to be about " + str(river.distance) +" miles away...")
            long_pause()
            print("Lastly, you can see base that your helicopter was heading to - it looks to be about " + str(original_destination.distance) + " miles away.")
            long_pause()
            print("Once again, the journey to the base is through denser woods and thus higher chance for wildlife encounters...\n")
            long_pause()
            print("Knowing this, which direction do you want to head to?\n")
            ans1 = int(input("[1] Head to the village\n[2] Head to the settlement at the end of the river\n[3] Head to the base\n"))
            dotdotdot()
            possible_choices = [1,2,3]
            if ans1 in possible_choices:
                loopend = True
            else: print("\n!!!Please input either option in number form\n")
        except: print("\n!!!Please input either option in number form\n")
    choices.append(ans1)
    index = + 1

def go_to_destination(destination):
    print("You've chosen to head to the " + str(destination.name) + "...")
    long_pause()
    for mile in range(destination.distance):
        if not player1.dead:
            if player1.distance_known:
                dotdotdot()
                animal_event(destination.destination_odds)
                player1.tictoc()
                destination.distance_left = destination.distance_left - 1
                if not player1.dead and not destination.distance_left==0:
                    print("You've traveled a mile. " + str(destination.distance_left) + str(" more to go..."))
            elif destination.distance_left == destination.distance:
                print("You've traveled a mile. Unknown how much longer you have to travel...")
                dotdotdot()
                animal_event(destination.destination_odds)
                player1.tictoc()
                destination.distance_left = destination.distance_left - 1
            else:
                print("You've traveled another mile. Unknown how much longer you have to travel...")
                dotdotdot()
                animal_event(destination.destination_odds)
                player1.tictoc()
                destination.distance_left = destination.distance_left - 1
    if not player1.dead:
        print("After a long and hard journey, you've arrived at civilization!")
        player1.dead = True
        story.victory = True
