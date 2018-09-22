from sys import exit

def input_number():
  while True:
    try:
      num_int = int(input("> "))
    except ValueError:
        print("Not an integer! Try again!")
        continue
    else:
      return num_int
      break


def gold_room():
  print("This room is full of gold. How much do you take?")

  how_much = input_number()

  if how_much < 50:
    print("Nice, you're not greedy, you win!")
    exit(0)
  else:
    dead("You greedy bastard!")
  

def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of the door.")
  print("How are you going to move the Bear?")
  bear_moved = False

  while True:
    choice = input("> ")

    if choice == "take honey":
      dead("The bear looks at you and slaps your face.")
    elif choice == "taunt bear" and not bear_moved:
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice  == "taunt bear" and bear_moved:
      dead("The bear got pissed of and chews you left arm!")
    else:
      print("I got no idea what it means.")
    

def cthulhu_room():
  print("Here you see the great evil Cthulhu.")
  print("he, it, whatever stares at you and you go insane.")
  print("Do you flee for your life or eat your head?")

  choice = input("> ")

  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that was tasty!")
  else:
    cthulhu_room()
  

def dead(why):
  print(why, "Good job!")
  exit(0)


def start():
  print("You are in a dark room.")
  print("There is a door in you right and left.")
  print("Which one do you take?")

  choice = input("> ")

  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")



#start()
gold_room()

  


