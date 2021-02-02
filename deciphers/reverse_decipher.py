#THIS IS THE SAME AS THE CIPHER

message = input()

def reverse(sentence):
    newsentence = []
    for i in range(1, len(sentence)+1):
        newsentence.append(sentence[-1*i])
    return ''.join(newsentence)
print(reverse(message))
