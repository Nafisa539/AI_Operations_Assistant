import pandas as pd
 
# Read FAQ CSV
faq = pd.read_csv("../data/faq.csv")
 
def faq_lookup(question):
 
    question = question.lower()
 
    for i in range(len(faq)):
 
        faq_question = str(faq["Question"][i]).lower()
 
        if question in faq_question or faq_question in question:
 
            return faq["Answer"][i]
 
    return None