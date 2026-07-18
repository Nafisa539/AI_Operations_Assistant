import pandas as pd
 
faq = pd.read_csv("../data/faq.csv")
 
def faq_lookup(question):
 
    question = question.lower()
 
    words = question.split()
 
    answers = []
 
    for i in range(len(faq)):
 
        faq_question = str(faq["Question"][i]).lower()
        faq_answer = str(faq["Answer"][i])
 
        score = 0
 
        for word in words:
 
            if word in faq_question:
                score += 1
 
        if score > 0:
 
            result = (
                f"Question : {faq['Question'][i]}\n"
                f"Answer   : {faq_answer}"
            )
 
            if result not in answers:
                answers.append(result)
 
    if len(answers) == 0:
        return None
 
    return "\n\n".join(answers)