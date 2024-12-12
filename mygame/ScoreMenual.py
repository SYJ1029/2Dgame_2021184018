from pico2d import * 
from gfw import *



Score = [[0 for _ in range(9)] for _ in range(2)]
Strike, Ballcount, Out, ScoreIndex = 0, 0, 0, 0
attackSequence = False
runs = 0
innings = 0
runInterval = 300
delaytime = 0

def InitScore():
    global Score, Strike, Ballcount, Out, attackSequence
    Score = [[0 for _ in range(9)] for _ in range(2)]
    Strike, Ballcount, Out, ScoreIndex = 0, 0, 0, 0
    attackSequence = False


def ChangeAtt():
    global Score, Strike, Ballcount, Out, attackSequence

    if(attackSequence == False): attackSequence = True
    else: attackSequence = False

    Out = 0
    Strike = 0
    Ballcount = 0



def ClearSBO():
    global Score, Strike, Ballcount, Out, attackSequence

    Strike = 0
    Ballcount = 0

def SetByHit():
    global runs, Score, ScoreIndex, innings
    runs += 1

    if(runs > 2 and innings < 9):
        Score[ScoreIndex][innings] += 1