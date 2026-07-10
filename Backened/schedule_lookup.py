import pandas as pd
 
# Read schedule.csv
schedule = pd.read_csv("../data/schedule.csv")
 
def schedule_lookup(question):
 
    question = question.lower()
 
    for i in range(len(schedule)):
 
        event = str(schedule["Event"][i]).lower()
        subject = str(schedule["Subject"][i]).lower()
 
        if event in question or subject in question:
 
            return (
                "Event : " + str(schedule["Event"][i]) +
                "\nSubject : " + str(schedule["Subject"][i]) +
                "\nSemester : " + str(schedule["Semester"][i]) +
                "\nDate : " + str(schedule["Date"][i]) +
                "\nTime : " + str(schedule["Time"][i])
            )
 
    return None