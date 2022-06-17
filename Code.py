import pygame, sys
from pygame.locals import *
from pygame import mixer
import webbrowser
import tkinter as tk
from tkinter import *
import random
import time
#https://www.geeksforgeeks.org/pygame-creating-sprites/
#-------------------------
#Music function (plays when start is pressed):
#def Play_music():
#from replit import audio
#def classical_music():
# source = audio.play_file('music.wav')
#classical_music()

#while True:
# pass
#Token Locations

players = []
playerCount = 0
playerDict = {}
turnc = 1
sixcount = 0
allTokens = []
winnerOrder = []
B_score = R_score = Y_score = G_score = 0
turnnum = 1
GOLD = (230, 180, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 250)
RED = (235, 0, 0)
GREEN = (0, 175, 0)
YELLOW = (230, 230, 0)
GRAY = (130, 130, 130)
COUNTER_GRAY = (220, 220, 220)


def display(message):
    window = tk.Tk()
    window.title("WARNING")
    window.geometry("350x125")
    window['background'] = 'white'
    p_op_label = tk.Label(font=('Helvetica', 8, 'bold'),
                          bg='white',
                          fg='black',
                          text=f"{message}")
    p_op_label.pack()
    p_op_label.place(x=25, y=25)
    window.mainloop()
    time.sleep(4)
    window.destroy()


def turn(player):
    global turnc, turnnum
    turnnum += 1
    if player.color == "green":
        pygame.draw.rect(screen, WHITE, (12, 12, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (12, 363, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (363, 10, 216, 218), 4)
        pygame.draw.rect(screen, GOLD, (363, 363, 216, 216), 3)  #green gold
    elif player.color == "blue":
        pygame.draw.rect(screen, GOLD, (12, 12, 216, 216), 3)  #blue gold
        pygame.draw.rect(screen, WHITE, (12, 363, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (363, 10, 216, 218), 4)
        pygame.draw.rect(screen, WHITE, (363, 363, 216, 216), 4)
    elif player.color == "red":  #red
        pygame.draw.rect(screen, WHITE, (12, 12, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (12, 363, 216, 216), 4)
        pygame.draw.rect(screen, GOLD, (363, 10, 216, 218), 3)  #red gold
        pygame.draw.rect(screen, WHITE, (363, 363, 216, 216), 4)
    elif player.color == "yellow":  #yellow
        pygame.draw.rect(screen, WHITE, (12, 12, 216, 216), 4)
        pygame.draw.rect(screen, GOLD, (12, 363, 216, 216), 3)  #yellow gold
        pygame.draw.rect(screen, WHITE, (363, 10, 216, 218), 4)
        pygame.draw.rect(screen, WHITE, (363, 363, 216, 216), 4)
    pygame.display.update()
    print(f"{player.name}, it is your turn")
    move(player)
    update_turn()
    print("__________________________")


def choose_token(player):
    while True:
        t = input("Choose a token(t1,t2,t3,t4): ")
        if t == "t1":
            selectedToken = player.token1
            break
        elif t == "t2":
            selectedToken = player.token2
            break
        elif t == "t3":
            selectedToken = player.token3
            break
        elif t == "t4":
            selectedToken = player.token4
            break
        else:
            print("Please enter a valid input...")
    return selectedToken


def tokenupdate():
    for each in players:
        if each.color == "blue":
            player1 = each
        elif each.color == "green":
            player2 = each
        elif each.color == "red":
            player3 = each
        elif each.color == "yellow":
            player4 = each
    colors = []
    for each in players:
        colors.append(each.color)
    if "blue" in colors:
        b1_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token1.find_tokencoordinates(),
                                      13)
        b2_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token2.find_tokencoordinates(),
                                      13)
        b3_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token3.find_tokencoordinates(),
                                      13)
        b4_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token4.find_tokencoordinates(),
                                      13)
    if "green" in colors:
        g1_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token1.find_tokencoordinates(),
                                      13)
        g2_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token2.find_tokencoordinates(),
                                      13)
        g3_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token3.find_tokencoordinates(),
                                      13)
        g4_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token4.find_tokencoordinates(),
                                      13)
    if "red" in colors:
        r1_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token1.find_tokencoordinates(),
                                      13)
        r2_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token2.find_tokencoordinates(),
                                      13)
        r3_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token3.find_tokencoordinates(),
                                      13)
        r4_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token4.find_tokencoordinates(),
                                      13)
    if "yellow" in colors:
        y1_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token1.find_tokencoordinates(),
                                      13)
        y2_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token2.find_tokencoordinates(),
                                      13)
        y3_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token3.find_tokencoordinates(),
                                      13)
        y4_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token4.find_tokencoordinates(),
                                      13)


def move(player):
    global sixcount
    if sixcount == 3:
        print("You rolled 3 sixes, you lost your turn")
    else:
        while True:
            inp = input("Press r to roll... ")
            if inp == "r":
                value = roll()
                displaydiceroll(value, player.color)
                pygame.display.update()
                time.sleep(1)
                if value == 6:
                    sixcount += 1
                break
            else:
                print("Please enter a valid input")
        movePossibility = check_move_possibility_for_player(player, value)
        if movePossibility == True:
            selectToken = False
            while selectToken == False:
                token = choose_token(player)
                if check_move_possibility_for_token(token, value) == True:
                    break
                else:
                    print(f"You cannot move this token, choose another...")
            while True:
                if token.inhome == True and value == 6:
                    out_of_home(token)
                    print(f"Roll again since you got a 6...")
                    move(player)
                    break
                elif token.inhome == False and value == 6:
                    move_token(player, token, value)
                    print(f"Roll again since you got a 6...")
                    move(player)
                    break
                elif token.inhome == False and value != 6:
                    move_token(player, token, value)
                    break
        else:
            print(f"{player.name}, you cannot move this turn...")


def displaydiceroll(diceroll, color):
    pygame.draw.rect(screen, (0, 0, 0), (182, 182, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (183, 183, 40, 40), 20)
    #Red
    pygame.draw.rect(screen, (0, 0, 0), (368, 182, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (369, 183, 40, 40), 20)
    #Yellow
    pygame.draw.rect(screen, (0, 0, 0), (182, 368, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (183, 369, 40, 40), 20)
    #Green
    pygame.draw.rect(screen, (0, 0, 0), (368, 368, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (369, 369, 40, 40), 20)
    if color == "green":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (389, 389), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (379, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 389), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
    if color == "red":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (389, 202), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (379, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 202), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
    if color == "yellow":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (202, 389), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (192, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 389), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 399), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 399), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 399), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (222, 399), 4)
    if color == "blue":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (202, 202), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (192, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 202), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)


def move_token(player, token, value):
    global Y_score, G_score, B_score, R_score
    spotNum = token.location.loc
    token.location.tokenson -= 1
    while value != 0:
        value -= 1
        if token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "yellow":
            spotNum = 48
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "blue":
            spotNum = 54
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "red":
            spotNum = 60
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "green":
            spotNum = 66
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved != 46 and token.location == board[47]:
            spotNum = 0
            token.location = board[spotNum]
            token.whitespacesmoved += 1
            token.totalspacesmoved += 1
        else:
            if token.location.type == "white":
                spotNum += 1
                token.location = board[spotNum]
                token.whitespacesmoved += 1
                token.totalspacesmoved += 1
            elif token.location.type == "runway":
                spotNum += 1
                token.location = board[spotNum]
                token.runwayspacesmoved += 1
                token.totalspacesmoved += 1
    if value == 0:
        token.location = board[spotNum]
        token.location.tokenson += 1
        if token.runwayspacesmoved == 6:
            score(token)

        if check_safe(token) == False and token.location.tokenson == 2:
            kill(token)
        if player.color == "yellow" and Y_score == 4:
            winnerOrder.append(player)
            end_player(player)
            Y_score = 0
        if player.color == "blue" and B_score == 4:
            winnerOrder.append(player)
            end_player(player)
            B_score = 0
        if player.color == "green" and G_score == 4:
            winnerOrder.append(player)
            end_player(player)
            G_score = 0
        if player.color == "red" and R_score == 4:
            winnerOrder.append(player)
            end_player(player)
            R_score = 0


def check_safe(token):
    safe = False
    if token.location.safe == True:
        safe = True
    elif token.location.tokenson >= 2:
        safe = True
    return safe


def kill(token):
    for each in allTokens:
        if each.location.loc == token.location.loc:
            otherToken = each
            send_home(otherToken)
    print(f"{token.owner.name} just ate {otherToken.owner.name}")


def score(token):
    global Y_score, G_score, B_score, R_score
    print(f"{token.owner.name} just got {token.tokennum} home")
    if token.color == "yellow":
        Y_score += 1
    elif token.color == "blue":
        B_score += 1
    elif token.color == "green":
        G_score += 1
    elif token.color == "red":
        R_score += 1
    token.location = finished_loc[0]


def create_turns():
    global playerCount
    for each in players:
        playerCount += 1
        playerDict[each] = playerCount


def find_turn():
    playerTurn = list(playerDict.keys())[list(
        playerDict.values()).index(turnc)]
    return playerTurn


def end_player(player):
    global playerCount, turnc
    players.remove(player)
    playerCount = 0
    turnc -= 1
    playerDict.clear()
    create_turns()


def update_turn():
    global playerCount, turnc, sixcount
    sixcount = 0
    if turnc == playerCount:
        turnc = 1
    else:
        turnc += 1


def working():
    print("working on this")


def check_move_possibility_for_player(player, value):
    move_possibility = False
    if check_move_possibility_for_token(player.token1, value) == True:
        move_possibility = True
        chooset1 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 1",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset1 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 1",
                             fg='black',
                             command=lambda: [working()])
    if check_move_possibility_for_token(player.token2, value) == True:
        move_possibility = True
        chooset2 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 2",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset2 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 2",
                             fg='black',
                             command=lambda: [working()])
    if check_move_possibility_for_token(player.token3, value) == True:
        move_possibility = True
        chooset3 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 3",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset3 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 3",
                             fg='black',
                             command=lambda: [working()])
    if check_move_possibility_for_token(player.token4, value) == True:
        move_possibility = True
        chooset4 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 4",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset4 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 4",
                             fg='black',
                             command=lambda: [working()])
    chooset1.pack()
    chooset1.place(x=90, y=165)
    chooset2.pack()
    chooset2.place(x=90, y=165)
    chooset3.pack()
    chooset3.place(x=90, y=165)
    chooset4.pack()
    chooset4.place(x=90, y=165)
    pygame.display.update()
    return move_possibility


def check_move_possibility_for_token(token, value):
    move_possibility = True
    if value != 6 and token.inhome == True:
        move_possibility = False
    elif token.find_spacesuntilhome() < value:
        move_possibility = False
    return move_possibility


def reset_token_parameters():
    token.totalspacesmoved = 0
    token.whitespacesmoved = 0
    token.runwayspacesmoved = 0


def roll():
    roll1 = random.randint(1, 6)
    print(f"You just rolled a {roll1}")
    return roll1


def find_home(token):
    for each in homes_board:
        if each.color == token.color and each.tokenowner == token.tokennum:
            spot = homes_board[each.loc - 71]
    return spot


def send_home(token):
    token.location = find_home(token)
    reset_token_parameters()
    tokenupdate()


def out_of_home(mytoken):
    mytoken.inhome = False
    if mytoken.color == "red":
        mytoken.location = board[24]
        mytoken.location.tokenson += 1
    elif mytoken.color == "green":
        mytoken.location = board[36]
        mytoken.location.tokenson += 1
    elif mytoken.color == "blue":
        mytoken.location = board[12]
        mytoken.location.tokenson += 1
    elif mytoken.color == "yellow":
        mytoken.location = board[0]
        mytoken.location.tokenson += 1
    print(f"{mytoken.tokennum} is out of home")


def display_winners():
    print("Leaderboards...")
    print(f"First Place: {winnerOrder[0].name}")
    print(f"Second Place: {winnerOrder[1].name}")
    if len(players) > 2:
        print(f"Third Place: {winnerOrder[2].name}")


#____________________________________


class player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.playingtokens = 4
        self.playing = True
        self.token1 = token(self, self.color, "token1")
        self.token2 = token(self, self.color, "token2")
        self.token3 = token(self, self.color, "token3")
        self.token4 = token(self, self.color, "token4")
        allTokens.append(self.token1)
        allTokens.append(self.token2)
        allTokens.append(self.token3)
        allTokens.append(self.token4)


class token():
    def __init__(self, owner, color, tokennum):
        self.owner = owner
        self.color = color
        self.tokennum = tokennum
        self.inhome = True
        self.totalspacesmoved = 0
        self.whitespacesmoved = 0
        self.runwayspacesmoved = 0
        self.location = find_home(self)
        self.safe = False

    def find_spacesuntilhome(self):
        self.spacesuntilhome = (46 - self.whitespacesmoved) + (
            6 - self.runwayspacesmoved)
        return self.spacesuntilhome

    def find_tokencoordinates(self):
        return self.location.coord


class location():
    def __init__(self, locnum, color, safe, runway, runwayhome, coordinates,
                 type):
        self.loc = locnum
        self.color = color
        self.safe = safe
        self.runway = runway
        self.runwayhome = runwayhome
        self.coord = coordinates
        self.type = type
        self.tokenson = 0


class home():
    def __init__(self, locnum, color, tokenowner, coordinates, type):
        self.loc = locnum
        self.color = color
        self.tokenowner = tokenowner
        self.coord = coordinates
        self.type = type


#White Locations
loc0 = location(0, "white", True, False, False, (252, 513), "white")
loc1 = location(1, "white", False, False, False, (252, 470), "white")
loc2 = location(2, "white", False, False, False, (252, 427), "white")
loc3 = location(3, "white", False, False, False, (252, 384), "white")
loc4 = location(4, "white", False, False, False, (252, 342), "white")
loc5 = location(5, "white", False, False, False, (209, 342), "white")
loc6 = location(6, "white", False, False, False, (166, 342), "white")
loc7 = location(7, "white", False, False, False, (123, 342), "white")
loc8 = location(8, "white", False, False, False, (80, 342), "white")
loc9 = location(9, "white", False, False, False, (37, 342), "white")
loc10 = location(10, "white", False, False, False, (37, 295), "white")
loc11 = location(11, "white", False, False, False, (37, 252), "white")
loc12 = location(12, "white", True, False, False, (80, 252), "white")
loc13 = location(13, "white", False, False, False, (123, 252), "white")
loc14 = location(14, "white", False, False, False, (166, 252), "white")
loc15 = location(15, "white", False, False, False, (209, 252), "white")
loc16 = location(16, "white", False, False, False, (252, 252), "white")
loc17 = location(17, "white", False, False, False, (252, 209), "white")
loc18 = location(18, "white", False, False, False, (252, 166), "white")
loc19 = location(19, "white", False, False, False, (252, 123), "white")
loc20 = location(20, "white", False, False, False, (252, 80), "white")
loc21 = location(21, "white", False, False, False, (252, 37), "white")
loc22 = location(22, "white", False, False, False, (296, 37), "white")
loc23 = location(23, "white", False, False, False, (340, 37), "white")
loc24 = location(24, "white", True, False, False, (341, 80), "white")
loc25 = location(25, "white", False, False, False, (341, 123), "white")
loc26 = location(26, "white", False, False, False, (341, 166), "white")
loc27 = location(27, "white", False, False, False, (341, 209), "white")
loc28 = location(28, "white", False, False, False, (341, 251), "white")
loc29 = location(29, "white", False, False, False, (384, 251), "white")
loc30 = location(30, "white", False, False, False, (427, 251), "white")
loc31 = location(31, "white", False, False, False, (470, 251), "white")
loc32 = location(32, "white", False, False, False, (513, 251), "white")
loc33 = location(33, "white", False, False, False, (556, 251), "white")
loc34 = location(34, "white", False, False, False, (556, 296), "white")
loc35 = location(35, "white", False, False, False, (556, 339), "white")
loc36 = location(36, "white", True, False, False, (513, 339), "white")
loc37 = location(37, "white", False, False, False, (470, 342), "white")
loc38 = location(38, "white", False, False, False, (427, 342), "white")
loc39 = location(39, "white", False, False, False, (384, 342), "white")
loc40 = location(40, "white", False, False, False, (341, 342), "white")
loc41 = location(41, "white", False, False, False, (341, 385), "white")
loc42 = location(42, "white", False, False, False, (341, 428), "white")
loc43 = location(43, "white", False, False, False, (341, 471), "white")
loc44 = location(44, "white", False, False, False, (341, 514), "white")
loc45 = location(45, "white", False, False, False, (340, 557), "white")
loc46 = location(46, "white", False, False, False, (297, 557), "white")
loc47 = location(47, "white", False, False, False, (253, 557), "white")
#Runway locations
loc48 = location(48, "yellow", True, True, False, (297, 513), "runway")
loc49 = location(49, "yellow", True, True, False, (297, 470), "runway")
loc50 = location(50, "yellow", True, True, False, (297, 427), "runway")
loc51 = location(51, "yellow", True, True, False, (297, 384), "runway")
loc52 = location(52, "yellow", True, True, False, (297, 341), "runway")
loc53 = location(53, "yellow", True, True, True, (297, 300), "runway")
loc54 = location(54, "blue", True, True, False, (80, 295), "runway")
loc55 = location(55, "blue", True, True, False, (123, 295), "runway")
loc56 = location(56, "blue", True, True, False, (166, 295), "runway")
loc57 = location(57, "blue", True, True, False, (209, 295), "runway")
loc58 = location(58, "blue", True, True, False, (252, 295), "runway")
loc59 = location(59, "blue", True, True, True, (295, 295), "runway")
loc60 = location(60, "red", True, True, False, (297, 82), "runway")
loc61 = location(61, "red", True, True, False, (297, 125), "runway")
loc62 = location(62, "red", True, True, False, (297, 168), "runway")
loc63 = location(63, "red", True, True, False, (297, 211), "runway")
loc64 = location(64, "red", True, True, False, (297, 254), "runway")
loc65 = location(65, "red", True, True, True, (297, 297), "runway")
loc66 = location(66, "green", True, True, False, (515, 295), "runway")
loc67 = location(67, "green", True, True, False, (472, 295), "runway")
loc68 = location(68, "green", True, True, False, (386, 295), "runway")
loc69 = location(69, "green", True, True, False, (343, 295), "runway")
loc70 = location(70, "green", True, True, True, (297, 295), "runway")
#Starting Home Locations
loc71 = home(71, "yellow", "token1", (80, 433), "home")
loc72 = home(72, "yellow", "token2", (160, 433), "home")
loc73 = home(73, "yellow", "token3", (80, 513), "home")
loc74 = home(74, "yellow", "token4", (160, 513), "home")
loc75 = home(75, "blue", "token1", (80, 80), "home")
loc76 = home(76, "blue", "token2", (160, 80), "home")
loc77 = home(77, "blue", "token3", (80, 160), "home")
loc78 = home(78, "blue", "token4", (160, 160), "home")
loc79 = home(79, "red", "token1", (435, 80), "home")
loc80 = home(80, "red", "token2", (515, 80), "home")
loc81 = home(81, "red", "token3", (435, 160), "home")
loc82 = home(82, "red", "token4", (515, 160), "home")
loc83 = home(83, "green", "token1", (432, 433), "home")
loc84 = home(84, "green", "token2", (512, 433), "home")
loc85 = home(85, "green", "token3", (432, 513), "home")
loc86 = home(86, "green", "token4", (512, 513), "home")

loc87 = home(87, "green", "token4", (1000, 1000), "home")

board = [
    loc0, loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9, loc10, loc11,
    loc12, loc13, loc14, loc15, loc16, loc17, loc18, loc19, loc20, loc21,
    loc22, loc23, loc24, loc25, loc26, loc27, loc28, loc29, loc30, loc31,
    loc32, loc33, loc34, loc35, loc36, loc37, loc38, loc39, loc40, loc41,
    loc42, loc43, loc44, loc45, loc46, loc47, loc48, loc49, loc50, loc51,
    loc52, loc53, loc54, loc55, loc56, loc57, loc58, loc59, loc60, loc61,
    loc62, loc63, loc64, loc65, loc66, loc67, loc68, loc69, loc70
]

homes_board = [
    loc71, loc72, loc73, loc74, loc75, loc76, loc77, loc78, loc79, loc80,
    loc81, loc82, loc83, loc84, loc85, loc86
]

finished_loc = [loc87]


#--------------------------------
def displayrules():
    webbrowser.open('https://www.ymimports.com/pages/how-to-play-ludo')


def nono():
    print("You need more than 1 player readied to start the game!")


#----------Player options----------
def playerscreen():
    global P1_entry, P2_entry, P3_entry, P4_entry
    global P1_Player, P2_Player, P3_Player, P4_Player
    global bcol, gcol, rcol, ycol
    bcol = gcol = rcol = ycol = 0
    #----------Window Style----------
    window = tk.Tk()
    window.title("Ludo Players Screen")
    window.geometry("300x250")
    window['background'] = '#34DDF7'

    #title to player options
    p_op_label = tk.Label(font=('Helvetica', 18, 'bold'),
                          bg='#34DDF7',
                          fg='black',
                          text="Player Options")
    p_op_label.pack()
    p_op_label.place(x=40, y=1)

    #---------PLAYER NAMES INPUTS--------------
    #Player name input variables
    P1_Player = tk.StringVar()
    P2_Player = tk.StringVar()
    P3_Player = tk.StringVar()
    P4_Player = tk.StringVar()
    P1_entry = tk.Entry(window,
                        textvariable=P1_Player,
                        font=('Calibri', 11, 'normal'))
    P2_entry = tk.Entry(window,
                        textvariable=P2_Player,
                        font=('Calibri', 11, 'normal'))
    P3_entry = tk.Entry(window,
                        textvariable=P3_Player,
                        font=('Calibri', 11, 'normal'))
    P4_entry = tk.Entry(window,
                        textvariable=P4_Player,
                        font=('Calibri', 11, 'normal'))
    P1_Player = P1_entry.get()
    P2_Player = P2_entry.get()
    P3_Player = P3_entry.get()
    P4_Player = P4_entry.get()

    #----------Start Button----------
    def startbuttton_stat():
        count = bcol + gcol + rcol + ycol
        if count >= 2:  #2 or more players are readied
            sbutton = tk.Button(
                font=('Helvetica', 12, 'italic'),
                bg='gold',
                text="Start Game!",
                fg='black',
                command=lambda: [gamestart(), window.destroy()])
            sbutton.pack()
            sbutton.place(x=90, y=165)
        if count < 2:  #less than 2 players are readied
            sbutton = tk.Button(font=('Helvetica', 12, 'italic'),
                                bg='grey',
                                text="Start Game!",
                                fg='black',
                                command=lambda: [nono()])
            sbutton.pack()
            sbutton.place(x=90, y=165)
#--------------------------------

#Player B

    def b_col():
        global bcol
        bcol += 1
        if bcol > 1:
            bcol = 0
        if bcol == 1:
            pb_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='blue',
                                  text="Player 1",
                                  fg='black',
                                  command=lambda: [b_col()])
            pb_status.pack()
            pb_status.place(x=10, y=42)
            P1_entry.place(x=80, y=42)
        if bcol == 0:
            pb_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 1",
                                  fg='black',
                                  command=lambda: [b_col()])
            pb_status.pack()
            pb_status.place(x=10, y=42)
            P1_entry.place(x=900, y=42)
        startbuttton_stat()

    b_col()

    #Player G
    def g_col():
        global gcol
        gcol += 1
        if gcol > 1:
            gcol = 0
        if gcol == 1:
            pg_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='green',
                                  text="Player 2",
                                  fg='black',
                                  command=lambda: [g_col()])
            pg_status.pack()
            pg_status.place(x=10, y=71)
            P2_entry.place(x=80, y=71)
        if gcol == 0:
            pg_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 2",
                                  fg='black',
                                  command=lambda: [g_col()])
            pg_status.pack()
            pg_status.place(x=10, y=71)
            P2_entry.place(x=900, y=71)
        startbuttton_stat()

    g_col()

    #Player R
    def r_col():
        global rcol
        rcol += 1
        if rcol > 1:
            rcol = 0
        if rcol == 1:
            pr_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='red',
                                  text="Player 3",
                                  fg='black',
                                  command=lambda: [r_col()])
            pr_status.pack()
            pr_status.place(x=10, y=100)
            P3_entry.place(x=80, y=100)
        if rcol == 0:
            pr_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 3",
                                  fg='black',
                                  command=lambda: [r_col()])
            pr_status.pack()
            pr_status.place(x=10, y=100)
            P3_entry.place(x=900, y=100)
        startbuttton_stat()

    r_col()

    #Player Y
    def y_col():
        global ycol
        ycol += 1
        if ycol > 1:
            ycol = 0
        if ycol == 1:
            py_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='yellow',
                                  text="Player 4",
                                  fg='black',
                                  command=lambda: [y_col()])
            py_status.pack()
            py_status.place(x=10, y=129)
            P4_entry.place(x=80, y=129)
        if ycol == 0:
            py_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 4",
                                  fg='black',
                                  command=lambda: [y_col()])
            py_status.pack()
            py_status.place(x=10, y=129)
            P4_entry.place(x=900, y=129)
        startbuttton_stat()

    y_col()

    #return to home button
    returnbutton = tk.Button(
        font=('Helvetica', 8, 'italic'),
        bg='white',
        text="Return to Home",
        fg='black',
        command=lambda: [window.destroy(), homescreen()])
    returnbutton.pack()
    returnbutton.place(x=95, y=210)
    tk.mainloop()


#---------------------------------------------------------


#----------Game Options-----------------------------------
def optionscreen():
    #----------Window Style----------
    window = tk.Tk()
    window.title("Ludo Options Screen")
    window.geometry("300x200")
    window['background'] = '#34DDF7'

    #title to general/game options
    g_op_label = tk.Label(font=('Helvetica', 22, 'bold'),
                          bg='#34DDF7',
                          fg='black',
                          text="Game Options")
    g_op_label.pack()
    g_op_label.place(x=29, y=5)

    #Game instructions
    gameinstruct = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='white',
                             text="Game Instructions",
                             fg='black',
                             command=lambda: [displayrules()])
    gameinstruct.pack()
    gameinstruct.place(x=60, y=100)

    #return to home
    returnbutton = tk.Button(
        font=('Helvetica', 8, 'italic'),
        bg='white',
        text="Return to Home",
        fg='black',
        command=lambda: [window.destroy(), homescreen()])
    returnbutton.pack()
    returnbutton.place(x=90, y=145)
    tk.mainloop()


def gamestart():
    global P1_Player, P2_Player, P3_Player, P4_Player
    global P1_entry, P2_entry, P3_entry, P4_entry, dimx, screen
    print("Game Started!\n___________________")
    if len(P1_entry.get()) != 0 and bcol == 1:
        player1 = player(P1_entry.get(), "blue")
        players.append(player1)
    elif len(P1_entry.get()) == 0 and bcol == 1:
        player1 = player("Player 1", "blue")
        players.append(player1)
    if len(P2_entry.get()) != 0 and gcol == 1:
        player2 = player(P2_entry.get(), "green")
        players.append(player2)
    elif len(P2_entry.get()) == 0 and gcol == 1:
        player2 = player("Player 2", "green")
        players.append(player2)
    if len(P3_entry.get()) != 0 and rcol == 1:
        player3 = player(P3_entry.get(), "red")
        players.append(player3)
    elif len(P3_entry.get()) == 0 and rcol == 1:
        player3 = player("Player 3", "red")
        players.append(player3)
    if len(P4_entry.get()) != 0 and ycol == 1:
        player4 = player(P4_entry.get(), "yellow")
        players.append(player4)
    elif len(P4_entry.get()) == 0 and ycol == 1:
        player4 = player("Player 4", "yellow")
        players.append(player4)
    #--------------------Board Display--------------------------
    pygame.init()  #Initializes all of pygame’s functions
    dimx = 593
    screen = pygame.display.set_mode((dimx, dimx + 50))
    pygame.display.set_caption(
        'LUDO')  #Displays the name of the window at the top
    GOLD = (230, 180, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 120, 250)
    RED = (235, 0, 0)
    GREEN = (0, 175, 0)
    YELLOW = (230, 230, 0)
    GRAY = (130, 130, 130)
    COUNTER_GRAY = (220, 220, 220)

    running = True  #turns on a command named 'running'
    while running:  #short form for when running is true:
        boardbgspace = pygame.draw.rect(screen, WHITE, (0, 0, dimx, dimx), 290)

        #coloured squares and shadow square
        board = pygame.draw.rect(screen, BLUE, (15, 15, 211, 211), 120)
        board = pygame.draw.rect(screen, YELLOW, (15, 365, 211, 211), 120)
        board = pygame.draw.rect(screen, RED, (365, 15, 211, 211), 120)
        board = pygame.draw.rect(screen, GREEN, (365, 365, 211, 211), 120)

        #Circles per big square
        #Blue
        board = pygame.draw.circle(screen, WHITE, (80, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (80, 160), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 160), 27)
        #Red
        board = pygame.draw.circle(screen, WHITE, (435, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (515, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (435, 160), 27)
        board = pygame.draw.circle(screen, WHITE, (515, 160), 27)
        #Yellow
        board = pygame.draw.circle(screen, WHITE, (80, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (80, 513), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 513), 27)
        #Green
        board = pygame.draw.circle(screen, WHITE, (432, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (512, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (432, 513), 27)
        board = pygame.draw.circle(screen, WHITE, (512, 513), 27)

        myfont = pygame.font.SysFont("Arial", 23)
        #Score Corners
        #BLUE
        board = pygame.draw.rect(screen, COUNTER_GRAY, (15, 15, 60, 30), 20)
        bscore = myfont.render(str(B_score), 1, BLACK)
        screen.blit(bscore, (40, 20))
        #RED
        board = pygame.draw.rect(screen, COUNTER_GRAY, (516, 15, 60, 30), 20)
        rscore = myfont.render(str(R_score), 1, BLACK)
        screen.blit(rscore, (542, 20))
        #YELLOW
        board = pygame.draw.rect(screen, COUNTER_GRAY, (15, 546, 60, 30), 20)
        yscore = myfont.render(str(Y_score), 1, BLACK)
        screen.blit(yscore, (40, 551))
        #GREEN
        board = pygame.draw.rect(screen, COUNTER_GRAY, (516, 546, 60, 30), 20)
        gscore = myfont.render(str(G_score), 1, BLACK)
        screen.blit(gscore, (542, 551))

        #Space coloured Yellow
        board = pygame.draw.rect(screen, YELLOW, (233, 495, 38, 38), 21)
        #Space coloured Red
        board = pygame.draw.rect(screen, RED, (320, 61, 40, 40), 21)
        #Space coloured Green
        board = pygame.draw.rect(screen, GREEN, (491, 320, 40, 40), 21)
        #Space coloured Blue
        board = pygame.draw.rect(screen, BLUE, (58, 229, 40, 42), 21)

        #Middle triangles
        board = pygame.draw.polygon(surface=screen,
                                    color=GREEN,
                                    points=[(322, 270), (322, 320),
                                            (295, 295)])
        board = pygame.draw.polygon(surface=screen,
                                    color=YELLOW,
                                    points=[(272, 320), (322, 320),
                                            (295, 295)])
        board = pygame.draw.polygon(surface=screen,
                                    color=BLUE,
                                    points=[(272, 270), (272, 320),
                                            (295, 295)])
        board = pygame.draw.polygon(surface=screen,
                                    color=RED,
                                    points=[(322, 270), (272, 270),
                                            (295, 295)])

        #Spaces
        #top row
        for x in range(3):
            board = pygame.draw.rect(screen, GRAY,
                                     (230 + (44 * x), 16, 44.1, 44.1), 3)
        next
        #Left Middle Top Row
        for x in range(6):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (15 + (43 * x), 229, 43, 44), 3)
        next
        #Left Middle Row
        board = pygame.draw.rect(screen, BLUE, (58, 273, 215, 47), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (58 + (43 * x), 273, 43, 47), 3)
        next
        #Right Middle Top Row
        for x in range(6):
            board = pygame.draw.rect(screen, GRAY,
                                     (319 + (43 * x), 228, 43, 44), 3)
        next
        #Left Middle Bottom Row
        for x in range(6):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (15 + (43 * x), 320, 43, 43), 3)
        next
        #Right Middle Row
        board = pygame.draw.rect(screen, GREEN, (322, 272, 213, 48), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (322 + (43 * x), 272, 43, 48), 3)
        next
        #Right Middle Bottom Row
        for x in range(6):
            board = pygame.draw.rect(screen, GRAY,
                                     (319 + (43 * x), 320, 43, 43), 3)
        next
        #BOTTOM row
        for x in range(3):
            board = pygame.draw.rect(screen, GRAY,
                                     (230 + (44 * x), 534, 44.1, 44.1), 3)
        next
        #-------y-axis spaces--------
        #L-Upper
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (230, 59 + (43 * x), 43, 43), 3)
        next
        #L-Bottom
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (230, 492 - (43 * x), 43, 43), 3)
        next
        #R-Upper
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (319, 59 + (43 * x), 43, 43), 3)
        next
        #R-Bottom
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (319, 492 - (43 * x), 43, 43), 3)
        next
        #L-MID
        board = pygame.draw.rect(screen, GRAY, (15, 271, 44.5, 50), 3)
        #Up-MID
        board = pygame.draw.rect(screen, RED, (273, 60, 47, 214), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (273, 60 + (43 * x), 47, 43), 3)
        next
        #Bot-MID
        board = pygame.draw.rect(screen, YELLOW, (273, 320, 47, 214), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (273, 320 + (43 * x), 47, 43), 3)
        next
        board = pygame.draw.rect(screen, GRAY, (534, 271, 43, 50), 3)

        #--------------DiCE-----------------
        #Dice Spot
        #Blue
        pygame.draw.rect(screen, BLACK, (182, 182, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (183, 183, 40, 40), 20)
        #Red
        pygame.draw.rect(screen, BLACK, (368, 182, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (369, 183, 40, 40), 20)
        #Yellow
        pygame.draw.rect(screen, BLACK, (182, 368, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (183, 369, 40, 40), 20)
        #Green
        pygame.draw.rect(screen, BLACK, (368, 368, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (369, 369, 40, 40), 20)

        tokenupdate()
        pygame.display.update()
        if turnnum == 1:
            create_turns()
            tokenupdate()
            pygame.display.update()
        if playerCount > 1:
            turn(find_turn())
        else:
            display_winners()
def homescreen():
    #----------Window Style----------
    window = tk.Tk()
    window.title("Ludo Starting Screen")
    window.geometry("350x200")
    window['background'] = '#B42DFC'

    #----------Game Title----------
    Bienvenue = tk.Label(font=('Helvetica', 24, 'bold', 'italic'),
                         bg='#B42DFC',
                         fg='white',
                         text="Welcome to Ludo!")
    Bienvenue.pack()
    Bienvenue.place(x=8, y=15)

    #----------Players Button----------
    pbutton = tk.Button(
        font=('Helvetica', 14, 'normal'),
        text="Players",
        fg='black',
        command=lambda: [window.destroy(), playerscreen()])
    pbutton.pack()
    pbutton['background'] = '#C2C2C2'
    pbutton.place(x=117.5, y=75)

    #----------Options Button----------
    obutton = tk.Button(
        font=('Helvetica', 14, 'normal'),
        text="Options",
        fg='black',
        command=lambda: [window.destroy(), optionscreen()])
    obutton.pack()
    obutton['background'] = '#C2C2C2'
    obutton.place(x=115, y=130)
    tk.mainloop()


homescreen()
import pygame, sys
from pygame.locals import *
from pygame import mixer
import webbrowser
import tkinter as tk
from tkinter import *
import random
import time
#https://www.geeksforgeeks.org/pygame-creating-sprites/
#-------------------------
#Music function (plays when start is pressed):
#def Play_music():
#from replit import audio
#def classical_music():
# source = audio.play_file('music.wav')
#classical_music()

#while True:
# pass
#Token Locations

players = []
playerCount = 0
playerDict = {}
turnc = 1
sixcount = 0
allTokens = []
winnerOrder = []
B_score = R_score = Y_score = G_score = 0
turnnum = 1
GOLD = (230, 180, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 250)
RED = (235, 0, 0)
GREEN = (0, 175, 0)
YELLOW = (230, 230, 0)
GRAY = (130, 130, 130)
COUNTER_GRAY = (220, 220, 220)


def display(message):
    window = tk.Tk()
    window.title("WARNING")
    window.geometry("350x125")
    window['background'] = 'white'
    p_op_label = tk.Label(font=('Helvetica', 8, 'bold'),
                          bg='white',
                          fg='black',
                          text=f"{message}")
    p_op_label.pack()
    p_op_label.place(x=25, y=25)
    window.mainloop()
    time.sleep(4)
    window.destroy()


def turn(player):
    global turnc, turnnum
    turnnum += 1
    if player.color == "green":
        pygame.draw.rect(screen, WHITE, (12, 12, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (12, 363, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (363, 10, 216, 218), 4)
        pygame.draw.rect(screen, GOLD, (363, 363, 216, 216), 3)  #green gold
    elif player.color == "blue":
        pygame.draw.rect(screen, GOLD, (12, 12, 216, 216), 3)  #blue gold
        pygame.draw.rect(screen, WHITE, (12, 363, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (363, 10, 216, 218), 4)
        pygame.draw.rect(screen, WHITE, (363, 363, 216, 216), 4)
    elif player.color == "red":  #red
        pygame.draw.rect(screen, WHITE, (12, 12, 216, 216), 4)
        pygame.draw.rect(screen, WHITE, (12, 363, 216, 216), 4)
        pygame.draw.rect(screen, GOLD, (363, 10, 216, 218), 3)  #red gold
        pygame.draw.rect(screen, WHITE, (363, 363, 216, 216), 4)
    elif player.color == "yellow":  #yellow
        pygame.draw.rect(screen, WHITE, (12, 12, 216, 216), 4)
        pygame.draw.rect(screen, GOLD, (12, 363, 216, 216), 3)  #yellow gold
        pygame.draw.rect(screen, WHITE, (363, 10, 216, 218), 4)
        pygame.draw.rect(screen, WHITE, (363, 363, 216, 216), 4)
    pygame.display.update()
    print(f"{player.name}, it is your turn")
    move(player)
    update_turn()
    print("__________________________")


def choose_token(player):
    while True:
        t = input("Choose a token(t1,t2,t3,t4): ")
        if t == "t1":
            selectedToken = player.token1
            break
        elif t == "t2":
            selectedToken = player.token2
            break
        elif t == "t3":
            selectedToken = player.token3
            break
        elif t == "t4":
            selectedToken = player.token4
            break
        else:
            print("Please enter a valid input...")
    return selectedToken


def tokenupdate():
    for each in players:
        if each.color == "blue":
            player1 = each
        elif each.color == "green":
            player2 = each
        elif each.color == "red":
            player3 = each
        elif each.color == "yellow":
            player4 = each
    colors = []
    for each in players:
        colors.append(each.color)
    if "blue" in colors:
        b1_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token1.find_tokencoordinates(),
                                      13)
        b2_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token2.find_tokencoordinates(),
                                      13)
        b3_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token3.find_tokencoordinates(),
                                      13)
        b4_token = pygame.draw.circle(screen, (0, 0, 235),
                                      player1.token4.find_tokencoordinates(),
                                      13)
    if "green" in colors:
        g1_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token1.find_tokencoordinates(),
                                      13)
        g2_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token2.find_tokencoordinates(),
                                      13)
        g3_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token3.find_tokencoordinates(),
                                      13)
        g4_token = pygame.draw.circle(screen, (0, 120, 0),
                                      player2.token4.find_tokencoordinates(),
                                      13)
    if "red" in colors:
        r1_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token1.find_tokencoordinates(),
                                      13)
        r2_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token2.find_tokencoordinates(),
                                      13)
        r3_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token3.find_tokencoordinates(),
                                      13)
        r4_token = pygame.draw.circle(screen, (170, 0, 0),
                                      player3.token4.find_tokencoordinates(),
                                      13)
    if "yellow" in colors:
        y1_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token1.find_tokencoordinates(),
                                      13)
        y2_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token2.find_tokencoordinates(),
                                      13)
        y3_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token3.find_tokencoordinates(),
                                      13)
        y4_token = pygame.draw.circle(screen, (190, 190, 0),
                                      player4.token4.find_tokencoordinates(),
                                      13)


def move(player):
    global sixcount
    if sixcount == 3:
        print("You rolled 3 sixes, you lost your turn")
    else:
        while True:
            inp = input("Press r to roll... ")
            if inp == "r":
                value = roll()
                displaydiceroll(value, player.color)
                pygame.display.update()
                time.sleep(1)
                if value == 6:
                    sixcount += 1
                break
            else:
                print("Please enter a valid input")
        movePossibility = check_move_possibility_for_player(player, value)
        if movePossibility == True:
            selectToken = False
            while selectToken == False:
                token = choose_token(player)
                if check_move_possibility_for_token(token, value) == True:
                    break
                else:
                    print(f"You cannot move this token, choose another...")
            while True:
                if token.inhome == True and value == 6:
                    out_of_home(token)
                    print(f"Roll again since you got a 6...")
                    move(player)
                    break
                elif token.inhome == False and value == 6:
                    move_token(player, token, value)
                    print(f"Roll again since you got a 6...")
                    move(player)
                    break
                elif token.inhome == False and value != 6:
                    move_token(player, token, value)
                    break
        else:
            print(f"{player.name}, you cannot move this turn...")


def displaydiceroll(diceroll, color):
    pygame.draw.rect(screen, (0, 0, 0), (182, 182, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (183, 183, 40, 40), 20)
    #Red
    pygame.draw.rect(screen, (0, 0, 0), (368, 182, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (369, 183, 40, 40), 20)
    #Yellow
    pygame.draw.rect(screen, (0, 0, 0), (182, 368, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (183, 369, 40, 40), 20)
    #Green
    pygame.draw.rect(screen, (0, 0, 0), (368, 368, 42, 42), 21)
    pygame.draw.rect(screen, (255, 255, 255), (369, 369, 40, 40), 20)
    if color == "green":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (389, 389), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (379, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 389), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (379, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 399), 4)
    if color == "red":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (389, 202), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (379, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 202), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (389, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (379, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (379, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (399, 212), 4)
    if color == "yellow":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (202, 389), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (192, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 389), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 399), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 399), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 399), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (192, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 399), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 379), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 389), 4)
            pygame.draw.circle(screen, (0, 0, 0), (222, 399), 4)
    if color == "blue":
        if diceroll == 1:
            pygame.draw.circle(screen, (0, 0, 0), (202, 202), 4)
        if diceroll == 2:
            pygame.draw.circle(screen, (0, 0, 0), (192, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 202), 4)
        if diceroll == 3:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)
        if diceroll == 4:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)
        if diceroll == 5:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (202, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)
        if diceroll == 6:
            pygame.draw.circle(screen, (0, 0, 0), (192, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (192, 212), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 192), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 202), 4)
            pygame.draw.circle(screen, (0, 0, 0), (212, 212), 4)


def move_token(player, token, value):
    global Y_score, G_score, B_score, R_score
    spotNum = token.location.loc
    token.location.tokenson -= 1
    while value != 0:
        value -= 1
        if token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "yellow":
            spotNum = 48
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "blue":
            spotNum = 54
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "red":
            spotNum = 60
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved == 46 and token.location.type == "white" and token.color == "green":
            spotNum = 66
            token.location = board[spotNum]
            token.runwayspacesmoved += 1
            token.totalspacesmoved += 1
        elif token.whitespacesmoved != 46 and token.location == board[47]:
            spotNum = 0
            token.location = board[spotNum]
            token.whitespacesmoved += 1
            token.totalspacesmoved += 1
        else:
            if token.location.type == "white":
                spotNum += 1
                token.location = board[spotNum]
                token.whitespacesmoved += 1
                token.totalspacesmoved += 1
            elif token.location.type == "runway":
                spotNum += 1
                token.location = board[spotNum]
                token.runwayspacesmoved += 1
                token.totalspacesmoved += 1
    if value == 0:
        token.location = board[spotNum]
        token.location.tokenson += 1
        if token.runwayspacesmoved == 6:
            score(token)

        if check_safe(token) == False and token.location.tokenson == 2:
            kill(token)
        if player.color == "yellow" and Y_score == 4:
            winnerOrder.append(player)
            end_player(player)
            Y_score = 0
        if player.color == "blue" and B_score == 4:
            winnerOrder.append(player)
            end_player(player)
            B_score = 0
        if player.color == "green" and G_score == 4:
            winnerOrder.append(player)
            end_player(player)
            G_score = 0
        if player.color == "red" and R_score == 4:
            winnerOrder.append(player)
            end_player(player)
            R_score = 0


def check_safe(token):
    safe = False
    if token.location.safe == True:
        safe = True
    elif token.location.tokenson >= 2:
        safe = True
    return safe


def kill(token):
    for each in allTokens:
        if each.location.loc == token.location.loc:
            otherToken = each
            send_home(otherToken)
    print(f"{token.owner.name} just ate {otherToken.owner.name}")


def score(token):
    global Y_score, G_score, B_score, R_score
    print(f"{token.owner.name} just got {token.tokennum} home")
    if token.color == "yellow":
        Y_score += 1
    elif token.color == "blue":
        B_score += 1
    elif token.color == "green":
        G_score += 1
    elif token.color == "red":
        R_score += 1
    token.location = finished_loc[0]


def create_turns():
    global playerCount
    for each in players:
        playerCount += 1
        playerDict[each] = playerCount


def find_turn():
    playerTurn = list(playerDict.keys())[list(
        playerDict.values()).index(turnc)]
    return playerTurn


def end_player(player):
    global playerCount, turnc
    players.remove(player)
    playerCount = 0
    turnc -= 1
    playerDict.clear()
    create_turns()


def update_turn():
    global playerCount, turnc, sixcount
    sixcount = 0
    if turnc == playerCount:
        turnc = 1
    else:
        turnc += 1


def working():
    print("working on this")


def check_move_possibility_for_player(player, value):
    move_possibility = False
    if check_move_possibility_for_token(player.token1, value) == True:
        move_possibility = True
        chooset1 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 1",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset1 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 1",
                             fg='black',
                             command=lambda: [working()])
    if check_move_possibility_for_token(player.token2, value) == True:
        move_possibility = True
        chooset2 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 2",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset2 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 2",
                             fg='black',
                             command=lambda: [working()])
    if check_move_possibility_for_token(player.token3, value) == True:
        move_possibility = True
        chooset3 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 3",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset3 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 3",
                             fg='black',
                             command=lambda: [working()])
    if check_move_possibility_for_token(player.token4, value) == True:
        move_possibility = True
        chooset4 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='gold',
                             text="Token 4",
                             fg='black',
                             command=lambda: [working()])
    else:
        chooset4 = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='grey',
                             text="Token 4",
                             fg='black',
                             command=lambda: [working()])
    chooset1.pack()
    chooset1.place(x=90, y=165)
    chooset2.pack()
    chooset2.place(x=90, y=165)
    chooset3.pack()
    chooset3.place(x=90, y=165)
    chooset4.pack()
    chooset4.place(x=90, y=165)
    pygame.display.update()
    return move_possibility


def check_move_possibility_for_token(token, value):
    move_possibility = True
    if value != 6 and token.inhome == True:
        move_possibility = False
    elif token.find_spacesuntilhome() < value:
        move_possibility = False
    return move_possibility


def reset_token_parameters():
    token.totalspacesmoved = 0
    token.whitespacesmoved = 0
    token.runwayspacesmoved = 0


def roll():
    roll1 = random.randint(1, 6)
    print(f"You just rolled a {roll1}")
    return roll1


def find_home(token):
    for each in homes_board:
        if each.color == token.color and each.tokenowner == token.tokennum:
            spot = homes_board[each.loc - 71]
    return spot


def send_home(token):
    token.location = find_home(token)
    reset_token_parameters()
    tokenupdate()


def out_of_home(mytoken):
    mytoken.inhome = False
    if mytoken.color == "red":
        mytoken.location = board[24]
        mytoken.location.tokenson += 1
    elif mytoken.color == "green":
        mytoken.location = board[36]
        mytoken.location.tokenson += 1
    elif mytoken.color == "blue":
        mytoken.location = board[12]
        mytoken.location.tokenson += 1
    elif mytoken.color == "yellow":
        mytoken.location = board[0]
        mytoken.location.tokenson += 1
    print(f"{mytoken.tokennum} is out of home")


def display_winners():
    print("Leaderboards...")
    print(f"First Place: {winnerOrder[0].name}")
    print(f"Second Place: {winnerOrder[1].name}")
    if len(players) > 2:
        print(f"Third Place: {winnerOrder[2].name}")


#____________________________________


class player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.playingtokens = 4
        self.playing = True
        self.token1 = token(self, self.color, "token1")
        self.token2 = token(self, self.color, "token2")
        self.token3 = token(self, self.color, "token3")
        self.token4 = token(self, self.color, "token4")
        allTokens.append(self.token1)
        allTokens.append(self.token2)
        allTokens.append(self.token3)
        allTokens.append(self.token4)


class token():
    def __init__(self, owner, color, tokennum):
        self.owner = owner
        self.color = color
        self.tokennum = tokennum
        self.inhome = True
        self.totalspacesmoved = 0
        self.whitespacesmoved = 0
        self.runwayspacesmoved = 0
        self.location = find_home(self)
        self.safe = False

    def find_spacesuntilhome(self):
        self.spacesuntilhome = (46 - self.whitespacesmoved) + (
            6 - self.runwayspacesmoved)
        return self.spacesuntilhome

    def find_tokencoordinates(self):
        return self.location.coord


class location():
    def __init__(self, locnum, color, safe, runway, runwayhome, coordinates,
                 type):
        self.loc = locnum
        self.color = color
        self.safe = safe
        self.runway = runway
        self.runwayhome = runwayhome
        self.coord = coordinates
        self.type = type
        self.tokenson = 0


class home():
    def __init__(self, locnum, color, tokenowner, coordinates, type):
        self.loc = locnum
        self.color = color
        self.tokenowner = tokenowner
        self.coord = coordinates
        self.type = type


#White Locations
loc0 = location(0, "white", True, False, False, (252, 513), "white")
loc1 = location(1, "white", False, False, False, (252, 470), "white")
loc2 = location(2, "white", False, False, False, (252, 427), "white")
loc3 = location(3, "white", False, False, False, (252, 384), "white")
loc4 = location(4, "white", False, False, False, (252, 342), "white")
loc5 = location(5, "white", False, False, False, (209, 342), "white")
loc6 = location(6, "white", False, False, False, (166, 342), "white")
loc7 = location(7, "white", False, False, False, (123, 342), "white")
loc8 = location(8, "white", False, False, False, (80, 342), "white")
loc9 = location(9, "white", False, False, False, (37, 342), "white")
loc10 = location(10, "white", False, False, False, (37, 295), "white")
loc11 = location(11, "white", False, False, False, (37, 252), "white")
loc12 = location(12, "white", True, False, False, (80, 252), "white")
loc13 = location(13, "white", False, False, False, (123, 252), "white")
loc14 = location(14, "white", False, False, False, (166, 252), "white")
loc15 = location(15, "white", False, False, False, (209, 252), "white")
loc16 = location(16, "white", False, False, False, (252, 252), "white")
loc17 = location(17, "white", False, False, False, (252, 209), "white")
loc18 = location(18, "white", False, False, False, (252, 166), "white")
loc19 = location(19, "white", False, False, False, (252, 123), "white")
loc20 = location(20, "white", False, False, False, (252, 80), "white")
loc21 = location(21, "white", False, False, False, (252, 37), "white")
loc22 = location(22, "white", False, False, False, (296, 37), "white")
loc23 = location(23, "white", False, False, False, (340, 37), "white")
loc24 = location(24, "white", True, False, False, (341, 80), "white")
loc25 = location(25, "white", False, False, False, (341, 123), "white")
loc26 = location(26, "white", False, False, False, (341, 166), "white")
loc27 = location(27, "white", False, False, False, (341, 209), "white")
loc28 = location(28, "white", False, False, False, (341, 251), "white")
loc29 = location(29, "white", False, False, False, (384, 251), "white")
loc30 = location(30, "white", False, False, False, (427, 251), "white")
loc31 = location(31, "white", False, False, False, (470, 251), "white")
loc32 = location(32, "white", False, False, False, (513, 251), "white")
loc33 = location(33, "white", False, False, False, (556, 251), "white")
loc34 = location(34, "white", False, False, False, (556, 296), "white")
loc35 = location(35, "white", False, False, False, (556, 339), "white")
loc36 = location(36, "white", True, False, False, (513, 339), "white")
loc37 = location(37, "white", False, False, False, (470, 342), "white")
loc38 = location(38, "white", False, False, False, (427, 342), "white")
loc39 = location(39, "white", False, False, False, (384, 342), "white")
loc40 = location(40, "white", False, False, False, (341, 342), "white")
loc41 = location(41, "white", False, False, False, (341, 385), "white")
loc42 = location(42, "white", False, False, False, (341, 428), "white")
loc43 = location(43, "white", False, False, False, (341, 471), "white")
loc44 = location(44, "white", False, False, False, (341, 514), "white")
loc45 = location(45, "white", False, False, False, (340, 557), "white")
loc46 = location(46, "white", False, False, False, (297, 557), "white")
loc47 = location(47, "white", False, False, False, (253, 557), "white")
#Runway locations
loc48 = location(48, "yellow", True, True, False, (297, 513), "runway")
loc49 = location(49, "yellow", True, True, False, (297, 470), "runway")
loc50 = location(50, "yellow", True, True, False, (297, 427), "runway")
loc51 = location(51, "yellow", True, True, False, (297, 384), "runway")
loc52 = location(52, "yellow", True, True, False, (297, 341), "runway")
loc53 = location(53, "yellow", True, True, True, (297, 300), "runway")
loc54 = location(54, "blue", True, True, False, (80, 295), "runway")
loc55 = location(55, "blue", True, True, False, (123, 295), "runway")
loc56 = location(56, "blue", True, True, False, (166, 295), "runway")
loc57 = location(57, "blue", True, True, False, (209, 295), "runway")
loc58 = location(58, "blue", True, True, False, (252, 295), "runway")
loc59 = location(59, "blue", True, True, True, (295, 295), "runway")
loc60 = location(60, "red", True, True, False, (297, 82), "runway")
loc61 = location(61, "red", True, True, False, (297, 125), "runway")
loc62 = location(62, "red", True, True, False, (297, 168), "runway")
loc63 = location(63, "red", True, True, False, (297, 211), "runway")
loc64 = location(64, "red", True, True, False, (297, 254), "runway")
loc65 = location(65, "red", True, True, True, (297, 297), "runway")
loc66 = location(66, "green", True, True, False, (515, 295), "runway")
loc67 = location(67, "green", True, True, False, (472, 295), "runway")
loc68 = location(68, "green", True, True, False, (386, 295), "runway")
loc69 = location(69, "green", True, True, False, (343, 295), "runway")
loc70 = location(70, "green", True, True, True, (297, 295), "runway")
#Starting Home Locations
loc71 = home(71, "yellow", "token1", (80, 433), "home")
loc72 = home(72, "yellow", "token2", (160, 433), "home")
loc73 = home(73, "yellow", "token3", (80, 513), "home")
loc74 = home(74, "yellow", "token4", (160, 513), "home")
loc75 = home(75, "blue", "token1", (80, 80), "home")
loc76 = home(76, "blue", "token2", (160, 80), "home")
loc77 = home(77, "blue", "token3", (80, 160), "home")
loc78 = home(78, "blue", "token4", (160, 160), "home")
loc79 = home(79, "red", "token1", (435, 80), "home")
loc80 = home(80, "red", "token2", (515, 80), "home")
loc81 = home(81, "red", "token3", (435, 160), "home")
loc82 = home(82, "red", "token4", (515, 160), "home")
loc83 = home(83, "green", "token1", (432, 433), "home")
loc84 = home(84, "green", "token2", (512, 433), "home")
loc85 = home(85, "green", "token3", (432, 513), "home")
loc86 = home(86, "green", "token4", (512, 513), "home")

loc87 = home(87, "green", "token4", (1000, 1000), "home")

board = [
    loc0, loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8, loc9, loc10, loc11,
    loc12, loc13, loc14, loc15, loc16, loc17, loc18, loc19, loc20, loc21,
    loc22, loc23, loc24, loc25, loc26, loc27, loc28, loc29, loc30, loc31,
    loc32, loc33, loc34, loc35, loc36, loc37, loc38, loc39, loc40, loc41,
    loc42, loc43, loc44, loc45, loc46, loc47, loc48, loc49, loc50, loc51,
    loc52, loc53, loc54, loc55, loc56, loc57, loc58, loc59, loc60, loc61,
    loc62, loc63, loc64, loc65, loc66, loc67, loc68, loc69, loc70
]

homes_board = [
    loc71, loc72, loc73, loc74, loc75, loc76, loc77, loc78, loc79, loc80,
    loc81, loc82, loc83, loc84, loc85, loc86
]

finished_loc = [loc87]


#--------------------------------
def displayrules():
    webbrowser.open('https://www.ymimports.com/pages/how-to-play-ludo')


def nono():
    print("You need more than 1 player readied to start the game!")


#----------Player options----------
def playerscreen():
    global P1_entry, P2_entry, P3_entry, P4_entry
    global P1_Player, P2_Player, P3_Player, P4_Player
    global bcol, gcol, rcol, ycol
    bcol = gcol = rcol = ycol = 0
    #----------Window Style----------
    window = tk.Tk()
    window.title("Ludo Players Screen")
    window.geometry("300x250")
    window['background'] = '#34DDF7'

    #title to player options
    p_op_label = tk.Label(font=('Helvetica', 18, 'bold'),
                          bg='#34DDF7',
                          fg='black',
                          text="Player Options")
    p_op_label.pack()
    p_op_label.place(x=40, y=1)

    #---------PLAYER NAMES INPUTS--------------
    #Player name input variables
    P1_Player = tk.StringVar()
    P2_Player = tk.StringVar()
    P3_Player = tk.StringVar()
    P4_Player = tk.StringVar()
    P1_entry = tk.Entry(window,
                        textvariable=P1_Player,
                        font=('Calibri', 11, 'normal'))
    P2_entry = tk.Entry(window,
                        textvariable=P2_Player,
                        font=('Calibri', 11, 'normal'))
    P3_entry = tk.Entry(window,
                        textvariable=P3_Player,
                        font=('Calibri', 11, 'normal'))
    P4_entry = tk.Entry(window,
                        textvariable=P4_Player,
                        font=('Calibri', 11, 'normal'))
    P1_Player = P1_entry.get()
    P2_Player = P2_entry.get()
    P3_Player = P3_entry.get()
    P4_Player = P4_entry.get()

    #----------Start Button----------
    def startbuttton_stat():
        count = bcol + gcol + rcol + ycol
        if count >= 2:  #2 or more players are readied
            sbutton = tk.Button(
                font=('Helvetica', 12, 'italic'),
                bg='gold',
                text="Start Game!",
                fg='black',
                command=lambda: [gamestart(), window.destroy()])
            sbutton.pack()
            sbutton.place(x=90, y=165)
        if count < 2:  #less than 2 players are readied
            sbutton = tk.Button(font=('Helvetica', 12, 'italic'),
                                bg='grey',
                                text="Start Game!",
                                fg='black',
                                command=lambda: [nono()])
            sbutton.pack()
            sbutton.place(x=90, y=165)
#--------------------------------

#Player B

    def b_col():
        global bcol
        bcol += 1
        if bcol > 1:
            bcol = 0
        if bcol == 1:
            pb_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='blue',
                                  text="Player 1",
                                  fg='black',
                                  command=lambda: [b_col()])
            pb_status.pack()
            pb_status.place(x=10, y=42)
            P1_entry.place(x=80, y=42)
        if bcol == 0:
            pb_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 1",
                                  fg='black',
                                  command=lambda: [b_col()])
            pb_status.pack()
            pb_status.place(x=10, y=42)
            P1_entry.place(x=900, y=42)
        startbuttton_stat()

    b_col()

    #Player G
    def g_col():
        global gcol
        gcol += 1
        if gcol > 1:
            gcol = 0
        if gcol == 1:
            pg_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='green',
                                  text="Player 2",
                                  fg='black',
                                  command=lambda: [g_col()])
            pg_status.pack()
            pg_status.place(x=10, y=71)
            P2_entry.place(x=80, y=71)
        if gcol == 0:
            pg_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 2",
                                  fg='black',
                                  command=lambda: [g_col()])
            pg_status.pack()
            pg_status.place(x=10, y=71)
            P2_entry.place(x=900, y=71)
        startbuttton_stat()

    g_col()

    #Player R
    def r_col():
        global rcol
        rcol += 1
        if rcol > 1:
            rcol = 0
        if rcol == 1:
            pr_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='red',
                                  text="Player 3",
                                  fg='black',
                                  command=lambda: [r_col()])
            pr_status.pack()
            pr_status.place(x=10, y=100)
            P3_entry.place(x=80, y=100)
        if rcol == 0:
            pr_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 3",
                                  fg='black',
                                  command=lambda: [r_col()])
            pr_status.pack()
            pr_status.place(x=10, y=100)
            P3_entry.place(x=900, y=100)
        startbuttton_stat()

    r_col()

    #Player Y
    def y_col():
        global ycol
        ycol += 1
        if ycol > 1:
            ycol = 0
        if ycol == 1:
            py_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='yellow',
                                  text="Player 4",
                                  fg='black',
                                  command=lambda: [y_col()])
            py_status.pack()
            py_status.place(x=10, y=129)
            P4_entry.place(x=80, y=129)
        if ycol == 0:
            py_status = tk.Button(font=('Helvetica', 6, 'bold'),
                                  bg='grey',
                                  text="Player 4",
                                  fg='black',
                                  command=lambda: [y_col()])
            py_status.pack()
            py_status.place(x=10, y=129)
            P4_entry.place(x=900, y=129)
        startbuttton_stat()

    y_col()

    #return to home button
    returnbutton = tk.Button(
        font=('Helvetica', 8, 'italic'),
        bg='white',
        text="Return to Home",
        fg='black',
        command=lambda: [window.destroy(), homescreen()])
    returnbutton.pack()
    returnbutton.place(x=95, y=210)
    tk.mainloop()


#---------------------------------------------------------


#----------Game Options-----------------------------------
def optionscreen():
    #----------Window Style----------
    window = tk.Tk()
    window.title("Ludo Options Screen")
    window.geometry("300x200")
    window['background'] = '#34DDF7'

    #title to general/game options
    g_op_label = tk.Label(font=('Helvetica', 22, 'bold'),
                          bg='#34DDF7',
                          fg='black',
                          text="Game Options")
    g_op_label.pack()
    g_op_label.place(x=29, y=5)

    #Game instructions
    gameinstruct = tk.Button(font=('Helvetica', 12, 'italic'),
                             bg='white',
                             text="Game Instructions",
                             fg='black',
                             command=lambda: [displayrules()])
    gameinstruct.pack()
    gameinstruct.place(x=60, y=100)

    #return to home
    returnbutton = tk.Button(
        font=('Helvetica', 8, 'italic'),
        bg='white',
        text="Return to Home",
        fg='black',
        command=lambda: [window.destroy(), homescreen()])
    returnbutton.pack()
    returnbutton.place(x=90, y=145)
    tk.mainloop()


def gamestart():
    global P1_Player, P2_Player, P3_Player, P4_Player
    global P1_entry, P2_entry, P3_entry, P4_entry, dimx, screen
    print("Game Started!\n___________________")
    if len(P1_entry.get()) != 0 and bcol == 1:
        player1 = player(P1_entry.get(), "blue")
        players.append(player1)
    elif len(P1_entry.get()) == 0 and bcol == 1:
        player1 = player("Player 1", "blue")
        players.append(player1)
    if len(P2_entry.get()) != 0 and gcol == 1:
        player2 = player(P2_entry.get(), "green")
        players.append(player2)
    elif len(P2_entry.get()) == 0 and gcol == 1:
        player2 = player("Player 2", "green")
        players.append(player2)
    if len(P3_entry.get()) != 0 and rcol == 1:
        player3 = player(P3_entry.get(), "red")
        players.append(player3)
    elif len(P3_entry.get()) == 0 and rcol == 1:
        player3 = player("Player 3", "red")
        players.append(player3)
    if len(P4_entry.get()) != 0 and ycol == 1:
        player4 = player(P4_entry.get(), "yellow")
        players.append(player4)
    elif len(P4_entry.get()) == 0 and ycol == 1:
        player4 = player("Player 4", "yellow")
        players.append(player4)
    #--------------------Board Display--------------------------
    pygame.init()  #Initializes all of pygame’s functions
    dimx = 593
    screen = pygame.display.set_mode((dimx, dimx + 50))
    pygame.display.set_caption(
        'LUDO')  #Displays the name of the window at the top
    GOLD = (230, 180, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 120, 250)
    RED = (235, 0, 0)
    GREEN = (0, 175, 0)
    YELLOW = (230, 230, 0)
    GRAY = (130, 130, 130)
    COUNTER_GRAY = (220, 220, 220)

    running = True  #turns on a command named 'running'
    while running:  #short form for when running is true:
        boardbgspace = pygame.draw.rect(screen, WHITE, (0, 0, dimx, dimx), 290)

        #coloured squares and shadow square
        board = pygame.draw.rect(screen, BLUE, (15, 15, 211, 211), 120)
        board = pygame.draw.rect(screen, YELLOW, (15, 365, 211, 211), 120)
        board = pygame.draw.rect(screen, RED, (365, 15, 211, 211), 120)
        board = pygame.draw.rect(screen, GREEN, (365, 365, 211, 211), 120)

        #Circles per big square
        #Blue
        board = pygame.draw.circle(screen, WHITE, (80, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (80, 160), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 160), 27)
        #Red
        board = pygame.draw.circle(screen, WHITE, (435, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (515, 80), 27)
        board = pygame.draw.circle(screen, WHITE, (435, 160), 27)
        board = pygame.draw.circle(screen, WHITE, (515, 160), 27)
        #Yellow
        board = pygame.draw.circle(screen, WHITE, (80, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (80, 513), 27)
        board = pygame.draw.circle(screen, WHITE, (160, 513), 27)
        #Green
        board = pygame.draw.circle(screen, WHITE, (432, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (512, 433), 27)
        board = pygame.draw.circle(screen, WHITE, (432, 513), 27)
        board = pygame.draw.circle(screen, WHITE, (512, 513), 27)

        myfont = pygame.font.SysFont("Arial", 23)
        #Score Corners
        #BLUE
        board = pygame.draw.rect(screen, COUNTER_GRAY, (15, 15, 60, 30), 20)
        bscore = myfont.render(str(B_score), 1, BLACK)
        screen.blit(bscore, (40, 20))
        #RED
        board = pygame.draw.rect(screen, COUNTER_GRAY, (516, 15, 60, 30), 20)
        rscore = myfont.render(str(R_score), 1, BLACK)
        screen.blit(rscore, (542, 20))
        #YELLOW
        board = pygame.draw.rect(screen, COUNTER_GRAY, (15, 546, 60, 30), 20)
        yscore = myfont.render(str(Y_score), 1, BLACK)
        screen.blit(yscore, (40, 551))
        #GREEN
        board = pygame.draw.rect(screen, COUNTER_GRAY, (516, 546, 60, 30), 20)
        gscore = myfont.render(str(G_score), 1, BLACK)
        screen.blit(gscore, (542, 551))

        #Space coloured Yellow
        board = pygame.draw.rect(screen, YELLOW, (233, 495, 38, 38), 21)
        #Space coloured Red
        board = pygame.draw.rect(screen, RED, (320, 61, 40, 40), 21)
        #Space coloured Green
        board = pygame.draw.rect(screen, GREEN, (491, 320, 40, 40), 21)
        #Space coloured Blue
        board = pygame.draw.rect(screen, BLUE, (58, 229, 40, 42), 21)

        #Middle triangles
        board = pygame.draw.polygon(surface=screen,
                                    color=GREEN,
                                    points=[(322, 270), (322, 320),
                                            (295, 295)])
        board = pygame.draw.polygon(surface=screen,
                                    color=YELLOW,
                                    points=[(272, 320), (322, 320),
                                            (295, 295)])
        board = pygame.draw.polygon(surface=screen,
                                    color=BLUE,
                                    points=[(272, 270), (272, 320),
                                            (295, 295)])
        board = pygame.draw.polygon(surface=screen,
                                    color=RED,
                                    points=[(322, 270), (272, 270),
                                            (295, 295)])

        #Spaces
        #top row
        for x in range(3):
            board = pygame.draw.rect(screen, GRAY,
                                     (230 + (44 * x), 16, 44.1, 44.1), 3)
        next
        #Left Middle Top Row
        for x in range(6):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (15 + (43 * x), 229, 43, 44), 3)
        next
        #Left Middle Row
        board = pygame.draw.rect(screen, BLUE, (58, 273, 215, 47), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (58 + (43 * x), 273, 43, 47), 3)
        next
        #Right Middle Top Row
        for x in range(6):
            board = pygame.draw.rect(screen, GRAY,
                                     (319 + (43 * x), 228, 43, 44), 3)
        next
        #Left Middle Bottom Row
        for x in range(6):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (15 + (43 * x), 320, 43, 43), 3)
        next
        #Right Middle Row
        board = pygame.draw.rect(screen, GREEN, (322, 272, 213, 48), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (322 + (43 * x), 272, 43, 48), 3)
        next
        #Right Middle Bottom Row
        for x in range(6):
            board = pygame.draw.rect(screen, GRAY,
                                     (319 + (43 * x), 320, 43, 43), 3)
        next
        #BOTTOM row
        for x in range(3):
            board = pygame.draw.rect(screen, GRAY,
                                     (230 + (44 * x), 534, 44.1, 44.1), 3)
        next
        #-------y-axis spaces--------
        #L-Upper
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (230, 59 + (43 * x), 43, 43), 3)
        next
        #L-Bottom
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (230, 492 - (43 * x), 43, 43), 3)
        next
        #R-Upper
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (319, 59 + (43 * x), 43, 43), 3)
        next
        #R-Bottom
        for x in range(4):
            board = pygame.draw.rect(screen, GRAY,
                                     (319, 492 - (43 * x), 43, 43), 3)
        next
        #L-MID
        board = pygame.draw.rect(screen, GRAY, (15, 271, 44.5, 50), 3)
        #Up-MID
        board = pygame.draw.rect(screen, RED, (273, 60, 47, 214), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (273, 60 + (43 * x), 47, 43), 3)
        next
        #Bot-MID
        board = pygame.draw.rect(screen, YELLOW, (273, 320, 47, 214), 25)
        for x in range(5):  #x-pos,y-pos,box-dimensions
            board = pygame.draw.rect(screen, GRAY,
                                     (273, 320 + (43 * x), 47, 43), 3)
        next
        board = pygame.draw.rect(screen, GRAY, (534, 271, 43, 50), 3)

        #--------------DiCE-----------------
        #Dice Spot
        #Blue
        pygame.draw.rect(screen, BLACK, (182, 182, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (183, 183, 40, 40), 20)
        #Red
        pygame.draw.rect(screen, BLACK, (368, 182, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (369, 183, 40, 40), 20)
        #Yellow
        pygame.draw.rect(screen, BLACK, (182, 368, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (183, 369, 40, 40), 20)
        #Green
        pygame.draw.rect(screen, BLACK, (368, 368, 42, 42), 21)
        pygame.draw.rect(screen, WHITE, (369, 369, 40, 40), 20)

        tokenupdate()
        pygame.display.update()
        if turnnum == 1:
            create_turns()
            tokenupdate()
            pygame.display.update()
        if playerCount > 1:
            turn(find_turn())
        else:
            display_winners()


def homescreen():
    #----------Window Style----------
    window = tk.Tk()
    window.title("Ludo Starting Screen")
    window.geometry("350x200")
    window['background'] = '#B42DFC'

    #----------Game Title----------
    Bienvenue = tk.Label(font=('Helvetica', 24, 'bold', 'italic'),
                         bg='#B42DFC',
                         fg='white',
                         text="Welcome to Ludo!")
    Bienvenue.pack()
    Bienvenue.place(x=8, y=15)

    #----------Players Button----------
    pbutton = tk.Button(
        font=('Helvetica', 14, 'normal'),
        text="Players",
        fg='black',
        command=lambda: [window.destroy(), playerscreen()])
    pbutton.pack()
    pbutton['background'] = '#C2C2C2'
    pbutton.place(x=117.5, y=75)

    #----------Options Button----------
    obutton = tk.Button(
        font=('Helvetica', 14, 'normal'),
        text="Options",
        fg='black',
        command=lambda: [window.destroy(), optionscreen()])
    obutton.pack()
    obutton['background'] = '#C2C2C2'
    obutton.place(x=115, y=130)
    tk.mainloop()


homescreen()
