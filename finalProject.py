import random # Import the random function
import time # Import the time function

# function for the instruction
print('\nHello and Welcome.')

def showHelp():
   
    # Stating game rules
    How2Play = """\nThere is a deck of cards that is shuffled and split equally between 2 players\nEach Player gets a deck and then starts the game.\nTo play each player shows the topmost card of their deck\nThe Player with the highest card wins the round\nAce is the highest card\nThe winner gets twice his/her bet\nA tie implies both Players lose their cards to the House\nWhen a Player is out of cards or the Player out of cash - the game ends\nThe Player with the most cash is declared winner.\n"""

    print(How2Play)

# function to display the instructions 
def instruction(prompt):
    action = input(prompt)
    if action == '--help':
        print("\nHint...")
        time.sleep(1)
        showHelp()
        return instruction(prompt)
    elif action == '--resume':
        print("\nContinue with your game")
        time.sleep(1)
        return instruction(prompt)
    else:
        return action

# print(instruction(showHelp()))  

# function to create deck of cards
def createDeck():
    Deck = []
    # set the facevalue variable
    faceValz = ['A', 'J', 'Q', 'K']
    for i in range(4): # four different suites
        for card in range(2, 11): # input the 2 - 10 to the Deck
            Deck.append(str(card))

        for card in faceValz:
            Deck.append(card)
        
    random.shuffle(Deck) # Mixing results
    return Deck # return the shuffled deck

# print(createDeck())

# Set a player class
class Player:
    def __init__(self, name = 'Player', bankroll = 100, hand = []):
        self.name = name
        self.hand = hand
        self.bankroll = int(bankroll)
        self.score = self.setScore()
        # self.value = value
        # self.BetKind = ''
        self.amount = 0
        self.bet = 0

    def __str__(self) -> str: # Display a string for name
        return self.name + ' draws '

    def win(self): # set function for wins
        self.bankroll += 2 * int(self.amount)

    def draw(self): # set function for draw
        self.bankroll += self.bet
        self.bet = 0

    def gameBet(self): # set function for Betting
        for i in range(1000):
            self.amount = int(instruction('How much do you want to bet? '))
            if self.amount <= self.bankroll:
                break
            else:
                print('You can only bet your current bank!')
                time.sleep(1)
                print('You have no money left\nOR\nYour bet is Higher.\nGame Over!')
                break

        self.bankroll -= int(self.amount)

    def setScore(self):
        self.score = 0
        Values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14} # define card values 
        # convert card to score
        for card in self.hand:
            self.score += Values[card]

        return self.score
    
Decks = createDeck()

PlayzList = []
NPlayz = int(instruction('How many Players are going to play: '))

# Define Players
for i in range(NPlayz):
    print('Intialization, Player ', i + 1)
    name = instruction('What is your name? ')
    bankroll = instruction('What is your Bank? ')
    playz = Player(name, bankroll)
    PlayzList.append(playz)

FirstPlayzDeck = []
SecondPlayzDeck = []

if len(PlayzList) == 2:
    while(len(Decks)) != 0:
        FirstPlayzDeck.append(Decks[0])
        Decks.remove(Decks[0])
        SecondPlayzDeck.append(Decks[0])
        Decks.remove(Decks[0])

    # print(FirstPlayzDeck)
    # print(SecondPlayzDeck)

else:
    instruction('This game is designed for 2 persons ')
    
round = 0        

while True:
    for playz in PlayzList: 
        print(playz.name + ', ', end='')
        playz.gameBet()
    
    if len(FirstPlayzDeck) != 0 and len(SecondPlayzDeck) != 0:

        FirstPlayz = FirstPlayzDeck.pop()
        SecondPlayz = SecondPlayzDeck.pop()

    else:
        print("You can't draw a card from an empty deck")
        time.sleep(1)
        print("Game Over!")
        break

    if NPlayz == 2:
        print(PlayzList[0], FirstPlayz)
        print(PlayzList[1], SecondPlayz)
   
    else:
        print('All Players bet! Draws are: ', FirstPlayz,':',  SecondPlayz)  

    if FirstPlayz > SecondPlayz:
        PlayzList[0].win()
        print(PlayzList[0], 'a win')
    elif FirstPlayz < SecondPlayz:
        PlayzList[1].win()
        print(PlayzList[1], 'a win')
    else:
        print("It's a tie between", PlayzList[0], 'and', PlayzList[1])
        time.sleep(0.5)
        print("You both lost to the House")

    for playz in PlayzList: # define win or loss
        
        playz.setScore()
        print(playz.bankroll)  
    
    if len(PlayzList) == 0: # no more players
        print('No more players left. Game Over!')
        break

    if playz.bankroll <= 0: # if player out of cash
        print(playz.name, 'You are out cash.\nGame Over!.')
        PlayzList.remove(playz)
        print(PlayzList[0], 'You are the WINNER of the GAME')
        break

    round += 1
    # for playz in PlayzList:
    if len(PlayzList) == 2:
        print('The current deck length:', len(FirstPlayzDeck), 'current round:', round)
                    
        Decks = createDeck()











    