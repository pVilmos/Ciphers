def reverse(sentence):
    newsentence = []
    for i in range(1, len(sentence)+1):
        newsentence.append(sentence[-1*i])
    return ''.join(newsentence)
    
if(__name__=="__main__"):

    print(reverse(message))
    message = input()
