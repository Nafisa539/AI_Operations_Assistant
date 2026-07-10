from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot import get_response
 
app = Flask(__name__)
 
CORS(app)
 
@app.route("/")
def home():
 
    return render_template("test.html")
 
 
@app.route("/chat", methods=["POST"])
def chat():
 
    data = request.get_json()
 
    question = data["message"]
 
    answer = get_response(question)
 
    return jsonify({
        "response": answer
    })
 
 
if __name__ == "__main__":
 
    app.run(debug=True)