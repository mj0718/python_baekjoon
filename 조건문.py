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

# ## <1330번 문제>
# ### 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오. A가 B보다 큰 경우에는 '>'를 출력한다. A가 B보다 작은 경우에는 '<'를 출력한다. A와 B가 같은 경우에는 '=='를 출력한다.

# +
a,b=map(int,input().split())

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')
# -

# ## <9498번 문제>
# ### 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# +
a=int(input())

if a>=90 and a<=100:
    print('A')
elif a>=80 and a<=89:
    print('B')
elif a>=70 and a<=79:
    print('C')
elif a>=60 and a<=69:
    print('D')
else:
    print('F')
# -

# ## <2753번 문제>
# ### 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오. 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다. 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

# +
a=int(input())

if a%4==0 and a%100!=0 or a%400==0:
    print(1)
else:
    print(0)
# -

# ## <14681번 문제>
# ### 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다. 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

# +
a=int(input())
b=int(input())

if a>0 and b>0:
    print(1)
elif a<0 and b>0:
    print(2)
elif a<0 and b<0:
    print(3)
else:
    print(4)
# -

# ## <2884번 문제>
# ### 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다. 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다. 상근이가 설정해 놓은 시간보다 45분 일찍 알람 설정하는 프로그램을 작성하시오.

# +
a,b=map(int,input().split())

if b>=45:
    print(a,b-45)
elif b<45 and a>0:
    print(a-1,b+15)
else:
    print(23,b+15)
# -

# ## <2525번 문제> 
# ### 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오. 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다. 

# +
hour,minute=map(int, input().split())
c=int(input())

hour+=c//60
minute+=c%60

if minute>=60:
    hour+=1
    minute-=60
    
if hour>=24: #0시 처리를 위해
    hour-=24
    
print(hour,minute)
# -

# ## <2480번 문제> 
# ### 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성하시오.

# +
a,b,c=map(int, input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b or a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)
