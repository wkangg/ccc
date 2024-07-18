T, N = input().split() # T = num strings, N = length of strings
strings = [input() for i in range(int(T))]

def is_alternating(string):
    # dictionary of letter counts
    letter_counts = {letter: string.count(letter) for letter in set(string)}
    # determine if each letter is heavy or light
    heavy_light = [letter_counts[letter] > 1 for letter in string]
    # check if the string alternates between heavy and light
    for i in range(1, len(heavy_light)):
        if heavy_light[i] == heavy_light[i-1]:
            return 'F'
    return 'T'

for string in strings:
    print(is_alternating(string))