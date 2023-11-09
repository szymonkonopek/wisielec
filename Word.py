from WordList import WordList
class Word:
    def __init__(self):
        self.word = ""

    def getRandomWord(self):
        self.word = WordList.getRandomWord()
    

