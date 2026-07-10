import pandas as pd
 
# Read Student Activity CSV
students = pd.read_csv("../data/student_activity.csv")
 
def data_query(question):
 
    question = question.lower()
 
    for i in range(len(students)):
 
        student_name = str(students["Student_Name"][i]).lower()
        student_id = str(students["Student_ID"][i]).lower()
 
        if student_name in question or student_id in question:
 
            return (
                "Student ID : " + str(students["Student_ID"][i]) +
                "\nStudent Name : " + str(students["Student_Name"][i]) +
                "\nAttendance : " + str(students["Attendance"][i]) +
                "\nAssignment Status : " + str(students["Assignment_Status"][i]) +
                "\nMarks : " + str(students["Marks"][i])
            )
 
    return None