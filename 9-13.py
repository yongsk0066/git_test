from random import randint
vocabulary_file = open('vocabulary.txt', 'r')
dict1 = {}

for line in vocabulary_file:
    data = line.strip().split(": ")
    dict1[data[1]] = data[0]


user_input = input("%s: " % (dict1[randint(1,len(dict1))])

    if user_input == dict1[user_input]:
        print('정답입니다!\n')
    else:
        print('아쉽습니다. 정답은 %s입니다.\n' % dict1.keys[user_input])

vocabulary_file.close()