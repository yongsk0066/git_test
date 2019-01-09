from random import randint

ball = []
# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    global ball
    ball = []

    ball.append(randint(1, 45))
    i = 1
    while i < 6:
        a = randint(1, 45)
        if a not in ball:
            ball.append(a)
            i += 1
    ball.sort()
    return ball

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    a = randint(1, 45)
    global ball
    while True:
        if a not in ball:
            ball.append(a)
            break
    return ball


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    i = 0
    count = 0
    bonus = 0
    for i in range(6):
        if list1[i] in list2[0:6]:
            count += 1
        if list1[i] == list2[6]:
            bonus += 1

    return count, bonus

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    a = count_matching_numbers(numbers, winning_numbers)
    if a[0] == 6:
        return 100000000
    elif a[0] == 5 and a[1] == 1:
        return 50000000
    elif a[0] == 5:
        return 30000000
    elif a[0] == 4:
        return 40000
    elif a[0] == 3:
        return 5000
    else:
        return 0

user_lotto = [1,3,5,40,25,23]

print(generate_numbers())
print(draw_winning_numbers())
print(ball)
print(count_matching_numbers(user_lotto, ball))
print(check(user_lotto, ball))