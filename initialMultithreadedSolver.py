#created to run the initial check to find the best possible word using multithreading over 2 batches
#best word: roate
#runners up: raile, soare, orate

from multiprocessing import Process
from words5Letter import words as totalWords
from words5Letter import otherWords as initialValids

#wordle.py, written to be be readable and also choose better words
def run():
    validWords = words
    print("Play __word__ to begin.")
    while True:
        pass
#a rules object contains all information that can be gathered from a board state
class Rules:
    def __init__(self, invalidLetters, greenLetters, includedLetters):
        #invalid letters can't appear anywhere in the solution
        self.invalidLetters = invalidLetters

        #green letters must appear at their location, but might appear elsewhere
        #green letters is a tuple, where the first element is the letter, and the second is the index
        self.greenLetters = greenLetters
        
        #included letters is a similar list of tuples, where the first element is a letter that must be included, but not
        #at the index that is the second element
        self.includedLetters = includedLetters

    #true if the given word is acceptable under this ruleset, false otherwise
    def isValid(self, word):
        
        for letter, location in self.greenLetters:
            if word[location] != letter:
                return False

        for letter, location in self.includedLetters:
            if letter not in word:
                return False
            if word[location] == letter:
                    return False
            
        for letter in self.invalidLetters:
            if letter in word:
                return False
        return True

    def __add__(self, other):
        return Rules(self.invalidLetters + other.invalidLetters, self.greenLetters + other.greenLetters, self.includedLetters + other.includedLetters)


def findBestWord(words, validWords, rules):
    #given words (all possible guesses),
    #validWords (all words that might be the answer),
    #and rules (a rules object that describes all current information)
    #return the best possible guess

    maxScore = 5208084
    maxScoreWord = "ariel"
    #For every possible guess:
    #Take each word in validWords and assume that it's the answer.
    #Find out how many words the information we would find in that case would knock out
    #And return the word out of possible guesses with the highest avg words knocked out
    i = 0
    for word in words:
        i+=1
        if i % 100 == 0:
            print(i)
        #print(word)
        score = 0
        
        for validWord in validWords:
            newRules = rules + generateRules(word, validWord)
            score += removedCount(validWords, newRules)
        if score > maxScore:
            print(f"{word=} {score=}")

            maxScore = score
            maxScoreWord = word
    return maxScoreWord


def removedCount(wordlist, rules):
    #find how many words out of wordlist are invalid because of rules
    total = 0
    for word in wordlist:
        if not rules.isValid(word):
            total += 1
    return total

def generateRules(guess, answer):
    #Create rules object based on the information revealed from guessing guess
    #with an answer of answer
    
    invalidLetters = ""
    greenLetters = []
    includedLetters = []
    for i, letter in enumerate(guess):
        if letter not in answer:
            invalidLetters += letter
        elif letter == answer[i]:
            greenLetters.append((letter, i))
        else:
            includedLetters.append((letter, i))
    return Rules(invalidLetters, greenLetters, includedLetters)
            
if __name__ == "__main__":
    
##    p1 = Process(target=findBestWord, args=(totalWords[0:1000],initialValids,Rules("",[],[])))
##    p2 = Process(target=findBestWord, args=(totalWords[1000:2000],initialValids,Rules("",[],[])))
##    p3 = Process(target=findBestWord, args=(totalWords[2000:3000],initialValids,Rules("",[],[])))
##    p4 = Process(target=findBestWord, args=(totalWords[3000:4000],initialValids,Rules("",[],[])))
##    p5 = Process(target=findBestWord, args=(totalWords[4000:5000],initialValids,Rules("",[],[])))
##    p6 = Process(target=findBestWord, args=(totalWords[5000:6000],initialValids,Rules("",[],[])))
##    p1.start()
##    p2.start()
##    p3.start()
##    p4.start()
##    p5.start()
##    p6.start()
    p1 = Process(target=findBestWord, args=(totalWords[6000:7000],initialValids,Rules("",[],[])))
    p2 = Process(target=findBestWord, args=(totalWords[7000:8000],initialValids,Rules("",[],[])))
    p3 = Process(target=findBestWord, args=(totalWords[8000:9000],initialValids,Rules("",[],[])))
    p4 = Process(target=findBestWord, args=(totalWords[9000:10000],initialValids,Rules("",[],[])))
    p5 = Process(target=findBestWord, args=(totalWords[10000:],initialValids,Rules("",[],[])))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    
