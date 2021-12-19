n = int(input("Enter the no. of nodes\n"))
print("\nEnter the matrix for the graph\n")
W = []
p = []
for i in range (n):
    a = input().split(' ')
    W.append(a)
    p.append(1)
l=[]
M = []
for i in range(n):
    for j in range(n):
        v = int(W[j][i])
        s = 0
        for k in range (len(W[j])):
            s = s + int(W[j][k]) 
        m = v/s
        l.append(m)
    M.append(l)
    l=[]
npr = []
for i in range (n):
    print(M[i])
print("\nIteration 0\n",p)
k = 0
while(p!=npr and k<10):
    print("\nIteration ",k,"\n")
    for i in range (n):
        q = 0
        for j in range (n):
            q = q + M[i][j]*p[j]
        npr.append(q)
    print("New Page Rank\n",npr)
    p = npr
    npr = []
    k = k+1







"""
Output:
Enter the no. of nodes
4

Enter the matrix for the graph

0 1 1 1
1 0 0 1
1 0 0 0
0 1 1 0
[0.0, 0.5, 1.0, 0.0]
[0.3333333333333333, 0.0, 0.0, 0.5]
[0.3333333333333333, 0.0, 0.0, 0.5]
[0.3333333333333333, 0.5, 0.0, 0.0]

Iteration 0
 [1, 1, 1, 1]

Iteration  0 

New Page Rank
 [1.5, 0.8333333333333333, 0.8333333333333333, 0.8333333333333333]

Iteration  1 

New Page Rank
 [1.25, 0.9166666666666666, 0.9166666666666666, 0.9166666666666666]

Iteration  2 

New Page Rank
 [1.375, 0.875, 0.875, 0.875]

Iteration  3 

New Page Rank
 [1.3125, 0.8958333333333333, 0.8958333333333333, 0.8958333333333333]

Iteration  4 

New Page Rank
 [1.34375, 0.8854166666666666, 0.8854166666666666, 0.8854166666666666]

Iteration  5 

New Page Rank
 [1.328125, 0.890625, 0.890625, 0.890625]

Iteration  6 

New Page Rank
 [1.3359375, 0.8880208333333333, 0.8880208333333333, 0.8880208333333333]

Iteration  7 

New Page Rank
 [1.33203125, 0.8893229166666666, 0.8893229166666666, 0.8893229166666666]

Iteration  8 

New Page Rank
 [1.333984375, 0.888671875, 0.888671875, 0.888671875]

Iteration  9 

New Page Rank
 [1.3330078125, 0.8889973958333333, 0.8889973958333333, 0.8889973958333333]
"""
