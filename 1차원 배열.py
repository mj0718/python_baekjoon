# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## <10818번 문제>
# ### N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 공백으로 구구분해 출력하는 프로그램을 작성하시오.

# +
N=int(input())
a=list(map(int,input().split()))

print(min(a), max(a))
# -

# ## <2562번 문제>
# ### 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오. 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# +
num=[] #list 생성

for i in range(9):
    a=int(input())
    num.append(a) #list에 객체 추가 
print(max(num))
print(num.index(max(num))+1) #index함수로 최대값의 위치 찾음 index는 0부터 시작이므로 +1해줌
# -

# ## <3052번 문제> 
# ### 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# +
num=[]

for i in range(10):
    a=int(input())
    num.append(a%42)
num=set(num) #set함수는 중복된 값 제거해줌
print(len(num)) #len은 문자열 길이를 나타냄
# -
# ## <1546번 문제>
# ### 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다. 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다. 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# +
N=int(input())
score=list(map(int, input().split()))

result=[]

for i in range(N): 
    result.append(score[i]/max(score)*100)
print(sum(result)/N)
# -

# ## <8958번 문제>
# ###  O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오. 

# +
N=int(input())


for i in range(N):
    a=input()
    count=0
    total=0
    for j in a:
        if j=='O':
            count+=1
        else:
            count=0
        total+=count
    print(total)
# -

# ## <4344번 문제>
# ### 첫째 줄에는 테스트 케이스의 개수 C가 주어진다. 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력하는 프로그램을 작성하시오.

# +
N=int(input())

for i in range(N):
    score=list(map(int, input().split()))
    avg=sum(score[1:])/score[0] #score[1:]은 학생들 점수, score[0]은 학생 수
    count=0
    for j in score[1:]:
        if j>avg:
            count+=1
    print('%.3f'%(count/score[0]*100)+'%')
