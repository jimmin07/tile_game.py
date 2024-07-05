#랜덤 타일 생성기
import random

N = random.randrange(1, 401)
tiles = []
number = []
color = []
letters = ['r', 'y', 'g', 'b']

for i in range(N):
    number.append(random.randrange(1,101))
    color.append(random.choice(letters))

#타일 합체기
for i in range(N):
    tiles.append(str(number[i-1])+color[i-1])

#타일 가능한 조합 만들고 계산해서 values에 값 저장
values = []
numbervalues = []
numbercount = {}

for i in number:
    try:
        numbercount[i] +=1
    except:
        numbercount[i] = 1

for i in numbercount.keys():
    value = numbercount[i]
    numbervalues.append(int(i)*int(value))    #ㅅㅂ왜 index가 1부터 시작해서 0인걸 마지막에 함?

colorvalues=[]
colornumber=[]
for n in range(0, N):
    for m in range(0, N):
        if color[n] == color[m]:
            index = m
            colornumber.append(number[index])
        else:
            pass
       
    colorsum = sum(colornumber)
    colorvalues.append(colorsum)
    colornumber.clear()
        

#타일 수, tiles, values에서 최대값 프린트하기
numbervalues.extend(colorvalues)
max_value = max(numbervalues)
print(N)
print(tiles)
print(numbervalues)
print(max_value)



