sentence = input("your sentence: ")
print(sentence)
characterCount = 0
wordCount = 1
for i in sentence:
    characterCount = characterCount + 1
    if(i == ' '):
        wordCount = wordCount + 1
print("number of characters in your sentence: ")
print(characterCount) 
print("number of words in your sentence: ")
print(wordCount)