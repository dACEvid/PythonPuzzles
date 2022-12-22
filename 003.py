# Kevin and Stuart want to play the 'The Minion Game'.
# Both players are given the same string. Both players have to make substrings using the letters of the string.
# Stuart has to make words starting with consonants. Kevin has to make words starting with vowels. The game ends when both players have made all possible substrings.
# A player gets +1 point for each occurrence of the substring in the string.
# Print the winner's name and score, separated by a space on one line, or Draw if there is no winner

def minion_game(string):
    vowels = set('AEIOU') # Note: set is faster when it comes to determining if an object is present in the set but its elements are not ordered
    stuart = kevin = 0
    for i, c in enumerate(string):
        if c in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)