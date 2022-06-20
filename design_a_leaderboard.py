# Original code from https://walkccc.me/LeetCode/problems/1244/
# Added additional features as an exercise 
# Modified the top score sum to display a list

from os import system, name
from collections import Counter
from rich.console import Console
from rich.table import Column, Table
import sys


class Leaderboard:
  def __init__(self):
    self.idToScore = Counter()

  def addScore(self, playerId: int, score: int, isAuto =  False) -> None:

    self.idToScore[playerId] += score


#    print(f'scores in collection : {self.idToScore.values()}')

    if (isAuto) : return

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


######################################
#Function to retrieve the (x) players#
######################################
  def top(self, K: int) -> int:
    print(f'\nRetrieving top {K} players and scores\n')

    if (len(self.idToScore.items()) <= 0): print('There are (0) player scores in the leaderboard')
    elif (K > len(self.idToScore.items())):
        print(f'Retreiving {len(self.idToScore.values())} record(s)')

    # '*' unpacks iterables
#    print(*(score for _, score in self.idToScore.most_common(K)), sep=', ')
#    print(*(score for _, score in self.idToScore.most_common(K)))
    for c in self.idToScore.most_common(K) : print(f'{c[0]} {c[1]}')

    respContinue = str(input('\nC\u0332ontinue?: '))
    print('\n')

    # _ is a throwaway variable
    return sum(score for _, score in self.idToScore.most_common(K))


#######################################
#Function to remove (playerId) records#
#######################################
  def reset(self, playerId: int) -> None:
    del self.idToScore[playerId]


# END OF CLASS & BEGINING OF FUNCTIONS

def switch(operation: int, input000 = 0, input001 = 0, isAuto = False):
    if operation == 1: leadObj.addScore(input000, input001, isAuto)
    elif operation == 2: leadObj.top(input000)
    elif operation == 3: leadObj.reset(input000)
   

def automatedOperation(actions : list, data : list ):
    for c in range(len(actions)):
        if (len(data[c]) > 0) : 
            switch(1, data[c][0], data[c][1], True) if (actions[c] == 'addScore') else None
            switch(2, data[c][0], False) if (actions[c] == 'top') else None
            switch(3, data[c][0], False) if (actions[c] == 'reset') else None

    print(f"{actions.count('addScore')} record(s) added.") 
    print(f"{actions.count('reset')} record(s) deleted.") 
    print(f"{actions.count('top')} record(s) displayed.") 
    respContinue = str(input('\nC\u0332ontinue?: '))
    print('\n')


def interactiveOperation():

    # clear the screen
    scrnClear()

    # Taking the operands from the users
    print('''
    Press 1 to Add a Score
    Press 2 to retreive top scores
    Press 3 to reset a player statistic''')
    print('\nEnter an operation: ')
    opInput = input('Or press Q to quit: ')
    print('\n')

    if opInput == '1':
        userInput000 = int(input('Enter Player ID: '))
        userInput001 = int(input('Enter Score: '))
        switch(int(opInput), userInput000, userInput001 )
    elif opInput == '2':
        prompt = 'Enter # of players to retrieve'
        if (userInput := checkInt(prompt)) != -1 : switch(int(opInput), userInput) 
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
            print('TAMA 111')
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
    autoInput = input('Or press Q\u0332 to quit: ')
    print('\n')

    if autoInput == '1':
        isAuto = True
        # passing parameters in case I decide to change it later
        automatedOperation(actions, data)
    elif autoInput == '2':
        isAuto = False
        interactiveOperation()
    elif autoInput.lower() == 'q':
        print('\n...> Exiting per user request')
        sys.exit()
    else:
        print('Please input a valid operation: ')
        introPrompt()
        print('\n')


def scrnClear():

    # Windows
    if name == 'nt': _ = system('cls')
    # For nix based devices
    else: _= system('clear')

    print('LEADER BOARDS')
    


if __name__ == '__main__':

    actions = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
    data = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

    isAuto = False

    console = Console()

    leadObj = Leaderboard()

    while True: introPrompt()




    


