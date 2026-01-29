vowels = ["a", "e", "i", "o", "u"]
while True:
    word = input("Enter a word(type 6132487 to stop): ").lower()
    if word == "6132487":
        print("Bye bye!")
        break
    letterOne = word[0]
    wordBack = word[1:]
    if letterOne in vowels:
        print(word + "ay")
    else: 
        print(wordBack + letterOne + "ay")