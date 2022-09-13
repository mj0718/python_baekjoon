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

# ## <2557번 문제>
# ### Hello World!를 출력하시오.

print('Hello World!')

# ## <10718번 문제>
# ### 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

print('강한친구 대한육군')
print('강한친구 대한육군')

# ## <1000번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
x=int(a)
y=int(b)
print(x+y)

# ## <1001번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
x=int(a)
y=int(b)
print(x-y)

# ## <10998번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
x=int(a)
y=int(b)
print(x*y)

# ## <1008번 문제>
# ### 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
x=int(a)
y=int(b)
print(float(x/y))

# ## <10869번 문제>
# ### 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

a,b=input().split()
x=int(a)
y=int(b)
print(x+y)
print(x-y)
print(x*y)
print(int(x/y))
print(x%y)

# ## <10926번 문제>
# ### 첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.

a=input()
print(a+'??!')

# ## <18108번 문제>
# ### 불기 연도를 서기 연도로 변환한 결과를 출력한다.

a=input()
x=int(a)
print(x-543)

# ## <3003번 문제> 
# ### 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다. 만약 수가 양수라면 동혁이는 그 개수 만큼 피스를 더해야 하는 것이고, 음수라면 제거해야 하는 것이다.

a=[1,1,2,2,2,8]
b=list(map(int,input().split())) #map은 형 변환을 한번에 시켜줌
for i in range(6):
    print(a[i]-b[i],end=" ") #end는 현재 출력을 그 다음 출력과 이어지게함

# ## <10430번 문제>
# ### 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a,b,c=map(int,input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# ## <2588번 문제> 
# ### 세 자리 수 * 세 자리 수를 첫째 줄부터 넷째 줄까지 차례대로 출력한다.

a=int(input())
b=input()
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))

# ## <10171번 문제>
# ### 아래 예제와 같이 고양이를 출력하시오.

print("\    /\\") #역슬래시를 쓸 때는 두번 연속해서 넣어야 인식함
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

# ## <10172번 문제>
# ### 아래 예제와 같이 개를 출력하시오.

print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")

# ## <25083번 문제> 
# ### 아래 예제와 같이 새싹을 출력하시오.

print("         ,r'\"7") #"" 또는 '' 안에 똑같은 것을 출력하기 위해서는 \" 또는 \'로 출력
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")
