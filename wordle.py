from words5Letter import words

invalidLetters = ""
class Rule:
    def __init__(self, letter, invalidLocations):
        self.letter = letter
        self.invalidLocations = invalidLocations
    def addLocations(self, locations):
        for location in locations:
            if location not in self.invalidLocations:
                self.invalidLocations.append(location)

    def getInvalidLocations(self):
        return self.invalidLocations

    def getLetter(self):
        return self.letter
def follows(rule, word):
    if rule.getLetter() not in word:
        return False
    for location in rule.getInvalidLocations():
        if word[location] == rule.getLetter():
            return False
    return True

    
def findValid(words):
    global rules, invalidLetters
    newWords = []
    for word in words:
        hasLetter = False
        for letter in invalidLetters:
            if letter in word:
                hasLetter = True
        if hasLetter:
            continue
        for rule in rules:
            if(not follows(rule, word)):
                break
            
        else:
            newWords.append(word)
    return newWords


def createRules():
    global rules, invalidLetters
    invalidLetters += input("new invalid letters: ")
    print("Create new rule? y/n")
    i = input()
    while i != "n":
        let = input("Letter: ")
        print("invalid locations:")
        locs = [int(i) for i in input()]


        rules.append(Rule(let, locs))
        i = input("continue? y/n")
    
rules = []

def replace(word):
    for c in range(len(word)):
        if word[c] in word[:c]:
            word = word[:c] + "1" + word[c+1:]
    return word
            
def wordScore(word, match):
    word = replace(word)
    score = 0
    for char in range(len(word)):
        if word[char] in match:
            score +=1
        if word[char] == match[char]:
            score += 2
        
    return score

def getWordWithMaxScores(possibleGuesses, validWords):
    maxScore = 0
    for word in possibleGuesses:
        score = 0
        for otherWord in validWords:
            score += wordScore(word, otherWord)
        if score > maxScore:
            maxScore = score
            maxWord = word
    return maxWord

def run():
    w = words
    while True:
        print("Play: " + getWordWithMaxScores(words, w))
        createRules()
        w=findValid(w)
        if (len(w) == 1):
            print("the only remaining word is: " + w[0])
            break
        
run()
