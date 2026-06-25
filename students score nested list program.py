if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        students.append([name, score])
    grades = sorted(set([score for name,score in students]))
    second_lowest = grades[1]
    result = []
    for name,score in students:
        if score == second_lowest:
            result.append(name)
    result.sort()

    # Print result
    for name in result:
        print(name)
