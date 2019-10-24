def LCS(x,y):
    L = [[0 for i in range(len(x)+1)] for j in range(len(y)+1)]
    m = len(x)+1
    n = len(y)+1

    for i in range(m):
        for j in range(n):
            if i==0 or j==0:
                L[i][j] = 0

            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    print(L)

    # printing LCS

    index = L[m-1][n-1]
    lcs = []
    i = m-1
    j = n-1
    while i>0 and j>0:
        if x[i-1] == y[j-1]:
            lcs.append(x[i-1])
            i-=1
            j-=1
            index-=1
        elif L[i-1][j]>L[i][j-1]:
            i-=1
        else:
            j-=1
    lcs.reverse()
    print(lcs)

x = 'abcdgh'
y = 'aedfhr'




LCS(x,y)