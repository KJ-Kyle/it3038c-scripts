from asyncio import constants


word = input("Give me a word and I will give you the stats on it: ")
cons = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz"
vow = "AaEeIiOoUuYy"

print("Length: " + str(len([x for x in word if x.isalpha()])))
print("Number of Conssonants: " + str(len([x for x in word if x in vow])))
print("Number of Vowels: " + str(len([x for x in word if x in cons])))