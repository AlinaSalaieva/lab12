import random

def generate_strings(alphabet, N, M):
    for _ in range(N):
        result = ''.join(random.choice(alphabet) for _ in range(M))
        print(result)
        
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
N = 5
M = 8
generate_strings(alphabet, N, M)
