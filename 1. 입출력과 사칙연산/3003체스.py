chess = [1, 1, 2, 2, 2, 8] # 체스 말의 수

a = list(map(int, input().split()))

for idx in range(6):
    print(chess[idx]-a[idx], end=' ') 
