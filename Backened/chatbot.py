import csv
 
def get_response(question):
 
    question = question.lower()
 
    #  FAQ 
    with open("../data/faq.csv", mode="r", encoding="utf-8") as file:
 
        reader = csv.DictReader(file)
 
        for row in reader:
 
            if row["Question"].lower() in question:
                return row["Answer"]
 
    #  Schedule 
    with open("../data/schedule.csv", mode="r", encoding="utf-8") as file:
 
        reader = csv.DictReader(file)
 
        for row in reader:
 
            if row["Subject"].lower() in question:
 
                return (
                    f"Subject : {row['Subject']}\n"
                    f"Event : {row['Event']}\n"
                    f"Semester : {row['Semester']}\n"
                    f"Date : {row['Date']}\n"
                    f"Time : {row['Time']}"
                )
 
    # Student Activity 
    with open("../data/student_activity.csv", mode="r", encoding="utf-8") as file:
 
        reader = csv.DictReader(file)
 
        for row in reader:
 
            if row["Student_Name"].lower() in question:
 
                return (
                    f"Student Name : {row['Student_Name']}\n"
                    f"Student ID : {row['Student_ID']}\n"
                    f"Attendance : {row['Attendance']}\n"
                    f"Assignment Status : {row['Assignment_Status']}\n"
                    f"Marks : {row['Marks']}"
                )
 
    return "Sorry! Information not found."