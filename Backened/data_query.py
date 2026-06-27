import csv
 
def get_student_data(question):
 
    question = question.lower()
 
    with open("../data/student_activity.csv", "r", encoding="utf-8") as file:
 
        reader = csv.DictReader(file)
 
        for row in reader:
 
            name = row["Student_Name"].lower()
            student_id = row["Student_ID"].lower()
 
            if name in question or student_id in question:
 
                return (
                    f"Student ID : {row['Student_ID']}\n"
                    f"Student Name : {row['Student_Name']}\n"
                    f"Attendance : {row['Attendance']}%\n"
                    f"Assignment Status : {row['Assignment_Status']}\n"
                    f"Marks : {row['Marks']}"
                )
 
    return None