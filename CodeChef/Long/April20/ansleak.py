from collections import Counter
t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    answers = []
    out = []
    for i in range(n):
        answers.append(list(map(int,input().split())))
    
    for i in answers:
        counts = Counter(i)
        out.append(counts.most_common(1)[0][0])
    print(*out)
