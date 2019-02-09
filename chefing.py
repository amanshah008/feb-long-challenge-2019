def special_ingridients(S):
    special=[]
    for i in range(len(S)-1):
        special=set(S[i]).intersection(S[i+1])
    return special



t=int(input())
while t not in range(1, 1001):
    t=int(input().strip())


while(t):
    N=int(input())
    S=[]
    if N in range(1001):
        for i in range(N):
            S.append(input().lower())
        print(special_ingridients(S))
        num=len(special_ingridients(S))
        print(num)





    t+=-1
