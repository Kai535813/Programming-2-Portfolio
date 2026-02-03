import random 
ps = random.randint(1,20)
rs = random.randint(1,20)
ss = random.randint(1,22)
prefixes = ["anti", "de", "dis", "en", "em", "fore", "in", "im", "inter", "mid", "mis", "non", "over", "pre", "re", "semi", "sub", "super", "trans", "un"]
root = ["ambi", "aqua", "aud", "anthropo", "auto", "bio", "cent", "circum", "contra", "counter", "dict", "fac", "chron", "dyna", "dys", "gram", "graph", "hetero", "homo", "hydr"]
suffixes = ["able", "ible", "al", "ial", "ed", "en", "er", "or", "est", "ful", "ic", "ing", "ion", "tion", "ation", "ity", "less", "ness", "ous", "eous", "ious", "y"]
preDef = ["against", "reverse", "not", "to make", "to put in", "before", "not", "not", "between", "middle of", "wrongly", "not", "over", "before", "again", "halfway between", "underneath of", "above of", "across of", "not"]
rootDef = ["ambivalent about something or someone (having two opposite feelings)", "water (as in aqua)", "hearing (as in audio)", "man (as in anthropology)", "self (as in automatic)", "life (as in biology)", "hundred (as in centennial)", "(around) circumvention of something or someone (as in circumnavigate)", "(in opposition to) counteraction of something or someone (as in counteract)", "(in opposition to) counteraction of something or someone (as in counteract)", "(to) speak or say something (as in dictation)", "(to) do something (as in factitious)", "(in time) chronology of something or someone (as in chronological)", "(power, strength, force) dynamism of something or someone (as in dynamic)", "(abnormal, difficult) dyslexia, dysphagia, etc.", "(to write) grammar and writing of something or someone (as in grammarian)", "(to write) graphing and writing of something or someone (as in graphic novel)", "(different from others) heterogeneity of something or someone (as in heterogeneous)", "(the same as others) homogeneity of something or someone (as in homogeneous)", "(water) hydrology and hydroelectricity of something or someone (as in hydroelectricity)"]
suffDef = ["capable of being done, able to be done, able to be done with a certain quality, able to be done with a certain quality that is not negative, able to be done with a certain quality that is not negative and is positive, able to be done with a certain quality that is not negative and is positive and is good for the person doing it, able to be done with a certain quality that is not negative and is positive and is good for the person doing it and is good for others doing it too, able to be done with a certain quality that is not negative and is positive and is good for the person doing it and is good for others doing it too and is good for society too, able to be done with a certain quality that is not negative and is positive and is good for the person doing it and is good for others doing it too and is good for society too but not necessarily all at once"]
response1 = input("If you would like to make a random word type yes: ")
while response1 == "yes":
    print(prefixes[ps] + root[rs] + suffixes[ss])
    print("The definitions are as follows:")
    print(preDef[ps-1] + rootDef[rs-1] + suffDef[ss-10])
    break 

response2 = input("Would you like to make another word? Type yes or no: ")
while response2 == "yes":
    ps = random.randint(1,20)
    rs = random.randint(1,20)
    ss = random.randint(1,22)
    print(prefixes[ps] + root[rs] + suffixes[ss])
    print("The definitions are as follows:")
    print(preDef[ps] + rootDef[rs] + suffDef[ss])
    response2 = input("Would you like to make another word? Type yes or no: ")
print("Bye bye!")