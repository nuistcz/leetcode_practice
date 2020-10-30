class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False for j in range(len(p)+1)] for i in range(len(s)+1)]    #生成dp矩阵，给定初始值False
        dp[0][0]=True
        for k in range(1,len(p)+1):                 #初始条件：dp[0][k] k∈[1,2,...,len(p)] 即二维数组第一行
            if len(p)>1:
                if p[k-1]=="*":
                    dp[0][k]=dp[0][k-2]
                else:
                    dp[0][k]=False
            else:
                dp[0][k]=False
        for l in range(1,len(s)+1):                 #初始条件 dp[l][0] l∈[1,2,...,len(p)] 即二维数组第一列
            dp[l][0]=False

        for i in range(1,len(s)+1):                 #填写二维数组列表内容
            for j in range(1,len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]==".":               #常规情况
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=="*":                               #处理带*情况
                    if dp[i][j-2]==True:
                        dp[i][j]=True
                    elif (p[j-2]==s[i-1] or p[j-2]==".") and dp[i-1][j]==True:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
                else:
                    dp[i][j]=False
        return dp[len(s)][len(p)]