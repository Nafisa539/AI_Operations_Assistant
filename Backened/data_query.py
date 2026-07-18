import pandas as pd
 
# Load Student Activity CSV
student = pd.read_csv("../data/student_activity.csv")
 
def data_query(question):
 
    question = question.lower()
 
    words = question.split()
 
    answers = []
 
    for i in range(len(student)):
 
        row = ""
 
        # Combine all column values into one string
        for column in student.columns:
            row += str(student[column][i]).lower() + " "
 
        score = 0
 
        # Check if any keyword matches
        for word in words:
            if word in row:
                score += 1
 
        if score > 0:
 
            result = ""
 
            # Display all column names and values
            for column in student.columns:
                result += f"{column} : {student[column][i]}\n"
 
            result = result.strip()
 
            # Remove duplicate records
            if result not in answers:
                answers.append(result)
 
    if len(answers) == 0:
        return None
 
    # Leave one blank line between records
    return "\n\n".join(answers)