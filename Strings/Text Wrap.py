import textwrap

def wrap(string, max_width):
  
    lines = textwrap.fill(string, max_width)
    return lines

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# I tried something like this also, but did not work
""" def wrap(string, max_width):
    string_list = []
    string_list.extend(string)
    result_list = []
    print(string_list)
    counter = 0
    for i in len(string_list):
        result_list.append(string_list[i])
        string_list.remove(string_list[i])
        counter += 1
        if counter == max_width:
            result_list = ''.join(result_list)
            print(result_list)
            counter = 0
            result_list.clear()
        continue
    return """