import sys
import os
import random
import time
import pickle

items = []
weapons = {'Great Sword':40}


class Player:
    def __init__(self,name):
        self.level = 21
        self.name = name
        self.maxhealth = 102
        self.health = self.maxhealth
        self.base_attack = 18
        self.magika = 100
        self.gold = 40
        self.agility = 10
        self.potions = 0
        self.weap = ['Rusty Sword']
        self.curweap = ['Rusty Sword']
        self.exp = 0

    @property
    def AttackGain(self):
        AttackGain = self.base_attack
        if self.curweap == 'Rusty Sword':
            AttackGain += 4

        if self.curweap == 'Great Sword':
            AttackGain += 14

        return AttackGain


#MonsterSplash = {"These small green creature only desire is gold. Nature's greatest thieves"}
#MonsterDesc = []
#{1:'Goblin' , 2:'Classic Ork', 3:'Lesser Dragon', 4:'Lesser DarkCrystal'}[random.randint(1,5)]
"""
class Monster:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 15
        self.health = self.maxhealth
        self.attack = 16
        self.agility = 2
        self.goldgain = random.randint(2,15)
        self.expgain = random.randint(2,15)
        self.desc =  ("These small green creature only desire is gold. Nature's greatest thieves - Goblin")
        self.splash = ("The Goblin stares at your coin pouch...")
        self.id = 0
MonsterIG = Monster('Monster')
"""
class Goblin:
     def __init__(self,name):
        self.name = name
        self.maxhealth = 5
        self.health = self.maxhealth
        self.attack = 6
        self.agility = 6
        self.goldgain = 10
        self.expgain = random.randint(2,15)
        self.desc =  ("These small green creature only desire is gold. Nature's greatest thieves - Goblin")
        self.splash = ("The Goblin stares at your coin pouch...")
        self.id = 0
GblinIG = Goblin('Goblin')

class ClassicOrk:
     def __init__(self,name):
        self.name = name
        self.maxhealth = 80
        self.health = self.maxhealth
        self.attack = 8
        self.goldgain = 20
        self.agility = 3
        self.expgain = random.randint(3,20)
        self.desc = ('Nothing special about these creatures apart from their stupidity and strength - ClassicOrk')
        self.splash = ("The ClassicOrc beckons for a fight.")
        self.id = 1
ClassicOrkIG = ClassicOrk('Classic Ork')

class LesserDragon:
     def __init__(self,name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 16
        self.goldgain = 20
        self.agility = 20
        self.expgain = random.randint(20,35)
        self.desc = ("This dragon is not as powerful as the other mighty dragons however this does hurt it's pride - LesserDragon")
        self.splash = ("Lesser Dragon tries to act fearsome.")
        self.id = 2
LesserDragonIG = LesserDragon('Lesser Dragon')

class LesserDarkCrystal:
     def __init__(self,name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 16
        self.goldgain = 20
        self.agility = 14
        self.expgain = random.randint(20,35)
        self.desc = ('A medium crystal with a dark hue - LesserDarkCrystal') 
        self.splash = ("Lesser DarkCrystal spins rapidly. It's preparing to attack!")
        self.id = 3;
LesserDarkCrystalIG = LesserDarkCrystal('Lesser DarkCrystal')

class DarkEnity:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 150
        self.health = self.maxhealth
        self.attack = 30
        self.goldgain = 100
        self.agility = 12
        self.expgain = random.randint(50,100)
        self.desc = ('A dark shapless creature with a blood red grin... - Dark Enity')
        self.splash =('The Dark Enity grins murderously....')
        self.id = 999
DarkEnityIG = DarkEnity('Dark Enity')

def Inventory():
    print('Whats do want to do?')
    print('1) Equip.')
    print('b) go back')
    optionOO = input('>>>')
    if optionOO == '1':
        equip()
    elif optionOO == 'b':
        print('')
        

def equip():
    print('What do you want to equip?')
    for weapon in PlayerIG.weap:
        print(weapon)
    print('b to go back')
    optionIO = input('>>> ')
    if optionIO == PlayerIG.curweap:
        print('You already have that equipped!')
        optionSpace = input(' ')
        equip()
    elif optionIO == 'b':
        Inventory()
    elif optionIO in PlayerIG.weap:
        PlayerIG.curweap = optionIO
        print('You have equipped %s' % optionIO)
        optionSpaceP = input(' ')
        equip()
    else:
        print("you don't have that item in your inventory")
        equip()


def store():
    os.system('cls')
    print("Ironfist's BlackSmith")
    print('Store owner - Pheric Ironfist')
    print('')
    print('Watch out!')
    print('\nPlease take a step back. The embers of my forge might fly that way.  ')
    print('So what brings you here?')
    print('')
    print('Buy')
    print(' ')
    print('Talk ')
    print(' ')
    print('Exit ')
    print(' ')
    optionLO = str.lower(input('--> '))
    if optionLO == 'buy':
        print('I only sell the finest weapons and armour.')
        print('')
        print('Item List')
        print('Great Sword')
        optionITB = input('')
        if optionITB in weapons:
          if PlayerIG.gold >= weapons[optionITB]:
              os.system('cls')
              PlayerIG.gold -= weapons[optionITB]
              PlayerIG.weap.append(optionITB)
              print('You have bought %s' % optionITB)
              optionPP = input(' ')
              store()
          elif PlayerIG.gold >= weapons[optionITB]:
              print("You don't have enough money!")

        else:
            print("That's not an item!")
            time.sleep(2)
            store()
    elif optionLO == 'talk':
        if "Za'khrim" in items:
            print("You found it! Za'khrim!")
            print("Thank you!")
            print("Here is a litle something for your efforts.")
            print('')
            print('                You aquired the super_saber! ')
            items.remove("Za'khrim")
            PlayerIG.weap.append('super_saber')
            optionLO
        else:
            print("Pheric says, Have you heard of the sword Za'khrim? They say it can vanquish all evil! ")
            print("They say it can vanquish all evil! Could you please get me that sword.")
            optionLO
    elif optionLO == 'exit':
        os.system('cls')
        print('You walk out of the shop. The blacksmith waves goodbye.')
        print("You are now in the middle of a merchant land. There are a few shops around. You should try and get a weapon.")
        direction
    else:
        store()

def Intro():
    if os.path.exists("savefile") == True:
        print('')
    else:
        start()
    os.system('cls')
    global PlayerIG
    print("--------Created by Dragon--------")
    print(" ")
    print("Please select one of the following.")
    print(" ")
    print("1) New Game")
    print("2) Load Game")
    print("3) Quit the game....")
    print(" ")

def start():
    os.system('cls')
    print('Hello what is your name?')
    xx = input('--> ')
    global PlayerIG
    PlayerIG = Player(xx)

def stats():
    print('Name: ' + PlayerIG.name)
    print('Level: ' + str(PlayerIG.level))
    print('Attack: ' + str(PlayerIG.base_attack))
    print('Gold: ' + str(PlayerIG.gold))
    print('Current Weapon:' + str(PlayerIG.curweap))
    print('Potions: ' + str(PlayerIG.potions))
    print('Health: ' + str(PlayerIG.health))
    print('Exp: ' + str(PlayerIG.exp))


def prefightM():
    enemyencounter = 1
    global enemy
    enemynum = random.randint(3,4)
    if PlayerIG.level >= 2:
         if enemynum == 3:
             enemy = GoblinIG
         else:
             enemy = ClassicOrkIG
         fight()
    enemynum = random.randint(1,2)
    if PlayerIG.level <= 3:
         if enemynum == 1: 
             enemy = ClassicOrkIG
         else:
             enemy = LesserDragonIG
         fight()

def fight():
    print('A %s appears! ' % (enemy.name))
    print(enemy.splash)
    print("%s 's Health: %d/%d   %s Health: %i/%i " % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print('Potions %i' % PlayerIG.potions)
    print('1.) Attack')
    print('2.) Drink Potion')
    print('3.) Run!')
    print('4.) Monster descption.')
    optionxx = input('--> ')
    if optionxx == '1':
        Attackdes()        
    elif optionxx == '2':
        drinkpotion()
    elif optionxx == '3':
        run()
        optionxx = input('-->')
    elif optionxx == '4':
        print('')
        print(enemy.desc)
        print('')
        optionxx = input('-->')
        fight()
    else:
        print("That's not an option!")
        fight()
    if PlayerIG.health == 0:
        dead()


def drinkpotion():
    os.system('cls')
    if PlayerIG.potions == 0:
        print(" You don't have any potions!")
    else:
        PlayerIG.health += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print('You drank the potion!')
    optionz = input(' ')
    fight()

def Attackdes():
    if enemy.agility >= PlayerIG.agility:
        MonAttack()
    elif PlayerIG.agility >= enemy.agility:
        attack()

def attack():
    Pattack = random.randint(PlayerIG.base_attack / 2, PlayerIG.base_attack)
    Eattack = random.randint(enemy.attack / 2, enemy.attack)
    if Pattack == PlayerIG.base_attack / 2:
        print('You miss!')
    else:
        enemy.health -= Pattack
        print('You deal %i damage!' % (Pattack))
    print(' ')
    if enemy.health <= 0:
        battle()
    if Eattack == enemy.attack / 2:
        print('The enemy missed!')
    else:
        PlayerIG.health -= Eattack
        print('The enemy deals %i damage!' % (Eattack))
    print(' ')
    if PlayerIG.health <= 0:
        dead()
    else:
        battle()
   

def MonAttack():
    Pattack = random.randint(PlayerIG.base_attack / 2, PlayerIG.base_attack)
    Eattack = random.randint(enemy.attack / 2, enemy.attack) 
    if Eattack == enemy.attack / 2:
        print('The enemy missed!')
    else:
        PlayerIG.health -= Eattack
        print('The enemy deals %i damage!' % (Eattack))
    print(' ')
    if PlayerIG.health <= 0:
        dead()  
    if Pattack == PlayerIG.base_attack / 2:
        print('You miss!')
    else:
        enemy.health -= Pattack
        print('You deal %i damage!' % (Pattack))
    print(' ')
    if enemy.health <= 0:
        battle()
    else:
        battle()
   


def exp_up():
    print("You gain %s EXP." % (enemy.expgain))
    optionOI = input(' ')
    PlayerIG.exp += enemy.expgain
    print("")
    if PlayerIG.exp > PlayerIG.level ** 2 * 10:
        PlayerIG.level += 1
        PlayerIG.maxhealth += PlayerIG.level
        PlayerIG.health = PlayerIG.maxhealth
        print("You've reached level " + str(PlayerIG.level))
        placeholder = input("")
        print('')
        print("")
   

def run():
    os.system('cls')
    runumber = random.randint(1,3)
    if runumber == 3:
        print('You have successfully ran away')
        optionop = input(' ')
        direction = str.lower(input("What would you like to do?\n"))
    else:
        print('You failed to get away!')
        optionPP = input(' ')
        os.system('cls')
    Eattack = random.randint(enemy.attack / 2, enemy.attack)
    if Eattack == enemy.attack / 2:
        print('The enemy missed!')
    else:
        PlayerIG.health -= Eattack
        print('The enemy deals %i damage!' % (Eattack))
    optionyy = input(' ')
    if PlayerIG.health <= 0:
        dead()
    else:
        battle()
        

def win():
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    print('Well done you defeated the mighty %s' % enemy.name)
    print('You found %i gold!' % enemy.goldgain)
    exp_up()

def battle():
     if enemy.health >= 0:
         fight()
     elif enemy.health <= 0:
         win()


def dead():
    print('You have died... May you find peace in the afterlife...')
    time.sleep(1)
    sys.exit()


while True:
    system  =  0
    global game
    game = 0
    location  =  0
    testa = 0
    spot  =  0
    while system == 0:
        while game == 0:
            Intro()
            startInput = input("Please choose an option.\n")
            if startInput == "1":
                print("BEGGINNING RPG")
                game = game + 1
            elif startInput == "2":
                if os.path.exists("savefile") == True:
                    os.system('cls')
                    with open('savefile', 'rb') as f:
                        global PlayerIG
                        PlayerIG = pickle.load(f)
                    print("Memories of your adventure flood back into your mind!")
                    print('Loaded Save State')
                    PlaceHolder = input(' ')
                    game = game + 1
                else:
                    print('A save file does not exist...')
            elif startInput == "3":
                print("EXITING")
                system = system + 1
                game = game + 50
            else:
                print("Please enter a command.")

        while game == 1:
            print("Starting Game")
            print(" ")
            print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
            print(" ")
            game  =  game + 1
    
        while game ==  2:
            print(" ")
            print("You are now in the middle of a merchant land. There are a few shops around. You should try and get a weapon.")
            items.append
            while location == 0:
                direction = str.lower(input("What would you like to do?\n"))
                if direction == "north":
                    print("You walk into the Corrupted Forest")
                    location  =  location + 1
                elif direction == "south":
                    print("You enter the city... and almost get hit by a falling trees. You leave immediately.")
                elif direction == "east":
                    location  =  location + 2
                    enemyencounter = random.randint(1,3)
                    if enemyencounter == 2:
                        prefightM()
                    else:
                        enemyencounter = 1
                    print("You enter the wasteland...")
                elif direction == "west":
                    print("You walk forwards and see a sign. It says Ironfist's BlackSmith.")
                    time.sleep(3)
                    print('Pehaps you lack weapons and armour.')
                    time.sleep(3)
                    print('You open the door and walked inside')
                    time.sleep(5)
                    store()
                elif direction == "commands":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                elif direction == "show inventory":
                    print(items)
                elif direction == "stats":
                    stats()
                elif direction == "inventory":
                    Inventory()
                elif direction == "search":
                    print("Nothing to search.")
                elif direction == "use":
                    print("Nothing to Use.")
                elif direction == "help":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                else:
                    print("Please type a command.")
        
            while location == 1 :
                direction = str.lower(input("What would you like to do?\n"))
                if direction == "north":
                    print("There is a fence of elctric fences. You head back to the center of the forest.")
                    enemyencounter = random.randint(1,3)
                    if enemyencounter == 2:
                        prefightM()
                    else:
                        enemyencounter = 1
                elif direction == "south":
                    print("You head back into the city.")
                    location  =  location - 1
                elif direction == "east":
                    print("You see an old shack. You go to knock on the door. Nobody's home.")
                    print("You head back to the center of the forest.")
                elif direction == "west":
                    print("You see a hole in the ground. You look inside. There is a bag of supplies.")
                elif direction == "commands":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command 'show inventory' to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                elif direction == "show inventory":
                    print(items)
                elif direction == "inventory":
                    Inventory()
                elif direction == "stats":
                    stats()
                elif direction == "search":
                    print("You search. And there's a tree, and another tree, and another tree...")
                elif direction == "search hole":
                    if "knife" in items:
                        print("Nothing but a coke bottle full of your p")
                    elif "gun" in items:
                        print("Nothing but a coke bottle full of your p")
                    else:
                        print("You find a knife, and a bottle of expired coke zero. You keep the knife and pee inside the bottle of coke. You head back to the forest.")
                        items.append ("knife")
                elif direction == "search bag":
                    if "knife" in items:
                        print("A sharp smooth balde - a knife")
                    elif "gun" in items:
                        print("A loaded and deadly gun.")
                    else:
                        print("You find a knife, and a bottle of expired coke zero. You keep the knife and pee inside the bottle of coke. You head back to the woods.")
                        items.append ("knife")
                elif direction == "use gun":
                    if "gun" in items:
                        print("You walk up to the little house. You see a little house. You go to knock on the door. Nobody's home.")
                        print("You pull out your gun and shoot the handle off. You walk inside.")
                        location  =  location + 3
                    else:
                        print("You don't got a gun")
                elif direction == "help":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                else:
                    print("Please type a command.")
            while location == 2:
                direction = str.lower(input("What would you like to do?\n"))
                if direction == "north":
                    if "knife" in items:
                        print("You walk down a hill. An evil tries to wack at your face with his bayonette. You duck just in time.")
                        ohno = input("WHAT DA!!!! WHAT DO YOU DO???\n")
                        if ohno == "use knife":
                            print("You pull out your knife just in time. You stab the evil cat in the stomach and blood goes everywhere... You leave the knife and pick up the the cat's gun. You head back to the wasteland.")
                            items.append ("gun")
                            items.remove ("knife")
                        else:
                            print("You get stabbed and crawl back to safety. You are now in the center of the wasteland")
                    elif "gun" in items:
                        print("Nothing to see hear except a dead cat mutilated by your knife.")
                    else:
                        print("You walk around. You hear something scurring in the bushes. You shrug it off and head back to the center of the wasteland.")
                elif direction == "south":
                    print("You hear Dragon using some puns on WinAsh. You walk away slowly to center of the wasteland.")
                elif direction == "east":
                    print("A wall stands before your eyes saying, 'Beyond here lies a Soobway'.")
                elif direction == "west":
                    print("You head back to city centre.")
                    location  =  location - 2
                elif direction == "commands":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                elif direction == "show inventory":
                    print(items)
                elif direction == "inventory":
                    Inventory()
                elif direction == "stats":
                    stats()
                elif direction == "search":
                    print("Nothing to search")
                elif direction == "use":
                    print("Nothing to use")
                elif direction == "help":
                   print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                else:
                    print("Please type a command.")
            while location == 4:
                while testa == 0:
                    print("The game is under develop ment soooo.")
                    testa = testa + 1
                direction = str.lower(input("What would you like to do?\n"))
                if direction == "north":
                    print("You see an old crooked painting of a mishapend figure.")
                elif direction == "south":
                    print("You walk out of the house")
                elif direction == "east":
                    print("You see a small glowing star like object.")
                    print("It's draws you towards it.") 
                    print('You touch the star!')
                    print('You are filled with overwhelming power!')
                    with open('savefile', 'wb') as f:
                        pickle.dump(PlayerIG, f)
                    print('You saved the game.')
                elif direction == "west":
                    print("insert junk")
                elif direction == "commands":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                elif direction == "show inventory":
                    print(items)
                elif direction == "inventory":
                    Inventory()
                elif direction == "stats":
                    stats()
                elif direction == "search":
                    print("")
                elif direction == "use":
                    print("")
                elif direction == "help":
                    print("Commands: type north, south, east, west in order to explore,to 'use' an item type use followed by the item name, type the command show inventory to look at the items in your posession, type the command search followed by a target to search for people or items, type the command commands to repeat these directions")
                else:
                    print("Please type a command.")


       
