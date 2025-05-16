from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    
    if "hello" in user_message:
        reply = "Hi there! How can I assist you today?"
    elif "services" in user_message:
        reply = "We offer Python training and cloud consulting."
    else:
        reply = "I'm not sure how to respond to that."
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(port=5000)
