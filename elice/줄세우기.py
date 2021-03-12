

def lining(n):

    Q=[0,1,2]
    P=[0,1,1]

    for i in range(3,n+1):
        Q.append((Q[i-1]+P[i-1])%1000000007)
        P.append(Q[i-1])

    return (Q[n] + P[n]) % 1000000007