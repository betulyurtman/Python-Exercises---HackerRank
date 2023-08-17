if __name__ == '__main__':
    python_students = [] # Creating a list to hold student name and score pairs.
    for i in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score]) # Appending the pairs to our list.
        scores = [] # Creating a list to hold scores seperately.
        for j in python_students: 
            scores.append(j[1])
    
    scores.sort() # Sorting the scores in ascending order.
    
    scores_unique = [] # Creating a list that does not contain duplicates to find the second lowest score.
    
    for score in scores:
        if score not in scores_unique: # Taking the different scores into our list.
            scores_unique.append(score)
    
    second_lowest = scores_unique[1] # Finding the second lowest score. 
    
    names = []
    for b in python_students:
        if b[1] == second_lowest: # Finding the scores that matches the second lowest score.
            names.append(b[0]) # Getting the student names.
            
    names.sort() # Sorting the name list to print them in alphabetical order.
    for n in names:
        print(n)