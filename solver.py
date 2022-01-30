from words5Letter import words as totalWords
from words5Letter import otherWords as initialValids

#wordle.py, written to be be readable and also choose better words
def run():
    rules = Rules("",[],[])
    validWords = initialValids
    print("Play: roate")
    word = "roate"
    while True:
        rules += getRulesFromUser(word)
        validWords = [word for word in validWords if rules.isValid(word)]
        if(len(validWords) < 3):
            print("The only remaining word(s) are: " + str(validWords))
            break
        if(len(validWords) > 100):
            word = findBestWord(validWords + totalWords, validWords, rules)
        else:
            word = findBestWord(validWords, validWords, rules)
        if(len(validWords) < 25):
            print("the remaining valid words are: ")
            print(validWords)
        print("Play: " + word)

def getRulesFromUser(wordPlayed):
    invalid = input("invalid letters:")
    if invalid == "rerun":
        run()
        quit()
    green = []
    included = []
    for i, letter in enumerate(wordPlayed):
        if letter in invalid:
            continue
        color = input(letter + " at position " + str(i) + " is (g/y): ")
        if color == "g":
            green.append((letter,i))
        else:
            included.append((letter,i))
            
        
            
            
    return Rules(invalid, green, included)
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
    if rules.invalidLetters == "roate":
        return "clips"
    #given words (all possible guesses),
    #validWords (all words that might be the answer),
    #and rules (a rules object that describes all current information)
    #return the best possible guess

    maxScore = 0
    maxScoreWord = ""
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
            print("new best word: ")
            print(word)
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

        
run()
