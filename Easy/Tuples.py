if __name__ == '__main__':
    N = int(input())
    A = tuple(input().split())
    T = [int(x) for x in A]
    print(hash(tuple(T)))
