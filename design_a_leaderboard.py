# Original code from https://walkccc.me/LeetCode/problems/1244/

from os import system, name
from collections import Counter
from rich.console import Console
from rich.table import Column, Table
import sys


class Leaderboard:
  def __init__(self):
    self.idToScore = Counter()

  def addScore(self, playerId: int, score: int) -> None:

    self.idToScore[playerId] += score

    print(f'scores in collection : {self.idToScore.values()}')

    self.userResponse = str(input('\nAdd another record (Y\u0332es) (N\u0332o): '))

    while True:
        if (self.userResponse.lower() == 'n'): return False
        elif (self.userResponse.lower() == 'y'):
            if (userInput000 := checkInt('Enter Player ID') != -1) :
                if (userInput001 := checkInt('Enter Score') != -1) : switch(1,
                    userInput000, userInput001)
        else:
            print('--> Enter a valid response.')
            self.userResponse = str(input('Add another record (Y\u0332es) (N\u0332o): '))


  def top(self, K: int) -> int:
    print(f'Retrieving top {K} players\n')

    if (len(self.idToScore.items()) <= 0): print('There are (0) player scores in the leaderboard')
    elif (K > len(self.idToScore.items())):
        print(f'Retreiving {len(self.idToScore.values())} record(s)')

    # _ is a throwaway variable
    return sum(score for _, score in self.idToScore.most_common(K))


  def reset(self, playerId: int) -> None:
    print('tama 4')      
    del self.idToScore[playerId]


# END OF CLASS & BEGINING OF FUNCTIONS

def switch(operation: int, input000 = 0, input001 = 0):
    if operation == 1: leadObj.addScore(input000, input001)
    elif operation == 2: leadObj.top(input000)
    elif operation == 3: leadObj.reset(input000)
   

def automatedOperation():
    print('Placeholder 1')
    opInput = input(input('Enter an operation: '))


def interactiveOperation():

    # clear the screen
    scrnClear()

    # Taking the operands from the users
    print('''
    Press 1 to Add a Score
    Press 2 to retreive top scores
    Press 3 to reset a player statistic
    Press Q to return to the main menu\n''')
    opInput = input('Enter an operation: ')
    print('\n')

    if opInput == '1':
        userInput000 = int(input('Enter Player ID: '))
        userInput001 = int(input('Enter Score: '))
        switch(int(opInput), userInput000, userInput001)
    elif opInput == '2':
        prompt = 'Enter # of players to retrieve'
        if (userInput := checkInt(prompt)) != -1: switch(int(opInput), userInput) 
    elif opInput == '3':
        userInput000 = int(input('Enter Player ID: '))
        switch(int(opInput), userInput000, 0)
    elif opInput.lower() == 'q':
        print('...> Exiting per user request')
        return
    else:
        print('Please input a valid choice: ')
        opInput = input('Enter an operation: ')
        print('\n')
        

def checkInt(promptOne : str) -> int:
    while True:
        try:
            userInput = int(input(promptOne + ': '))
            if (userInput <= 0): 
                print('--> Enter a valid number.')
                continue
            return userInput
        except:
            print('-->Enter a valid number.')

    return -1


def introPrompt():

    # clear the screen
    scrnClear()

    print(
    '''\nPress 1 for pre-populated data\n'''
    '''Press 2 for interactive\n''')
    print('Enter auto or interactive operations')
    autoInput = input('Or press Q to quit: ')

    if autoInput == '1':
        automatedOperation()
    elif autoInput == '2':
        interactiveOperation()
    elif autoInput.lower() == 'q':
        print('\n...> Exiting per user request')
        sys.exit()
    else:
        print('Please input a valid operation: ')
        introPrompt()
#        autoInput = input('Enter auto or interactive operations, Q (Quit): ')
        print('\n')


def scrnClear():

    # Windows
    if name == 'nt': _ = system('cls')
    # For nix based devices
    else: _= system('clear')

    print('LEADER BOARDS')
    


if __name__ == '__main__':

    actions = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]

    console = Console()

    leadObj = Leaderboard()

    while True: introPrompt()



#highScore = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

    


