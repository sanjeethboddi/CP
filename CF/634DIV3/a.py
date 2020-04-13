t = int(input())
for _ in range(t):
    n = int(input())
    ways = n//2-1 if n%2 == 0 else n//2
    print(max(0,ways))
