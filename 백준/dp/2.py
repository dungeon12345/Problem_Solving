import sys
input = sys.stdin.readline
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
        for j in range(21):
            for k in range(21):
                if i <=0 or j<=0 or k<=0:
                    dp[i][j][k] = 1
                    continue
                if i < j and j < k:
                    dp[i][j][k] = dp[i][j][k-1]+ dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

while True:
    a,b,c = list(map(int, input().split()))
    res = 0
    if a == -1 and b == -1 and c == -1:
        break
    if a <=0 or b <=0 or c<=0:
        res = 1
    elif a > 20 or b > 20 or c > 20:
        res = dp[20][20][20]
    else:
        res = dp[a][b][c]
    print("w("+str(a)+", "+str(b)+", "+str(c)+") = "+str(int(res)))
