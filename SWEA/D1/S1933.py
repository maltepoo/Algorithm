#1933. 간단한 N 의 약수
T = int(input())
for i in range(1,T+1):
    if T % i == 0:
        print(i, end=' ')