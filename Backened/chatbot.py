import csv
 
def get_faq_response(question):
 
    question = question.lower()
 
    with open("../data/faq.csv", "r", encoding="utf-8") as file:
 
        reader = csv.DictReader(file)
 
        for row in reader:
 
            csv_question = row["Question"].lower()
 
            if csv_question in question or question in csv_question:
 
                return row["Answer"]
 
    return None