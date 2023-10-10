#length = len()
#first = [0]
#def multiple_returns(sentence):
#    if sentence == " ":
#        [0] == None
#    else:
#        print("Length: {:d} - First character: {}".format(length, first))


def multiple_returns(sentence):
    lenght = len(sentence)
    char = sentence[0] if lenght > 0 else None
    return lenght, char