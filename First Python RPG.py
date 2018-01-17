from time import sleep
import os, sys, time
import random

name = ''
role = ''
hp = 200
ap = 50
mp = 60
inventory = ''
boosts = 0
gameOver = False

# Title Screen
def title_screen():
    print('#########################')
    print('# Welcome to the EOS RPG#')
    print('#########################')
    print('          -Play-         ')
    print('          -Help-         ')
    print('####By Gautam Singh #### ')

title_screen()

def main_game():
    print_slow('\nThe story starts now\n\n')
    print_slow('\nYour eyes open. You find yourself in a tavern.\n')
    print_slow('\nBartender: Want something to drink?')
    print('\nAsk where you are or I will have a drink. ask/drink')
    choice1 = input('> ')
    # If
    if choice1.lower() == 'ask':
        print_slow("\nBartender: You are in Timmy's Tavern")
        print_slow('\nYou get up and leave')
    elif choice1.lower() == 'drink':
        print_slow('\nThe bartender brings you a drink')
        print_slow('\nYou: Where am I?')
        print_slow("\nBartender: You are in Timmy's Tavern")
        print_slow('\nYou get up and leave')
    print_slow('\nYou are now in a street full of people')
    print_slow('\nYou ask someone what city you are in. He says Alphiem')
    print_slow('\nYou continue walking down the street')
    print_slow('\nYou see some Guards patroling')
    print_slow('\nYou keep walking. The guards notice you \n')
    print_slow("\nGuards: Hey, wait a second!")
    print_slow('\nYou start to run')
    print_slow('\nYou see a dead end ahead, the street branches left and right.')
    print_slow('\nWhich way do you go left or right. left/right')
    choice3 = input('\n> ')
    if choice3.lower() == "left":
        print_slow('\nYou turn left. Oh no another dead end!')
        print_slow('\nThe guards capture you!')
    if choice3.lower() == "right":
        print_slow('\nYou turn right. Oh no another dead end!')
        print_slow('\nThe guards capture you!')
    print_slow('\nThey place you in a cell and give you bread to eat\n')
    print_slow('\n## 2 HOURS LATER ##\n')
    print_slow('\nGuard: Hey, I got bad news for you.')
    print_slow('\nYou: It cant be worse than it already is.\n')
    print_slow('Guard: You will be beheaded tommorow')
    print_slow('You: What!! Why! I did not do anyting')
    print_slow('Guard: You have been charged with murder')
    print_slow('\n\n##GameMaster: You must find a way to escape!##\n')
    print_slow('Would you eat or throw it away, you may lose health if you starve')
    choiceEat = input('\n> ')
    if choiceEat == "no":
        hp = h - 5
        print_slow('You lost 5 hp')
    if choiceEat == "yes":
        hp = hp + 0
    print_slow('Your health is' + hp)
    print_slow("A guard approaches")
    print_slow('He opens the gate to your cell')
    print_slow('Guard: My name is Reigar')
    print_slow('Reigar: The king was a good man and you killed him!')
    print_slow('You: What!?? I didnt kill anybody')
    print_slow('Reigar: Admit your crimes scum!')
    print_slow('Reigar: I am going to kill you and feed your bones to the hounds!')
    print_slow('Reigar: Prepare to die!!!')

# Now for the Battle Loop #
    Reigar = 200
# assassin attacks
    # loop of victory
    while Reigar > 0:
        attack = int(input('\nChoose an attack.\n Fists of fury, 1, 50 damage.\n Thunder Smash, 2, 100 damage.\n Taunt, 3, 200 damage\n'))
        # damage calculation
        # player attacks
        if attack == 1:
        	Reigar = Reigar - 20
        	print('The enemys health is', Reigar, '\n')
        elif attack == 2:
            Reigar = Reigar - 40
            print('\nThe enemys health is', Reigar, '\n')
        elif attack == 3:
            Reigar = Reigar - 60
            print('\nThe enemys health is', Reigar, '\n')

        if Reigar > 0:
            print('\nYou weakened the enemy, attack again\n')
            comp_attack = random.randint(1,3)
            comp_attack = random.randint(1,3)
        if comp_attack == 1:
            hp = hp - 30
            print('You lost 30 health in that battle\nYour health is now ', hp)
        if comp_attack == 2:
            hp = hp - 60
            print('You lost 60 health.\nYour health is now ', hp)
        if comp_attack == 3:
            hp = hp - 90
            print('You lost 90 health.\nYour health is now ', hp)


        if Reigar <= 0 and hp > 0 :
            print("Nice, you beat Reigar")




def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)

def main_game_intro():
    print_slow('Hello, What is your name\n')
    player_name = input('> ')
    print_slow('What role do you want to play as in the game?\n')
    print_slow('You can play as a warrior, mage, priest or assassin.\n')
    player_role = input('> ')
    # Player stats
# If player enters invalid player_role
    if player_role.lower() not in ['warrior', 'mage', 'priest', 'assassin']:
        print('Choose a valid role')

# making it look nice

    print_slow('Welcome ' + player_name + ' the ' + player_role + "\n")
    print_slow('Welcome to this fantasy world!')
    print_slow('I hope you enjoy it')
    print_slow('\nRemember, you can collect items throuhout the game.')
    main_game()



def title_screen_selection():
    option = input('> ')
    if option.lower() == 'play':
        main_game_intro()
    if option.lower() == "help":
        print('   -use you inventory wisely-  ')
        print('   -type an sction to do it-   ')
        print('   -Always type in lowercase-  ')
        print('   -Good luck and have fun-/n/n')

title_screen_selection()


# Finnaly we start

#Lets start the intro of main game#


main_game_intro()

# Lets start the story #
