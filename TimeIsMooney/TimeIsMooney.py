import sys 
from collections import defaultdict
        
def main():

    '''Input N,M,C'''
    line = sys.stdin.readline()
    if not line:
        return 
    N,M,C = list(map(int,line.strip().split(' ')))

    '''Input moonies'''
    line = sys.stdin.readline()
    if not line:
        return
    moonies = list(map(int,line.strip().split(' ')))

    '''Input graph'''
    graph = defaultdict(list)
    for _ in range(M):
        line = sys.stdin.readline()
        if not line:
            return 
        u,v = list(map(int,line.strip().split(' ')))
        graph[u].append(v)

    '''setup graph'''
    dp = [  [-1 for _ in range(1001)] for _ in range(N+1)]
    dp[1][0] = 0

    '''start executing the logic'''
    for t in range(1000):
        for node in graph.keys():
            if dp[node][t] ==-1: 
                continue 
            for child_node in graph[node]:
                dp[child_node][t+1] = max(dp[child_node][t+1],dp[node][t]+moonies[child_node-1])
    res = 0
    for t in range(1,1000):
        if dp[1][t] ==-1:
            continue
        profit = dp[1][t] - (C*t*t)
        res = max(res,profit)
    sys.stdout.write(str(res)+'\n')
    return 
        
if __name__ == '__main__':
    sys.stdin = open('time.in','r')
    sys.stdout = open('time.out','w')
    main()
