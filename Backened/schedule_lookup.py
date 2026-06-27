import csv
 
def get_schedule(question):
 
    question = question.lower()
 
    with open("../data/schedule.csv", "r", encoding="utf-8") as file:
 
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
 
    return None