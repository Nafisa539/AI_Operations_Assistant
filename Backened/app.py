from flask import Flask, request, jsonify
from flask_cors import CORS
 
from chatbot import get_faq_response
from schedule_lookup import get_schedule
from data_query import get_student_data
 
app = Flask(__name__)
CORS(app)
 
 
@app.route("/")
def home():
    return "AI Powered Operations Assistant is Running"
 
 
@app.route("/chat", methods=["POST"])
def chat():
 
    data = request.get_json()
 
    question = data["message"]
 
    # FAQ
    answer = get_faq_response(question)
 
    # Schedule
    if answer is None:
        answer = get_schedule(question)
 
    # Student Data
    if answer is None:
        answer = get_student_data(question)
 
    # No Match
    if answer is None:
        answer = "Sorry, I couldn't find the requested information."
 
    return jsonify({"response": answer})
 
 
if __name__ == "__main__":
    app.run(debug=True)