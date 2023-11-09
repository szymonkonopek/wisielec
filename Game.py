from Word import Word

class Game:
    def __init__(self):
        self.numOfMistakes = 0
        self.currnetWord = ""

    def startGame(self):
        print('gram')

    def endGame(self):
        print('koniec gry')

    def guessLetter(self):
        letter = input("Enter any letter: ")

    def getRandomLetter(self):
        self.currnetWord = Word().getRandomWord()