vocabulary_file = open('vocabulary.txt', 'w')

while True:
    #out_file.write("%s: %s\n" % (english_word, korean_meaning))
    english = input('영어 단어를 입력하세요: ')
    if english == 'q':
        break
    korean = input('한국어 뜻을 입력하세요: ')
    vocabulary_file.write("%s: %s\n" % (english, korean))
    continue
out_file.close()