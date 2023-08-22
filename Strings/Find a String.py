# This is not exactly my solution, I made some parts differently but it did not work so I got some help..
def count_substring(string, sub_string):
    counting = 0 #This will be the output.
    for i in range(0, len(string)): #We need a for loop for comparisons.
        if string[i:i+len(sub_string)] == sub_string: #We check if the part of the string matches with sub string using slicing method.
            counting += 1 #If the match is a yes, we increase the count. 
    return counting

if __name__ == '__main__': #This part is given by HackerRank.
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)