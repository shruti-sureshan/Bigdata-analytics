h1 = lambda x: (3*x + 1) % 5
 
def fm(inp):
    est = []
    for h in [h1]:
        r = []
        for i in inp:
            a = h(i)
            b = bin(a)[2:][::-1]
            if '1' in b:
                r.append(b.index('1'))
            else:
                r.append(0)
        est.append(2**max(r))
    print(f"Average estimated unique values: {sum(est)/len(est)}")
 
inp = [10, 12, 13, 3, 4, 25, 7, 10, 4]
fm(inp)
