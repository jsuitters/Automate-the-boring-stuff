spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam)


def list_sentence(listn):
    sentence = ""
    for i in range(len(listn)-2):
        sentence = sentence + str(listn[i]) + ", "
    sentence = sentence + str(listn[-2])
    sentence = sentence + " and " + str(listn[-1])
    return sentence

print(list_sentence(spam))
