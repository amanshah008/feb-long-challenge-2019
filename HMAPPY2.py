def lcm(a,b):
    if b>a:
        a,b = b,a
    product=a*b
    while b:
        a, b= b, a%b


    return product/a

t=int(input())
while t not in range(1, 16):
    t=int(input().strip())



while(t):
    N,A,B,K=map(int, input().split(" "))
    if (int(N/A)+int(N/B)-2*int(N/lcm(a,b)))>= K:
        print("Win")
    else:
        print("Lose")

    t+=-1
