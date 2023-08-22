# This is not exactly my solution, I made some parts different but it did not work so I got some help..
def count_substring(string, sub_string):
    counting = 0 #This will be the output.
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            counting += 1
    return counting

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)