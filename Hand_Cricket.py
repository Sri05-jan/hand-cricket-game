import random
from PIL import Image
#to do the toss
def toss():
    print("Lets toss the coin")
    toss_options = ['head', 'tails']
    outcome = random.choice(toss_options)
    t_caller=['player' , 'computer']
    caller=random.choice(t_caller)
    if caller == 'player':
        print("Please do the calling")
        i=1
        while i:
            players_call = input("Choose 'head' or 'tails': ")
            if players_call == 'head' or players_call == 'tails':
                break
            else:
                print('Invalid input')
        print("Players call : ", players_call)
        print("Outcome of the toss : ", outcome)
        if players_call == outcome:
            return 'Player'
        else:
            return 'Computer'
    else:
        print("Computer will do the calling")
        comps_call = random.choice(toss_options)
        print("Computers call : ", comps_call)
        print("Outcome of the toss : ", outcome)
        if comps_call == outcome:
            return 'Computer'
        else:
            return 'Player'

#to decide what the toss winner wants to choose
def decis(winner):
    if winner == 'Computer':
        print("Computer will choose 'batting' or 'bowling' : ")
        ch = random.choice(['batting','bowling'])
        return ch
    else:
        i=1
        while i:
            ch = input("Please choose 'batting' or 'bowling' : ")
            if ch == 'batting' or ch == 'bowling':
                break
            else:
                print("Invalid choice")
        return ch

#to display the image of the number chosen either by the user or the computer
def Display(ch,p):
    pass
    '''try:
        img = Image.open(f"{ch}.png")
        img.show(f"{p}'s choice")
    except FileNotFoundError:
        print(f"Image for {ch} not found!")'''

#to check the validity of the input
def validity(player_ch):
    if player_ch not in [1,2,3,4,5,6]:
        print("Invalid input")
        return 0
    else:
        return 1

#works for both player's batting and computer's bowling in the 1st innings
def Player_batting1():
    player_ch = 0
    comp_ch = 1
    score = 0
    while (player_ch != comp_ch):
        player_ch=int(input("Choose a number from the following list-(1,2,3,4,5,6) : "))
        v = validity(player_ch)
        if v == 0:
            continue
        Display(player_ch,"Player")
        comp_ch = random.choice([1,2,3,4,5,6])
        Display(comp_ch,"Computer")
        print("Computers choice = ", comp_ch)
        if player_ch != comp_ch :
            score += player_chh
        print("Player's score = ", score)
    print("Player is out")
    return score

#works for both computer's batting and player's bowling in the 1st innings
def Player_bowling1():
    player_ch = 0
    comp_ch = 1
    score = 0
    while (player_ch != comp_ch):
        player_ch = int(input("Choose a number from the following list-(1,2,3,4,5,6) : "))
        v = validity(player_ch)
        if v == 0:
            continue
        Display(player_ch,"Player")
        comp_ch = random.choice([1, 2, 3, 4, 5, 6])
        Display(comp_ch,"Computer")
        print("Computers choice = ",comp_ch)
        if player_ch != comp_ch:
            score += comp_ch
        print("Computers score = ",score)
    print("Computer is out")
    return score

#works for both players batting and computers bowling in the 2nd innings
def Player_batting2(c1_sc):
    player_ch = 0
    comp_ch = 1
    score = 0
    while (player_ch != comp_ch):
        player_ch = int(input("Choose a number from the following list-(1,2,3,4,5,6) : "))
        v = validity(player_ch)
        if v == 0:
            continue
        Display(player_ch,"Player")
        comp_ch = random.choice([1, 2, 3, 4, 5, 6])
        Display(comp_ch,"Computer")
        print("Computers choice = ",comp_ch)
        if player_ch != comp_ch:
            score += player_ch
            print("Players score = ", score)
            if score>c1_sc:
                break
        else :
            print("Player is out")
    return score

#works for both players bowling and computers batting in the 2nd innings
def Player_bowling2(p1_sc):
    player_ch = 0
    comp_ch = 1
    score = 0
    while player_ch != comp_ch:
        player_ch = int(input("Choose a number from the following list-(1,2,3,4,5,6) : "))
        v = validity(player_ch)
        if v == 0:
            continue
        Display(player_ch,"Player")
        comp_ch = random.choice([1, 2, 3, 4, 5, 6])
        Display(comp_ch,"Computer")
        print("Computers choice = ",comp_ch)
        if player_ch != comp_ch:
            score += comp_ch
            print("Computers score = ", score)
            if score > p1_sc:
                break
        else:
            print("Computer is out")
    return score

#to print a message after the 1st innings is over
def message (p1,p2,sc):
    print(p1," has scored ",sc," runs in the 1st innings")
    print(p2," has to score ", sc+1, " runs to win the match")

#to decide the outcome of the match
def Result(p1_score, p2_score, p1, p2):
    if p2_score<p1_score:
        print(p1," has won the match by ", p1_score-p2_score, " runs")
    elif p2_score == p1_score:
        print("The match is a draw")
    else:
        print(p2, " has won the match")

#it uses the functions-Player_batting(),Player_bowling(),Result() and message() to handle the entire game
def play(toss_w, ch):
    if toss_w == 'Player':
        if ch == 'batting':
            player_sc = Player_batting1()
            message('Player', 'Computer', player_sc)
            comp_sc = Player_bowling2(player_sc)
            Result(player_sc, comp_sc, 'Player', 'Computer')
        else:
            comp_sc = Player_bowling1()
            message('Computer', 'Player', comp_sc)
            player_sc = Player_batting2(comp_sc)
            Result(comp_sc, player_sc, 'Computer', 'Player')
    else:
        if ch == 'batting':
            comp_sc=Player_bowling1()
            message('Computer', 'Player', comp_sc)
            player_sc = Player_batting2(comp_sc)
            Result(comp_sc, player_sc, 'Computer', 'Player')
        else:
            player_sc = Player_batting1()
            message('Player', 'Computer', player_sc)
            comp_sc = Player_bowling2(player_sc)
            Result(player_sc, comp_sc, 'Player', 'Computer')
    print("Match over")

print("Welcome to the Hand Cricket Game")
i = 1
while i:
    toss_w = toss()
    print("The winner of toss is : ", toss_w)
    ch = decis(toss_w)
    print(toss_w,"has chosen to do ", ch)
    print("The 1st innings begins : ")
    play(toss_w, ch)
    while i:
        ch = input("Do you want to play again?\nEnter 'Yes' or 'No' : ")
        if ch == 'No':
            i=0
        elif ch == 'Yes':
            break
        else:
            print("Invalid choice")
            continue