import pandas as pd
 
# Read CSV files
faq = pd.read_csv("../data/faq.csv")
schedule = pd.read_csv("../data/schedule.csv")
student = pd.read_csv("../data/student_activity.csv")
 
 
def get_response(question):
 
    question = question.lower()
 
    # ---------------- FAQ ----------------
    for index, row in faq.iterrows():
 
        if row["Question"].lower() in question:
            return row["Answer"]
 
    # ---------------- Schedule ----------------
    for index, row in schedule.iterrows():
 
        if row["Subject"].lower() in question:
 
            return (
                f"Subject: {row['Subject']}\n"
                f"Event: {row['Event']}\n"
                f"Semester: {row['Semester']}\n"
                f"Date: {row['Date']}\n"
                f"Time: {row['Time']}"
            )
 
    # ---------------- Student Activity ----------------
    for index, row in student.iterrows():
 
        if row["Student_Name"].lower() in question:
 
            return (
                f"Student Name: {row['Student_Name']}\n"
                f"Student ID: {row['Student_ID']}\n"
                f"Attendance: {row['Attendance']}%\n"
                f"Assignment Status: {row['Assignment_Status']}\n"
                f"Marks: {row['Marks']}"
            )
 
    return "Sorry! I couldn't find the requested information."