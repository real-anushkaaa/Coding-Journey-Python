# Compare middle characters of two words.

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

mid1 = len(word1) // 2
mid2 = len(word2) // 2

if word1[mid1] == word2[mid2]:
    print("Middle characters are same")

else:
    print("Middle characters are different")