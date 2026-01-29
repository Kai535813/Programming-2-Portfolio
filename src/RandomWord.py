import random 
affixes = random.randint(1,20)
rs = random.randint(1,22)
prefixes = ["anti", "de", "dis", "en", "em", "fore", "in", "im", "inter", "mid", "mis", "non", "over", "pre", "re", "semi", "sub", "super", "trans", "un"]
root = ["ambi", "aqua", "aud", "anthropo", "auto", "bio", "cent", "circum", "contra", "counter", "dict", "fac", "chron", "dyna", "dys", "gram", "graph", "hetero", "homo", "hydr"]
suffixes = ["able", "ible", "al", "ial", "ed", "en", "er", "or", "est", "ful", "ic", "ing", "ion", "tion", "ation", "ity", "less", "ness", "ous", "eous", "ious", "y"]
response1 = input("If you would like to make a random word type yes: ")
while response1 == "yes":
    print(prefixes[affixes] + root[affixes] + suffixes[rs])
    break 
print("Bye bye!")


