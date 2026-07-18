from faq_lookup import faq_lookup
from schedule_lookup import schedule_lookup
from data_query import data_query
from email_generator import generate_email
from rag import rag_search
 
 
def add_response(results, response_no, text):
    if text and text.strip() and text != "Email type not found.":
        results.append(
            f"Response {response_no}\n"
            f"------------------------------\n"
            f"{text.strip()}"
        )
        return response_no + 1
    return response_no
 
 
def get_response(question):
 
    question = question.lower()
 
    results = []
    response_no = 1
 
    # FAQ
    faq_answer = faq_lookup(question)
    response_no = add_response(results, response_no, faq_answer)
 
    # Schedule
    schedule_answer = schedule_lookup(question)
    response_no = add_response(results, response_no, schedule_answer)
 
    # Student Activity
    data_answer = data_query(question)
    response_no = add_response(results, response_no, data_answer)
 
    # Email Generator
    email_keywords = [
        "leave",
        "attendance",
        "assignment",
        "technical",
        "bonafide",
        "fee",
        "library",
        "exam",
        "id card",
        "password"
    ]
 
    if any(word in question for word in email_keywords):
 
        if "id card" in question:
            email_answer = generate_email("id card")
 
        elif "attendance" in question:
            email_answer = generate_email("attendance")
 
        elif "assignment" in question:
            email_answer = generate_email("assignment")
 
        elif "technical" in question:
            email_answer = generate_email("technical")
 
        elif "bonafide" in question:
            email_answer = generate_email("bonafide")
 
        elif "fee" in question:
            email_answer = generate_email("fee")
 
        elif "library" in question:
            email_answer = generate_email("library")
 
        elif "exam" in question:
            email_answer = generate_email("exam")
 
        elif "password" in question:
            email_answer = generate_email("password")
 
        elif "leave" in question:
            email_answer = generate_email("leave")
 
        else:
            email_answer = ""
 
        response_no = add_response(results, response_no, email_answer)
 
    # PDF Search
    rag_answer = rag_search(question)
 
    if rag_answer:
 
        duplicate = False
 
        for r in results:
            if rag_answer[:100] in r:
                duplicate = True
                break
 
        if not duplicate:
            response_no = add_response(results, response_no, rag_answer)
 
    if len(results) == 0:
        return "Sorry, I couldn't find any relevant information."
 
    return "\n\n".join(results)