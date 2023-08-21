asciiDict = {}

for letter in range(ord('a'), ord('z') + 1):
    asciiDict[chr(letter)] = letter

print(asciiDict)
