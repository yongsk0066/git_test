from random import randint

# 컴퓨터 숫자 생성
computer_list = []
computer_list.append(randint(0, 9))
i = 1
while i < 3:
    a = randint(0, 9)
    if a not in computer_list:
        computer_list.append(a)
        i += 1

# 횟수 카운트
count = 1

# 유저 숫자 입력
while True:

    while True:
        first_num = int(input("1번째 수를 입력하세요: "))
        if first_num > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue
        else:
            break
    while True:
        second_num = int(input("2번째 수를 입력하세요: "))
        if second_num == first_num:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        elif second_num > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue
        else:
            break
    while True:
        third_num = int(input("3번째 수를 입력하세요: "))
        if third_num == first_num or third_num == second_num:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        elif second_num > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
            continue
        else:
            break

# 유저 리스트 생성
    user_list=[first_num, second_num, third_num]

# 성공 여부 확인
    if user_list == computer_list:
        print('축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.' % (count))
        break
    #스트라이크
    s = 0
    for j in range(0, 3):
        if user_list[j] == computer_list[j]:
            s += 1

    #볼
    b = 0
    for k in range(0,3):
        if user_list[k] in computer_list and user_list[k] != computer_list[k]:
            b += 1

    #결과값
    print('%dS %dB' % (s,b))
    count += 1
    continue
