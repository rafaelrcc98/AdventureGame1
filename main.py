# This controls the main story prompts and chooses the story beats based on the imputed answers.

from Resources import *

print("Welcome to my mini adventure game!")
pause()
print("You were a passenger on a helicopter flying over the woods when suddenly, you experienced a malfunction...")
print("Unable to maintain level flight, the pilot was forced to perform an emergency landing on the most suitable spot he could find...")
print("Unfortunately the terrain was treacherous, and the pilot was not able to land safely...")
print("\nYou wake up with a massive headache and your ears ringing. The last thing you remember was a loud explosion...")
print("You look around and find yourself in the wreckage of the helicopter. The pilot is dead, and there are flames everywhere...")
print("You unbuckle your seatbelt and consider your next move...\n\n")
pause()

skip = False
while not skip:
      ans1 = input("Type 'continue' when ready: ")
      if ans1.lower() in UserAnswers.get('cont'):
            skip = True
            dotdotdot()
      else:
            print("Incorrect input!")


checkpoint1()

if not player1.dead and choices[index] == 1:
      if helicopter_explosion(60):
            print("It seems like your gamble didn't pay off, and the helicopter has exploded with you in it...\n")
            long_pause()
            player1.death_scene()
      else:
            print("You managed to get the first aid kit and leave the burning wreck before the helicopter exploded...")
            long_pause()
            print("You've patched up your wounds and have stopped much (but not all) of the bleeding. You've bought yourself some time...\n")
            long_pause()
            player1.health = player1.health + .2
if not player1.dead and choices[index] == 2:
      print("You chose the safe route and left the wreckage, however your wounds are still a concern...\n")
      long_pause()

if not player1.dead:
      print("You are alone in the dark woods, defenseless. You desperately want to call for aid, but you also want to obtain a weapon to defend yourself.")
      print("Wildlife is all around you and it is only a matter of time before a predator tries to score an easy meal.")
      print("Every moment you spend scavenging, searching, and traveling is a chance that an animal could attack...")
      print("\n\nYou remember that, in the helicopter, there was a handheld radio, as well as weapons. The crash may have scattered them somewhere near the crash site...")
      print("Do you search for the radio, search for a weapon, or leave immediately to look for help?")
      long_pause()
      checkpoint2()

if not player1.dead and choices[index] == 1:
      checkpoint2_1()
elif not player1.dead and choices[index] == 2:
      checkpoint2_2()
elif not player1.dead and choices[index] == 3:
      pass

while not player1.dead and not choices[index] ==3:
      print("While you are still in the area...")
      checkpoint2()
      if not player1.dead and choices[index] == 1:
            checkpoint2_1()
      elif not player1.dead and choices[index] == 2:
            checkpoint2_2()

if not player1.dead:
      if player1.radio: radio_prompt = ". Perhaps you can use that radio you found to broadcast a help message..."
      else: radio_prompt = "..."
      print("You have left the crash site, and examine your options...\n"
            "You can barely make out a hill up ahead where you could get a vantage point to look for any nearby settlements, and determine your next move" + radio_prompt + "\n")
      print("You also hear a river nearby. If you follow it long enough, you are sure to find civilization, however "
            "there is no telling how long the river is and how long it will take to follow. Time that you may not have...")
      print("Lastly, you can continue on the original direction of the helicopter flight path on foot -- you were not "
            "too far away from your final destination, however the denser woods are bound to present more animal threats. "
            "A most likely quicker, but riskier route...\n")
      long_pause()
      checkpoint3()

if not player1.dead and choices[index] == 1:
      vantage_point()
elif not player1.dead and choices[index] == 2:
      go_to_destination(river)
elif not player1.dead and choices[index] == 3:
      go_to_destination(original_destination)

if not player1.dead and player1.distance_known and choices[index] == 1:
      go_to_destination(village)
if not player1.dead and player1.distance_known and choices[index] == 2:
      go_to_destination(river)
if not player1.dead and player1.distance_known and choices[index] == 3:
      go_to_destination(original_destination)

if story.victory: story.game_won()
