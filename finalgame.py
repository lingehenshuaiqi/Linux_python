import random
import time


MAX_SPIRIT_STONES = 1000
NUM_FORESTS = 7


class Archer:
  def __init__(self, name):
    self.name = name
    self.price = 100
    self.max_hp = 100
    self.curr_hp = self.max_hp
  
  def attack(self, monster):
    if isinstance(monster, EagleDemon):
      self.curr_hp -= 20
    elif isinstance(monster, WolfDemon):
      self.curr_hp -= 80
    else:
      raise ValueError("Invalid monster type")
  
  def is_alive(self):
    return self.curr_hp > 0


class Axemen:
  def __init__(self, name):
    self.name = name
    self.price = 120
    self.max_hp = 120
    self.curr_hp = self.max_hp
  
  def attack(self, monster):
    if isinstance(monster, EagleDemon):
      self.curr_hp -= 80
    elif isinstance(monster, WolfDemon):
      self.curr_hp -= 20
    else:
      raise ValueError("Invalid monster type")
  
  def is_alive(self):
    return self.curr_hp > 0


class Monster:
  def __init__(self, name):
    self.name = name
  
  def attack(self, soldier):
    soldier.curr_hp = 0

class EagleDemon(Monster):
  def __init__(self):
    super().__init__("Eagle Demon")

class WolfDemon(Monster):
  def __init__(self):
    super().__init__("Wolf Demon")


def start_game():
  
  forests = []
  for i in range(NUM_FORESTS):
    monster_type = random.choice([EagleDemon, WolfDemon])
    forests.append(monster_type())
  

  print("Monsters:")
  for i, forest in enumerate(forests):
    print(f"Forest {i+1}: {forest.name}")
  print("\n" * 20)


  spirit_stones = MAX_SPIRIT_STONES
  soldiers = []
  while True:
    print(f"You have {spirit_stones} spirit stones.")
    print("Enter the number of archers and axemen to hire, separated by a space (or enter 'done' to start the journey):")
    response = input()
    if response.lower() == "done":
      break
    
    try:
      num_archers, num_axemen = map(int, response.split())
    except ValueError:
      print("Invalid input, please try again.")
      continue
    
    cost = num_archers * Archer.price + num_axemen *Axemen.price
    if cost > spirit_stones:
      print("You don't have enough spirit stones to hire that many soldiers.")
      continue
    

    spirit_stones -= cost
    for i in range(num_archers):
      print("Enter a name for the archer:")
      name = input()
      soldiers.append(Archer(name))
    for i in range(num_axemen):
      print("Enter a name for the axeman:")
      name = input()
      soldiers.append(Axemen(name))
  

  for i, forest in enumerate(forests):
    print(f"You have entered forest {i+1}.")
    print("Enter the name of the soldier you want to send (or enter 'nourish' to use a Holy Stone):")
    while True:
      response = input()
      if response.lower() == "nourish":
        if spirit_stones == 0:
          print("You don't have any Holy Stones.")
        else:
          print("Enter the name of the soldier you want to nourish:")
          soldier_name = input()
          soldier = next((s for s in soldiers if s.name == soldier_name), None)
          if soldier is None:
            print("Invalid soldier name.")
          elif soldier.curr_hp == soldier.max_hp:
            print("This soldier is already at full health.")
          else:
            spirit_stones -= 1
            soldier.curr_hp = min(soldier.max_hp, soldier.curr_hp + 1)
            print("The soldier has been nourished.")
      else:
        soldier = next((s for s in soldiers if s.name == response), None)
        if soldier is None:
          print("Invalid soldier name.")
        elif not soldier.is_alive():
          print("This soldier is dead.")
        else:
          soldier.attack(forest)
          if soldier.is_alive():
            print("The soldier has defeated the monster.")
            break
          else:
            print("The soldier has died.")
            soldiers.remove(soldier)
  
  print("You have successfully passed through all the forests.")
  print(f"You have {spirit_stones} spirit stones remaining.")

start_game()


