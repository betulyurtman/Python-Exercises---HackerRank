def mutate_string(string, position, character):
    string_list = list(string) #The input string is a tuple and immutable so we first change it to a list.
    string_list[position] = character #Then we change the value at the "position" and replace it with the "character".
    string = ''.join(string_list) #Lastly, join it back.
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)