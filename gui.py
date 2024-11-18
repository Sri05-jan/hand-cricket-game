from tkinter import *
import random
import pygame
# Initialize the main window
root = Tk()
root.title("Hand Cricket Game")
root.geometry('900x600')
root.resizable(False,False)

# Create frames for different pages
home_frame = Frame(root)
about_frame = Frame(root)
play_frame = Frame(root)
player_tw_frame = Frame(root)
comp_tw_frame = Frame(root)
player_batting1_frame = Frame(root)
player_bowling1_frame = Frame(root)
player_batting2_frame = Frame(root)
player_bowling2_frame = Frame(root)

pygame.mixer.init()

toss_options=['head','tails']
outcome=random.choice(toss_options)
caller='Player'

comp_dec=random.choice(['Batting','Bowling'])
score1 = 0
score2 = 0
def batting1_buttons(player_ch,b1,b2,b3,b4,b5,b6):
    img_p=PhotoImage(file=str(player_ch)+'_p.png')
    p_im = Label(player_batting1_frame, image=img_p)
    p_im.image = img_p
    p_im.place(x=20, y=138)
    comp_ch=random.choice([1,2,3,4,5,6])
    Label(player_batting1_frame,text="Computer's choice :",font=("Arial",25),bg='light blue').place(x=370,y=88)
    img_c = PhotoImage(file=str(comp_ch) + '_c.png')
    c_im = Label(player_batting1_frame, image=img_c)
    c_im.image = img_c
    c_im.place(x=370, y=138)
    global score1
    if player_ch==comp_ch:
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        Label(player_batting1_frame, text="Player is out", font=("Arial", 25), bg='light blue').place(x=690, y=220)
        Label(player_batting1_frame, text="Player's\nScore : " + str(score1), font=("Arial", 25), bg='light blue').place(x=700, y=100)
        Label(player_batting1_frame, text="Computer has to score "+str(score1+1)+" runs to win", font=("Arial", 25), bg='light blue').place(x=20, y=394)
        Button(player_batting1_frame,text='Continue',bg='light blue',font=("Arial",25),command=show_player_bowling2_buttons).place(x=700,y=320)
        pygame.mixer.music.load("out.mp3")
        pygame.mixer.music.play()
        return
    else:
        score1 += player_ch
        if player_ch==4:
            pygame.mixer.music.load("4.mp3")
            pygame.mixer.music.play()
        if player_ch==6:
            pygame.mixer.music.load("6.mp3")
            pygame.mixer.music.play()
    Label(player_batting1_frame, text="Player's\nScore : " + str(score1), font=("Arial", 25), bg='light blue').place(x=700, y=90)

def bowling1_button(player_ch,b1,b2,b3,b4,b5,b6):
    img_p = PhotoImage(file=str(player_ch) + '_p.png')
    p_im = Label(player_bowling1_frame, image=img_p)
    p_im.image = img_p
    p_im.place(x=20, y=138)
    comp_ch=random.choice([1,2,3,4,5,6])
    Label(player_bowling1_frame, text="Computer's choice :", font=("Arial", 25), bg='light blue').place(x=370, y=88)
    img_c = PhotoImage(file=str(comp_ch) + '_c.png')
    c_im = Label(player_bowling1_frame, image=img_c)
    c_im.image = img_c
    c_im.place(x=370, y=138)
    global score1
    if player_ch==comp_ch:
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        Label(player_bowling1_frame, text="Computer is out", font=("Arial", 25), bg='light blue').place(x=663, y=220)
        Label(player_bowling1_frame, text="Computer's\nScore : " + str(score1), font=("Arial", 25), bg='light blue').place(x=700, y=90)
        Label(player_bowling1_frame, text="Player has to score " + str(score1 + 1) + " runs to win", font=("Arial", 25),bg='light blue').place(x=20, y=394)
        Button(player_bowling1_frame,text='Continue',bg='light blue',font=("Arial",25),command=show_player_batting2_buttons).place(x=700,y=320)
        pygame.mixer.music.load("out.mp3")
        pygame.mixer.music.play()
        return
    else:
        score1 += comp_ch
        if comp_ch==4:
            pygame.mixer.music.load("4.mp3")
            pygame.mixer.music.play()
        if comp_ch==6:
            pygame.mixer.music.load("6.mp3")
            pygame.mixer.music.play()
    Label(player_bowling1_frame, text="Computer's\nScore : " + str(score1), font=("Arial", 25), bg='light blue').place(x=700, y=90)

def batting2_buttons(player_ch,b1,b2,b3,b4,b5,b6):
    img_p = PhotoImage(file=str(player_ch) + '_p.png')
    p_im = Label(player_batting2_frame, image=img_p)
    p_im.image = img_p
    p_im.place(x=20, y=138)
    comp_ch = random.choice([1, 2, 3, 4, 5, 6])
    Label(player_batting2_frame, text="Computer's choice : ", font=("Arial", 25), bg='light blue').place(x=370, y=88)
    img_c = PhotoImage(file=str(comp_ch) + '_c.png')
    c_im = Label(player_batting2_frame, image=img_c)
    c_im.image = img_c
    c_im.place(x=370, y=138)
    global score1
    Label(player_batting2_frame, text="Target : " + str(score1+1), font=("Arial", 25), bg='light blue').place(x=700, y=210)
    global score2
    if player_ch!=comp_ch:
        score2 += player_ch
        if score2 <= score1:
            if player_ch==4:
                pygame.mixer.music.load("4.mp3")
                pygame.mixer.music.play()
            if player_ch==6:
                pygame.mixer.music.load("6.mp3")
                pygame.mixer.music.play()
        else :
            b1['state'] = DISABLED
            b2['state'] = DISABLED
            b3['state'] = DISABLED
            b4['state'] = DISABLED
            b5['state'] = DISABLED
            b6['state'] = DISABLED
            Label(player_batting2_frame, text="Player's\nScore : " + str(score2), font=("Arial", 25), bg='light blue').place(x=700, y=90)
            Label(player_batting2_frame, text="Player has won the match", font=("Arial", 25), bg='light blue').place(x=20, y=394)
            pygame.mixer.music.load("victory.mp3")
            pygame.mixer.music.play()
    if player_ch == comp_ch:
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        Label(player_batting2_frame, text='Player is out', bg='light blue', font=("Arial", 25)).place(x=690, y=330)
        if score2<score1:
            Label(player_batting2_frame, text="Player has lost the match by "+str(score1-score2)+" runs", font=("Arial", 25), bg='light blue').place(x=20, y=394)
        if score2==score1:
            Label(player_batting2_frame, text="Match drawn", font=("Arial", 25), bg='light blue').place(x=220, y=394)
        Label(player_batting2_frame, text="Player's\nScore : " + str(score2), font=("Arial", 25), bg='light blue').place(x=700,y=90)
        pygame.mixer.music.load("out.mp3")
        pygame.mixer.music.play()
    Label(player_batting2_frame, text="Player's\nScore : " + str(score2), font=("Arial", 25), bg='light blue').place(x=700, y=90)
    return

def bowling2_buttons(player_ch,b1,b2,b3,b4,b5,b6):
    img_p = PhotoImage(file=str(player_ch) + '_p.png')
    p_im = Label(player_bowling2_frame, image=img_p)
    p_im.image = img_p
    p_im.place(x=20, y=138)
    comp_ch = random.choice([1, 2, 3, 4, 5, 6])
    Label(player_bowling2_frame, text="Computer's choice : " , font=("Arial", 25), bg='light blue').place(x=370, y=88)
    img_c = PhotoImage(file=str(comp_ch) + '_c.png')
    c_im = Label(player_bowling2_frame, image=img_c)
    c_im.image = img_c
    c_im.place(x=370, y=138)
    global score1
    Label(player_bowling2_frame, text="Target : " + str(score1 + 1), font=("Arial", 25), bg='light blue').place(x=700, y=210)
    global score2
    if player_ch!=comp_ch:
        score2 += comp_ch
        if score2 <= score1:
            if comp_ch==4:
                pygame.mixer.music.load("4.mp3")
                pygame.mixer.music.play()
            if comp_ch==6:
                pygame.mixer.music.load("6.mp3")
                pygame.mixer.music.play()
        else:
            b1['state'] = DISABLED
            b2['state'] = DISABLED
            b3['state'] = DISABLED
            b4['state'] = DISABLED
            b5['state'] = DISABLED
            b6['state'] = DISABLED
            Label(player_bowling2_frame, text="Computer has won the match", font=("Arial", 25), bg='light blue').place(x=20, y=394)
            pygame.mixer.music.load("victory.mp3")
            pygame.mixer.music.play()
    if player_ch == comp_ch:
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        Label(player_bowling2_frame,text='Computer is out',bg='light blue',font=("Arial",25)).place(x=663,y=330)
        pygame.mixer.music.load("out.mp3")
        pygame.mixer.music.play()
        if score2 < score1:
            Label(player_bowling2_frame, text="Computer has lost the match by " + str(score1 - score2) + " runs", font=("Arial", 25), bg='light blue').place(x=20, y=394)
            pygame.mixer.music.load("victory.mp3")
            pygame.mixer.music.play()
        if score2 == score1:
            Label(player_bowling2_frame, text="Match drawn", font=("Arial", 25), bg='light blue').place(x=220, y=394)
    Label(player_bowling2_frame, text="Computer's\nScore : " + str(score2), font=("Arial", 25), bg='light blue').place(x=700,y=90)
    return

def head_button(hb,tb):
    hb.config(font="underlineFontOpts")
    Label(play_frame, text="Outcome of the toss : " + outcome, bg='light blue', font=("Arial", 20)).place(x=20, y=150)
    if outcome=='head':
        Label(play_frame, text="Player has won the toss", bg='light blue', font=("Arial", 20)).place(x=420, y=150)
        Button(play_frame, text='Take decision', bg='light blue', font=("Arial", 20),command=show_player_tw).place(x=350, y=210)
        winner='Player'
    else:
        Label(play_frame, text="Computer has won the toss", bg='light blue', font=("Arial", 20)).place(x=420, y=150)
        Button(play_frame, text="Show decision", bg='light blue', font=("Arial", 20),command=show_comp_tw).place(x=350, y=210)
        winner='Computer'
    hb['state']=DISABLED
    tb['state'] = DISABLED

def tails_button(tb,hb):
    tb.config(font="underline")
    Label(play_frame, text="Outcome of the toss : " + outcome, bg='light blue', font=("Arial", 20)).place(x=20, y=150)
    if outcome=='tails':
        Label(play_frame, text="Player has won the toss", bg='light blue', font=("Arial", 20)).place(x=420, y=150)
        Button(play_frame,text='Take decision',bg='light blue',font=("Arial", 20),command=show_player_tw).place(x=350, y=210)
    else:
        Label(play_frame, text="Computer has won the toss", bg='light blue', font=("Arial", 20)).place(x=420, y=150)
        Button(play_frame, text="Show decision", bg='light blue', font=("Arial", 20),command=show_comp_tw).place(x=350, y=210)
        #Label(play_frame,text='Computer has chosen to do '+comp_dec,bg='light blue',font=("Arial", 20)).place(x=400, y=210)
    tb['state']=DISABLED
    hb['state'] = DISABLED

def toss(b1):
    Label(play_frame,text=caller+' will do the calling : ',bg='light blue',font=("Arial",20)).place(x=20,y=90)
    if caller=='Computer':
        comp_ch=random.choice(toss_options)
        Label(play_frame, text="Computer's choice is "+comp_ch, bg='light blue', font=("Arial", 20)).place(x=400,y=90)
        Label(play_frame, text="Outcome of the toss : " + outcome, bg='light blue', font=("Arial", 20)).place(x=20,y=150)
        if comp_ch==outcome:
            Label(play_frame, text="Computer has won the toss", bg='light blue', font=("Arial", 20)).place(x=420, y=150)
        else:
            Label(play_frame, text="Player has won the toss", bg='light blue', font=("Arial", 20)).place(x=420, y=150)
    else :
        hb=Button(play_frame,text='Head',bg='light blue',font=('Arial',20),height=1)
        tb=Button(play_frame,text='Tails',bg='light blue',font=('Arial',20),height=1)
        hb.config(command=lambda:head_button(hb,tb))
        tb.config(command=lambda:tails_button(tb,hb))
        hb.place(x=400,y=88)
        tb.place(x=500,y=88)
    b1['state'] = DISABLED
    pygame.mixer.music.load("coin toss.mp3")
    pygame.mixer.music.play()


def setup_home_page():
    img=PhotoImage(file='hcg_bg1.png')
    bgl=Label(home_frame,image=img)
    bgl.image=img
    label = Label(home_frame, text="Welcome to Hand Cricket Game",bg='light blue',font=("Arial", 40))
    label.pack(side=TOP, pady=20)
    bf=Frame(home_frame)
    bf.pack(side=BOTTOM,pady=10)
    b1 = Button(bf,text='Play',bg='light blue',font=("Arial", 25),command=show_play)
    b2 = Button(bf, text="About",bg='light blue',font=("Arial", 25),command=show_about)
    b3 = Button(bf, text="Exit",bg='light blue',font=("Arial", 25),command=root.destroy)
    b1.pack(side=LEFT, padx=5)
    b2.pack(side=LEFT, padx=5)
    b3.pack(side=LEFT, padx=5)
    bgl.place(relwidth=1,relheight=1)
  
def setup_about():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(about_frame, image=img)
    bgl.image = img
    label = Label(about_frame, text="About Hand Cricket Game", font=('Arial',30),bg='light blue')
    label.pack(pady=20)
    msg="The rules of the Hand Cricket Game are as follows - \n1)First there will be a toss(the calling of the toss will be done by the player)\n2)The winner of the toss will decide whether to do batting or bowling\n3)The bowler has to match the choice of the batsman to get them out\n4)The batsman's choice if not matched by the bowler will be counted as their score\n5)Both the computer and the player will choose a number from the list - 1,2,3,4,5,6 whether batting or bowling"
    mv=Message(about_frame,text=msg,font=('Arial',22),width='800',bg='light green')
    mv.pack()
    button = Button(about_frame, text="Back to Home",bg='light blue', font=('Arial',20),command=show_home_page)
    button.pack(side=BOTTOM,pady=10)
    bgl.place(relwidth=1, relheight=1)

def setup_play():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(play_frame, image=img)
    bgl.image = img
    heading = Label(play_frame, text='Lets toss the coin!', bg='light blue', font=("Arial", 30))
    heading.pack(pady=15)
    toss_img = PhotoImage(file='toss1.png')
    t_im = Label(play_frame, image=toss_img)
    t_im.image = toss_img
    t_im.place(x=320, y=270)
    bf = Frame(play_frame)
    bf.pack(side=BOTTOM, pady=10)
    b1 = Button(bf, text='Toss', bg='light blue', font=('Arial', 20), command=lambda:toss(b1))
    b2 = Button(bf, text="Back to Home", bg='light blue', font=('Arial', 20), command=show_home_page)
    b1.pack(side=LEFT, padx=5)
    b2.pack(side=LEFT, padx=5)
    bgl.place(relwidth=1, relheight=1)

def setup_player_tw():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(player_tw_frame, image=img)
    bgl.image = img
    bat_b=Button(player_tw_frame,text='Batting',font=('Arial', 30),bg='light blue',command=show_player_batting1_buttons)
    bat_b.place(x=270,y=90)
    ball_b=Button(player_tw_frame,text='Bowling',font=('Arial', 30),bg='light blue',command=show_player_bowling1_buttons)
    ball_b.place(x=450,y=90)
    b1=Button(player_tw_frame,text='Exit',bg='light blue',font=('Arial', 30),command=root.destroy)
    b1.pack(side=BOTTOM,pady=20)
    bgl.place(relwidth=1, relheight=1)

def setup_comp_tw():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(comp_tw_frame, image=img)
    bgl.image = img
    h=Label(comp_tw_frame,text='Computer has decided to do '+comp_dec,bg='light blue',font=("Arial",30))
    h.pack(pady=20)
    bf=Frame(comp_tw_frame)
    bf.pack(side=BOTTOM,pady=10)
    b1 = Button(bf, text='Play', bg='light blue', font=("Arial", 30))
    b2=Button(bf,text='Exit',bg='light blue',font=("Arial",30),command=root.destroy)
    if comp_dec == 'Bowling':
        b1.config(command=show_player_batting1_buttons)
    else:
        b1.config(command=show_player_bowling1_buttons)
    b1.pack(side=LEFT, padx=5)
    b2.pack(side=LEFT,padx=5)
    bgl.place(relwidth=1, relheight=1)
    
def setup_player_batting1():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(player_batting1_frame, image=img)
    bgl.image = img
    heading=Label(player_batting1_frame,text=' The 1st innings begins! ', bg='light blue',font=("Arial",30))
    heading.pack(pady=20)
    Label(player_batting1_frame,text="Player's choice :", bg='light blue',font=("Arial",25)).place(x=20,y=88)
    b1 = Button(player_batting1_frame, text='    1    ',bg='light blue',font=("Arial", 25))
    b2 = Button(player_batting1_frame, text='    2    ',bg='light blue',font=("Arial", 25))
    b3 = Button(player_batting1_frame, text='    3    ',bg='light blue',font=("Arial", 25))
    b4 = Button(player_batting1_frame, text='    4    ',bg='light blue',font=("Arial", 25))
    b5 = Button(player_batting1_frame, text='    5    ',bg='light blue',font=("Arial", 25))
    b6 = Button(player_batting1_frame, text='    6    ',bg='light blue',font=("Arial", 25))
    b_ex=Button(player_batting1_frame, text='Exit',bg='light blue',font=("Arial", 20),command=root.destroy)
    b1.config(command=lambda: batting1_buttons(1, b1, b2, b3, b4, b5, b6))
    b2.config(command=lambda: batting1_buttons(2, b1, b2, b3, b4, b5, b6))
    b3.config(command=lambda: batting1_buttons(3, b1, b2, b3, b4, b5, b6))
    b4.config(command=lambda: batting1_buttons(4, b1, b2, b3, b4, b5, b6))
    b5.config(command=lambda: batting1_buttons(5, b1, b2, b3, b4, b5, b6))
    b6.config(command=lambda: batting1_buttons(6, b1, b2, b3, b4, b5, b6))

    b1.place(x=80, y=444)
    b2.place(x=200,y=444)
    b3.place(x=320,y=444)

    b4.place(x=440,y=444)
    b5.place(x=560,y=444)
    b6.place(x=680,y=444)
    b_ex.pack(side=BOTTOM, pady=10)
    bgl.place(relwidth=1, relheight=1)

def setup_player_bowling1():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(player_bowling1_frame, image=img)
    bgl.image = img
    heading = Label(player_bowling1_frame, text=' The 1st innings begins! ', bg='light blue', font=("Arial", 30))
    heading.pack(pady=20)
    Label(player_bowling1_frame, text="Player's choice : ", bg='light blue', font=("Arial", 25)).place(x=20, y=88)
    b1 = Button(player_bowling1_frame, text='    1    ', bg='light blue', font=("Arial", 25))
    b2 = Button(player_bowling1_frame, text='    2    ', bg='light blue', font=("Arial", 25))
    b3 = Button(player_bowling1_frame, text='    3    ', bg='light blue', font=("Arial", 25))
    b4 = Button(player_bowling1_frame, text='    4    ', bg='light blue', font=("Arial", 25))
    b5 = Button(player_bowling1_frame, text='    5    ', bg='light blue', font=("Arial", 25))
    b6 = Button(player_bowling1_frame, text='    6    ', bg='light blue', font=("Arial", 25))
    b_ex = Button(player_bowling1_frame, text='Exit', bg='light blue', font=("Arial", 20), command=root.destroy)
    b1.config(command=lambda: bowling1_button(1, b1, b2, b3, b4, b5, b6))
    b2.config(command=lambda: bowling1_button(2, b1, b2, b3, b4, b5, b6))
    b3.config(command=lambda: bowling1_button(3, b1, b2, b3, b4, b5, b6))
    b4.config(command=lambda: bowling1_button(4, b1, b2, b3, b4, b5, b6))
    b5.config(command=lambda: bowling1_button(5, b1, b2, b3, b4, b5, b6))
    b6.config(command=lambda: bowling1_button(6, b1, b2, b3, b4, b5, b6))

    b1.place(x=80, y=444)
    b2.place(x=200, y=444)
    b3.place(x=320, y=444)

    b4.place(x=440, y=444)
    b5.place(x=560, y=444)
    b6.place(x=680, y=444)
    b_ex.pack(side=BOTTOM, pady=10)
    bgl.place(relwidth=1, relheight=1)

def setup_player_batting2():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(player_batting2_frame, image=img)
    bgl.image = img
    heading = Label(player_batting2_frame, text=' The 2nd innings begins! ', bg='light blue', font=("Arial", 30))
    heading.pack(pady=20)
    Label(player_batting2_frame, text="Player's choice : ", bg='light blue', font=("Arial", 25)).place(x=20, y=88)
    b1 = Button(player_batting2_frame, text='    1    ', bg='light blue', font=("Arial", 25))
    b2 = Button(player_batting2_frame, text='    2    ', bg='light blue', font=("Arial", 25))
    b3 = Button(player_batting2_frame, text='    3    ', bg='light blue', font=("Arial", 25))
    b4 = Button(player_batting2_frame, text='    4    ', bg='light blue', font=("Arial", 25))
    b5 = Button(player_batting2_frame, text='    5    ', bg='light blue', font=("Arial", 25))
    b6 = Button(player_batting2_frame, text='    6    ', bg='light blue', font=("Arial", 25))
    b_ex = Button(player_batting2_frame, text='Exit', bg='light blue', font=("Arial", 20), command=root.destroy)
    b1.config(command=lambda: batting2_buttons(1, b1, b2, b3, b4, b5, b6))
    b2.config(command=lambda: batting2_buttons(2, b1, b2, b3, b4, b5, b6))
    b3.config(command=lambda: batting2_buttons(3, b1, b2, b3, b4, b5, b6))
    b4.config(command=lambda: batting2_buttons(4, b1, b2, b3, b4, b5, b6))
    b5.config(command=lambda: batting2_buttons(5, b1, b2, b3, b4, b5, b6))
    b6.config(command=lambda: batting2_buttons(6, b1, b2, b3, b4, b5, b6))

    b1.place(x=80, y=444)
    b2.place(x=200, y=444)
    b3.place(x=320, y=444)

    b4.place(x=440, y=444)
    b5.place(x=560, y=444)
    b6.place(x=680, y=444)
    b_ex.pack(side=BOTTOM, pady=10)
    bgl.place(relwidth=1, relheight=1)

def setup_player_bowling2():
    img = PhotoImage(file='hcg_bg1.png')
    bgl = Label(player_bowling2_frame, image=img)
    bgl.image = img
    heading = Label(player_bowling2_frame, text=' The 2nd innings begins! ', bg='light blue', font=("Arial", 30))
    heading.pack(pady=20)
    Label(player_bowling2_frame, text="Player's choice : ", bg='light blue', font=("Arial", 25)).place(x=20, y=88)
    b1 = Button(player_bowling2_frame, text='    1    ', bg='light blue', font=("Arial", 25))
    b2 = Button(player_bowling2_frame, text='    2    ', bg='light blue', font=("Arial", 25))
    b3 = Button(player_bowling2_frame, text='    3    ', bg='light blue', font=("Arial", 25))
    b4 = Button(player_bowling2_frame, text='    4    ', bg='light blue', font=("Arial", 25))
    b5 = Button(player_bowling2_frame, text='    5    ', bg='light blue', font=("Arial", 25))
    b6 = Button(player_bowling2_frame, text='    6    ', bg='light blue', font=("Arial", 25))
    b_ex = Button(player_bowling2_frame, text='Exit', bg='light blue', font=("Arial", 20), command=root.destroy)
    b1.config(command=lambda: bowling2_buttons(1, b1, b2, b3, b4, b5, b6))
    b2.config(command=lambda: bowling2_buttons(2, b1, b2, b3, b4, b5, b6))
    b3.config(command=lambda: bowling2_buttons(3, b1, b2, b3, b4, b5, b6))
    b4.config(command=lambda: bowling2_buttons(4, b1, b2, b3, b4, b5, b6))
    b5.config(command=lambda: bowling2_buttons(5, b1, b2, b3, b4, b5, b6))
    b6.config(command=lambda: bowling2_buttons(6, b1, b2, b3, b4, b5, b6))

    b1.place(x=80, y=444)
    b2.place(x=200, y=444)
    b3.place(x=320, y=444)

    b4.place(x=440, y=444)
    b5.place(x=560, y=444)
    b6.place(x=680, y=444)
    b_ex.pack(side=BOTTOM, pady=10)
    bgl.place(relwidth=1, relheight=1)

def show_about():
    home_frame.pack_forget()  # Hide home frame
    play_frame.pack_forget()
    player_tw_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    about_frame.pack(fill="both", expand=True)  # Show page 2 frame

def show_home_page():
    about_frame.pack_forget() # Hide page 2 frame
    play_frame.pack_forget()
    player_tw_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)  # Show home frame

def show_play():
    home_frame.pack_forget()
    about_frame.pack_forget()
    player_tw_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    play_frame.pack(fill="both",expand=True)

def show_player_tw():
    home_frame.pack_forget()
    about_frame.pack_forget()
    play_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    player_tw_frame.pack(fill='both',expand=True)

def show_comp_tw():
    home_frame.pack_forget()
    about_frame.pack_forget()
    play_frame.pack_forget()
    player_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    comp_tw_frame.pack(fill='both', expand=True)

def show_player_batting1_buttons():
    home_frame.pack_forget()
    about_frame.pack_forget()
    play_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_tw_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    player_batting1_frame.pack(fill='both', expand=True)

def show_player_bowling1_buttons():
    home_frame.pack_forget()
    about_frame.pack_forget()
    play_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    player_bowling1_frame.pack(fill='both', expand=True)

def show_player_batting2_buttons():
    home_frame.pack_forget()
    about_frame.pack_forget()
    play_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_bowling2_frame.pack_forget()
    player_batting2_frame.pack(fill='both',expand=True)

def show_player_bowling2_buttons():
    home_frame.pack_forget()
    about_frame.pack_forget()
    play_frame.pack_forget()
    comp_tw_frame.pack_forget()
    player_tw_frame.pack_forget()
    player_batting1_frame.pack_forget()
    player_bowling1_frame.pack_forget()
    player_batting2_frame.pack_forget()
    player_bowling2_frame.pack(fill='both', expand=True)

# Setup the pages
setup_home_page()
setup_about()
setup_play()
setup_player_tw()
setup_comp_tw()
setup_player_batting1()
setup_player_bowling1()
setup_player_batting2()
setup_player_bowling2()

# Start with the home page
home_frame.pack(fill="both", expand=True)

# Run the application
mainloop()
