if __name__ == '__main__':
    n = int(input()) # n is the number of students taken as an input.
    student_marks = {} # Creating a dictionary for name and score pairs. 
    for _ in range(n): 
        name, *line = input().split() # Splits the input string into two parts: the name of the student and the scores of the student. The * operator in Python expands the list line into its individual elements. So, the name variable will store the name of the student, and the scores variable will store a list of the scores of the student.
        scores = list(map(float, line)) # Converts the scores in the line list to floats. The map() function in Python takes a function and a sequence as input and returns a new sequence where each element in the new sequence is the result of applying the function to the corresponding element in the original sequence.
        student_marks[name] = scores # Adds the name and scores of the student to the student_marks dictionary. The student_marks dictionary is a mapping from names to lists of scores. The [name] = scores syntax in Python assigns the value of the scores variable to the key name in the student_marks dictionary.
    query_name = input()
    
    # Above part was given already. I added the explanations.
    
    sum_of_scores = 0
    
    for i in student_marks[query_name]: # Getting the scores of the query name.
        
        sum_of_scores += i # Taking the sum.
    
    average_of_scores = sum_of_scores / len(student_marks[query_name]) # Finding the average of the scores.
    
    print("%.2f" %average_of_scores) # Printing the score with 2 decimal points.
    