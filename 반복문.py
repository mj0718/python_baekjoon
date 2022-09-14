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

# ## <2739번 문제>
# ### N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.

# +
a=int(input())

for i in range(1,10):
    print(a,'*',i,'=',a*i)
# -

# ## <10950번 문제>
# ### 두 정수 A와 B를 입력받은 다음, 각 케이스마다 A+B를 출력하는 프로그램을 작성하시오.

# +
n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    print(a+b)
# -

# ## <8393번 문제>
# ### n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# +
a= int(input())
sum=0

for i in range(1,a+1):
    sum+=i
print(sum)
# -

# ## <25304번 문제>
# ### 영수증에 적힌 구매한 각 물건의 가격과 개수,구매한 물건들의 총 금액을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사하는 프로그램을 작성하시오.

# +
X=int(input())
N=int(input())

sum=0

for i in range(N):
    a,b=map(int,input().split())
    sum+=a*b

if X==sum:
    print('Yes')
else:
    print('No')
# -

# ## <15552번 문제>
# ### 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다. Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다. 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

# +
import sys

n=int(input())

for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    print(a+b)
#jupyter에서는 sys.stdin.readline() 사용하면 오류 발생함 
#따라서 다른 파이썬 프로그램에서는 sys.stdin.readline()을 사용하면 input()보다 빠르게 입력 받을 수 있음 
# -

# ## <11021번 문제>
# ### 두 정수 A와 B를 입력받은 다음 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# +
n=int(input())

for i in range(1,n+1):
    a,b=map(int,input().split())
    print('Case #'+str(i)+':',a+b) #문자열로 바꾸는 것이 중요함
# -

# ## <11022번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

# +
n=int(input())

for i in range(1,n+1):
    a,b=map(int,input().split())
    print('Case #'+str(i)+':',a,'+',b,'=',a+b)
# -

# ## <2438번 문제>
# ### 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 프로그램을 작성하시오.

# +
n=int(input())

for i in range(1,n+1):
    print('*'*i)
# -

# ## <2439번 문제>
# ### 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 프로그램을 작성하시오. 단, 오른쪽을 기준으로 별을 정렬하시오.

# +
n=int(input())

for i in range(1,n+1):
    print(" "*(n-i)+'*'*i) #공백으로 빈 공간 채워주기
# -

# ## <10871번 문제>
# ### 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# +
N,X=map(int,input().split())

A=list(map(int,input().split()))

for i in range(N):
    if X>A[i]:
        print(A[i],end=" ")
# -

# ## <10952번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. 입력의 마지막에는 0 두 개가 들어온다.

while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    print(a+b)

# ## <10951번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. 

while True:
    try: 
        a,b=map(int,input().split())
    except:
        break
    print(a+b)

# #### -try: 실행할 코드  except: 예외가 발생했을 때 처리하는 코드
# #### -try, except문으로 오류 예외 처리함

# ## <1110번 문제>
# ### 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# +
N=int(input())

num=N
count=0

while True:   #예로 26 넣기
    a=num//10   #26을 10으로 나눈 몫 a=2
    b=num%10   #10으로 나눈 나머지 b=6
    c=(a+b)%10   #a와b를 더한 후 10으로 나눈 나머지 c=8
    num=(b*10)+c   #새로운 수인 num=68
    count+=1   #사이클 길이를 1씩 더해줌 
    if num==N: 
        break   #원래 수와 같아지면 멈추기
print(count)
