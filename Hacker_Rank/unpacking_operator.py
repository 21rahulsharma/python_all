if __name__ == '__main__':
    n = int(input("Enter the number of students "))
    student_marks = {}
    for i in range(n):
        name, *line = input("Enter").split() #after storing the first value in name rest all the values will be stored in * line
        scores = list(map(float, line)) #  * Is a unpacking operator in python
        student_marks[name] = scores
        print(student_marks)
    # query_name = input()
    # l=list(student_marks[query_name])
    # s=0
    # for i in l:
    #     s=s+i
    # a=len(l)
    # avg=s/a
    # print('%.2f'%avg)
        