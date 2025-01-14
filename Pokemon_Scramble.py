import random
import time
with open("All_Pokemon.txt","r") as file:
    data=file.read()
arr=data.split("\n")
def scramble(name):
    name=name.lower()
    space=-1
    if " " in name:
        space=name.index(" ")
        p1=name[:space]
        p2=name[space+1:]
    letters=[x for x in name]
    random.shuffle(letters)
    if " " in letters:
        letters.remove(" ")
    ret=""
    for x in letters:
        ret+=x
    if space>-1:
        ret=""
        l1=[x for x in p1]
        l2=[x for x in p2]
        random.shuffle(l1)
        random.shuffle(l2)
        for x in l1:
            ret+=x
        ret+=" "
        for x in l2:
            ret+=x
    return ret.lower()
def one():
    name=random.choice(arr).lower()
    ret=scramble(name)
    guesses=0
    print(f"The scrambled Pokemon name is {ret}")
    guess=""
    while guess!=name:
        guess=str(input("Enter a pokemon name, type 'Done' to give up"))
        if guess=="Done":
            print("The correct answer was",name)
            break
        guesses+=1
    print(f"Correct! It took you {guesses} guesses to get it right")
def two():
    start=time.time()
    streak=-1
    guess=""
    name=""
    while guess==name:
        streak+=1
        name=random.choice(arr).lower()
        ret=scramble(name)
        print(ret)
        guess=str(input("Enter guess"))
        end=time.time()-start
    print("The correct answer was",name)
    print(f"You guessed {streak} in a row! Congratulations")
    if streak>0:
        print(f"It took you {end} seconds, meaning it took about {end/streak} seconds per guess")
def three():
    mons=[]
    mixed=[]
    times=[]
    i=int(input("How many Pokemon would you like to speedrun?"))
    start=time.time()
    streak=0
    guess=""
    name=""
    while guess==name and streak<i:
        print(f"Streak: {streak}")
        inter=time.time()
        name=random.choice(arr)
        mons.append(name)
        arr.remove(name)
        name=name.lower()
        space=-1
        if " " in name:
            space=name.index(" ")
            p1=name[:space]
            p2=name[space+1:]
        letters=[x for x in name]
        random.shuffle(letters)
        if " " in letters:
            letters.remove(" ")
        ret=""
        for x in letters:
            ret+=x
        if space>-1:
            ret=""
            l1=[x for x in p1]
            l2=[x for x in p2]
            random.shuffle(l1)
            random.shuffle(l2)
            for x in l1:
                ret+=x
            ret+=" "
            for x in l2:
                ret+=x
        print(ret)
        mixed.append(ret)
        guess=str(input("Enter guess"))
        interend=time.time()-inter
        times.append(float("{:.2f}.".format(interend)[:-1]))
        streak+=1
    end="{:.2f}".format(time.time()-start)
    end=float(end)
    avg="{:.2f}".format(end/streak)
    if streak==i and guess==name:
        print(f"It took you {end} seconds to guess {i} Pokemon, meaning it took about {avg} seconds per guess")
        with open("Pokemon_Scramble_Save.txt","a") as a:
            a.write(f"{i} Pokemon in {end} seconds, {avg} seconds per Pokemon: \n")
            for mon in range(len(mons)):
                a.write(f"{mons[mon]} {mixed[mon]} {times[mon]}s\n")
            a.write("\n")
    else:
        print("You failed! The answer was",name)
def four():
    pl1=str(input("Enter Player 1 name"))
    pl2=str(input("Enter Player 2 name"))
    print(f"{pl1} vs. {pl2}, who will win?")
    num=int(input("How many seconds would you like to do?"))
    print("If you don't know the Pokemon, just press enter to skip")
    i=input(f"{pl1}'s turn. Press enter to start")
    start=time.time()
    count=0
    while(time.time()-start<num):
        guess=""
        name=""
        name=random.choice(arr).lower()
        ret=scramble(name)
        print(ret)
        guess=str(input("Enter guess: "))
        if guess==name and time.time()-start<num:
            print("Correct!")
            count+=1
        elif guess!=name:
            print(f"Incorrect! Correct answer: {name}")
        if time.time()-start<num:
            print(f"Time used: {(time.time()-start):.2f}/{num} seconds")
    print(f"Time's up! {pl1} guessed {count} Pokemon. Good job!")
    p1count=count
    i=input(f"{pl2}'s turn. Press enter to start")
    start=time.time()
    count=0
    while(time.time()-start<num):
        guess=""
        name=""
        name=random.choice(arr).lower()
        ret=scramble(name)
        print(ret)
        guess=str(input("Enter guess: "))
        if guess==name and time.time()-start<num:
            print("Correct!")
            count+=1
        elif guess!=name:
            print(f"Incorrect! Correct answer: {name}")
        if time.time()-start<num:
            print(f"Time used: {(time.time()-start):.2f}/{num} seconds")
    print(f"Time's up! {pl2} guessed {count} Pokemon. Good job!")
    p2count=count
    if p1count==p2count:
        print(f"Tie! {p1count}-{p1count}")
    elif p1count>p2count:
        print(f"{pl1} wins {p1count}-{p2count}!")
    else:
        print(f"{pl2} wins {p2count}-{p1count}!")
print("Welcome to Guess That Pokemon!")
print("You will be given a scrambled Pokemon name, your job is to guess it correctly")
print("Enter 1 to guess a single Pokemon and enter 2 to try and get as many in a row as you can, press 3 to speedrun a certain amount of Pokemon, 4 for multiplayer anything else to quit")
num=str(input())
choices=['1','2','3','4']
while num in choices:
    if num=='1':
        one()
    elif num=='2':
        two()
    elif num=='3':
        three()
    elif num=='4':
        four()
    print("To play again, press 1,2,3, or 4. Else press anything else")
    num=str(input())
