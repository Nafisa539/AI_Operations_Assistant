from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response
 
app = Flask(__name__)
CORS(app)
 
@app.route("/")
def home():
    return "AI Powered Operations Assistant is Running"
 
@app.route("/chat", methods=["POST"])
def chat():
 
    data = request.get_json()
 
    question = data["message"]
 
    answer = get_response(question)
 
    return jsonify({"response": answer})
 
if __name__ == "__main__":
    app.run(debug=True)