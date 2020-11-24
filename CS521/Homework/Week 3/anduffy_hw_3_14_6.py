"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: November 24, 2020
Homework Problem 14.6
Description: This reads a text file containing a students records and stores that info in lists/tuples.
"""
def student_records():
    try:
        students = open("students.txt", "r")
    except:
        print("Error: The input file does not exist!")
        return
    records = []
    file_lines = students.readlines()
    for line in file_lines:
        current_record = []
        for part in line.split(", "):
            if part[len(part) - 1] == '\n': #This filters out the new line character for the GPA.
                gpa = float(part[:len(part) - 1])
                current_record.append(gpa)
                continue
            try:
                id = int(part)
                current_record.append(id)
            except:
                current_record.append(part)
        records.append(current_record)
    students.close()
    print(records)

if __name__ == "__main__":
    student_records()