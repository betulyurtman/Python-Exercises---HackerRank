def split_and_join(line):
    # write your code here
    an_array = line.split(" ")
    an_array = '-'.join(an_array)
    return an_array
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)