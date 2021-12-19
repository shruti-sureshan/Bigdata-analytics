import math
import operator

def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(0,m+1):
        for j in range(0,n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

def cosine():
    p1 = list(map(int, input('Enter first vector: ').split()))
    p2 = list(map(int, input('Enter second vector: ').split()))
    n = sum(map(operator.mul, p1, p2))
    print(n)
    def mag(p):
        return sum(pi*pi for pi in p) ** 0.5
    a = mag(p1) * mag(p2)
    d = math.acos(round(n / a, 8))
    print(f'Distance: {d}')

def hamming():
    s1 = input('Enter string1: ')
    s2 = input('Enter string2: ')
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    d = sum(el1 != el2 for el1, el2 in zip(s1, s2))
    print(f'Distance: {d}')

def euclid():
    p1 = list(map(int, input('Enter first point: ').split()))
    p2 = list(map(int, input('Enter second point: ').split()))
    d = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    print(f'Distance: {d}')

def edit():
    a = input('Enter first string: ')
    b = input('Enter second string: ')
    d = len(a) + len(b) - 2*lcs(a, b)
    print(f'Distance: {d}')

def jaccard():
    l1 = set(list(map(int, input('Enter first list: ').split())))
    l2 = set(list(map(int, input('Enter second list: ').split())))
    intersection = len(set(l1).intersection(l2))
    union = len(l1.union(l2))
    d = float(intersection) / union
    print(f'Similarity: {d}, {intersection}, {union}')

if __name__ == '__main__':
    inp = int(input('1. Euclid\n2. Cosine\n3. Edit\n4. Jaccard\n5.Hamming\nEnter your option: '))
    if inp == 1:
        euclid()
    elif inp == 2:
        cosine()
    elif inp == 3:
        edit()
    elif inp == 4:
        jaccard()
    else:
        hamming()
