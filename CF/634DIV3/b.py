t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    asc = [i for i in range(97,123)]
    ans = []
    for i in range(n):
        ans.append(chr(asc[i%b]))
    print("".join(ans))
