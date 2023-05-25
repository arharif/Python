# Finding The Percentage HackerRank challenge
# Tasks 
# The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Dictionaries are used to store data values in key:value pairs.
# List items are ordered, changeable, and allow duplicate values.
# [name, * line] This allows you to handle variable-length input where you want to assign the first word to name and the rest of the words to line regardless of their number.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
# My solution

print( "%.2f" % (sum(list(student_marks[query_name])) / (len(list(student_marks[query_name])))))
