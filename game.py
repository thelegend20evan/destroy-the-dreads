import random

attacks = ["punch"]

playerhealth = 10

def is_int_or_float(currentattack):
    if type(currentattack) is int or type(currentattack) is float:
        return True
    else:
        return False


def attack():
    tru = True
    while tru is True:
        weapondmg = 1
        currentattack = raw_input("Choose your attack: Punch (1 damage/1 stamina)")
        if currentattack == "punch" or currentattack == "Punch":
            randnum = random.randint(1, 10)
            if randnum == 1:
                weapondmg = 1.5
                print "Critical Hit!"
        if is_int_or_float(currentattack) is True:
            print "You dealt %s damage!" % weapondmg
            return weapondmg
    else:
        print "Your only option is: punch"


# intro

print "OH NO! The dreads have invaded the rap game! You must save us all, make your way through this quest, and most importantly, DESTROY THE DREADS!"
name = raw_input("What is your name, warrior?")
print "It's settled then. You, DreadSlayer %s, are destined to save the rap game." % (name)
print '\033[1m' + 'Commence!' + '\033[0m'
print "*Journey Starts*"
print
print "Discovered Fist! (weapon)"
print "Damage:1 / Crit Rate:10%"
print
print "*Encountered a new enemy!*"
print "'Weak Bars'"
print "Health:3 / Damage:1"
opphealth = 3


def battle():
    tru2 = True
    while tru2 is True:
        runchance = random.randint(1, 3)
        response = raw_input("What would you do?(Attack, Run)")
        if response == "attack" or response == "Attack":
            damage = attack()
            opphealth = opphealth - damage
        elif response == "run" and runchance != 1:
            print "Couldn't escape!"
        elif response == "run" and runchance == 1:
            print "Got away safely!"
            tru2 = False
        else:
            print "Your only options are: attack / run"

            elif opphealth > 0:
                print "Opponent health = %s/3" % (opphealth)
                    elif playerhealth <= 0:
                        print death()
                    else:
                    print
                    print "Well done, warrior! You survived your first battle. Take this as a reward!"
                    print  '\033[1m' + 'Obtained the Wooden Club.' + '\033[0m'
                    print "Damage:2 / Crit Rate:+1%"
        if opphealth <= 0:
            print "You win!"
            tru2 = False

# def death():
"""     if playerhealth <=0:
         print "YOU ARE DEAD."
         # change something from within the other functions to make this go back to some sort of checkpoint/point in the main story.
"""




attacks.append("club")
print attacks
# def lvl_up():
