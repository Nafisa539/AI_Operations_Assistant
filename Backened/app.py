import csv

print("      AI Operations Assistant      ")
print("--------------------------------------")
 
while True:
 
    question = input("\nEnter your question or Student ID (type 'exit' to quit): ")
 
    if question.lower() == "exit":
        print("Thank you for using AI Operations Assistant.")
        break
 
    found = False
 
    # Search FAQ.csv
    with open("../data/faq.csv","r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if question.lower() == row["Question"].lower():
                print("\nAnswer:", row["Answer"])
                found = True
                break
 
    # Search schedule.csv
    if not found:
        with open("../data/schedule.csv","r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if question.lower() == row["Event"].lower():
                    print("\nEvent:", row["Event"])
                    print("Subject:", row["Subject"])
                    print("Semester:", row["Semester"])
                    print("Tentative_Date:", row["Tentative_Date"])
                    print("Time:", row["Time"])
                    found = True
                    break
 
    # Search student_activity.csv
    if not found:
        with open("../data/student_activity.csv","r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if question.lower() == row["Student_ID"].lower():
                    print("\nStudent Details")
                    print("Student ID:", row["Student_ID"])
                    print("Student Name:", row["Student_Name"])
                    print("Attendance:", row["Attendance"])
                    print("Assignment Status:", row["Assignment_Status"])
                    print("Marks:", row["Marks"])
                    found = True
                    break
 
    if not found:
        print("Sorry! No matching record found.")