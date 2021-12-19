h = lambda x: int(x, 2) % 11
 
def bloom_filter(n, N):
    bloom_array = [0]*N
    for i in inp:
        print(f"Adding element: {n}")
        bin_n = bin(i).replace("0b", "")
        a = h(bin_n[1::2])
        b = h(bin_n[::2])
        if bloom_array[a] == 1 and bloom_array[b] == 1:
            print(f"Element {i} already exists, or it is false positive.")
        else: 
            print(f"Element {i} does not exist, adding element.")
            bloom_array[a], bloom_array[b] = 1, 1
            print(f"Bloom Array {bloom_array} after inserting {i}.")
 
if __name__ == '__main__':
    N = int(input('Enter stream size: '))
    inp = list(map(int, input("Enter the input elements: ").strip().split()))
    bloom_filter(inp, N)
