from random import randint
vocabulary_file = open('vocabulary.txt', 'r')
dict1 = {}
dict2 = {}

for line in vocabulary_file:
    data = line.strip().split(": ")
    dict1[data[0]] = data[1]
    dict2[data[1]] = data[0]

dictvalue = list(dict1.values())

while True:
    randword = dictvalue[randint(0, len(dict1)-1)]
    user_input = input("%s: " % (randword))
    if user_input == 'q':
        break

    elif user_input in list(dict1.keys()) and dict1[user_input] == randword:
        print('정답입니다!\n')
    else:
        print('아쉽습니다. 정답은 %s입니다.\n' % dict2[randword])


vocabulary_file.close()