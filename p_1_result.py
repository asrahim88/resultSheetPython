def checkGPA(marks):
    if marks>=80:
        return "A+"
    elif marks>=70:
        return "A"
    elif marks>=60:
        return "A-"
    elif marks>=50:
        return "B"
    elif marks>=40:
        return "C"
    elif marks>=33:
        return "D"
    else:
        return "F"
    
def passFail(resultInfo):
    if any(marks in range(1,33) for marks in [i[0] for i in resultInfo.values()]):
        return "Fail"
    else:
        return "Pass"
    
def individualResult(resultInfo, subjectName):
    if len(resultInfo) == 0:
        print("Not found any data. Please insert data using option 1")
    else:
        print(f"Subject name: {subjectName}\nSubject marks: {resultInfo[subjectName][0]}\nSubject GPA: {resultInfo[subjectName][1]}")
            

def allSubjectResult(resultInfo):
    if len(resultInfo) == 0:
        print("Not found any data. Please at first insert data using option 1. And try again!")
    else:
        result = passFail(resultInfo)
        if result == "Pass":
            allSubjectsMarks = 0
            golden = []
            for result in resultInfo.values():
                allSubjectsMarks += result[0]
                if result[1] =="A+":
                    golden.append(result[1])
            average = allSubjectsMarks/len(resultInfo)
            if len(resultInfo) == len(golden):
                print(f"Total Marks: {allSubjectsMarks}\nAverage Marks: {round(average,2)}\nFinal GPA: (G-A+)")
            else:
                print(f"Total Marks: {allSubjectsMarks}\nAverage Marks: {round(average,2)}\nFinal GPA: ({checkGPA(average)})")
        else:
            print("Failed")

subjectsAndMarks = {}
       
print('''
                    Welcome To GRADING application
                        Please Select Your Option
                        
        1) No of subjects
        2) Individual subject wise result
        3) All subjects result
        
      ''')

while True:
    
    option = int(input("Enter your option: "))
    if option <0 or option> 3:
        print("Invalid Input! Please Try again among 1 to 3 .")
    else:
        if option == 1:
            countSubjects = int(input("How many subjects do you want to get results? "))

            for i in range(countSubjects):
                subject, marks = input("Enter your subject name and marks: ").split(" ")
                if int(marks) < 0 or int(marks) > 100:
                    print("Invalid marks! Please try again from the start.")
                    break
                else:
                    subjectsAndMarks[subject.lower()] = [int(marks), checkGPA(int(marks))]
        elif option == 2:
            subject = input("Enter your subject name: ").lower()
            individualResult(subjectsAndMarks, subject)
        else:
            allSubjectResult(subjectsAndMarks)
    
    next_move = input("Do you want to perform another option? (yes or no) ")
    if next_move.lower() != "yes":
        print("Successfully exit..")
        break

    

