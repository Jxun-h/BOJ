n=int(input())
dp=[0]*(n+1)
try:dp[0]=dp[1]=1
except:dp[0]=1
for i in range(2,n+1):
    dp[i]=(dp[i-1]+dp[i-2]+1)%int(1e9+7) #이부분을 1000000007로 바꾸니 AC나왔습니다
print(dp[n])