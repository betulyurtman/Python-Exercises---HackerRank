if __name__ == '__main__':
    N = int(input())
    output_array = []
    for i in range(N):
        a = list(input().split())
        if a[0] =="insert":
            output_array.insert(int(a[1]), int(a[2]))
        if a[0] == "remove":
            output_array.remove(int(a[1]))
        if a[0]=='append':
            output_array.append(int(a[1]))
        if a[0]=='sort':
            output_array.sort()
        if a[0]=='pop':
            output_array.pop()
        if a[0]=='reverse':
            output_array.reverse()     
        if a[0]=='print':
            print(output_array)