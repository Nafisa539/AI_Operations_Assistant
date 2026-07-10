from faq_lookup import faq_lookup
from schedule_lookup import schedule_lookup
from data_query import data_query
from email_generator import generate_email
from rag import rag_search
 
 
def get_response(question):
 
    question = question.lower()
 
    # FAQ
    answer = faq_lookup(question)
    if answer:
        return answer
 
    # Schedule
    answer = schedule_lookup(question)
    if answer:
        return answer
 
    # Student Activity
    answer = data_query(question)
    if answer:
        return answer
 
    # Email Generator
    if "leave email" in question:
        return generate_email("leave")
 
    elif "assignment email" in question:
        return generate_email("assignment")
 
    elif "technical email" in question:
        return generate_email("technical")
 
    elif "attendance email" in question:
        return generate_email("attendance")
 
    elif "bonafide email" in question:
        return generate_email("bonafide")
 
    elif "fee email" in question:
        return generate_email("fee")
 
    elif "library email" in question:
        return generate_email("library")
 
    elif "exam email" in question:
        return generate_email("exam")
 
    elif "id card email" in question:
        return generate_email("id card")
 
    elif "password email" in question:
        return generate_email("password")
 
    # RAG Search
    answer = rag_search(question)
    if answer:
        return answer
 
    return "Sorry! I couldn't find an answer."