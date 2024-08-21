def indicies(guess, letters, track):
    for x in range(len(word)):
        if letters[x] == guess:
            track[x] = guess

def checker(guess, word, track):
    if len(guess) == 1:
        if guess in list(word):
            indicies(guess, list(word),track)
            return True
    else:
        if guess == word:
            return True
    return False
    

hungman = {0:("",
              "",
              ""),
            1:("          o",
               "",
               ""),
            2:("          o",
               "          |",
               ""),
            3:("          o",
               "         /|",
               ""),
            4:("          o",
               "         /|\\",
               ""),
            5:("          o",
               "         /|\\",
               "         /"),
            6:("          o",
               "         /|\\",
               "         / \\")}
print("Welcome to my hang man game")
print("1 Wrong letter = 1 strike, 1 Wrong word = 2 strikes")
print("If you get more than 6 strikes, you lose.")
word = (input('Enter the word to be guessed: ')).lower()
guessed = False
hung = False
strikes = 0
track = []
for x in range(len(word)):
    track.append('_')

while guessed == False and hung == False:
    print('*********************')
    print('          |          ')
    for x in hungman[strikes]:
        print(x)
    print()
    print('*********************')
    print(track)
    print(f'Strikes: {strikes}')
    guess = (input('Enter a guess: ')).lower()
    result = checker(guess, word, track)
    if len(guess) == 1 and result == False:
        strikes += 1
    elif len(guess) > 1 and result == False:
        strikes += 2
    
    if guess == word or ''.join(track) == word:
        print('You did it!')
        quit()
    elif strikes > 6:
        print('The man has been hung, you lose!')
        quit()