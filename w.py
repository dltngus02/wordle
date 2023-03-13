#wordle

import random


result_list = [['ㅇ','ㅏ','ㄴ','ㄴ','ㅕ','ㅇ'],['ㅈ','ㅏ','ㄱ','ㄱ','ㅗ','ㄱ']]

print("wordle입니다. 모음과 자음을 띄어쓰기로 분리하여 입력해주세요")
print("일치하면 파란색 위치는 다르지만 있으면 보라색 아얘 없으면 빨간색이 출력됩니다")

r = random.randrange(0,2)
user_input = list(input().split())

while (user_input!=result_list[r]):
    for i in range(6):
      
        if(user_input[i]==result_list[r][i]):
            print('\033[44m',end=' ')
            print('\033[0m', end=' ')
       
        elif(user_input[i] in result_list[r]):
            print('\033[45m',end=' ')
            print('\033[0m', end=' ')
        else:
            print('\033[41m',end=' ')
            print('\033[0m', end=' ')

    print()
    user_input = list(input().split())
print('\033[44m',end=' ')
print('\033[0m', end=' ')

print('\033[44m',end=' ')
print('\033[0m', end=' ')

print('\033[44m',end=' ')
print('\033[0m', end=' ')

print('\033[44m',end=' ')
print('\033[0m', end=' ')

print('\033[44m',end=' ')
print('\033[0m', end=' ')

print('\033[44m',end=' ')
print('\033[0m')