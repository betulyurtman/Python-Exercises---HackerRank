def swap_case(s):
    an_array = []
    an_array.extend(s)
    
    for i in range(len(an_array)):
        if isinstance(an_array[i], str): 
            if (an_array[i].islower()):
                an_array[i] = an_array[i].upper()
            else:
                an_array[i] = an_array[i].lower()
                
    an_array = ''.join(an_array)

    return an_array

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)