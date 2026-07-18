import pandas as pd
 
# Load Schedule CSV
schedule = pd.read_csv("../data/schedule.csv")
 
def schedule_lookup(question):
 
    question = question.lower()
 
    words = question.split()
 
    answers = []
 
    for i in range(len(schedule)):
 
        row = ""
 
        for column in schedule.columns:
            row += str(schedule[column][i]).lower() + " "
 
        score = 0
 
        for word in words:
            if word in row:
                score += 1
 
        if score > 0:
 
            result = ""
 
            for column in schedule.columns:
                result += f"{column} : {schedule[column][i]}\n"
 
            if result not in answers:
                answers.append(result.strip())
 
    if len(answers) == 0:
        return None
 
    return "\n\n".join(answers)